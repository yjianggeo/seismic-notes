# DAS – Distributed Acoustic Sensing

## Introduction

**Distributed Acoustic Sensing (DAS)** is a fiber-optic seismic sensing technology that converts an ordinary optical fiber cable into a continuous, dense seismic array. A single fiber tens of kilometers long can simultaneously provide tens of thousands of virtual sensors with channel spacings as small as 1 m and sampling rates of several kHz.

Compared with conventional seismometers, DAS offers three core advantages:

| Feature | Conventional geophone | DAS |
|---------|----------------------|-----|
| Deployment cost | Each sensor installed separately | Cable laid in one pass |
| Spatial density | Limited stations (tens–hundreds) | Thousands to tens of thousands of channels |
| Low-frequency limit | Constrained by natural frequency (e.g., 4.5 Hz) | Responds from DC to high frequency (flat response) |
| Environment | Requires power, waterproofing | All-optical passive; can use submarine cables |

DAS measures the **dynamic axial strain** (or strain rate) along the fiber, not particle velocity. This fundamental difference gives rise to its distinctive directional response pattern and gauge length effect.

---

## Basic Principle

### Rayleigh Scattering and Phase-Sensitive OTDR

DAS operates by combining **Rayleigh backscattering** in optical fiber with **phase-sensitive Optical Time Domain Reflectometry (φ-OTDR)**:

1. **Pulse injection**: A coherent laser pulse is sent into the fiber (pulse width sets spatial resolution).
2. **Rayleigh backscattering**: Along the fiber, light scatters from random refractive-index inhomogeneities; a fraction returns to the interrogator.
3. **Phase detection**: The interrogator coherently demodulates the returned light to measure the **phase** of backscattered light at each depth.
4. **Phase → strain**: Phase shifts are proportional to changes in optical path length, i.e., to axial strain.

$$
\Delta\phi = \frac{4\pi n}{\lambda} \cdot \Delta L
$$

where $n$ is the fiber refractive index, $\lambda$ is the laser wavelength, and $\Delta L$ is the change in physical path length caused by strain.

!!! note "What DAS Measures"
    DAS measures the **axial dynamic strain** $\varepsilon_{xx}$ (or strain rate $\dot{\varepsilon}_{xx}$) along the fiber—that is, relative elongation/compression along the fiber axis. The response to seismic waves depends strongly on the angle between the wave propagation direction and the fiber axis.

### Key System Parameters

| Parameter | Typical values | Description |
|-----------|---------------|-------------|
| Channel spacing | 1–10 m | Distance between adjacent virtual sensors |
| Gauge length (GL) | 5–50 m | Strain integration length; governs spatial resolution and SNR |
| Sampling rate | 1–10 kHz | Temporal resolution |
| Maximum cable length | 10–100 km | Limited by laser power and fiber attenuation |
| Dynamic range | ~80–100 dB | Related to laser coherence |

---

## Typical Applications

### Vertical Seismic Profiling (VSP)

The first large-scale application of DAS in oil and gas exploration was **Vertical Seismic Profiling (VSP)**. Fiber cables cemented behind well casing record seismic wavefields over hundreds of meters depth simultaneously.

- **Advantages**: No repeated tripping; covers the entire well at high resolution.
- **Typical gauge length**: 5–10 m.
- **Signal types**: Direct P/S waves, reflections, converted waves.

### Urban Shallow Subsurface Imaging

Fiber cables in urban telecommunications conduits (existing infrastructure) use **ambient noise** from traffic and machinery as passive seismic sources to invert for shallow S-wave velocity structure.

- Representative work: Lindsey et al. (2017) imaged subsurface structure under the Stanford campus using telecom fiber.
- No active source required; near-zero marginal cost.

### Submarine Seismic Monitoring

**Existing submarine communication cables** serve as seismic sensors, filling the large gaps in ocean-bottom seismic networks.

- Detects microearthquakes, submarine landslides, and tsunami precursors.
- Representative work: Marra et al. (2018, *Science*) used a transatlantic cable to detect earthquakes.

### Microseismic and Induced Seismicity Monitoring

In geothermal energy, hydraulic fracturing, and CO₂ storage, DAS provides real-time monitoring of **microseismic activity** to track fracture propagation and induced seismicity.

---

## Sensitivity to Incident Angles

### Geometry

Let the fiber lie along the $x$-axis. A seismic plane wave propagates in the $x$–$z$ plane, with its propagation direction making angle $\theta$ to the fiber axis.

Wave vector:

$$
\mathbf{k} = k(\cos\theta\,\hat{x} + \sin\theta\,\hat{z}), \quad k = \frac{2\pi f}{c}
$$

Component along the fiber: $k_x = k\cos\theta$.

DAS measures axial strain $\varepsilon_{xx} = \partial u_x / \partial x$.

### P-Wave Directional Response

P-wave particle displacement is parallel to the propagation direction:

$$
\mathbf{u} = A\hat{k}\,e^{i(\mathbf{k}\cdot\mathbf{x} - \omega t)}
= A(\cos\theta\,\hat{x} + \sin\theta\,\hat{z})\,e^{i(k_x x + k_z z - \omega t)}
$$

The $x$-component: $u_x = A\cos\theta \cdot e^{i(\cdots)}$

Axial strain:

$$
\varepsilon_{xx}^{P} = \frac{\partial u_x}{\partial x} = ik_x A\cos\theta \cdot e^{i(\cdots)} = ik\cos\theta \cdot A\cos\theta \cdot e^{i(\cdots)}
$$

Therefore:

$$
\boxed{|\varepsilon_{xx}^{P}| \propto \cos^2\theta}
$$

- $\theta = 0°$ (wave propagates along fiber): **maximum response**
- $\theta = 90°$ (wave propagates perpendicular to fiber): $\varepsilon_{xx} = 0$, **no response**

### SV-Wave Directional Response

SV-wave particle displacement is perpendicular to the propagation direction, within the $x$–$z$ plane:

$$
\mathbf{u} = A(-\sin\theta\,\hat{x} + \cos\theta\,\hat{z})\,e^{i(k_x x + k_z z - \omega t)}
$$

The $x$-component: $u_x = -A\sin\theta \cdot e^{i(\cdots)}$

Axial strain:

$$
\varepsilon_{xx}^{SV} = \frac{\partial u_x}{\partial x} = ik_x(-A\sin\theta) = -ik\cos\theta \cdot A\sin\theta
$$

Therefore:

$$
\boxed{|\varepsilon_{xx}^{SV}| \propto |\sin\theta\cos\theta| = \frac{1}{2}|\sin 2\theta|}
$$

- $\theta = 0°$ or $\theta = 90°$: zero response
- $\theta = 45°$: **maximum response**

!!! note "SH-Wave Blind Spot"
    SH-wave particle displacement is perpendicular to the $x$–$z$ plane (along $y$), producing no $x$-direction displacement component. DAS is therefore **completely insensitive** to SH waves when the fiber lies in the $x$–$z$ plane. This is an inherent limitation.

### Directional Sensitivity Polar Diagram

Taking $\theta$ as the polar angle and $|\varepsilon_{xx}|$ as the radius, the polar diagrams for P-wave ($\cos^2\theta$) and SV-wave ($|\sin 2\theta|/2$) responses are shown in Figure 1.

![DAS directional sensitivity](../assets/images/das_angle_response.png)
*Figure 1: Polar diagrams of DAS directional sensitivity for P-waves (blue) and SV-waves (orange). Shaded area represents relative response amplitude. The fiber axis lies along the horizontal (0°–180°).*

---

## Flat Frequency Response

### Strain-to-Particle-Velocity Conversion

DAS measures axial strain, while seismology conventionally works with particle velocity. Their relationship determines DAS's frequency characteristics.

For a plane P-wave propagating along $x$ with displacement $u_x = A e^{i(kx - \omega t)}$:

$$
v_x = \frac{\partial u_x}{\partial t} = -i\omega A e^{i(\cdots)}
$$

$$
\varepsilon_{xx} = \frac{\partial u_x}{\partial x} = ikA e^{i(\cdots)} = \frac{ik}{-i\omega} \cdot v_x = -\frac{k}{\omega} v_x = -\frac{v_x}{c_P}
$$

Including the directional factor $\cos^2\theta$ for a general incident angle $\theta$:

$$
\varepsilon_{xx} = -\frac{\cos^2\theta}{c_P} \cdot v_P
$$

Solving for particle velocity:

$$
\boxed{v_P = -\frac{c_P}{\cos^2\theta} \cdot \varepsilon_{xx}}
$$

**Key property: the conversion factor $c_P / \cos^2\theta$ is frequency-independent.**

### Why It Is Called "Flat Response"

This frequency independence gives DAS a **flat frequency response** — unlike traditional geophones:

