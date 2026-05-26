# Brune 震源谱模型

## 引言

Brune 模型（Brune source model）由 Brune（1970, 1971）提出，是地震学中最广泛使用的震源谱模型。它将断层破裂简化为**圆形裂纹的瞬时应力降**，从而用少量参数——地震矩 $M_0$、拐角频率 $f_c$、应力降 $\Delta\sigma$——描述地震辐射的远场位移谱。

模型的核心预测是远场 S 波位移振幅谱满足：

$$
\boxed{|\Omega(f)| = \frac{\Omega_0}{1 + (f/f_c)^2}}
$$

低频平坦、高频按 $f^{-2}$ 衰减，因此又称 **$\omega^{-2}$ 模型**或 **omega-square 模型**。

---

## 物理模型

### 基本假设

| 假设 | 说明 |
|------|------|
| 圆形断层 | 断层面为半径 $r$ 的圆形裂纹 |
| 瞬时均匀应力降 | $t=0$ 时刻全断层面均匀卸载，应力降 $\Delta\sigma$ 为常数 |
| 无限均匀介质 | 忽略波速梯度、介质非均匀性 |
| 远场近似 | 观测距离 $R \gg r$，只考虑辐射波场 |
| S 波主导 | 位移谱由 S 波贡献，P 波类似但常数不同 |

### 震源几何

断层面为半径 $r$ 的圆盘，面积 $S = \pi r^2$。地震矩由滑动量 $D$ 和剪切模量 $\mu = \rho\beta^2$ 决定：

$$
M_0 = \mu \bar{D} S = \rho\beta^2 \bar{D} \pi r^2
$$

其中 $\bar{D}$ 是断层面上的平均滑动量，$\rho$ 是介质密度，$\beta$ 是 S 波速度。

---

## 远场位移与地震矩

### 点源远场位移

对于点震源，远场 S 波位移可写为（Aki & Richards, 2002）：

$$
u^S(\mathbf{x}, t) = \frac{\mathcal{R}_{\theta\phi}}{4\pi\rho\beta^3 R}\, \dot{M}_0\!\left(t - \frac{R}{\beta}\right)
$$

其中：

- $\mathcal{R}_{\theta\phi}$：S 波辐射花样系数（radiation pattern）
- $R$：震中距（台站到震源距离）
- $\dot{M}_0(t)$：地震矩率（seismic moment rate），即地震矩对时间的导数
- $t - R/\beta$：考虑 S 波传播的延迟时间

!!! note "物理含义"
    远场位移正比于矩率 $\dot{M}_0(t)$，而非矩 $M_0(t)$ 本身。矩率反映了断层滑动的**速度**，即震源辐射能量的快慢。

### 频域表达式

对上式两边做傅里叶变换（忽略传播延迟相位因子 $e^{-i\omega R/\beta}$ 的影响，只关注振幅谱）：

$$
|\Omega^S(\omega)| = \frac{\mathcal{R}_{\theta\phi}}{4\pi\rho\beta^3 R}\, |\dot{M}_0(\omega)|
$$

因此，**振幅谱的形状完全由矩率的傅里叶变换** $|\dot{M}_0(\omega)|$ **决定**。

---

## 震源时间函数的推导

### 矩函数与矩率函数

Brune 的物理图像是：$t=0$ 时断层面上应力瞬间降落，断层自由滑动。他认为矩函数（seismic moment function）满足一个类似临界阻尼振子的响应：

$$
M_0(t) = M_0 \left[1 - (1 + \omega_c t)\,e^{-\omega_c t}\right] H(t)
$$

其中 $H(t)$ 为阶跃函数，$\omega_c = 2\pi f_c$ 为拐角角频率。

**验证边界条件：**

- 当 $t = 0$ 时：$M_0(0) = M_0[1 - 1 \cdot 1] = 0$ ✓（破裂前无滑动）
- 当 $t \to \infty$ 时：$e^{-\omega_c t} \to 0$，$M_0(\infty) = M_0$ ✓（最终达到完整地震矩）

**矩率函数**为矩函数对时间的导数：

$$
\dot{M}_0(t) = \frac{d M_0(t)}{dt} = M_0\, \omega_c^2\, t\, e^{-\omega_c t}\, H(t)
$$

