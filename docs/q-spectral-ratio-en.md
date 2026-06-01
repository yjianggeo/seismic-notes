# Spectral Ratio Method for Q Inversion

## Introduction

As seismic waves propagate through the Earth, they lose energy due to the anelastic (viscoelastic) properties of the medium. This amplitude decay is quantified by the **quality factor** $Q$. A smaller $Q$ means a more dissipative medium and faster decay; $Q \to \infty$ corresponds to a perfectly elastic solid with no energy loss.

The **spectral ratio method** is one of the most widely used techniques for estimating $Q$. Its key idea is to take the **ratio** of displacement spectra recorded at two stations from the same source, so that the source spectrum cancels exactly, leaving only the attenuation signal.

For S-waves propagating along the same ray path to two stations, the log spectral ratio satisfies:

$$
\boxed{
\ln\!\left[\frac{A(f,r_2)}{A(f,r_1)}\right] = \underbrace{\ln\!\left(\frac{r_1}{r_2}\right)}_{\text{intercept}} - \underbrace{\pi\,\Delta t^*}_{\text{slope}} \cdot f
}
$$

This is a **linear equation in frequency** $f$. The fitted slope $m = -\pi\Delta t^*$ directly yields the effective Q:

$$
Q_{\mathrm{eff}} = -\frac{\pi\,\Delta t}{m}
$$

---

## Seismic Wave Attenuation and the Definition of Q

### Physical Definition of the Quality Factor

The quality factor $Q$ is a dimensionless measure of the fractional energy loss per cycle:

$$
\frac{1}{Q} \equiv \frac{1}{2\pi} \cdot \frac{-\Delta E}{E}
$$

where $\Delta E < 0$ is the elastic energy dissipated in one oscillation cycle and $E$ is the peak elastic energy.

- $Q \gg 1$: very small per-cycle loss, nearly elastic; typical upper-crustal granite $Q \sim 200$–$1000$
- $Q \sim 10$–$50$: strong attenuation; water-saturated sediments, fault zones

### Single-Path Amplitude Spectrum

For a monochromatic plane S-wave traveling at speed $\beta$, the amplitude decays exponentially with distance $r$:

$$
A(r, f) = A_0 \exp\!\left(-\frac{\pi f\, r}{\beta\, Q}\right) = A_0 \exp(-\alpha r)
$$

The attenuation coefficient $\alpha = \pi f / (\beta Q)$ scales with frequency, so high-frequency energy is attenuated much more rapidly than low-frequency energy.

### The t* Parameter

In a heterogeneous medium, the cumulative attenuation along a ray path is described by $t^*$ ("t-star"):

$$
t^* = \int_{\mathrm{path}} \frac{\mathrm{d}s}{\beta(s)\, Q(s)}
$$

For a homogeneous medium with constant $\beta$ and $Q$, and travel time $t = r/\beta$:

$$
t^* = \frac{t}{Q} = \frac{r}{\beta\, Q}
$$

$t^*$ has units of time and serves as a single parameter that encodes both path length and medium Q.

### Common Q Models

| Model | Expression | Characteristic |
|-------|-----------|----------------|
| Constant Q | $Q = \mathrm{const}$ | Simplest; log spectral ratio linear in $f$ |
| Power-law Q | $Q(f) = Q_0\, f^{\eta}$ | $\eta \in [0,1]$; common in shallow sediments |
| Futterman model | Satisfies Kramers–Kronig | Weak frequency dependence |

The spectral ratio method assumes **constant Q** by default, making the log spectral ratio strictly linear in $f$.

---

## Derivation of the Spectral Ratio Method

### Full Displacement Amplitude Spectrum Model

The far-field displacement amplitude spectrum can be written as a product of independent factors (Aki & Richards 2002):

$$
A(f, r) = S(f) \cdot I(f) \cdot G(r) \cdot \exp\!\left(-\pi f\, t^*\right)
$$

where:

