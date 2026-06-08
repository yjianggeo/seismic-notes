# Vertical Seismic Profiling (VSP)

## Introduction

**Vertical Seismic Profiling (VSP)** is a borehole seismic technique in which receivers (geophones or DAS fiber) are deployed inside a wellbore while sources are activated at the surface (or in a second well). Compared with surface reflection seismology, VSP offers several unique advantages:

- **Shorter propagation path**: Seismic energy travels one-way through the target, preserving higher frequencies and yielding better vertical resolution.
- **Direct velocity measurement**: First-arrival times of downgoing direct waves give interval velocities without velocity analysis.
- **Dual wavefield recording**: Both downgoing direct waves and upgoing reflected waves are recorded simultaneously and can be exploited separately.
- **Accurate Q estimation**: The nearly vertical propagation path of direct waves between adjacent receiver levels makes VSP ideal for spectral-ratio Q inversion.
- **Near-well high-resolution imaging**: Upgoing reflections can be migrated to produce a detailed subsurface image in the vicinity of the well.

$$
\boxed{
t_\downarrow(z) = \frac{z}{V}, \qquad
t_\uparrow(z) = \frac{2z_r - z}{V}
}
$$

Downgoing direct-wave travel time increases with depth (**positive slope**); upgoing reflected-wave travel time decreases with depth (**negative slope**). This is the most characteristic feature of a VSP gather and forms the basis of wavefield separation.

---

## Observation Geometry and Wavefield Composition

### Basic Geometry

A standard VSP deploys a **receiver array** (or DAS fiber) in a borehole from the surface to near the target depth, while a **seismic source** is activated at the surface.

| Element | Typical values | Notes |
|---------|---------------|-------|
| Receiver depth range | 100 m – full well depth | Limited by target position |
| Level spacing | 5–50 m (conventional); 1 m (DAS) | Determines spatial sampling |
| Source offset | 0 (zero-offset) to several km | Controls illumination angle |
| Sampling rate | 0.25–2 ms | Often finer than surface acquisition |

### Wavefield Components

A VSP record contains several distinct phases:

| Phase | Apparent velocity | Role |
|-------|------------------|------|
| **Downgoing direct P-wave** | $+V_P$ | Strongest, most stable; used for velocity and Q |
| **Downgoing direct S-wave** | $+V_S$ | Converted or S-wave source |
| **Upgoing P reflection** | $-V_P$ | From impedance contrasts below; used for imaging |
| **Upgoing converted wave (PS)** | $-V_S$ | P-to-S conversion; useful for anisotropy |
| **Tube wave** | $\approx$ 1000–1500 m/s | Propagates along the borehole; treated as noise |
| **Multiples** | $\pm V_P$ | Require suppression |

### Apparent Velocity and Wavefield Separation

In a depth-time ($z$-$t$) VSP gather, each phase has a characteristic **apparent velocity slope**.

For vertical incidence (zero-offset VSP), with the source at $z = 0$, receiver at depth $z$, and reflector at depth $z_r$:

$$
t_\downarrow = \frac{z}{V_P} \quad \Rightarrow \quad \frac{\partial t_\downarrow}{\partial z} = +\frac{1}{V_P} \quad \text{(downgoing — positive slope)}
$$

$$
t_\uparrow = \frac{z_r}{V_P} + \frac{z_r - z}{V_P} = \frac{2z_r - z}{V_P} \quad \Rightarrow \quad \frac{\partial t_\uparrow}{\partial z} = -\frac{1}{V_P} \quad \text{(upgoing — negative slope)}
$$

The two lines intersect at $z = z_r$ — the **crossover point** — whose depth equals the reflector depth.

![VSP geometry and gather](../assets/images/vsp_overview.png)
*Figure 1: Left — VSP observation geometry (zero-offset and offset sources, downgoing direct and upgoing reflected ray paths). Right — typical VSP gather: orange = downgoing direct P-wave (positive slope); green = upgoing reflection (negative slope); they cross at the reflector depth.*

---

## VSP Survey Configurations

| Configuration | Source setup | Primary use | Characteristics |
|---------------|-------------|------------|-----------------|
| **Zero-Offset VSP** (ZVSP) | Single point, directly above well | Velocity, Q, VSP-CDP imaging | Most common; near-vertical incidence |
| **Offset VSP** | Single point, fixed horizontal offset | Wider near-well imaging; anisotropy | Oblique ray paths |
| **Walk-above VSP** | Single offset; corridor stack only | Comparison with surface seismic | High-resolution "corridor" |
| **Walkaway VSP** | Multiple points along a surface line | Lateral velocity model; anisotropy | Analogous to refraction/reflection profiling |
| **3D VSP** | Dense surface grid | 3D near-well imaging | Analogous to 3D surface seismic |
| **DAS VSP** | Any configuration | High-resolution Q profile; dense imaging | Fiber replaces geophone string |

