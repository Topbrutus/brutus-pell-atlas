# Brutus–Pell Post-Frontier Attack A1

Date: 2026-09-30  
Author: Gabriel St-Pierre  
Status: VERIFIED_COMPUTATION / NEGATIVE_BOUNDED_RESULT

This note records the first bounded continuation immediately beyond the previously documented compiled frontier k <= 10^10 for gates 47, 71, and 83.

It is not a nonexistence theorem.

## Search interval

For each gate q in {47,71,83}, scan:

- start_k = 10,000,000,001
- end_k = 10,000,100,000
- target rank = q^2
- candidate form = p = k q^2 +/- 1
- Gate-8 congruence filter retained
- deterministic 64-bit primality test
- exact Pell target-rank test

## Results

| gate q | target q^2 | prime candidates tested | exact-rank hits |
|---:|---:|---:|---:|
| 47 | 2209 | 1,673 | 0 |
| 71 | 5041 | 1,590 | 0 |
| 83 | 6889 | 1,590 | 0 |

Total prime candidates tested: **4,853**.  
Total exact-rank hits: **0**.

Therefore the documented bounded no-hit frontier is extended from k <= 10^10 to:

k <= 10,000,100,000

for these three gates.

## First legal prime controls after k = 10^10

The first prime candidate encountered on a legal Gate-8 rail for each selected gate was also checked independently:

| gate | sign | k | p | prime | P_(q^2) mod p | exact rank q^2 |
|---:|---:|---:|---:|---|---:|---|
| 47 | +1 | 10,000,000,072 | 22,090,000,159,049 | yes | 6,785,485,971,658 | no |
| 71 | -1 | 10,000,000,038 | 50,410,000,191,557 | yes | 15,070,090,373,130 | no |
| 83 | -1 | 10,000,000,038 | 68,890,000,261,781 | yes | 45,244,365,050,142 | no |

These three primes are **negative controls**, not witnesses.

## ZELSTÉRÉOS attack context

The roots 47, 71, and 83 were also sent through the visible/audible ZELSTÉRÉOS session as a sequential triple attack.

Each root returned:

- status PASS;
- verdict RESISTE;
- 1,413 Z transformations;
- 16,956 active Zenodo formula evaluations;
- 5,301 F006 checks;
- 1,296 / 1,296 inverse reconstruction;
- 23,670 calculation events.

These ZELSTÉRÉOS results are machine-trace context only. They do **not** establish the Pell gate-witness property.

The three post-frontier prime controls were then queued into the same visible/audible machine as the next attack salve.

## Boundary

A bounded negative scan proves only that no explicit witness was found in the stated finite interval.

It does not contradict primitive-divisor existence and must not be described as proof of nonexistence.
