# Borehole DAS Surface Waves: From Depth Response to Structural Constraints

Borehole arrays extend surface-wave observations into depth. **DAS measures axial strain or strain rate averaged over a finite gauge, not the vertical displacement eigenfunction itself.** Amplitude minima, polarity reversals and improved fits require checks of the measurement operator, wavefield and parameter identifiability.

Read [surface-wave eigenfunctions and dispersion](surface-coda-en.md) first. Practical event screening and phase evidence are covered in the [data and evidence workflow](field-workflow-en.md). This chapter retains transferable methods rather than unpublished project velocities or event classifications.

## 1. Four Different Observables

| Quantity | Definition | Not equivalent to |
|---|---|---|
| Displacement eigenfunction | $\mathbf U_n(z,f)$ | DAS strain versus depth |
| Strain tensor | $\varepsilon_{ij}=(\partial_i u_j+\partial_j u_i)/2$ | A displacement component |
| DAS axial strain | Gauge average of $\mathbf t^\mathsf T\boldsymbol\varepsilon\mathbf t$ | Point strain or three-component motion |
| Relative complex depth response | Amplitude and phase relative to one reference | Absolute instrument calibration or a unique velocity profile |

Use the convention $e^{i(\mathbf k_h\cdot\mathbf x_h-\omega t)}$, positive downward $z$, cable arclength $s$ and gauge length $L$. Strain-rate output adds a factor $-i\omega$ in frequency space. Unify units, signs and clock conventions before comparing records.

## 2. Finite Gauge and Measured Trajectory

### 2.1 Straight-Cable Differences and Curved-Cable Integration

For small strain, perfect ground–cable coupling and uniform gauge weighting, the ideal response is

$$
d(s,f)=\frac{1}{L}\int_{s-L/2}^{s+L/2}
\mathbf t(\xi)^\mathsf T\boldsymbol\varepsilon[\mathbf r(\xi),f]\mathbf t(\xi)\,\mathrm d\xi.
$$

On a straight segment the tangent is constant and this equals the along-fibre displacement difference divided by $L$. For a vertical segment,

$$
d(z,f)=\frac{U_z(z+L/2,f)-U_z(z-L/2,f)}{L}
\xrightarrow{L\to0}\partial_z U_z.
$$

For a curved cable, integrate along its trajectory. Differencing endpoint displacements projected onto their different local tangents introduces $\mathbf t'\cdot\mathbf u$, because $\mathrm d(\mathbf t\cdot\mathbf u)/\mathrm ds$ contains that extra term. Actual spatial weighting, pulse averaging and instrument filters must also be represented when relevant. See [Kennett (2022)](https://doi.org/10.1098/rspa.2021.0812) for the finite-gauge measurement framework.

### 2.2 Measured Depth, Vertical Depth and Horizontal Offset

Let inclination $i(s)$ be measured from vertical and azimuth $\alpha(s)$ clockwise from true north. With horizontal coordinates ordered east, north,

$$
z(s)=\int_0^s\cos i(\xi)\,\mathrm d\xi,\qquad
\mathbf x_h(s)=\int_0^s\sin i(\xi)
\begin{bmatrix}\sin\alpha(\xi)\\\cos\alpha(\xi)\end{bmatrix}\mathrm d\xi.
$$

Use a validated survey interpolation method, such as minimum curvature, and cross-check reconstructed coordinates against reported vertical depth and offsets. Optical distance, measured borehole depth (MD), true vertical depth (TVD) and depth below sea level are distinct. The fibre may end above the drilled bottom.

### 2.3 Small Inclination Does Not Guarantee Small Response Changes

For Rayleigh waves in an ideal isotropic 1-D medium, define propagation azimuth $\beta$ and $q=\cos(\alpha-\beta)$. The local projection is

$$
\varepsilon_{ss}=\sin^2i\,q^2\varepsilon_{rr}
+\cos^2i\,\varepsilon_{zz}
+2\sin i\cos i\,q\,\varepsilon_{rz}.
$$

The shear coefficient is first order in small inclination, whereas the horizontal normal-strain coefficient is second order. A small $\sin^2i$ alone therefore does not establish a negligible azimuth effect. The trajectory also changes propagation phase through $e^{i\mathbf k_h\cdot\mathbf x_h(s)}$.

Scan, jointly estimate or marginalize unknown orientation as a nuisance parameter; prefer independent measured geometry when available. One event's direction cosine can imply two mirror azimuths. Multiple arrival directions reduce ambiguity but do not guarantee a unique 3-D trajectory. With inclination fixed, changing azimuth does not change MD–TVD conversion.