**推导过程：**

$$
\frac{d}{dt}\left[(1 + \omega_c t) e^{-\omega_c t}\right]
= \omega_c e^{-\omega_c t} + (1 + \omega_c t)(-\omega_c)e^{-\omega_c t}
= \omega_c e^{-\omega_c t}\left[1 - 1 - \omega_c t\right]
= -\omega_c^2 t\, e^{-\omega_c t}
$$

因此：

$$
\dot{M}_0(t) = M_0 \cdot \omega_c^2 t\, e^{-\omega_c t}\, H(t)
$$

矩率函数从 $t=0$ 处的零值出发，在 $t^* = 1/\omega_c$ 处达到峰值，随后指数衰减：

$$
\dot{M}_0(t^*) = M_0\, \omega_c^2 \cdot \frac{1}{\omega_c} \cdot e^{-1} = \frac{M_0 \omega_c}{e}
$$

下图展示了 $f_c = 5\,\text{Hz}$ 时，矩率函数与矩函数的时程：

![Brune 震源时间函数](../assets/images/brune_source_time.png)

### 矩率函数的傅里叶变换

对 $\dot{M}_0(t) = M_0\,\omega_c^2\, t\, e^{-\omega_c t}\, H(t)$ 做傅里叶变换：

$$
\dot{M}_0(\omega) = M_0\,\omega_c^2 \int_0^{+\infty} t\, e^{-\omega_c t}\, e^{-i\omega t}\, dt
= M_0\,\omega_c^2 \int_0^{+\infty} t\, e^{-(\omega_c + i\omega)\, t}\, dt
$$

利用拉普拉斯积分公式 $\displaystyle\int_0^{+\infty} t\, e^{-at}\, dt = \frac{1}{a^2}$（其中 $a = \omega_c + i\omega$）：

$$
\dot{M}_0(\omega) = M_0\,\omega_c^2 \cdot \frac{1}{(\omega_c + i\omega)^2}
$$

振幅谱：

$$
|\dot{M}_0(\omega)| = \frac{M_0\,\omega_c^2}{|\omega_c + i\omega|^2} = \frac{M_0\,\omega_c^2}{\omega_c^2 + \omega^2}
$$

将分子分母同除以 $\omega_c^2$：

$$
|\dot{M}_0(\omega)| = \frac{M_0}{1 + (\omega/\omega_c)^2}
$$

---

## Brune 位移谱

### 振幅谱形式

将矩率频谱代入远场位移频谱公式：

$$
|\Omega(\omega)| = \frac{\mathcal{R}_{\theta\phi}}{4\pi\rho\beta^3 R} \cdot \frac{M_0}{1 + (\omega/\omega_c)^2}
$$

定义**低频平台**：

$$
\Omega_0 \equiv \frac{\mathcal{R}_{\theta\phi}\, M_0}{4\pi\rho\beta^3 R}
$$

则位移振幅谱为：

$$
\boxed{|\Omega(\omega)| = \frac{\Omega_0}{1 + (\omega/\omega_c)^2}}
$$

或等价地，用频率 $f$（$\omega = 2\pi f$，$\omega_c = 2\pi f_c$）表示：

$$
|\Omega(f)| = \frac{\Omega_0}{1 + (f/f_c)^2}
$$

### 渐近行为

**低频段**（$f \ll f_c$）：

$$
|\Omega(f)| \approx \Omega_0 = \text{常数}
$$

谱平坦，低频平台 $\Omega_0$ 直接反映地震矩 $M_0$。

**高频段**（$f \gg f_c$）：

$$
|\Omega(f)| \approx \Omega_0 \cdot \frac{f_c^2}{f^2} \propto f^{-2}
$$

谱以 $f^{-2}$ 速率衰减，这正是 $\omega^{-2}$ 模型的命名来源。

**拐角处**（$f = f_c$）：

$$
|\Omega(f_c)| = \frac{\Omega_0}{2}
$$

振幅降至低频平台的一半，对应 $-3\,\text{dB}$ 点。

### 对数谱斜率

在双对数坐标下，取对数：