- $S(f)$: **source spectrum** (e.g., Brune $\omega^{-2}$ spectrum, includes radiation pattern $\mathcal{R}_{\theta\phi}$)
- $I(f)$: **instrument response** (converts ground motion to output voltage)
- $G(r)$: **geometric spreading**; for body waves in the far field, $G(r) = 1/r$
- $\exp(-\pi f\, t^*)$: **anelastic attenuation** factor

### Two-Station Spectral Ratio

Consider two stations along the same ray path: a **near station** (station 1, distance $r_1$) and a **far station** (station 2, distance $r_2 > r_1$).

**Near-station** amplitude spectrum:

$$
A(f, r_1) = S(f) \cdot I(f) \cdot \frac{1}{r_1} \cdot \exp(-\pi f\, t_1^*)
$$

**Far-station** amplitude spectrum:

$$
A(f, r_2) = S(f) \cdot I(f) \cdot \frac{1}{r_2} \cdot \exp(-\pi f\, t_2^*)
$$

Dividing the two equations, **$S(f)$ and $I(f)$ cancel exactly** (assuming identical instrument responses, or that instrument corrections have been applied):

$$
\frac{A(f, r_2)}{A(f, r_1)} = \frac{r_1}{r_2} \cdot \exp\!\left[-\pi f (t_2^* - t_1^*)\right]
$$

Define the **differential t-star**:

$$
\Delta t^* = t_2^* - t_1^* = \frac{t_2 - t_1}{Q_{\mathrm{eff}}} = \frac{\Delta t}{Q_{\mathrm{eff}}}
$$

where $\Delta t = (r_2 - r_1)/\beta$ is the differential S-wave travel time.

### Linearization

Taking the natural logarithm of both sides:

$$
\ln\!\left[\frac{A(f, r_2)}{A(f, r_1)}\right] = \ln\!\left(\frac{r_1}{r_2}\right) - \pi\,\Delta t^*\cdot f
$$

Writing $L(f) = \ln[A_2(f)/A_1(f)]$, this is a linear function of $f$:

$$
L(f) = b + m \cdot f
$$

| Parameter | Expression | Physical meaning |
|-----------|-----------|-----------------|
| Intercept $b$ | $\ln(r_1/r_2)$ | Geometric spreading ratio (known, can serve as a constraint) |
| Slope $m$ | $-\pi\,\Delta t^*$ | Encodes all attenuation information; $m < 0$ |

### Extracting Q

From $m = -\pi\,\Delta t^* = -\pi\,\Delta t / Q_{\mathrm{eff}}$:

$$
\boxed{Q_{\mathrm{eff}} = -\frac{\pi\,\Delta t}{m}}
$$

$\Delta t$ is obtained either from picked S-wave arrival times or from the distance difference and mean velocity:

$$
\Delta t = t_2^{\mathrm{arr}} - t_1^{\mathrm{arr}} \quad \text{or} \quad \Delta t = \frac{r_2 - r_1}{\bar{\beta}}
$$

!!! note "Condition for Source Cancellation"
    The spectral ratio method requires both stations to record **the same phase from the same earthquake** (e.g., both recording direct S-waves), so that $S(f)$ cancels exactly. If two different earthquakes are used, source spectrum normalization is required.

!!! tip "Practical Tip: Choosing Δt"
    Prefer picking the S-wave arrival time difference directly from the waveforms rather than computing it from distance and velocity. Actual travel time differences implicitly account for lateral velocity heterogeneity.

---

## Practical Workflow

### Data Processing Steps

| Step | Operation | Purpose |
|------|-----------|---------|
| 1 | Demean, detrend | Remove DC and long-period drift |
| 2 | Cut S-wave time window | Isolate target phase |
| 3 | Apply taper (Hanning / Tukey) | Reduce spectral leakage |
| 4 | Remove instrument response → displacement | Convert record to true ground displacement |
| 5 | Compute FFT amplitude spectrum | Obtain $A_1(f)$, $A_2(f)$ |
| 6 | Smooth spectra (optional) | Reduce spectral variance, stabilize fit |
| 7 | Compute log spectral ratio $L(f)$ | Enter fitting stage |

### Selecting the Frequency Band

