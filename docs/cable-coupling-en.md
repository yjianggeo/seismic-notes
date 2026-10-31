# Detecting and Assessing DAS Cable Coupling State

> Keywords: DAS, cable coupling, installation state, Poincaré spectral coherence, Burial Index (BI), validation

## Introduction

The [DAS fundamentals](das-en.md) chapter separates formation-to-jacket and jacket-to-fibre transfer. Installation, geometry, wavefield and optical response all affect a recorded trace. This chapter asks which data-derived indicators support which coupling interpretations and how those interpretations can be tested. Label-free calculation does not remove the need for independent validation.

## Define the Evaluation Target First

| Target | Example output | Matching validation |
|---|---|---|
| Task-specific channel quality | SNR, reliability, earthquake usability probability | Independent detection, picking or location performance |
| Installation/contact-state proxy | Burial, exposure, suspension or change | Engineering records, diver surveys, controlled state changes |
| Relative amplitude/phase response | Gain and phase relative to reference | Comparable wavefields, reference sensitivity and repeated events |
| Band-limited strain transfer | Regression or complex transfer against reference strain | Calibrated strain reference with matched direction and scale |

These outputs are not interchangeable. For noiseless $y=0.2x$, correlation and magnitude-squared coherence can both be one while the amplitude ratio is 0.2. Knowing an installation category such as fine/coarse backfill does not supply a mechanical-transfer ground truth. [Forbriger et al. (2025)](https://doi.org/10.1785/0220240308)

## Four Coupling States and Their Physical Effects

| State | Mechanical constraint | Possible response |
|---|---|---|
| Buried | Sediment confinement changes mass, stiffness and damping | High-frequency water-driven motion may be suppressed; ground-strain transfer may improve |
| Partially buried | Intermediate or intermittent contact | Spatially variable transition |
| Exposed | Hydrodynamic forcing plus seabed contact | Potentially broadband response, depending on contact and forcing |
| Suspended/free span | Endpoints, tension and bending stiffness constrain an unsupported span | VIV or cable resonance dependent on current, span and tension |

These are scenario-dependent interpretations, not universal spectral templates. Amplitude bands can also arise from seabed stiffness in a well-buried cable. Marine frequency bands and thresholds should not be transplanted directly into a backfilled borehole.

!!! note "Quality depends on the observation goal"
    Stable contact is generally desirable for ground-strain amplitudes. A suspended span may instead be useful for current sensing through vibration. “Well coupled” and “high quality” therefore need a target quantity and frequency band.

## Overview of Coupling-State Detection Methods

| Method | Observable | Strength | Main limitation |
|---|---|---|---|
| Neighbour coherency, Hudson et al. (2025) | Relative coherency with reference calibration | Noise/event applications and amplitude examples | Comparable wavefields needed; geometry, common noise and heterogeneity interfere |
| Spectral clustering/correlation, Yin et al. (2024) | Ringing and anomalous spectra | Automated borehole VSP screening | Shared ringing may evade detection; local thresholds |
| Repeated excitation, Muñoz et al. (2023) | Same-location repeatability across events | Finds stable observation positions | Source type, speed and direction must be comparable |
| Vessel band energy, Harmon et al. (2025) | Single/double envelope peaks and band energy | Physical response interpretation | Suitable source trajectory and SNR; some state labels inferred |
| Resonance analysis | Spectral peaks and vibration modes | Mechanism-sensitive evidence | Depends on boundary conditions, forcing and structure |
| Reference-wavefield comparison | Effective complex transfer | Amplitude and phase evaluation | Independent reference or adequate wavefield model |
| Poincaré spectral coherence, Shiri and Belal (2026) | Spread/gradient of two-band fingerprints | Label-free, lightweight mapping | Site-specific bands; BI is a relative proxy |

### Difference from Conventional Coherence and Reliability

Standard **magnitude-squared coherence** uses averaged auto- and cross-spectra:

$$
\gamma^2_{ij}(f)=\frac{|S_{ij}(f)|^2}{S_{ii}(f)S_{jj}(f)},\qquad 0\leq\gamma^2\leq1.
$$

A single unaveraged Fourier realization degenerates to unit coherence at nonzero bins. State the Welch/multitaper averaging scheme. The Poincaré statistic discards phase, compresses band powers into fingerprints and evaluates a **spatial spread/gradient ratio**. It is neither MSC nor naturally bounded by one. Hudson's method has its own time-domain normalization and lag definitions; replacing it with Pearson correlation or MSC is not a faithful reproduction.

PCCF reliability, CQI and ORION primarily validate channel selection and downstream tasks. They are useful baselines, but task quality does not automatically measure absolute mechanical transfer. [Muñoz and Soto (2022)](https://doi.org/10.1038/s41467-022-31681-x), [Rodriguez et al. (2025)](https://doi.org/10.1109/JSTARS.2025.3593330), [Bozzi et al. (2026)](https://doi.org/10.26443/seismica.v5i1.2251)

## The Poincaré Spectral-Coherence Framework

Shiri and Belal (2026) construct a coupling-state proxy using short-time FFTs and spatial block statistics, followed by robust normalization, smoothing and temporal aggregation.

### Stage 1: Two-Band Spectral Fingerprints

Split traces into overlapping 2–4 s windows and apply a Hann taper:

$$
h[n]=\tfrac12\left(1-\cos\frac{2\pi n}{N_t^{(w)}-1}\right),
\qquad \tilde y_i^{(w)}[n]=y_i^{(w)}[n]h[n].
$$

Sum Fourier power over the actual bins $K_k$ of each band:

$$
P_{i,k}^{(w)}=\sum_{\ell\in K_k}|\hat y_i^{(w)}[\ell]|^2,\qquad
\mathbf f_i^{(w)}=
\frac{[P_{i,1}^{(w)},P_{i,2}^{(w)}]^{\mathsf T}}
{P_{i,1}^{(w)}+P_{i,2}^{(w)}+\varepsilon_1}.
$$

The paper's lower-band text says 0.01–10 Hz while equation (5) says 0.1–10 Hz; record the implemented choice. A 2–4 s window has approximately 0.5–0.25 Hz Fourier-bin spacing, so it does **not** independently resolve 0.01 Hz or tidal periods. Its higher example band, 100–120 Hz, targets intermittent vessel/hydrodynamic/cable vibration.

!!! note "Band selection is site-specific"
    Select bands on development data, then freeze them for independent dates/events. Respect Nyquist and anti-alias filtering. Retuning on the validation section boundaries does not demonstrate generalization.

### Stage 2: The Poincaré-Type Spatial Coherence Coefficient

For a block $I_b$ of $M$ channels with mean fingerprint $\bar{\mathbf f}$,

$$
\mathrm{Spread}=
\sqrt{\frac1M\sum_{i\in I_b}\|\mathbf f_i-\bar{\mathbf f}\|_2^2},
\qquad
\mathrm{Grad}=
\sqrt{\frac1{M-1}\sum_{i\in I_b\setminus\{\mathrm{last}\}}
\|\mathbf f_{i+1}-\mathbf f_i\|_2^2}.
$$

The normalized fingerprint scale supplies a gradient floor:

$$
\mathrm{Scale}=\sqrt{\frac1M\sum_{i\in I_b}\|\mathbf f_i\|_2^2},
\quad \mathrm{Grad}_{\rm eff}=\max(\mathrm{Grad},\alpha\,\mathrm{Scale}),
\quad
\boxed{C_{\rm eff}=\frac{\mathrm{Spread}}{\mathrm{Grad}_{\rm eff}+\varepsilon_2}}.
$$

The paper uses $\alpha=0.05$ and reports stable results for 0.01–0.1 in its datasets. Other deployments need their own sensitivity checks.

!!! tip "Why 'Poincaré'?"
    Poincaré inequalities relate variability to gradient magnitude. Here the ratio compares block-scale variation with neighbour-scale variation. A common multiplicative gain leaves normalized fingerprints nearly unchanged, but source spectral shape, additive noise and spatially heterogeneous forcing need not cancel.

!!! warning "The high-value interpretation is empirical"
    The paper associates high BI with exposed/weakly constrained sections at its sites. The printed spread/gradient ratio is not mathematically monotonic in every notion of spatial roughness. Ignoring the floor, an $M$-channel linear ramp gives $\sqrt{(M^2-1)/12}$ while a balanced alternating sequence gives $1/2$; for $M=10$, these are about 2.87 and 0.5. A smooth ramp can therefore score above rapid alternation. An exactly constant fingerprint has zero spread and zero index.

    Preserve the reported high/low BI association as a **site observation**, not a universal proof of coupling. Do not silently invert the ratio and call that the original method.

### Stage 3: Robust log–MAD–exp Normalisation

Let $C_{\rm raw}[w,b]=C_{\rm eff}^{(w,b)}$. Define

$$
L=\log(C_{\rm raw}+\varepsilon_3),\qquad
Z_L=\frac{L-m_L}{1.4826\,\mathrm{MAD}_L+\varepsilon_3},
\qquad C_{\rm norm}=\exp(Z_L),
$$

with $m_L=\operatorname{median}(L)$ and $\mathrm{MAD}_L=\operatorname{median}|L-m_L|$. State which windows/blocks define these statistics. The factor 1.4826 supplies a conventional reference scale without imposing normality. Robust scaling does not physically eliminate environmental or instrument confounding.

### Stage 4: Spatial Smoothing and the Burial Index (BI)

Smooth along the **block axis**, using block-centre spacing $\Delta x_b$:

$$
\sigma_b=L_{\rm smooth}/\Delta x_b,\qquad
C_{\rm smooth}[w,b]=\sum_k g_{\sigma_b}(b-k)C_{\rm norm}[w,k],
\qquad
\boxed{\mathrm{BI}(b)=\operatorname{median}_w C_{\rm smooth}[w,b]}.
$$

For non-overlapping $M$-channel blocks, $\Delta x_b=M\Delta x$; do not substitute single-channel spacing. Reflective end padding is a numerical boundary convention, not a physical reflection.

!!! warning "BI is a proxy, not burial depth"
    BI does not directly measure burial depth, contact stiffness or strain-transfer efficiency. Bathymetry, sediment, forcing, protective structures and free spans can all affect the pattern. Coherent common vibration can also coexist with poor ground-strain fidelity.

### Cross-Period Comparison and Reproducibility

- Preserve raw band powers, fingerprints, $C_{\rm eff}$, normalization median/MAD, masks and actual window times. BI values normalized independently per period cannot be directly compared; monitoring needs a fixed development-period reference and checks of unnormalized quantities.
- Select actual FFT bins with explicit endpoint rules. Avoid duplicate bins or rounding during band scans. Zero padding refines plotted bins, not the true window-limited resolution.
- Mask near-zero energy, missing-data padding, saturation and dropouts. Dimensionless fingerprints do not replace PSD/RMS calibration.
- Overlapping gauges can inflate neighbour similarity. Gauge length, block width, block stride and smoothing jointly limit spatial resolution. Treat boundary-crossing blocks separately.
- Track windows across file boundaries, gaps and clock conventions explicitly. Do not concatenate per-file edge-trimmed windows as if they formed a gapless uniform time series. See [field workflow](field-workflow-en.md).

## Field Validation

The study applies the method to EMEC Eday and OBSEA.

| Parameter | EMEC Eday | OBSEA |
|---|---|---|
| Cable length | About 2.2 km | About 5.8 km |
| Channels/spacing | 1083 / 2.04 m | 4560 / 1.275 m |
| Sampling/gauge length | 1 kHz / 10 m | 2 kHz / 20 m |
| Context | Strong tidal currents, heterogeneous seabed | Sediment-dominated coastal setting |
| Independent context | Geological units and aerial imagery | Some diver/vessel-reported states |

The EMEC response corresponds to mapped geological transitions, but geological context is not a channel-by-channel mechanical ground truth.

For OBSEA, the paper labels intervals as onshore, **suspected buried**, **unknown**, and unburied. The reported ranges overlap or leave gaps; retain that uncertainty rather than calling the whole profile diver-verified classification. The observed spectra support site-specific response differences, not a universal BI threshold.

Reported runtime supports computational feasibility in the stated environment. It does not establish long-term alarm delay, false-alarm rate or transfer performance at a new site.

## Artefacts and Pitfalls

!!! danger "Check instrumental artefacts"
    Optical-end reflections, phase fading, slack, gain changes, saturation and channel dropouts can create spectral or spatial anomalies. Inspect their acquisition context before assigning mechanical meaning.

Raw time–distance plots remain useful for propagation and artefact checks, but do not alone determine contact state. Water depth and roughness alter forcing as well as contact, and coherent guided waves can resemble stable ground signals.

## Limitations and Outlook

A relative state map can inform selection, but quantitative burial or stiffness inversion needs a calibrated model and matching independent measurements. Existing work already includes automatic screening, state labels, reference calibration and downstream-task validation; research gaps should concern specific unresolved confounders and generalization conditions, rather than claim that no quantitative methods exist.

## Transfer to Borehole Observations

Build a channel-to-cable-distance, measured-depth, true-vertical-depth and three-dimensional tangent mapping. DAS measures $\varepsilon_\parallel=\mathbf t^{\mathsf T}\boldsymbol\varepsilon\mathbf t$. Surface and borehole segments have different orientations; amplitude ordering alone cannot rank their coupling. Near a directional zero, reduce confidence instead of dividing by a near-zero factor.

For a narrowband packet confined to one backfill interval, test consistent up/down moveout, stable spatial nodes, pre-event modes, boundary energy changes and reflection travel times. A single along-cable apparent phase speed around 1.4 km/s cannot distinguish water acoustics, formation P waves or tube waves. Water in porous backfill does not automatically supply an open liquid-column waveguide. Completion, water-level, pressure or operational records are needed. See [field interpretation](field-workflow-en.md).

### Minimum Validation and Statistical Requirements

1. **Synthetic isolation:** vary receiver gain, phase, source spectrum, incidence, noise and local structure independently; measure false attribution to coupling.
2. **External state comparison:** installation categories support segmentation, not a forced “suspended < surface < fine sand < coarse sand” quality ordering. Depth and geology confound grain size.
3. **Whole-event/whole-period holdout:** freeze bands, thresholds and normalization; split by event/date to avoid leakage through neighbouring channels and overlapping windows.
4. **Independent task benefit:** select channels using noise metrics and evaluate unseen earthquakes using detection, blinded picks or arrival residuals, controlling channel count and aperture. Do not validate only with the same coherence used to construct the score.
5. **Temporal confounders:** track configuration, source spectrum/direction, weather and coverage. Gaps are not observations. Use event/day or temporal-block uncertainty, not thousands of correlated channels as independent repeats.

Without an independent reference, report relative receiver response or coupling-related anomalies. Absolute transfer, freeze–thaw causality or post-earthquake mechanical change needs matching evidence. Surface air temperature is not deep-borehole temperature; disconnected winter/spring and summer/autumn campaigns do not by themselves establish a repeatable annual cycle.

## References

- Shiri, H., & Belal, M. (2026). A real-time framework for mapping subsea cable burial state using Poincaré spectral coherence of DAS measurements. *Scientific Reports*, 16, 23647. [DOI](https://doi.org/10.1038/s41598-026-59846-4). Framework checked against full-text equations (5), (11)–(26); reproduction caveats above.
- Hudson, T., Stork, A., Muir, J., & Fichtner, A. (2025). Unlocking DAS amplitude information through coherency coupling quantification. *Seismica*, 4(1). [DOI](https://doi.org/10.26443/seismica.v4i1.1488).
- Forbriger, T., et al. (2025). Calibration of the Strain Amplitude Recorded with DAS Using a Strainmeter Array. *Seismological Research Letters*, 96, 2356–2367. [DOI](https://doi.org/10.1785/0220240308); [author full text](https://arxiv.org/html/2408.01151v3).
- Muir, J. B., & Zhan, Z. (2022). Wavefield-based evaluation of DAS instrument response and array design. *Geophysical Journal International*. [DOI](https://doi.org/10.1093/gji/ggab439).
- Yin, J., Mizuno, T., & Le Calvez, J. (2024). Using the amplitude spectrum to characterize cable coupling of DAS traces. *IMAGE Expanded Abstracts*. [DOI](https://doi.org/10.1190/image2024-4094798.1).
- Muñoz, F., et al. (2023). Finding Well-Coupled Optical Fiber Locations for Railway Monitoring Using Distributed Acoustic Sensing. *Sensors*, 23, 6599. [DOI](https://doi.org/10.3390/s23146599). Partial-text evidence in this review.
- Harmon, N., et al. (2025). Distributed Acoustic Sensing Along a Shallow Water Energy Cable. *IEEE Journal of Oceanic Engineering*. [DOI](https://doi.org/10.1109/JOE.2024.3523363).
- Muñoz, F., & Soto, M. A. (2022). Enhancing fibre-optic distributed acoustic sensing capabilities with blind near-field array signal processing. *Nature Communications*. [DOI](https://doi.org/10.1038/s41467-022-31681-x).
- Rodriguez, T., et al. (2025). Automatic Identification of High-Quality Channels in Distributed Acoustic Sensing Through Implementation of a Channel Quality Index. *IEEE JSTARS*. [DOI](https://doi.org/10.1109/JSTARS.2025.3593330). Partial text and author implementation reviewed; entry point for task-quality assessment.
- Bozzi, E., et al. (2026). Near real-time channel selection for Distributed Acoustic Sensing technology. *Seismica*. [DOI](https://doi.org/10.26443/seismica.v5i1.2251). Partial-text entry point for joint geometry/quality selection.
- Gurevich, B., et al. (2023). The Effect of the Method of Downhole Deployment on Distributed Acoustic Sensor Measurements: Field Experiments and Numerical Simulations. *Sensors*, 23, 7501. [DOI](https://doi.org/10.3390/s23177501).
