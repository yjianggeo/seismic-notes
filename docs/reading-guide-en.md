# Learning paths and concept index

The central question is what seismic records measure after source, propagation, receiver and processing effects—and which parameters those records can constrain.

## Suggested path

| Stage | Reading order | Main question |
|---|---|---|
| Foundations and propagation | [Geometry](geom-seismic-en.md) → [Brune source model](brune-en.md) → [Spectral-ratio Q](q-spectral-ratio-en.md) | How do apparent speed, source spectra and attenuation differ? |
| Measurement and coupling | [DAS](das-en.md) → [Cable coupling](cable-coupling-en.md) | What is measured, and how do direction, gauge and mechanical transfer affect it? |
| Processing and interpretation | [Field workflow](field-workflow-en.md) → [F-K / Radon](fk-radon-en.md) → [VSP](vsp-en.md) | Is a packet real, which direction does it travel, and does it justify inversion? |
| Structure and monitoring | [Surface waves and coda](surface-coda-en.md) → [Borehole Rayleigh waves](borehole-rayleigh-en.md) → [Cryoseismology](glacier-en.md) | What do dispersion, depth response and temporal change constrain? |
| Literature | [Reading index](literature-notes-en.md) | Which methods have full-text support and which require further reading? |

## Start from a practical question

| Question | Entry point |
|---|---|
| Which files and time window should I download? | [Field inventory and time windows](field-workflow-en.md) |
| Why is a P window downgoing, or S difficult to identify? | [Mixed-wavefield interpretation](field-workflow-en.md) → [VSP](vsp-en.md) |
| Is low-frequency dominance physical or caused by processing? | [Array averaging](field-workflow-en.md) → [Gauge response](das-en.md) |
| Does larger cable amplitude imply better coupling? | [Coupling diagnostics](cable-coupling-en.md) |
| Does a depth minimum or phase reversal identify a Rayleigh mode? | [Borehole Rayleigh waves](borehole-rayleigh-en.md) |
| How can dispersion, depth response and priors constrain velocity? | [Surface-wave inversion](surface-coda-en.md) → [Borehole identifiability](borehole-rayleigh-en.md) |
| How can small medium changes be monitored? | [Coda interferometry](surface-coda-en.md) → [Glacier monitoring](glacier-en.md) |

## Distinguish these quantities

| Quantity | Definition | Do not equate it with |
|---|---|---|
| Displacement \(u\) | Particle displacement, m | DAS strain or strain rate |
| Strain \(\varepsilon\) | Symmetric displacement gradient, dimensionless | Displacement eigenfunction |
| Strain rate \(\dot\varepsilon\) | Time derivative of strain, s⁻¹ | Particle velocity |
| Gauge length \(L_g\) | Single-channel spatial averaging length | Channel spacing or whole-array aperture |
| Along-well distance \(\ell\) | Trajectory arc length | True vertical depth \(z\) |
| Along-well slowness \(q\) | \(dt/d\ell=\mathbf p\cdot\mathbf t\), s/m | Reciprocal material velocity |
| Phase speed \(c\) | Speed of equal-phase surfaces | Packet group speed \(U\) |
| Coherence | Consistency under a stated spectral/spatial definition | Amplitude, stiffness or detection significance |
| BI / state indicator | Proxy conditional on bands, normalization and environment | Universal burial depth or transfer coefficient |
| Prior model | External constraints on parameter ranges | Independently recovered structure |

## Reading conventions

State measurement units, coordinates, signs and the sinc convention before comparing formulas. Separate observations from interpretations and inversions. A wave packet or correlation peak is an observation; phase identity and mechanism require comparison; velocity and coupling parameters require a forward model, uncertainty and resolution checks.

Use the header language button for paired Chinese/English pages. Read formulas with their assumptions. Teaching illustrations and feasibility syntheses do not replace observations; the [literature index](literature-notes-en.md) records the scope of recent readings.