$$
\log|\Omega(f)| = \log\Omega_0 - \log\left[1 + (f/f_c)^2\right]
$$

- $f \ll f_c$：斜率 $\approx 0$（水平）
- $f \gg f_c$：斜率 $\approx -2$（每十倍频程下降 2 个量级）
- 拐点即为 $f_c$

---

## 低频平台与地震矩

### 反演公式

由低频平台 $\Omega_0$ 的定义出发：

$$
\Omega_0 = \frac{\mathcal{R}_{\theta\phi}\, M_0}{4\pi\rho\beta^3 R}
$$

反解地震矩：

$$
M_0 = \frac{4\pi\rho\beta^3 R\, \Omega_0}{\mathcal{R}_{\theta\phi}}
$$

### 辐射花样修正

实际应用中，辐射花样 $\mathcal{R}_{\theta\phi}$ 因台站方位不同而异。通常对多台或多方位取平均，并加入自由表面放大系数 $S_{\text{fs}}$（通常取 2）：

$$
\boxed{M_0 = \frac{4\pi\rho\beta^3 R\, \Omega_0}{F \cdot S_{\text{fs}}}}
$$

其中 $F$ 是对辐射花样的方位平均值（S 波约为 0.63）。

!!! tip "实用意义"
    在频谱图上读取低频平台 $\Omega_0$（单位 m·s），结合介质参数和震中距，即可直接计算地震矩，进而得到矩震级 $M_w = \frac{2}{3}\log_{10}M_0 - 6.07$。

---

## 拐角频率与震源尺度

### 物理推导

Brune（1970）的关键论断：断层破裂引发的 S 波穿越断层所需时间（破裂上升时间）决定了谱拐角频率的量级。

对于半径 $r$ 的圆形断层，S 波穿越时间约为：

$$
t_r \sim \frac{r}{\beta}
$$

因此拐角频率量级为：

$$
f_c \sim \frac{\beta}{r}
$$

Brune（1970）通过更严格的辐射场计算，给出了精确系数：

$$
f_c = \frac{0.37\,\beta}{r}
$$

或等价地写为：

$$
r = \frac{k\,\beta}{f_c}, \quad k = 0.37
$$

不同研究给出的常数 $k$ 略有差异（表中列举常用值）：

| 来源 | 波型 | $k$ 值 |
|------|------|--------|
| Brune (1970) | S 波 | 0.37 |
| Madariaga (1976) | S 波 | 0.21 |
| Madariaga (1976) | P 波 | 0.32 |

!!! warning "注意"
    不同文献使用不同的 $k$ 值，计算应力降时需与所用 $k$ 值对应，不可混用。

### 震源半径与矩震级的关系

将 $r = k\beta/f_c$ 代入地震矩，可得震源尺度与地震矩的量级关系。应力降基本恒定时（通常 $\Delta\sigma \sim 1\text{--}10\,\text{MPa}$），更大地震矩意味着更大的震源半径和更低的拐角频率：

$$
M_0 \uparrow \implies r \uparrow \implies f_c \downarrow
$$

---

## 应力降

### 圆形裂纹理论（Eshelby 1957）

对均匀弹性介质中的圆形裂纹，利用 Eshelby（1957）的结果，均匀应力降 $\Delta\sigma$ 下断层面上的滑动量分布为：

$$
D(\xi) = \frac{24}{7\pi} \frac{\Delta\sigma}{\mu} \sqrt{r^2 - \xi^2}, \quad \xi \leq r
$$

其中 $\xi$ 是断层面内到圆心的径向距离。

### 平均滑动量计算

对断层面积分求平均滑动量：

$$
\bar{D} = \frac{1}{\pi r^2}\int_0^r D(\xi) \cdot 2\pi\xi\, d\xi
= \frac{2}{r^2} \cdot \frac{24}{7\pi} \frac{\Delta\sigma}{\mu} \int_0^r \xi\sqrt{r^2 - \xi^2}\, d\xi
$$

计算内层积分，令 $u = r^2 - \xi^2$，$du = -2\xi\,d\xi$：

