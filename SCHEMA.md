# Atlas Schema

Each numeric record contains:

- `n`: integer input;
- `rank`: verified Pell rank;
- `square_rank_root`: $C$ when rank is $C^2$, otherwise null;
- `role`: one or more atlas roles;
- `status`: validation label;
- `notes`: short provenance or structural note.

Each relation contains:

- `relation_id`;
- `kind`;
- `members`;
- `rank` when applicable;
- `status`;
- `statement`.

## Validation labels

`VERIFIED_COMPUTATION` means the rank is recomputed by exact modular recurrence in the repository tests.

`DERIVED_RELATION` means the statement follows algebraically from explicitly listed assumptions.

`KNOWN_THEORY` is reserved for externally sourced theorems.

`RESEARCH_CANDIDATE` is not a theorem claim.
