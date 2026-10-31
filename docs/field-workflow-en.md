# Borehole DAS: from raw data to phase interpretation

Use this workflow to establish clocks, coordinates and measurement units before detecting a wave packet, naming a phase or attempting inversion. See [DAS fundamentals](das-en.md) and [borehole Rayleigh waves](borehole-rayleigh-en.md) for the forward operators.

## 1. Inventory data and geometry

Record the event time zone, filename clock, internal timestamps, independent timing checks, sampling rate, gaps, gauge length, actual channel spacing, measurement type and calibration. Channel counts and lead-in lengths can change between acquisition periods.

For cable coordinate \(s_j=s_0+j\Delta s\) and well entry \(s_w\), distance along the borehole is \(\ell_j=s_j-s_w\). A gauge-centred channel is wholly in the well only if its full interval \([s_j-L_g/2,s_j+L_g/2]\) is inside it. Flag gauges crossing deployment boundaries. True vertical depth requires the trajectory: \(z(\ell)=\int_0^\ell\cos\alpha(s)\,ds\).

Keep original clock fields when UTC+8 filenames conflict with +00:00 attributes. Resolve them using acquisition records or independent timing; never shift a trace merely to match a prediction. GPS status alone is not independent proof of absolute timing. Check NaN/Inf, zero channels, clipping, fading and termination reflections.

## 2. Define search and download windows

[ObsPy TauP](https://docs.obspy.org/packages/obspy.taup.html) predicts body-wave arrivals in a one-dimensional spherical model. Comparing IASP91 and AK135 provides search scenarios, not a confidence interval for a regional path. Account for source depth and receiver depth.

For epicentral distance \(D\), bracket surface-wave packets with assumed group speeds:

\[
t_{\mathrm{surf}}\in[t_0+D/U_{\max},\ t_0+D/U_{\min}].
\]

Add pre-event noise, model-error margins and late arrivals. State whether downloads use half-open intervals \([t_a,t_b)\); for minute files, the file starting exactly at the end normally lies outside that interval. Packet travel times constrain group speed, not phase dispersion. See the [TauP calculation notes](https://taup.readthedocs.io/en/latest/calculations.html) for spherical and distance assumptions.

## 3. Preprocess continuous records

1. Check monotonic timestamps, sampling intervals and every file seam.
2. Anti-alias before decimation. Use real neighbouring data at internal boundaries and mask filter transients at the outer ends.
3. Fix the background, passbands and channel mask; preserve signed amplitudes. AGC or trace-normalized displays cannot supply quantitative depth amplitudes.
4. Compare raw/broadband, two-pass zero-phase and causal filtering near onsets. Two-pass filters can produce pre-ringing; causal filters and envelopes introduce delays.
5. Recompute representative channels at the native sampling rate.

A local impulse can become an oscillatory narrowband packet. Vary passbands, windows and impulse masks on diagnostic copies, recording all exclusions. Removing a wide interval can remove genuine signal as well, so this is a sensitivity check rather than an unbiased test.

## 4. Separate detection from phase identification

| Evidence | Defensible statement | Further checks |
|---|---|---|
| Exceeds matched noise; reproducible from raw data | Candidate packet exists | Non-event controls and instrument artefacts |
| Timing, spectra and depth coherence agree | Compatible with a phase family | Polarization, direction, nearby stations and competing branches |
| Independent observations identify a branch | Reliable phase identification | Pick and model uncertainty |
| Adequate signal and validated forward operator | Conditional parameter inversion | Coupling, orientation, resolution and holdout tests |

Energy near predicted S time may contain P coda, conversions or scattering. Failure to isolate an S onset does not prove absence of S energy. Ideal vertical DAS is insensitive to SH, but its SV geometrical factor \(|\sin i\cos i|\) peaks near \(45^\circ\). General statements that vertical DAS cannot see S are therefore inappropriate; see [Näsholm et al. (2022)](https://doi.org/10.1029/2021JB023587).

## 5. Distinguish amplitude statistics and array operators

\[
R_{\mathrm{stack}}=\frac{\operatorname{RMS}_E[\sum_jw_jd_j]}{\operatorname{RMS}_B[\sum_jw_jd_j]},\qquad
R_{\mathrm{channel}}=\operatorname{median}_j\frac{\operatorname{RMS}_E[d_j]}{\operatorname{RMS}_B[d_j]}.
\]

These are different quantities. The first includes coherence gain, noise suppression and cancellation; both compare signal-plus-noise against background, not automatically pure-signal SNR. Noise-power subtraction requires stationary, uncorrelated noise assumptions and explicit treatment of non-positive differences.

For an equal-amplitude plane wave with along-well slowness \(q\), direct averaging over aperture \(A\) has response

\[
H_A(f)=\operatorname{sinc}_\pi(fqA),\quad
\operatorname{sinc}_\pi(x)=\sin(\pi x)/(\pi x).
\]

Its first zero is \(1/(|q|A)\). A teaching example with \(q=0.20\,\mathrm{s/km}\) and \(A=2.9\,\mathrm{km}\) gives 1.72 Hz, whereas an 8 m gauge gives 625 Hz for the same wave. Whole-well stacking and gauge averaging operate at different spatial scales. Compare moveout-corrected stacks, subapertures and single-channel spectra before attributing a low-frequency preference to the medium.

## 6. Interpret signed slowness and mixed wavefields

For a pure plane wave, \(q=dt/d\ell=\mathbf p\cdot\mathbf t\); a straight vertical well gives \(q=\cos i/c\). Its reciprocal is apparent along-well speed, not generally material velocity. Define the sign convention: with depth positive down, positive \(q\) means deeper channels arrive later.

An upgoing incident P wave can overlap downgoing reflected P and converted SV at a free surface. Their DAS strain weights differ. A downward phase gradient in a P window neither uniquely identifies downgoing P nor necessarily follows net energy flow. Separate regional packet generation from receiver-side conversions.

Scan both signs of slowness and compare adjacent bands, odd/even channels, subapertures and fixed control windows. A coherence maximum remains candidate evidence. See [VSP](vsp-en.md) and [F-K / Radon](fk-radon-en.md).

## 7. Decide whether inversion is justified

Require adequate signal, known units/clocks/geometry and a forward model containing the dominant receiver effects. A visible stack need not support channel-by-channel amplitude inversion; timing and slowness compatible with S need not identify S sufficiently for \(V_S\) inversion.

Report observables first: passbands, windows, channels, signed slowness, amplitude statistics, phase/coherence and sensitivity. Then report model assumptions, coupling/orientation, regularization and withheld frequency/event validation. A mechanism synthesis is a feasibility test until compared against data.

## Sources

- [ObsPy TauP](https://docs.obspy.org/packages/obspy.taup.html) and [TauP calculation notes](https://taup.readthedocs.io/en/latest/calculations.html).
- Näsholm, S. P., et al. (2022). *Array Signal Processing on Distributed Acoustic Sensing Data: Directivity Effects in Slowness Space*. [DOI](https://doi.org/10.1029/2021JB023587).
- Lellouch, A., et al. (2019). *Seismic Velocity Estimation Using Passive Downhole Distributed Acoustic Sensing Records: Examples From the San Andreas Fault Observatory at Depth*. [DOI](https://doi.org/10.1029/2019JB017533).

Processing recommendations also synthesize project experience. Teaching examples and quality-control procedures do not independently identify phases in a particular earthquake.