![VSP types](../assets/images/vsp_types.png)
*Figure 2: From left to right — zero-offset VSP, offset VSP, walkaway VSP (multiple sources), DAS VSP (continuous fiber). Background color gradients represent different geological layers.*

---

## Wavefield Separation

### Purpose

Separating the **downgoing** and **upgoing** wavefields is a fundamental VSP processing step:

- **Downgoing direct waves** → interval velocity and Q estimation
- **Upgoing reflected waves** → subsurface imaging and well-seismic tie

The opposite apparent-velocity signs of the two wavefields enable clean separation.

### F-K Filtering

Apply a 2D Fourier transform to the VSP gather over depth $z$ and time $t$:

$$
D(f, k_z) = \iint d(z, t)\, e^{-i(2\pi f t - k_z z)}\, dz\, dt
$$

- **Downgoing waves**: $k_z > 0$ (positive wavenumber, energy moving downward)
- **Upgoing waves**: $k_z < 0$ (negative wavenumber, energy moving upward)

Applying a two-sided F-K mask that passes only positive or negative $k_z$ and inverse transforming back to the $z$-$t$ domain yields the separated wavefields.

!!! warning "Spatial Aliasing"
    If the level spacing $\Delta z$ is too large, spatial aliasing mixes upgoing and downgoing energy in the F-K domain. The Nyquist spatial frequency is $k_{z,\max} = \pi/\Delta z$, requiring $\Delta z < V_P / (2f_{\max})$. DAS's sub-meter channel spacing nearly eliminates this problem.

### Median Filtering

Apply a median filter along **constant apparent-velocity trajectories** (fixed-slope lines) to model and extract the downgoing wavefield, then subtract it from the original gather to isolate upgoing reflections. Computationally efficient and robust to non-stationary noise.

### Polynomial Subtraction

For each frequency component, fit the downgoing wave phase and amplitude across receiver depths using least-squares polynomials, then subtract to obtain the upgoing wavefield.

---

## Applications

### Interval Velocity and Velocity Model Building

First-arrival times of downgoing direct P-waves give **interval velocities** directly:

$$
V_P(z_1, z_2) = \frac{z_2 - z_1}{t_\downarrow(z_2) - t_\downarrow(z_1)}
$$

This is among the most accurate velocity measurement techniques available, and serves as a hard constraint for full-waveform inversion (FWI) and seismic velocity analysis.

### Q Estimation — Spectral Ratio Method

The amplitude spectral ratio of downgoing direct waves between depths $z_1$ and $z_2$ encodes the attenuation of the intervening layer:

$$
\ln\!\left[\frac{A(f, z_2)}{A(f, z_1)}\right] = \ln\!\left(\frac{G_1}{G_2}\right) - \pi f\,\Delta t^*
$$

where $\Delta t^* = \Delta t / Q_\text{eff}$ and $\Delta t = (z_2 - z_1)/V_P$. The slope of the log spectral ratio versus frequency yields Q directly.

!!! tip "Why VSP Spectral Ratios Are Especially Clean"
    Compared with surface seismic, VSP spectral-ratio Q estimation benefits from: ① nearly vertical, geometrically simple propagation paths (easy geometric-spreading correction); ② source wavelet directly recorded in the well (no assumptions needed); ③ dense channel spacing (DAS VSP can reach 1 m), enabling a near-continuous Q(z) profile. See [Spectral Ratio Q Inversion](q-spectral-ratio-en.md) for the full derivation.

### Well-Seismic Tie

VSP connects **well log data** (acoustic and density logs → impedance) to **surface seismic** by providing a reliable time-depth relationship:

1. Extract a zero-phase wavelet from the VSP downgoing direct waves (deconvolve the source signature).
2. Convolve the log-derived reflectivity series with this wavelet to generate a **synthetic VSP trace**.
3. Compare with the real VSP record to calibrate horizon picks and tie well tops to seismic events.

!!! note "Q Effects on Synthetic Records"
    Standard synthetic seismograms computed from well logs ignore attenuation. VSP wavelets naturally include Q effects accumulated along the real propagation path, making VSP-based well ties more accurate for deep targets than pure log-convolution synthetics.

### VSP-CDP Reflection Imaging

Upgoing reflected waves carry information about subsurface interfaces near the well. The **VSP-CDP transformation** maps each (source position, receiver depth, reflection travel time) triplet to the spatial position of the reflection point:

For zero-offset VSP, the one-way travel time from receiver depth $z$ to the reflector is:

$$
t_\text{refl}(z) = \frac{t_\uparrow(z) - t_\downarrow(z)}{2}
$$

Converting $t_\text{refl}$ to depth using the velocity model gives the reflection-point depth and, for non-vertical geometries, its lateral position. The resulting **VSP-CDP section** typically has higher vertical resolution than surface reflection data but more limited lateral coverage.

### Anisotropy Measurement

In offset or walkaway VSP acquisitions, P-wave and converted S-wave (PS) velocities vary with source azimuth when the formation has **elastic anisotropy** (e.g., fracture-induced HTI). The time difference and polarization direction of the fast and slow S-waves constrain fracture orientation and density.