$$
\int_0^r \xi\sqrt{r^2 - \xi^2}\, d\xi = -\frac{1}{2}\int_{r^2}^{0} \sqrt{u}\, du = \frac{1}{2}\int_0^{r^2} u^{1/2}\, du = \frac{1}{2}\cdot\frac{2}{3} r^3 = \frac{r^3}{3}
$$

代入：

$$
\bar{D} = \frac{2}{r^2} \cdot \frac{24}{7\pi} \cdot \frac{\Delta\sigma}{\mu} \cdot \frac{r^3}{3} = \frac{16}{7\pi} \cdot \frac{\Delta\sigma\, r}{\mu}
$$

### 从 $M_0$ 推导应力降公式

$$
M_0 = \mu\,\bar{D}\,\pi r^2 = \mu \cdot \frac{16}{7\pi}\frac{\Delta\sigma\, r}{\mu} \cdot \pi r^2 = \frac{16}{7}\,\Delta\sigma\, r^3
$$

反解应力降：

$$
\boxed{\Delta\sigma = \frac{7}{16}\frac{M_0}{r^3}}
$$

### 用可观测量表示

将 $r = k\beta/f_c$ 代入：

$$
\Delta\sigma = \frac{7}{16}\,\frac{M_0}{(k\beta/f_c)^3} = \frac{7}{16k^3}\,\frac{M_0\,f_c^3}{\beta^3}
$$

取 Brune（1970）的 $k = 0.37$，$k^3 = 0.0507$：

$$
\Delta\sigma = \frac{7}{16 \times 0.0507}\,\frac{M_0\,f_c^3}{\beta^3} \approx 8.6\,\frac{M_0\,f_c^3}{\beta^3}
$$

这是应力降的实用计算公式：只需知道地震矩 $M_0$、拐角频率 $f_c$ 和 S 波速度 $\beta$，即可估算应力降。

### 典型量级

地壳地震的应力降通常在：

$$
\Delta\sigma \sim 0.1 \text{--} 50\,\text{MPa}
$$

大多数构造地震集中在 $1\text{--}10\,\text{MPa}$ 量级，且与地震矩的相关性较弱——这体现了**地震的自相似性**（self-similarity）：不同大小的地震具有相似的应力降。

---

## 参数之间的关系网络

三个核心参数 $M_0$、$f_c$、$\Delta\sigma$ 通过以下关系相互约束：

$$
\underbrace{M_0 = \frac{16}{7}\Delta\sigma\,r^3}_{\text{矩-应力降-尺度}} \qquad
\underbrace{r = \frac{k\beta}{f_c}}_{\text{尺度-拐角频率}} \qquad
\underbrace{\Omega_0 = \frac{\mathcal{R}M_0}{4\pi\rho\beta^3 R}}_{\text{矩-平台值}}
$$

给定两个即可求第三个，这是震源参数反演的基础。

---

## Python 示例

### 绘制 Brune 位移谱

```python
import numpy as np
import matplotlib.pyplot as plt

def brune_spectrum(f, omega0, fc):
    """
    Brune (1970) 位移振幅谱

    参数
    ----
    f      : 频率数组 (Hz)
    omega0 : 低频平台 (m·s)
    fc     : 拐角频率 (Hz)

    返回
    ----
    振幅谱数组
    """
    return omega0 / (1 + (f / fc) ** 2)


# 参数设置
f = np.logspace(-1, 2, 2000)   # 0.1 ~ 100 Hz
omega0 = 1.0                    # 低频平台（归一化）
fc = 5.0                        # 拐角频率 5 Hz

spec = brune_spectrum(f, omega0, fc)

# 渐近线
low_freq_asymptote  = np.full_like(f, omega0)
high_freq_asymptote = omega0 * (fc / f) ** 2

# 绘图
fig, ax = plt.subplots(figsize=(7, 5))

ax.loglog(f, spec,                 lw=2.5, color='steelblue', label='Brune 谱')
ax.loglog(f, low_freq_asymptote,   lw=1,   color='gray',       ls='--', label='低频渐近线（斜率 0）')
ax.loglog(f, high_freq_asymptote,  lw=1,   color='tomato',     ls='--', label=r'高频渐近线（斜率 $-2$）')

# 标注拐角频率
ax.axvline(x=fc, color='orange', lw=1, ls=':')
ax.axhline(y=omega0 / 2, color='orange', lw=1, ls=':')
ax.annotate(f'$f_c = {fc}$ Hz', xy=(fc, omega0/10),
            xytext=(fc*2, omega0/6), fontsize=10,
            arrowprops=dict(arrowstyle='->', color='k'))

ax.set_xlabel('频率 $f$ (Hz)', fontsize=12)
ax.set_ylabel(r'位移振幅谱 $|\Omega(f)|$', fontsize=12)
ax.set_title('Brune (1970) 震源谱', fontsize=13)
ax.legend(fontsize=10)
ax.grid(True, which='both', ls=':', alpha=0.5)

plt.tight_layout()
plt.show()
```