The usable frequency band is limited by:

- **Low-frequency cutoff**: poor signal-to-noise ratio; microseismic noise (0.1–0.3 Hz) dominates
- **High-frequency cutoff**: Brune spectrum falls off as $f^{-2}$ above $f_c$; κ effect at very high frequencies

!!! warning "Consequence of Wrong Frequency Range"
    Including $f > f_c$ in the fit causes the Brune source spectral slope ($f^{-2}$) to contaminate the spectral ratio slope, leading to **systematically underestimated Q**. Estimate the corner frequency $f_c$ first, and set the upper frequency limit to $\approx 0.8\, f_c$.

### The κ Effect (Near-Surface High-Frequency Attenuation)

Anderson & Hough (1984) showed that at high frequencies an additional exponential decay — the **κ (kappa) operator** — is present:

$$
A(f) \propto \exp(-\pi \kappa f), \quad f \gtrsim f_E
$$

$\kappa$ reflects cumulative attenuation in the near-surface low-Q sediment column and is site-dependent. If the two stations have different $\kappa$ values ($\Delta\kappa = \kappa_2 - \kappa_1 \neq 0$), the observed slope includes an extra contribution:

$$
m_{\mathrm{obs}} = -\pi\,\Delta t^* - \pi\,\Delta\kappa = -\frac{\pi\,\Delta t}{Q} - \pi\,\Delta\kappa
$$

Ignoring $\Delta\kappa$ causes Q to be **underestimated**. Mitigation: choose station pairs with similar site conditions, or invert $\Delta\kappa$ and $Q$ jointly.

---

## Python Example

The code below simulates a two-station scenario with true Q = 150, adds Gaussian noise to mimic observational scatter, and recovers Q via linear regression.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# ── Parameters ────────────────────────────────────────────
Q_true    = 150          # True Q value
r1, r2    = 10e3, 60e3   # Near/far station distances from source (m)
beta      = 3500.0        # Mean S-wave velocity (m/s)
dt_travel = (r2 - r1) / beta   # Differential travel time Δt (s)

f = np.linspace(1, 20, 300)  # Frequency axis 1–20 Hz

# ── Theoretical log spectral ratio ────────────────────────
# L(f) = ln(r1/r2) - π·f·Δt/Q
log_ratio_theory = np.log(r1 / r2) - np.pi * f * dt_travel / Q_true

# ── Add Gaussian noise (simulate observational scatter) ───
rng = np.random.default_rng(seed=42)
log_ratio_obs = log_ratio_theory + rng.normal(0, 0.25, size=len(f))

# ── Linear regression: L(f) = b + m·f ────────────────────
slope, intercept, r_val, _, _ = linregress(f, log_ratio_obs)
Q_est         = -np.pi * dt_travel / slope
log_ratio_fit = slope * f + intercept

print(f"True Q       = {Q_true}")
print(f"Estimated Q  = {Q_est:.1f}")
print(f"Slope m      = {slope:.5f}  (theory: {-np.pi*dt_travel/Q_true:.5f})")
print(f"R²           = {r_val**2:.4f}")

# ── Plots ─────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Left: attenuation (dB) vs frequency for various Q values
ax = axes[0]
palette = ['#e74c3c', '#e67e22', '#3498db', '#2ecc71']
for Q_val, color in zip([50, 100, 200, 500], palette):
    tstar   = dt_travel / Q_val
    attn_db = 20 * np.log10(np.exp(-np.pi * f * tstar))
    ax.plot(f, attn_db, color=color, lw=2, label=f'Q = {Q_val}')
ax.set(xlabel='Frequency (Hz)', ylabel='Attenuation (dB)',
       title='Attenuation vs. Frequency for Different Q', xlim=[1, 20])
ax.axhline(0, color='k', lw=0.6, ls='--', alpha=0.4)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Right: log spectral ratio — observed, theory, and fit
ax = axes[1]
ax.scatter(f, log_ratio_obs, s=5, alpha=0.45, color='#3498db',
           label='Observed (noisy)', zorder=2)
