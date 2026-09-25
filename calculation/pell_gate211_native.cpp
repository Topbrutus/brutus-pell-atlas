#include <bits/stdc++.h>
#include <omp.h>
using namespace std;
using u64 = uint64_t;
using u128 = __uint128_t;

static const u64 R = 44521ULL;
static inline u64 mulmod(u64 a,u64 b,u64 m){ return (u64)((u128)a*b % m); }
static u64 powmod(u64 a,u64 e,u64 m){ u64 r=1; while(e){ if(e&1) r=mulmod(r,a,m); a=mulmod(a,a,m); e>>=1; } return r; }

static bool isprime(u64 n){
  if(n<2) return false;
  static const u64 small[]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97};
  for(u64 p:small){ if(n==p) return true; if(n%p==0) return false; }
  u64 d=n-1; int s=0; while((d&1)==0){ d>>=1; ++s; }
  static const u64 bases[]={2,325,9375,28178,450775,9780504,1795265022ULL};
  for(u64 aa:bases){
    u64 a=aa%n; if(a==0) continue; u64 x=powmod(a,d,n); if(x==1||x==n-1) continue;
    bool composite=true; for(int r=1;r<s;r++){ x=mulmod(x,x,n); if(x==n-1){ composite=false; break; } }
    if(composite) return false;
  }
  return true;
}

struct M{u64 a,b,c,d;};
static inline M mmul(const M&x,const M&y,u64 m){
  return {(mulmod(x.a,y.a,m)+mulmod(x.b,y.c,m))%m,
          (mulmod(x.a,y.b,m)+mulmod(x.b,y.d,m))%m,
          (mulmod(x.c,y.a,m)+mulmod(x.d,y.c,m))%m,
          (mulmod(x.c,y.b,m)+mulmod(x.d,y.d,m))%m};
}
static u64 pellmod(u64 n,u64 m){ M r{1,0,0,1},q{2,1,1,0}; while(n){ if(n&1) r=mmul(r,q,m); q=mmul(q,q,m); n>>=1; } return r.b%m; }
static inline bool exactrank(u64 p){ return pellmod(R,p)==0 && pellmod(211,p)!=0; }

int main(int argc,char**argv){
  if(argc<3){ cerr<<"usage: pell_gate211_native START_K STOP_K\n"; return 2; }
  u64 start=strtoull(argv[1],nullptr,10), stop=strtoull(argv[2],nullptr,10);
  if(start<1 || stop<start){ cerr<<"invalid range\n"; return 2; }
  const int residues[4]={0,6,6,4};
  const int signs[4]={+1,+1,-1,-1};
  u64 j0=start/8, j1=stop/8+1, bestk=ULLONG_MAX, bestp=0; int bests=0;
  unsigned long long checked=0; double t0=omp_get_wtime();
#pragma omp parallel for schedule(static) reduction(+:checked)
  for(long long jj=(long long)j0; jj<=(long long)j1; ++jj){
    u64 j=(u64)jj;
    for(int z=0; z<4; ++z){
      u64 k=8*j+(u64)residues[z]; if(k<start||k>stop) continue;
      u128 raw=(u128)k*R; raw = signs[z]>0 ? raw+1 : raw-1;
      if(raw>numeric_limits<u64>::max() || raw<=2) continue;
      u64 p=(u64)raw; if(!isprime(p)) continue; ++checked;
      if(exactrank(p)){
#pragma omp critical
        { if(k<bestk || (k==bestk && p<bestp)){ bestk=k; bestp=p; bests=signs[z]; } }
      }
    }
  }
  double dt=omp_get_wtime()-t0;
  cout<<"checked="<<checked<<" seconds="<<fixed<<setprecision(3)<<dt;
  if(bestk!=ULLONG_MAX) cout<<" hit_p="<<bestp<<" hit_k="<<bestk<<" sign="<<bests; else cout<<" hit=NONE";
  cout<<"\n"; return 0;
}
