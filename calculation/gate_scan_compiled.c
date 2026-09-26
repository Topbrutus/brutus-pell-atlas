#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <inttypes.h>
#include <limits.h>
#include <omp.h>

typedef uint64_t u64;
typedef __uint128_t u128;

static const u64 DEFAULT_START = 1ULL;
static const u64 DEFAULT_STOP = 1000000ULL;
static const u64 DEFAULT_SEG = 1000000ULL;
static const int SIEVE_LIMIT = 100000;
static const int MAX_ROOT_FACTORS = 32;

typedef struct { u64 a,b,c,d; } Mat;

static inline u64 mulmod(u64 a,u64 b,u64 m){
    return (u64)(((u128)a*b)%m);
}
static inline u64 addmod(u64 a,u64 b,u64 m){
    return (u64)(((u128)a+b)%m);
}
static Mat mmul(Mat x,Mat y,u64 m){
    Mat z;
    z.a=addmod(mulmod(x.a,y.a,m),mulmod(x.b,y.c,m),m);
    z.b=addmod(mulmod(x.a,y.b,m),mulmod(x.b,y.d,m),m);
    z.c=addmod(mulmod(x.c,y.a,m),mulmod(x.d,y.c,m),m);
    z.d=addmod(mulmod(x.c,y.b,m),mulmod(x.d,y.d,m),m);
    return z;
}
static u64 pell_mod(u64 n,u64 m){
    Mat r={1,0,0,1}, q={2,1,1,0};
    while(n){
        if(n&1) r=mmul(r,q,m);
        q=mmul(q,q,m);
        n>>=1;
    }
    return r.b % m;
}
static u64 powmod(u64 a,u64 e,u64 m){
    u64 r=1;
    while(e){
        if(e&1) r=mulmod(r,a,m);
        a=mulmod(a,a,m);
        e>>=1;
    }
    return r;
}
static int isprime64(u64 n){
    static const u64 small[]={2,3,5,7,11,13,17,19,23,29,31,37};
    if(n<2) return 0;
    for(size_t i=0;i<sizeof(small)/sizeof(small[0]);++i){
        if(n==small[i]) return 1;
        if(n%small[i]==0) return 0;
    }
    u64 d=n-1,s=0;
    while((d&1)==0){ d>>=1; s++; }
    static const u64 bases[]={
        2ULL,325ULL,9375ULL,28178ULL,
        450775ULL,9780504ULL,1795265022ULL
    };
    for(size_t i=0;i<sizeof(bases)/sizeof(bases[0]);++i){
        u64 a=bases[i]%n;
        if(a==0) continue;
        u64 x=powmod(a,d,n);
        if(x==1 || x==n-1) continue;
        int witness=1;
        for(u64 j=1;j<s;j++){
            x=mulmod(x,x,n);
            if(x==n-1){ witness=0; break; }
        }
        if(witness) return 0;
    }
    return 1;
}

static long invmod(long a,long m){
    long t=0,newt=1,r=m,newr=a;
    while(newr){
        long q=r/newr;
        long tt=t-q*newt; t=newt; newt=tt;
        long rr=r-q*newr; r=newr; newr=rr;
    }
    if(r>1) return -1;
    if(t<0) t+=m;
    return t;
}

static int legendre8(u64 p){
    u64 r=p&7ULL;
    if(r==1 || r==7) return 1;
    if(r==3 || r==5) return -1;
    return 0;
}

static int factor_root_distinct(u64 root,u64 *factors){
    int nf=0;
    u64 x=root;
    if((x&1ULL)==0){
        factors[nf++]=2;
        while((x&1ULL)==0) x>>=1;
    }
    for(u64 q=3;q<=x/q;q+=2){
        if(x%q==0){
            if(nf>=MAX_ROOT_FACTORS) return -1;
            factors[nf++]=q;
            while(x%q==0) x/=q;
        }
    }
    if(x>1){
        if(nf>=MAX_ROOT_FACTORS) return -1;
        factors[nf++]=x;
    }
    return nf;
}

static int exact_target_rank(
    u64 modulus,u64 target,
    const u64 *root_factors,int nf
){
    if(pell_mod(target,modulus)!=0) return 0;
    for(int i=0;i<nf;i++){
        if(pell_mod(target/root_factors[i],modulus)==0) return 0;
    }
    return 1;
}

static int sign_admissible(u64 p,int sign){
    if(p<=2 || (p&1ULL)==0) return 0;
    return legendre8(p)==sign;
}