### DAS VSP

Deploying DAS fiber in a borehole combines the benefits of both technologies:

- **Continuous coverage**: simultaneous recording along the entire well depth without dead zones
- **Ultra-dense spatial sampling**: channel spacings as small as 1 m dramatically improve wavefield separation and Q profile resolution
- **Low deployment cost**: no tripping required; can share infrastructure with permanent fiber monitoring systems

DAS VSP processing requires additional corrections for **directional sensitivity** ($\cos^2\theta$) and the **gauge-length sinc filter**, as detailed in [DAS Distributed Acoustic Sensing](das-en.md) and [Spectral Ratio Q Inversion](q-spectral-ratio-en.md).

---

## Python Example

The code below reproduces both figures in this note.

```python
import numpy as np
import matplotlib.pyplot as plt

# ── Figure 1: VSP geometry and gather ─────────────────────
fig, axes = plt.subplots(1, 2, figsize=(13, 7))

# Left: geometry cross-section
ax = axes[0]
ax.set_xlim(-600, 2800); ax.set_ylim(3200, -300)
ax.set_xlabel('Offset (m)'); ax.set_ylabel('Depth (m)')
ax.set_title('VSP Observation Geometry', fontweight='bold')
borehole_x = 600
ax.axhline(0, color='saddlebrown', lw=2.5)
ax.fill_between([-600, 2800], [-300, -300], [0, 0], color='bisque', alpha=0.6)
ax.plot([borehole_x]*2, [0, 3000], color='gray', lw=2.5, ls='--')
recv_depths = np.arange(250, 2750, 250)
for z in recv_depths:
    ax.plot(borehole_x, z, 's', color='steelblue', ms=8)
refl_d = 2600
ax.axhline(refl_d, xmin=0.05, xmax=0.9, color='darkorange', lw=2.5)
for sx, color in [(600, 'red'), (1800, 'darkred')]:
    ax.plot(sx, -100, '*', color=color, ms=16)
for z in recv_depths[::2]:
    ax.annotate('', xy=(borehole_x, z), xytext=(600, 0),
                arrowprops=dict(arrowstyle='->', color='#e67e22', lw=0.9, alpha=0.55))
ax.annotate('', xy=(borehole_x, 1500), xytext=(borehole_x, refl_d),
            arrowprops=dict(arrowstyle='->', color='#27ae60', lw=2.0))
ax.grid(True, alpha=0.2)

# Right: VSP gather
ax = axes[1]
V = 2000.0; z_r = 2600.0
depths = np.linspace(50, 3000, 500)
t_down = depths / V * 1000
t_up   = (2*z_r - depths) / V * 1000
mask   = depths < z_r
ax.plot(t_down, depths, color='#e67e22', lw=2.5, label='Downgoing (direct P)')
ax.plot(t_up[mask], depths[mask], color='#27ae60', lw=2.5, label='Upgoing (reflection)')
ax.axhline(z_r, color='darkorange', lw=1.5, ls='--', alpha=0.8, label='Reflector depth')
ax.plot(z_r/V*1000, z_r, 'o', color='darkorange', ms=11)
ax.fill_betweenx(depths[mask], t_down[mask], t_up[mask], alpha=0.06, color='royalblue')
ax.set_xlabel('Time (ms)'); ax.set_ylabel('Receiver Depth (m)')
ax.set_title('VSP Gather', fontweight='bold')
ax.set_ylim(3100, 0); ax.set_xlim(0, 2800)
ax.legend(loc='lower right', fontsize=9); ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('docs/assets/images/vsp_overview.png', dpi=150, bbox_inches='tight')
plt.show()
```

---

## References

- Aki, K., & Richards, P. G. (2002). *Quantitative Seismology* (2nd ed.). University Science Books.
- Hardage, B. A. (1983). *Vertical Seismic Profiling. Part A: Principles* (2nd ed.). Geophysical Press.
- Hinds, R. C., Anderson, N. L., & Kuzmiski, R. D. (1996). *VSP Interpretive Processing: Theory and Practice*. Society of Exploration Geophysicists.
- Balch, A. H., & Lee, M. W. (1984). *Vertical Seismic Profiling: Technique, Applications and Case Histories*. International Human Resources Development Corp.
- Mateeva, A., Lopez, J., Potters, H., Mestayer, J., Cox, B., Kiyashchenko, D., … & Berlang, W. (2014). Distributed acoustic sensing for reservoir monitoring with vertical seismic profiling. *Geophysical Prospecting*, 62(4), 679–692.
- Tonn, R. (1991). The determination of the seismic quality factor Q from VSP data: A comparison of different computational methods. *Geophysical Prospecting*, 39(1), 1–27.
- Toverud, T., & Ursin, B. (2005). Comparison of seismic attenuation models using zero-offset vertical seismic profiling (VSP) data. *Geophysics*, 70(2), F17–F25.
