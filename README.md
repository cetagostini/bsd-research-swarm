# BSD Research Swarm

**A distributed multi-agent research effort attacking the Birch and Swinnerton-Dyer Conjecture**

## The Problem

The Birch and Swinnerton-Dyer (BSD) Conjecture — a Clay Millennium Prize Problem ($1M) — states:

> For an elliptic curve $E/\mathbb{Q}$, the analytic rank of $L(E,s)$ at $s=1$ equals the algebraic rank of $E(\mathbb{Q})$, and the leading Taylor coefficient is given by the BSD formula involving the period $\Omega$, regulator $R$, Tamagawa numbers $c_v$, the order of the Tate-Shafarevich group $|\text{III}|$, and the torsion subgroup $|E(\mathbb{Q})_{\text{tors}}|$:

$$\frac{L^{(r)}(E,1)}{r!} = \frac{\Omega \cdot R \cdot |\text{III}| \cdot \prod c_v}{|E(\mathbb{Q})_{\text{tors}}|^2}$$

### What's Proven
- **Rank 0 and 1:** Weak BSD established via Gross-Zagier, Kolyvagin, and Skinner-Urban (conditional on GRH)
- **Modularity:** All elliptic curves over $\mathbb{Q}$ are modular (Wiles, Taylor-Wiles, Breuil-Conrad-Diamond-Taylor)
- **Finiteness of III:** Known for rank 0 and 1 (Kato, 2004)

### What's Open
- General rank $\geq 2$
- Finiteness of $\text{III}$ for rank $\geq 2$
- The strong BSD formula for rank $\geq 2$

## Architecture

This project organizes 115 research directions into 10 independent research groups:

| Group | Name | Directions | Branch |
|-------|------|------------|--------|
| A | Iwasawa Theory | 12 | `group-a-iwasawa` |
| B | Euler Systems | 12 | `group-b-euler-systems` |
| C | Arithmetic Statistics | 12 | `group-c-arithmetic-statistics` |
| D | Tate-Shafarevich Group | 12 | `group-d-tate-shafarevich` |
| E | p-adic Methods | 11 | `group-e-padic-methods` |
| F | Motivic/Cohomological | 12 | `group-f-motivic-cohomological` |
| G | Deformation/Langlands | 11 | `group-g-deformation-langlands` |
| H | Computational | 11 | `group-h-computational` |
| I | Connections | 10 | `group-i-connections` |
| J | Unconventional | 12 | `group-j-unconventional` |

## Swarm Model

**Two-tier hierarchy:**
- **Research Director** (Main): Generates directions, assigns groups, cross-pollinates, maintains `main` branch
- **Group Leaders** (10 agents): Each leads a group with 20-50 internal researcher agents, one per direction

**Cross-pollination:** Status updates flow from group branches → main → other groups, identifying collaboration opportunities.

## Repository Structure

```
main branch:
├── README.md              # This file
├── DIRECTIONS.md          # Full list of 115 research directions
├── STATUS.md              # Live dashboard
└── groups/
    ├── a-iwasawa/
    │   ├── README.md       # Group overview
    │   ├── directions/     # One .md per direction
    │   ├── results/        # Lemmas, theorems, computations
    │   └── formal/         # Lean 4 fragments
    ├── b-euler-systems/
    │   └── ...
    └── ... (through group-j-unconventional)
```

## Verification Standards

Every result is classified:
- **Theorem:** Formal proof (Lean 4 verified or peer-reviewed)
- **Lemma:** Proven within the research program
- **Conjecture:** Testable prediction, computationally verified for examples
- **Experiment:** Computational result with code and data
- **Speculation:** Theoretically motivated guess with stated requirements

## Contributing

Each group works on its own branch. Progress merges to `main` via PR with:
- What was explored
- What was found (promising directions, dead ends, computations)
- Evidence (code, Lean fragments, citations)

## Status

See [STATUS.md](STATUS.md) for the live dashboard.

## License

This is open research. All results, computations, and formal proofs are publicly available.