int main(int argc,char **argv){
    if(argc<2){
        fprintf(stderr,
            "usage: %s ROOT [START_K] [STOP_K] [SEGMENT]\n",
            argv[0]);
        return 2;
    }
    u64 root=strtoull(argv[1],NULL,10);
    u64 start=argc>2?strtoull(argv[2],NULL,10):DEFAULT_START;
    u64 stop=argc>3?strtoull(argv[3],NULL,10):DEFAULT_STOP;
    u64 seg=argc>4?strtoull(argv[4],NULL,10):DEFAULT_SEG;
    if(root<2 || start<1 || stop<start || seg<1){
        fprintf(stderr,"invalid arguments\n");
        return 2;
    }
    if(root>UINT64_MAX/root){
        fprintf(stderr,"root^2 overflow\n");
        return 2;
    }
    u64 target=root*root;
    if(stop>(UINT64_MAX-1)/target){
        fprintf(stderr,"candidate range overflows uint64\n");
        return 2;
    }

    u64 root_factors[MAX_ROOT_FACTORS];
    int nf=factor_root_distinct(root,root_factors);
    if(nf<1){
        fprintf(stderr,"root factorization failed\n");
        return 2;
    }

    uint8_t *sv=calloc(SIEVE_LIMIT+1,1);
    int *pr=malloc((SIEVE_LIMIT+1)*sizeof(int));
    int *rp=malloc((SIEVE_LIMIT+1)*sizeof(int));
    int *rm=malloc((SIEVE_LIMIT+1)*sizeof(int));
    if(!sv || !pr || !rp || !rm){
        fprintf(stderr,"allocation failed\n");
        return 2;
    }
    int np=0;
    for(int i=2;i<=SIEVE_LIMIT;i++) sv[i]=1;
    for(int i=2;i*i<=SIEVE_LIMIT;i++)
        if(sv[i])
            for(int j=i*i;j<=SIEVE_LIMIT;j+=i) sv[j]=0;
    for(int q=3;q<=SIEVE_LIMIT;q+=2){
        if(!sv[q] || target%(u64)q==0) continue;
        long inv=invmod((long)(target%(u64)q),q);
        pr[np]=q;
        rp[np]=(q-inv)%q;
        rm[np]=inv%q;
        np++;
    }
    free(sv);

    u64 segments=(stop-start+seg)/seg;
    unsigned long long total_surv=0;
    unsigned long long total_pell=0;
    unsigned long long total_prime=0;
    u64 best_k=UINT64_MAX,best_p=0;
    int best_sign=0,completed=0;
    double t0=omp_get_wtime();

    printf(
        "GATE root=%" PRIu64 " target=%" PRIu64
        " start=%" PRIu64 " stop=%" PRIu64
        " segment=%" PRIu64 " threads=%d\n",
        root,target,start,stop,seg,omp_get_max_threads());
    printf("ROOT_FACTORS");
    for(int i=0;i<nf;i++) printf(" %" PRIu64,root_factors[i]);
    printf("\n");
    fflush(stdout);

    #pragma omp parallel for schedule(dynamic)         reduction(+:total_surv,total_pell,total_prime)
    for(u64 si=0;si<segments;si++){
        u64 a=start+si*seg,b=a+seg-1;
        if(b>stop) b=stop;
        size_t L=(size_t)(b-a+1);
        uint8_t *cp=calloc(L,1),*cm=calloc(L,1);
        if(!cp || !cm){
            fprintf(stderr,"segment allocation failed\n");
            exit(2);
        }
        for(int z=0;z<np;z++){
            int q=pr[z];
            u64 offp=((u64)rp[z]+q-(a%(u64)q))%(u64)q;
            for(u64 idx=offp;idx<L;idx+=(u64)q) cp[idx]=1;
            u64 offm=((u64)rm[z]+q-(a%(u64)q))%(u64)q;
            for(u64 idx=offm;idx<L;idx+=(u64)q) cm[idx]=1;
        }

        for(size_t idx=0;idx<L;idx++){
            u64 k=a+(u64)idx;
            if(!cp[idx]){
                u64 p=k*target+1;
                if(sign_admissible(p,1)){
                    total_surv++;
                    if(exact_target_rank(
                        p,target,root_factors,nf)){
                        total_pell++;
                        if(isprime64(p)){
                            total_prime++;
                            #pragma omp critical
                            {
                                if(k<best_k){
                                    best_k=k;best_p=p;best_sign=1;
                                    printf(
                                        "HIT p=%" PRIu64
                                        " k=%" PRIu64 " sign=+1\n",
                                        p,k);
                                    fflush(stdout);
                                }
                            }
                        }
                    }
                }
            }
            if(!cm[idx]){
                u64 p=k*target-1;
                if(sign_admissible(p,-1)){
                    total_surv++;
                    if(exact_target_rank(
                        p,target,root_factors,nf)){
                        total_pell++;
                        if(isprime64(p)){
                            total_prime++;
                            #pragma omp critical
                            {
                                if(k<best_k){
                                    best_k=k;best_p=p;best_sign=-1;
                                    printf(
                                        "HIT p=%" PRIu64
                                        " k=%" PRIu64 " sign=-1\n",
                                        p,k);
                                    fflush(stdout);
                                }
                            }
                        }
                    }
                }
            }
        }
        free(cp);free(cm);
        #pragma omp atomic update
        completed++;
        int c;
        #pragma omp atomic read
        c=completed;
        if(c%25==0){
            #pragma omp critical
            {
                printf(
                    "PROGRESS segments=%d/%" PRIu64
                    " elapsed=%.1f\n",
                    c,segments,omp_get_wtime()-t0);
                fflush(stdout);
            }
        }
    }

    printf(
        "FINAL segments=%" PRIu64
        " survivors=%llu pell_hits=%llu prime_hits=%llu"
        " best_p=%" PRIu64 " best_k=%" PRIu64
        " best_sign=%d elapsed=%.3f\n",
        segments,total_surv,total_pell,total_prime,best_p,
        best_k==UINT64_MAX?0:best_k,best_sign,
        omp_get_wtime()-t0);
    free(pr);free(rp);free(rm);
    return 0;
}
