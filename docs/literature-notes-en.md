# Literature Reading and Method Boundaries

> Updated through **31 October 2026**. This index distils saved paper-tracking and reading reports. Reading coverage is stated explicitly: finishing a paper does not reproduce its experiments, and the discovery date is not the publication date.

## Use the index by research question

Start with the relevant method chapter, then use the papers to examine its assumptions. “Complete main text” describes the saved reading record; it does not imply that all data and code were obtained or executed.

| Question | Method notes | Reading entry |
|---|---|---|
| Does waveform similarity establish accurate strain amplitude? | [DAS principles](das-en.md), [cable coupling](cable-coupling-en.md) | [Cemented fibre experiment](#cemented-das) |
| Are channel differences repeatable, and do they identify coupling? | [Cable coupling](cable-coupling-en.md) | [Semblance Distance](#semblance-distance) |
| Does a stable spectral shape mean stable noise power? | [DAS principles](das-en.md) | [Seasonal borehole noise](#seasonal-noise) |
| How can P-wave and surface-wave observations constrain a common structure? | [Geometrical seismology](geom-seismic-en.md), [surface and coda waves](surface-coda-en.md), [VSP](vsp-en.md) | [Joint inversion](#joint-inversion) |
| How should direction, parameter trade-offs and search bounds be tested? | [F-K and Radon](fk-radon-en.md), [surface waves](surface-coda-en.md), [glacier seismology](glacier-en.md) | [Sea-ice example](#partial-reading) |

## Papers with complete main-text reading records

### Cemented fibre: separate waveform shape from amplitude calibration {#cemented-das}

**Forbriger et al. (2026), Measuring rock strain with distributed acoustic sensing (DAS) and cemented patch cables.** [Paper](https://doi.org/10.1093/gji/ggag423) · [Separate supplement](https://doi.org/10.5445/ir/1000198393). Online publication: 9 October 2026; main text and supplement read on 28 October. Some metadata records give 8 October; 9 October agrees with the paper's front page and online field.

Thin tight-buffered single-fibre cables cemented into a concrete groove were compared with calibrated strainmeters about 350 m away. The useful design separates waveform correlation from amplitude regression, after matching physical quantity, polarity, timing and frequency band. High correlation alone does not establish accurate amplitude.

**Boundary:** the 0.02–0.2 Hz comparison has an independent rock-strain reference; results extending to 14 Hz mainly compare interrogators with each other. These do not establish absolute rock-strain calibration over the full band. Neighbouring channels may share much of their gauge length and are not independent replicates. Common-mode subtraction using a mechanically decoupled reference coil does not justify subtracting the mean of all valid borehole channels. The installation does not calibrate armoured cables or sand-backfilled boreholes.

### Semblance Distance: retain the validation design and the formula caveat {#semblance-distance}

**Rading et al. (2026), Semblance Distance Analysis for Channel Quality Assessment in Distributed Acoustic Sensing.** [arXiv:2610.30401v1](https://arxiv.org/abs/2610.30401v1). First submitted on 21 October 2026 UTC; the v1 main text, figures, tables and official TeX were read on 28 October. This is a preprint; template DOI fields do not establish journal publication.

Comparing the same network across earthquakes, a drop-weight source and monthly records is a useful way to test whether spatial anomalies recur. Differences can also arise from the wavefield, orientation, installation, instrument and local sources. They do not directly measure coupling stiffness.

**Reproduction caveat:** as printed in v1 equation (2), the numerator and denominator contain the same energy sum for real signals and their Hilbert transforms, so the reference reduces to $1/N$ when energy is nonzero. Equation (4) instead gives 1 for identical channels. This is an algebraic check of the public formulas, not evidence of which implementation generated the figures. Code or an erratum is needed before adopting the calculation. Dynamic time warping can also absorb genuine propagation delays; preserve the original timing information for structural analysis.

### Seasonal borehole noise: measure power and shape together {#seasonal-noise}

**Fan et al. (2026), Winter-to-spring changes in borehole seismic noise beneath permafrost in the northeastern Tibetan Plateau.** [Research Square v1](https://doi.org/10.21203/rs.3.rs-11247202/v1). Posted on 22 October 2026; main text and supplement read on 28 October. This version has not undergone journal peer review.

The study uses the vertical component of a conventional seismometer at approximately 300 m depth. Its transferable lesson is to report strength, spectral shape and valid-window counts together: PSD and band power describe strength, while normalised spectra and spectral entropy describe how power is distributed. Compare them using the same valid time windows.

With $p_i=P_i/\sum_jP_j$, normalised spectral entropy is $SE=-\sum_i p_i\ln p_i/\ln N$. Scaling every linear power value by the same constant changes neither the fractions nor the entropy. Stable entropy therefore does not imply stable power. Fix the band, frequency grid and units; do not normalise dB values as if they were linear powers.

**Boundary:** one sensor, one component and one winter-to-spring interval do not resolve a noise-depth profile or separate source, path and receiver changes. The paper does not demonstrate thaw-driven changes or seasonal DAS coupling. Its velocity/acceleration spectra and selected bands cannot be copied directly to strain-rate measurements.

### Refraction–dispersion inversion: inspect the common model and error definition {#joint-inversion}

**Wang, Le & Huo (2026), Reverse-learning-enhanced sine cosine algorithm for joint inversion of seismic refraction and Rayleigh-wave dispersion data.** [Publisher](https://accscience.com/journal/JSE/articles/online_first/9493) · [DOI](https://doi.org/10.36922/jse026290140). Online on 28 October 2026; the current Online First main text was read on 31 October.

First arrivals and fundamental-mode Rayleigh dispersion share layer thicknesses, $V_P$ and $V_S$ in a one-dimensional horizontally layered model. The objective is an equally weighted sum of two relative-residual RMS terms, not one RMS over pooled residuals and not pointwise variance weighting. Report each data type's residuals in physical units, individual versus joint inversion, and model-recovery error separately.

**Boundary:** scatter across 30 optimisation runs measures search repeatability, not posterior geological uncertainty. Field reference models use the same source data and informed search bounds, so they are not independent truth. The saved reading audit found some statistical combinations in tables 1 and 3 incompatible with their stated definitions. Retain the joint-modelling framework, but defer strong claims of superior optimiser accuracy or stability until run-level outputs or corrections resolve these issues. The paper supplies no borehole-trajectory, gauge-averaging or DAS coupling operator.

## Partial text, abstracts and metadata leads {#partial-reading}

| Paper and reading date | Material actually available | Useful question and boundary |
|---|---|---|
| Baker et al. (2026), [sea-ice thickness from flexural-gravity waves recorded by seafloor DAS](https://doi.org/10.1785/0220260056); 30 October | Publisher text, equations, tables and captions; original images, PDF and supplement pending | Examine directional projection, thickness–modulus trade-offs, bounds and external validation. Floating ice and water are not a borehole Rayleigh-wave system; their depth response cannot replace an elastic surface-wave kernel. A misfit surface is not automatically a probability posterior. Online on 28 October. |
| Ma et al. (2026), [near-surface characterisation using local seismic signals](https://doi.org/10.1785/0220260078); 30 October | Abstract | The authors propose footstep detection, subarray dispersion-spectrum stacking and structural inversion. Detector details, acquisition parameters, accuracy and borehole applicability await the full text. Online on 28 October. |
| Zhong et al. (2026), [inter-well fracture interactions using fibre sensing and multiphysics modelling](https://doi.org/10.1002/nag.70467); 31 October | Abstract | Distinguish DAS event/qualitative constraints from DTS temperature comparisons. They do not jointly establish quantitative DAS validation. Thermal–hydraulic–mechanical mechanisms and errors require the main text. Online on 28 October. |
| [Integrated DAS-VSP and borehole DAS ambient noise for high-resolution near-wellbore characterization in geologic carbon storage systems](https://doi.org/10.1016/j.ijggc.2026.104824); discovered 31 October | Metadata only; no abstract | Active/passive integration is a title-based lead, not a verified method or result. The first-online date remains unresolved; the December 2026 issue date is not a precise publication timestamp. |

## Follow-up priorities and coverage gaps

The saved material from 27–31 October 2026 contains **four complete main-text reading records, one partial-text report, two abstract reports and one metadata lead**. Dataset, software and supplement records viewed only as metadata are not additional fully read research papers.

This is a selective reading index. Results were saved for specified OpenAlex queries; later arXiv runs encountered rate limits and timeouts, leaving version checks incomplete. Other databases, earlier classics and earlier-preprint relationships were not exhaustively covered. A run with no recommendation does not establish that the field has no new work.

For pending papers, verify measurement quantity, geometry and independent validation before transferring algorithms. For SemD and ESCA, resolve formula or statistical definitions before reproduction. Every durable method note should distinguish the observation, the model-based inference and factors that were not independently controlled.