![Brune 震源谱](../assets/images/brune_spectrum.png)

### 多个拐角频率对比

```python
import numpy as np
import matplotlib.pyplot as plt

f = np.logspace(-1, 3, 3000)
fc_list = [0.5, 2, 10, 50]    # Hz
colors = ['royalblue', 'green', 'orange', 'crimson']

fig, ax = plt.subplots(figsize=(7, 5))

for fc, color in zip(fc_list, colors):
    spec = 1.0 / (1 + (f / fc) ** 2)
    ax.loglog(f, spec, lw=2, color=color, label=f'$f_c = {fc}$ Hz')
    ax.axvline(x=fc, color=color, lw=0.8, ls=':')

ax.set_xlabel('频率 $f$ (Hz)', fontsize=12)
ax.set_ylabel(r'$|\Omega(f)| / \Omega_0$（归一化）', fontsize=12)
ax.set_title('不同拐角频率的 Brune 谱（同等地震矩）', fontsize=13)
ax.legend(fontsize=10)
ax.grid(True, which='both', ls=':', alpha=0.4)

plt.tight_layout()
plt.show()
```

![不同拐角频率的 Brune 谱](../assets/images/brune_multi_fc.png)

### 从谱参数计算震源参数

```python
import numpy as np

def compute_source_params(omega0, fc, R,
                          rho=2700, beta=3500,
                          F=0.63, S_fs=2.0, k=0.37):
    """
    从 Brune 谱参数计算震源参数

    参数
    ----
    omega0 : 低频平台 (m·s)
    fc     : 拐角频率 (Hz)
    R      : 震中距 (m)
    rho    : 密度 (kg/m^3)，默认 2700
    beta   : S 波速度 (m/s)，默认 3500
    F      : 辐射花样均值，默认 0.63
    S_fs   : 自由表面放大，默认 2.0
    k      : Brune 常数，默认 0.37

    返回
    ----
    dict: M0 (N·m), Mw, r (m), delta_sigma (Pa)
    """
    # 地震矩
    M0 = 4 * np.pi * rho * beta**3 * R * omega0 / (F * S_fs)

    # 矩震级
    Mw = (2/3) * np.log10(M0) - 6.07

    # 震源半径
    r = k * beta / fc

    # 应力降
    delta_sigma = (7/16) * M0 / r**3

    return {"M0": M0, "Mw": Mw, "r": r, "delta_sigma": delta_sigma}


# 示例
result = compute_source_params(
    omega0=1e-8,   # m·s
    fc=5.0,        # Hz
    R=100e3,       # 100 km
)

print(f"地震矩   M0 = {result['M0']:.3e} N·m")
print(f"矩震级   Mw = {result['Mw']:.2f}")
print(f"震源半径  r = {result['r']:.0f} m")
print(f"应力降 Δσ = {result['delta_sigma']/1e6:.2f} MPa")
```

---

## 实际观测中的修正

理想 Brune 谱需要经过一系列修正才能与实际记录的地震谱对应。

### 路径效应

**几何扩散（Geometric Spreading）：** 体波振幅随距离衰减 $\propto 1/R$，已包含在公式中。

**非弹性衰减（Anelastic Attenuation）：** 介质的品质因子 $Q$ 导致振幅随传播距离指数衰减：

$$
|\Omega_{\text{obs}}(f)| = |\Omega_{\text{src}}(f)| \cdot \exp\!\left(-\frac{\pi f R}{\beta Q}\right)
$$