| Instrument | Measures | Frequency response | Low-frequency behavior |
|------------|----------|-------------------|----------------------|
| Short-period geophone | Particle velocity | Flat above $f_0$, rolls off below | 12 dB/octave roll-off below natural frequency |
| Accelerometer | Particle acceleration | Flat below resonance | Requires integration for velocity |
| **DAS (strain)** | **Axial strain** | **Flat from DC to $f_{\rm notch}$** | **No low-frequency cutoff** |

!!! tip "Practical Significance"
    DAS strain records can be converted to particle velocity with a single **frequency-independent** constant ($c_P/\cos^2\theta$) across the full band from 0 Hz to the gauge-length notch frequency. No frequency correction is needed. This makes DAS naturally suited for recording low-frequency seismic signals — surface waves, slow earthquakes, tidal deformation — that fall below the natural frequency of short-period geophones.

!!! warning "Strain vs. Strain Rate"
    Many DAS systems output **strain rate** $\dot{\varepsilon}$ (time derivative of strain) rather than strain. Strain rate relates to particle velocity as $\dot{\varepsilon} = -(\cos^2\theta / c_P) \cdot \dot{v}_P$, i.e., proportional to **acceleration** — not flat in velocity. To recover the flat velocity response, integrate in time (divide by $i\omega$ in the frequency domain) to obtain strain first.

---

## Gauge Length Effect

### Spatial Integration Filter

DAS does not measure strain at a true point. Instead, it measures the phase difference between the two ends of a gauge-length segment of length $L$, equivalent to **spatial averaging** of the strain over that segment:

$$
\varepsilon_\mathrm{GL}(x_0, t) = \frac{u_x(x_0 + L/2,\, t) - u_x(x_0 - L/2,\, t)}{L}
$$

### Transfer Function Derivation

For a plane wave $u_x = A e^{i(k_x x - \omega t)}$:

$$
\varepsilon_\mathrm{GL} = \frac{Ae^{ik_x(x_0+L/2)} - Ae^{ik_x(x_0-L/2)}}{L} \cdot e^{-i\omega t}
= \frac{2i\sin(k_x L/2)}{L} \cdot Ae^{ik_x x_0} e^{-i\omega t}
$$

Since the point strain is $\varepsilon_\mathrm{point} = ik_x Ae^{ik_x x_0}e^{-i\omega t}$, the gauge-length transfer function is:

$$
H(k_x) = \frac{\varepsilon_\mathrm{GL}}{\varepsilon_\mathrm{point}} = \frac{\sin(k_x L/2)}{k_x L/2} = \mathrm{sinc}\!\left(\frac{k_x L}{2\pi}\right)
$$

In terms of frequency (substituting $k_x = 2\pi f \cos\theta / c$):

$$
\boxed{H(f, \theta) = \mathrm{sinc}\!\left(\frac{f L \cos\theta}{c}\right)}
$$

### Notch Frequencies

The sinc function is zero at $k_x L/2 = n\pi$ ($n = 1, 2, 3, \ldots$), giving **notch frequencies**:

$$
f_n = \frac{n \cdot c}{L\cos\theta} = \frac{n \cdot c_\mathrm{app}}{L}
$$

where $c_\mathrm{app} = c/\cos\theta$ is the **apparent velocity** along the fiber.

!!! note "Physical Interpretation"
    When the apparent wavelength along the fiber $\lambda_\mathrm{app} = c_\mathrm{app}/f$ equals the gauge length $L$ (i.e., $f = c_\mathrm{app}/L$), displacements at the two gauge endpoints are **equal in magnitude but opposite in sign**, so their difference is exactly zero — producing the first notch.

### Gauge Length Trade-offs

| Gauge length $L$ | First notch $f_1$ ($c$ = 3000 m/s, $\theta$ = 0°) | SNR |
|------------------|----------------------------------------------------|-----|
| 5 m | 600 Hz | Low (short integration) |
| 10 m | 300 Hz | Medium |
| 20 m | 150 Hz | Higher |
| 50 m | 60 Hz | High, but significant high-frequency loss |

!!! warning "Gauge Length Selection Is Critical"
    A gauge length that is too large lowers the notch frequency, causing high-frequency signal loss. Too small a gauge length reduces the per-channel SNR. In practice, $L = 5$–$20$ m is typical, chosen based on the target signal band and deployment geometry.

The angular dependence: larger $\theta$ (wave more perpendicular to fiber) → smaller $k_x$ → higher notch frequency (better high-frequency preservation), but weaker amplitude (smaller $\cos^2\theta$ factor).