Regularize changes in the actual tangent rather than azimuth differences alone. For angles in radians, $\|\mathbf t'(s)\|^2=[i'(s)]^2+\sin^2i(s)[\alpha'(s)]^2$. Near vertical, a large azimuth change can represent a small bend. Test predictions after adding trajectory flexibility, which may otherwise absorb structural, coupling or wavefield errors.

## 3. Depth Decay, Gauge Averaging and Nodes

### 3.1 A Displacement Maximum Can Be a Strain Node

Half-space Rayleigh displacement combines fast and slow exponential terms; strain involves their derivatives. A shallow displacement maximum can thus coincide with a strain node and reversal. **A strain minimum is not automatically a low-velocity layer, lithological interface or displacement node.** Downhole DAS strain-depth modelling has direct precedents, including [Glubokovskikh et al. (2021)](https://doi.org/10.1029/2020JB021463).

Keep complex responses: a real-part zero does not imply zero total amplitude if the imaginary part remains nonzero. Phase is unstable near low amplitude, so a roughly $180^\circ$ jump alone does not establish a physical node. Compare neighbouring depths, frequencies, events, windows and quality coverage; gauge averaging may shift or weaken minima.

### 3.2 Evanescent Exponentials Give sinhc, Not sinc

For $U_z(z)=C e^{-bz}$ with constant $b>0$, uniform gauge averaging gives

$$
d(z)=-bC e^{-bz}\operatorname{sinhc}(bL/2),\qquad
\operatorname{sinhc}x=\frac{\sinh x}{x}.
$$

This is **sinhc**, not the $\operatorname{sinc}(k_sL/2)$ factor of a propagating plane wave. Constant $b$ and $L$ change amplitude only: the log-amplitude slope remains $-b$. Multiplying that slope by inverse sinc is incorrect. Two-exponential, layered, curved or interface-crossing cases require the full operator.

### 3.3 Limits of Single-Exponential Velocity Estimates

If a homogeneous half-space's S-evanescent term truly dominates and the same mode's **phase velocity** $c$ is independently known,

$$
b=\frac{2\pi f}{c}\sqrt{1-\frac{c^2}{V_S^2}},\qquad
V_S=\frac{c}{\sqrt{1-(bc/2\pi f)^2}}.
$$

Check $0\le bc/(2\pi f)<1$, SNR, coupling and the asymptotic interval. Offset divided by an active-source envelope arrival gives a group/travel-time velocity, not automatically phase velocity. Repeating this formula at multiple frequencies and assigning depths $\lambda/4$ does not recover a layered $V_S(z)$ profile. Layered inference needs full dispersion, eigenfunction and sensitivity modelling.

## 4. Estimating Complex Depth Response

For depth bin $j$ and reference $r$, define $S_{jr}=\langle D_jD_r^*\rangle$:

$$
H_j=\frac{S_{jr}}{S_{rr}},\qquad
\gamma_{jr}^2=\frac{|S_{jr}|^2}{S_{jj}S_{rr}}.
$$

$H_j$ approximates $g_j/g_r$ only with a common source and negligible or appropriately treated reference noise. A nodal or noise-dominated reference makes the denominator unstable. Preserve reference choices, valid-depth masks and coherence, and avoid per-depth normalization that destroys the target amplitude information.

SVD extracts dominant coherent shape, not necessarily a pure mode. Its real and imaginary parts describe one axial quantity, not vertical and horizontal motion. High coherence can arise from coherent mode mixtures, common-source noise or stable observation transfer. Near-quadrature radial–vertical phase in three-component records should be combined with transverse energy, propagation direction and dispersion. A distant station provides regional context rather than local coupling calibration or modal-order confirmation. [Meyers et al. (2019)](https://doi.org/10.1785/0120190026) illustrate comparisons using a co-located 3-D array and independently constrained structure.

## 5. Finite Windows and Multimode Forward Modelling

Windowing and spectral smoothing mix neighbouring frequencies. A linear spectral coefficient can be represented schematically as

$$
\widetilde D_j(f_0)=\int W(f_0-f)\sum_n A_n(f)g_{jn}(f)\,\mathrm df+N_j(f_0).
$$

$W$ is the spectral window; subsequent cross-spectra, whitening or SVD must also be applied. Short-window observations generally differ from $A(f_0)g_j(f_0)$. Bandwidth depends on duration and multitaper time–bandwidth product. Overlapping frequency centres are not independent measurements.

Pass synthetic waveforms through the same windowing, detrending, filtering, sampling, depth binning and spectral estimation as observations. Test source envelopes, modal composition and window location; check quadrature, frequency integration and padding convergence. Arbitrary per-frequency complex sources absorb some structural differences, while restricted source families impose additional assumptions.

!!! note "Repeatability has different meanings"
    Overlapping windows and bands do not add independent events. Cross-event depth-shape repeatability supports a stable response component, but stable coupling can also repeat. High-frequency body-wave repeatability does not independently validate low-frequency surface-wave structure.

## 6. Inversion, Material Relations and Identifiability

### 6.1 Sensitivity to Vp Does Not Establish Precise Joint Inversion

Depth response depends on P–SV coupling, gradients and geometry. Its $V_P$, $V_S$ and density sensitivity ordering need not match that of phase velocity. Surface ellipticity kernels cannot substitute for DAS kernels. [Cercato (2018)](https://doi.org/10.1093/gji/ggx558) illustrates model-dependent ellipticity sensitivity; compute the actual borehole observation derivatives separately.

Perturb each layer's material properties independently:

$$
J_{a\ell}\approx\frac{F(m_{a\ell}e^h)-F(m_{a\ell}e^{-h})}{2h},
\qquad a\in\{V_P,V_S,\rho\}.
$$

Recompute phase velocity, eigenfunctions and the entire observation for every perturbation, and compare multiple step sizes. Avoid division by near-zero nodal responses. Unequal-thickness layer kernels are not directly information density per unit depth. Stack real and imaginary parts under one noise weighting; inspect column correlation, singular values, resolution and trade-offs. Large derivatives and nearly collinear parameter responses can coexist.

For linearly fitted sources, a local diagnostic is $J_\mathrm{eff}=(I-QQ^\mathsf T)J$, where $Q$ spans the source design in the **same weighted real representation**. It measures changes not absorbed by local source adjustments. It is not a posterior or automatically the exact derivative of a refitted objective with nonzero residual.

Identify theoretical null directions too. In a 1-D elastic model without gravity, multiplying densities in all layers and the half-space by one constant while keeping velocities fixed leaves phase velocity and normalized eigenfunction responses unchanged. Density contrasts can matter even though its absolute uniform scale is not identifiable from these normalized observations.

### 6.2 Empirical Relations Act as Priors and Change the Derivative

With $V_P=f(V_S)$ and $\rho=g(V_P)$,

$$
J_\mathrm{linked}=J_{V_S}
+\frac{\mathrm d\ln V_P}{\mathrm d\ln V_S}J_{V_P}
+\frac{\mathrm d\ln\rho}{\mathrm d\ln V_S}J_\rho.
$$

Contributions may reinforce or cancel. Relations such as [Brocher (2005)](https://doi.org/10.1785/0120050077) can define a stated baseline or prior; check lithology, units and validity ranges. Empirically generated $V_P$ is not an independent measurement. Compare fixed relations, justified soft departures and independently constrained $V_P$.

Regional models help specify backgrounds and large-scale combinations, but output grid spacing is not resolving power. Unify surface/sea-level depth datums, check whether $V_P$ itself was generated from $V_S$, and document shared data and starting models. The author [SWChinaCVM 2.0 repository](https://github.com/liuyingustc/SWChinaCVM-V2.0) provides an example of checking depth references and resolution.

### 6.3 Boundary Solutions and Layer Count

A velocity reaching a chosen bound means no interior optimum was obtained under those assumptions; it does not establish the true velocity at or beyond that bound. Test layer count, thickness, deep background connection, material policy, geometry, sources and coupling. Curves coinciding at a bound do not imply small uncertainty.

Lower training residual is not higher velocity accuracy, and more layers do not establish more resolved geological units. Scenario spread is not a posterior confidence interval. Label tested candidates, statistical intervals and independent measurements distinctly.

## 7. Prediction Tests and Information Leakage

| Test | Question | Limitation |
|---|---|---|
| Full-depth fit | Can a model explain fitted observations? | Does not establish prediction |
| Depth-block holdout | Can training depths predict excluded depths? | Full-depth feature/weight/layer selection makes the test conditional |
| Cross-event transfer | Can shared structure explain another event? | Fit the receiving event's source only on its training depths |
| New event with frozen models | Is new data compatible with old structure? | Retrospective if already inspected; joint refitting changes its role |

Include every data-dependent operation inside the training boundary: frequency selection, SVD, references, weights, normalization, candidate choice and hyperparameters. Use test depths only for final scoring. Perturb actual holdout signals and weights to verify that fitted training coefficients and predictions remain unchanged. A historical full-depth template does not become an independent depth-holdout inversion merely by being frozen later.

If

$$
E=\sqrt{\frac{\sum_{j\in\mathrm{test}}w_j|d_j-\widehat d_j|^2}
{\sum_{j\in\mathrm{test}}w_j|d_j|^2}},
$$

then $E=1$ is zero prediction, and $E<1$ only beats that baseline. Report test energy, quality coverage, normalization and failures. A residual normalized by full-depth energy is not the same score. Prediction failure tests the joint structural, geometric, wavefield, source and observation assumptions; one score cannot isolate a physical cause.

## 8. A Practical Reading and Analysis Sequence

Start with [surface-wave eigenfunctions](surface-coda-en.md) and [DAS response and coupling](das-en.md). Check clocks, channel–depth mapping and surveys; freeze noise and quality rules; extract complex responses; run the same processing on synthetics; diagnose material and geometric sensitivity; then test predictions with explicit training boundaries. Surveys, near-well three-component records, sonic logs and local dispersion each constrain different trade-offs.