或写成：

$$
|\Omega_{\text{obs}}(f)| = |\Omega_{\text{src}}(f)| \cdot e^{-\pi f t^*}
$$

其中 $t^* = R/(\beta Q)$ 称为**衰减算子**（attenuation operator）。

### 高频截止（$\kappa$ 衰减）

实际地震谱在高于某一频率 $f_{\max}$ 时观测到比 $f^{-2}$ 更陡的截止，用参数 $\kappa$（kappa）描述：

$$
|\Omega_{\text{obs}}(f)| \propto e^{-\pi \kappa f}
$$

$\kappa$ 主要反映近地表低 $Q$ 层的衰减，是台站特性（约 $10 \text{--} 100\,\text{ms}$）。

### 完整的观测谱模型

综合上述修正，实际观测振幅谱为：

$$
|\Omega_{\text{obs}}(f)| = \frac{\mathcal{R}_{\theta\phi}\,M_0}{4\pi\rho\beta^3 R}
\cdot \frac{1}{1+(f/f_c)^2}
\cdot e^{-\pi f t^*}
\cdot e^{-\pi \kappa f}
\cdot I(f)
$$

其中 $I(f)$ 为仪器响应的倒数（去仪器项）。

### 场地效应

地表软土层对地震波有放大作用，通常需要经验性场地响应修正。可通过水平/垂向谱比（HVSR）或参考台站法估计。

---

## 扩展与对比模型

### Boatwright（1980）模型

将高频衰减改为更陡的 $f^{-4}$：

$$
|\Omega(f)| = \frac{\Omega_0}{\left[1 + (f/f_c)^4\right]^{1/2}}
$$

- 高频衰减 $\propto f^{-2}$（同 Brune）
- 频谱在拐角处更"尖锐"
- 更适合某些短周期辐射特征

### Madariaga（1976）动力学破裂模型

基于断层动力学数值模拟，给出了 P 波和 S 波各自的拐角频率：

$$
f_c^P = \frac{0.32\,\alpha}{r}, \qquad f_c^S = \frac{0.21\,\beta}{r}
$$

$\alpha$ 为 P 波速度。P 波和 S 波拐角频率不同，两者之比约为 1.5。

### 双拐角频率（Double Corner Frequency）模型

对于复杂破裂过程，位移谱可引入两个拐角频率 $f_1$、$f_2$（$f_1 < f_2$）：

$$
|\Omega(f)| = \frac{\Omega_0}{\left[1+(f/f_1)^2\right]^{1/2}\left[1+(f/f_2)^2\right]^{1/2}}
$$

常用于描述：

- 多段破裂
- 慢滑事件
- 次级应力降过程

### 模型比较

| 模型 | 高频斜率 | 特点 |
|------|---------|------|
| Brune (1970) | $-2$ | 最简单，应用最广 |
| Boatwright (1980) | $-2$ | 拐角更锐 |
| Madariaga (1976) | $-2$ | P/S 拐角频率分离 |
| $\omega^{-3}$ 模型 | $-3$ | 适合某些深震 |
| 双拐角频率 | $-2$ | 多段破裂 |

---

## 参考文献

Brune, J. N. (1970). Tectonic stress and the spectra of seismic shear waves from earthquakes. *Journal of Geophysical Research*, 75(26), 4997–5009.

Brune, J. N. (1971). Correction. *Journal of Geophysical Research*, 76, 5002.

Aki, K. (1967). Scaling law of seismic spectrum. *Journal of Geophysical Research*, 72(4), 1217–1231.

Eshelby, J. D. (1957). The determination of the elastic field of an ellipsoidal inclusion, and related problems. *Proceedings of the Royal Society of London*, 241(1226), 376–396.

Madariaga, R. (1976). Dynamics of an expanding circular fault. *Bulletin of the Seismological Society of America*, 66(3), 639–666.

Boatwright, J. (1980). A spectral theory for circular seismic sources: simple estimates of source dimension, dynamic stress drop, and radiated seismic energy. *Bulletin of the Seismological Society of America*, 70(1), 1–27.

Aki, K., & Richards, P. G. (2002). *Quantitative Seismology* (2nd ed.). University Science Books.