![Gauge length effect](../assets/images/das_gauge_length.png)
*Figure 2: DAS transfer function $|H(f)|$ for different gauge lengths ($\theta = 0°$, $c = 3000$ m/s). Larger gauge lengths shift the first notch to lower frequencies.*

### Optimum Gauge Length: SNR–Resolution Trade-off

The analysis above reveals two opposing effects: **too short a gauge length → poor SNR; too long a gauge length → reduced resolution and wavelet distortion**. Dean, Cuny & Hartog (2017) provide a quantitative treatment for axially incident P-waves ($\theta = 0°$, the VSP geometry).

#### SNR Analysis

For a P-wave propagating along the fiber axis, the strain waveform is a spatial **Ricker wavelet**:

$$
\varepsilon(x) = \left(1 - 2\pi^2 k^2 x^2\right) e^{-\pi^2 k^2 x^2}, \quad k = \frac{\pi f_p}{v}
$$

The total fiber length change $\Delta L$ measured by DAS is the integral of strain over the gauge length:

$$
\Delta L = \int_{-L/2}^{L/2} \varepsilon(x)\,\mathrm{d}x = L\, e^{-\pi^2 k^2 (L/2)^2}
$$

The phase measurement error $E(\Delta L)$ is independent of gauge length (determined by laser coherence), so **SNR ∝ $\Delta L$**. Maximizing $\Delta L$ with respect to $L$:

$$
\boxed{L_\mathrm{SNR} = \frac{\lambda_s}{\sqrt{3}} \approx 0.577\,\lambda_s}
$$

where the spatial wavelength is $\lambda_s = v\lambda_t = v\sqrt{6}/(\pi f_p)$.

#### Resolution Analysis — Wavelet Distortion Modes

The gauge-length integration acts as a **box-car (moving-average) filter**, whose frequency response is the sinc function. As $L$ increases, the notch frequency moves into the signal band:

| GL/$\lambda_s$ ratio | Wavelet state | SNR |
|---------------------|---------------|-----|
| $< 0.40$ | Normal, high resolution | Low (weak signal) |
| $0.40$–$0.54$ | **Optimal zone**: high SNR + good resolution | > 90 % of maximum |
| $\approx 0.577$ | Peak SNR; slight wavelet broadening | Maximum |
| $\approx 1.0$ | Notch enters main bandwidth; **flat-topped** wavelet | High but poor resolution |
| $> 1.0$ | **Double-lobed** (two peaks) wavelet; severe distortion | Avoid |

#### Optimum Gauge Length Formula

Combining SNR > 90% of maximum and wavelength error < 15%, the optimal ratio is $GL/\lambda_s \approx 0.40$–$0.54$; the recommended value is 0.5, giving (Dean et al. 2017, eq. 18):

$$
\boxed{L_\mathrm{opt} = \frac{\mathrm{ratio} \times v}{f_p} \approx \frac{0.5\,v}{f_p} = \frac{\lambda_s}{2}}
$$

!!! tip "Practical Example"
    In a VSP survey, a zone with apparent velocity $v = 3000$ m/s and peak frequency $f_p = 50$ Hz:
    $$L_\mathrm{opt} \approx \frac{0.5 \times 3000}{50} = 30\text{ m}, \quad \lambda_s \approx 46.8\text{ m}$$
    If apparent velocities range from 2900 to 5900 m/s over the full well, **apply different optimum gauge lengths at different depths** to maintain optimal SNR and resolution throughout.

!!! warning "Hardware Lower Bound"
    When $L$ approaches the laser pulse width (~8 m), the phase–strain relationship becomes nonlinear and the DAS measurement breaks down. Thus $L_\mathrm{min} \approx 8$ m is a hard lower limit regardless of the theoretical optimum.

![Optimum gauge length](../assets/images/das_gauge_opt.png)
*Figure 3: Left — normalised $\Delta L$ (SNR proxy) vs $GL/\lambda_s$; the green region marks SNR > 90 % of the maximum, and the red region marks the wavelet-distortion zone. Right — normalised DAS wavelet output for five GL/$\lambda_s$ ratios ($f_p$ = 40 Hz, $v$ = 1000 m/s, $\lambda_s \approx$ 19.5 m). After Dean et al. (2017).*

---

## Python Example

The code below reproduces both figures: the directional sensitivity polar plot and the gauge-length transfer function.