ax.plot(f, log_ratio_theory, 'k--', lw=1.5, label=f'Theory  (Q = {Q_true})')
ax.plot(f, log_ratio_fit,   'r-',  lw=2,
        label=f'Linear fit  (Q ≈ {Q_est:.0f})')
ax.text(0.97, 0.97,
        f'slope = {slope:.4f}\nQ est = {Q_est:.1f}\nR² = {r_val**2:.3f}',
        transform=ax.transAxes, ha='right', va='top', fontsize=9,
        bbox=dict(boxstyle='round', fc='wheat', alpha=0.7))
ax.set(xlabel='Frequency (Hz)', ylabel='ln [ A₂(f) / A₁(f) ]',
       title='Spectral Ratio Method')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('docs/assets/images/q_spectral_ratio.png', dpi=150, bbox_inches='tight')
plt.show()
```

Output:

```
True Q       = 150
Estimated Q  = 149.8
Slope m      = -0.29958  (theory: -0.29920)
R²           = 0.9806
```

![Spectral ratio example](../assets/images/q_spectral_ratio.png)
*Figure 1: Left — attenuation (dB) versus frequency for Q = 50, 100, 200, 500; lower Q causes faster high-frequency decay. Right — noisy observed log spectral ratio (blue dots), theoretical curve (black dashed), and linear regression fit (red line); the slope yields Q.*

---

## Extension to Frequency-Dependent Q

When Q varies with frequency, the power-law model is commonly adopted:

$$
Q(f) = Q_0\, f^{\eta}, \quad \eta \in [0, 1]
$$

The attenuation factor becomes:

$$
\exp\!\left(-\pi f\, t^*\right) = \exp\!\left(-\frac{\pi f\, t}{Q(f)}\right) = \exp\!\left(-\frac{\pi\, t}{Q_0} f^{1-\eta}\right)
$$

The log spectral ratio is then:

$$
L(f) = \ln\!\left(\frac{r_1}{r_2}\right) - \frac{\pi\,\Delta t}{Q_0}\, f^{1-\eta}
$$

Setting $u = f^{1-\eta}$ restores linearity: $L$ is linear in $u$. In practice, sweep over candidate $\eta$ values, linearize with respect to $f^{1-\eta}$, and select the $\eta$ that maximizes $R^2$.

!!! note "Typical η Values"
    Upper-crustal crystalline rock: $\eta \approx 0$ (constant-Q approximation valid); shallow unconsolidated sediments: $\eta \approx 0.5$–$0.8$; global mantle: $\eta \approx 0.1$–$0.3$.

---

## Method Variants

| Variant | Setup | Advantages | Limitations |
|---------|-------|-----------|-------------|
| **Two-station** (this note) | Same source, two stations along the same ray | Source spectrum cancels; accurate $\Delta t$ | Strict geometric alignment required |
| **Single-station, two-event** | Same station, two sources at different distances | Identical site response for both paths | Requires assumption that source spectral shapes are equal |
| **VSP spectral ratio** | Surface + downhole receivers | Simple path geometry; avoids site effects | Requires a borehole |
| **Coda wave spectral ratio** | S-wave coda from single station | Large sample size; statistically robust | Intrinsic vs. scattering attenuation harder to separate |

---

## References

- Aki, K., & Richards, P. G. (2002). *Quantitative Seismology* (2nd ed.). University Science Books.
- Anderson, J. G., & Hough, S. E. (1984). A model for the shape of the Fourier amplitude spectrum of acceleration at high frequencies. *Bulletin of the Seismological Society of America*, 74(5), 1969–1993.
- Tonn, R. (1991). The determination of the seismic quality factor Q from VSP data: A comparison of different computational methods. *Geophysical Prospecting*, 39(1), 1–27.
- Toverud, T., & Ursin, B. (2005). Comparison of seismic attenuation models using zero-offset vertical seismic profiling (VSP) data. *Geophysics*, 70(2), F17–F25.
- Xie, J. (2002). Seismic attenuation: Measurement and uncertainty. *Pure and Applied Geophysics*, 159(7–8), 1823–1849.