```python
import numpy as np
import matplotlib.pyplot as plt

# ── Figure 1: Directional sensitivity polar plots ─────────
theta = np.linspace(0, 2 * np.pi, 720)
resp_P  = np.cos(theta) ** 2
resp_SV = np.abs(np.sin(2 * theta)) / 2

fig, axes = plt.subplots(1, 2, figsize=(11, 5),
                          subplot_kw=dict(projection='polar'))

for ax, resp, color, desc in [
    (axes[0], resp_P,  '#3498db',
     'P-wave\n' + r'$|\varepsilon_{xx}| \propto \cos^2\theta$'),
    (axes[1], resp_SV, '#e67e22',
     'SV-wave\n' + r'$|\varepsilon_{xx}| \propto |\sin 2\theta|/2$'),
]:
    ax.plot(theta, resp, color=color, lw=2)
    ax.fill(theta, resp, alpha=0.25, color=color)
    ax.set_theta_zero_location('E')
    ax.set_theta_direction(1)
    ax.set_xticks(np.deg2rad([0, 45, 90, 135, 180, 225, 270, 315]))
    ax.set_xticklabels(['0° (fiber)', '45°', '90°', '135°',
                         '180°', '225°', '270°', '315°'], fontsize=8)
    ax.set_yticks([0.5, 1.0])
    ax.set_title(desc, pad=14, fontsize=10)

plt.suptitle('DAS Directional Sensitivity  (fiber along 0°–180° axis)',
             y=1.02, fontsize=12)
plt.tight_layout()
plt.savefig('docs/assets/images/das_angle_response.png', dpi=150, bbox_inches='tight')

# ── Figure 2: Gauge length transfer function ──────────────
c   = 3000.0
GLs = [5, 10, 20, 50]
colors = ['#2ecc71', '#3498db', '#e67e22', '#e74c3c']
f = np.linspace(0.1, 650, 3000)

fig, ax = plt.subplots(figsize=(9, 5))
for L, color in zip(GLs, colors):
    kxL_half = np.pi * f * L / c
    H = np.abs(np.sinc(kxL_half / np.pi))
    ax.plot(f, 20 * np.log10(np.clip(H, 1e-6, None)),
            color=color, lw=2, label=f'GL = {L} m   (1st notch: {int(c/L)} Hz)')

ax.axhline(-3, color='k', lw=0.8, ls=':', alpha=0.6, label=r'$-3$ dB')
ax.set(xlabel='Frequency (Hz)', ylabel='DAS / Point-sensor (dB)',
       title=r'Gauge Length Effect: $|H(f)|$  ($\theta=0°$, $c_{\rm app}=3000$ m/s)',
       xlim=[0, 650], ylim=[-60, 3])
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('docs/assets/images/das_gauge_length.png', dpi=150, bbox_inches='tight')
plt.show()
```

---

## References

- Lindsey, N. J., Martin, E. R., Dreger, D. S., Freifeld, B., White, S., Monga, S. K., … & Ajo-Franklin, J. B. (2017). Fiber-optic network observations of earthquake wavefields. *Geophysical Research Letters*, 44(23), 11–792.
- Mateeva, A., Lopez, J., Potters, H., Mestayer, J., Cox, B., Kiyashchenko, D., … & Berlang, W. (2014). Distributed acoustic sensing for reservoir monitoring with vertical seismic profiling. *Geophysical Prospecting*, 62(4), 679–692.
- Marra, G., Clivati, C., Luckett, R., Tampellini, A., Kronjäger, J., Wright, L., … & Margolis, H. S. (2018). Ultrastable laser interferometry for earthquake detection with terrestrial and submarine cables. *Science*, 361(6401), 486–490.
- Wang, H. F., Zeng, X., Miller, D. E., Fratta, D., Feigl, K. L., Thurber, C. H., & Mellors, R. J. (2018). Ground motion response to an ML 4.3 earthquake using co-located distributed acoustic sensing and seismometers. *Geophysical Journal International*, 213(3), 2020–2036.
- Daley, T. M., Miller, D. E., Dodds, K., Cook, P., & Freifeld, B. M. (2016). Field testing of modular borehole monitoring with simultaneous distributed acoustic sensing and geophone vertical seismic profiles at Citronelle, Alabama. *Geophysical Prospecting*, 64(5), 1318–1334.
- Zhan, Z. (2020). Distributed acoustic sensing turns fiber-optic cables into seismic stations. *Bulletin of the Seismological Society of America*, 110(3), 975–985.
- Dean, T., Cuny, T., & Hartog, A. H. (2017). The effect of gauge length on axially incident P-waves measured using fibre optic distributed vibration sensing. *Geophysical Prospecting*, 65(1), 184–193. https://doi.org/10.1111/1365-2478.12419
