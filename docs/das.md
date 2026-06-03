# DAS 分布式声学传感

## 引言

**分布式声学传感**（Distributed Acoustic Sensing，DAS）是一种基于光纤的地震传感技术，可将普通通信光缆改造为连续的密集地震台阵。一根长达数十千米的光缆，可同时提供数万个虚拟传感器，道间距低至 1 m，采样率可达数千 Hz。

与传统检波器相比，DAS 具有三大核心优势：

| 特性 | 传统检波器 | DAS |
|------|-----------|-----|
| 部署成本 | 每个传感器单独安装 | 光缆一次性铺设 |
| 空间密度 | 有限台站（tens–hundreds） | 数千至数万虚拟道 |
| 频段下限 | 受自然频率限制（如 4.5 Hz） | 直流至高频均响应（平坦响应） |
| 环境适应 | 需电源、防水处理 | 全光无源，可用海底光缆 |

DAS 测量的物理量是沿光纤轴向的**动态应变**（dynamic strain）或**应变率**（strain rate），而非粒子速度，这一根本差异决定了其独特的方向性响应特征与标距效应。

---

## 基本原理

### 瑞利散射与相敏 OTDR

DAS 的工作原理基于光纤中的**瑞利散射**（Rayleigh backscattering）和**相位光时域反射法**（phase-sensitive Optical Time Domain Reflectometry，φ-OTDR）：

1. **脉冲注入**：仪器向光纤发射一段相干激光脉冲（脉宽决定空间分辨率）
2. **瑞利后向散射**：光在光纤内沿途与随机折射率不均匀点发生散射，部分散射光沿原路返回
3. **相位检测**：仪器对返回光进行相干解调，测量不同深度处散射光的**相位差**
4. **相位→应变**：相位变化与光纤局部**光程长度变化**成正比，即与轴向应变成正比

$$
\Delta\phi = \frac{4\pi n}{\lambda} \cdot \Delta L
$$

其中 $n$ 为光纤折射率，$\lambda$ 为激光波长，$\Delta L$ 为物理路径长度变化（应变引起）。

!!! note "DAS 测量的是什么"
    DAS 测量的是沿光纤**轴线方向**的**动态应变** $\varepsilon_{xx}$（或应变率 $\dot{\varepsilon}_{xx}$），即光纤轴向的相对拉伸/压缩。对于垂直或水平入射的地震波，其响应强烈依赖于波的传播方向与光纤轴线的夹角。

### 关键系统参数

| 参数 | 典型值 | 说明 |
|------|--------|------|
| 道间距（channel spacing） | 1–10 m | 相邻虚拟传感器之间的距离 |
| 标距（gauge length，GL） | 5–50 m | 单道应变积分长度，决定空间分辨率与信噪比 |
| 采样率 | 1–10 kHz | 时间分辨率 |
| 最大电缆长度 | 10–100 km | 受激光功率与损耗限制 |
| 动态范围 | ~80–100 dB | 与激光相干性相关 |

---

## DAS 的典型应用

### 垂直地震剖面（VSP）

在油气勘探中，DAS 最早的大规模应用是**垂直地震剖面**（VSP）。将光缆布设于油井套管外，可同时记录数百米深度范围内的地震波场。

- **优势**：无需反复起下钻，节省作业时间；覆盖整口井，分辨率高
- **典型标距**：5–10 m
- **信号类型**：直达 P/S 波、反射波、转换波

### 城市浅层地下结构成像

将光缆铺设于城市道路下的通信管道（已有光缆），利用车辆振动等**环境噪声**作为被动震源，反演浅地表 S 波速度结构。

- 代表工作：Lindsey et al. (2017) 利用斯坦福大学园区光缆成像地下结构
- 无需主动震源，成本极低

### 海底地震观测

利用已有**海底通信光缆**进行地震监测，弥补海洋地震台网的稀疏不足。

- 检测微震、海底滑坡、海啸前兆
- 代表工作：Marra et al. (2018, *Science*) 用大西洋海底光缆探测地震

### 微地震与诱发地震监测

在地热能、页岩气水力压裂、CO₂封存等工程中，DAS 用于实时监测**微地震活动**，追踪裂缝发育。

---

## 对入射角的方向性响应

### 几何关系

设光纤沿 $x$ 轴方向铺设，地震平面波在 $x$-$z$ 平面内传播，传播方向与光纤轴线（$x$ 轴）的夹角为 $\theta$（以下称**入射角**）。

波矢量：

$$
\mathbf{k} = k(\cos\theta\,\hat{x} + \sin\theta\,\hat{z}), \quad k = \frac{2\pi f}{c}
$$

沿光纤方向的分量：$k_x = k\cos\theta$

DAS 测量的是轴向应变 $\varepsilon_{xx} = \partial u_x / \partial x$。

### P 波的方向性响应

P 波粒子位移沿传播方向，即：

$$
\mathbf{u} = A\hat{k}\,e^{i(\mathbf{k}\cdot\mathbf{x} - \omega t)}
= A(\cos\theta\,\hat{x} + \sin\theta\,\hat{z})\,e^{i(k_x x + k_z z - \omega t)}
$$

$x$ 分量：$u_x = A\cos\theta \cdot e^{i(k_x x + k_z z - \omega t)}$

轴向应变：

$$
\varepsilon_{xx}^{P} = \frac{\partial u_x}{\partial x} = ik_x \cdot A\cos\theta \cdot e^{i(\cdots)} = ik\cos\theta \cdot A\cos\theta \cdot e^{i(\cdots)}
$$

因此：

$$
\boxed{|\varepsilon_{xx}^{P}| \propto \cos^2\theta}
$$

- $\theta = 0$（波平行于光纤传播）：**响应最强**
- $\theta = 90°$（波垂直于光纤传播）：$\varepsilon_{xx} = 0$，**完全无响应**

### SV 波的方向性响应

SV 波粒子位移垂直于传播方向，在 $x$-$z$ 平面内：

$$
\mathbf{u} = A(-\sin\theta\,\hat{x} + \cos\theta\,\hat{z})\,e^{i(k_x x + k_z z - \omega t)}
$$

$x$ 分量：$u_x = -A\sin\theta \cdot e^{i(\cdots)}$

轴向应变：

$$
\varepsilon_{xx}^{SV} = \frac{\partial u_x}{\partial x} = ik_x(-A\sin\theta) = -ik\cos\theta \cdot A\sin\theta \cdot e^{i(\cdots)}
$$

因此：

$$
\boxed{|\varepsilon_{xx}^{SV}| \propto |\sin\theta\cos\theta| = \frac{1}{2}|\sin 2\theta|}
$$

- $\theta = 0$ 或 $\theta = 90°$：响应为零
- $\theta = 45°$：**响应最强**

!!! note "SH 波盲区"
    SH 波的粒子位移垂直于 $x$-$z$ 平面（沿 $y$ 轴），因此对 $x$ 方向没有位移分量，DAS 对 SH 波**完全不响应**（如果光纤在 $x$-$z$ 平面内）。这是 DAS 的固有盲区。

### 方向性响应的极坐标图

以 $\theta$ 为极角，$|\varepsilon_{xx}|$ 为极径，P 波响应（$\cos^2\theta$）和 SV 波响应（$|\sin 2\theta|/2$）的极坐标图见图 1。

![DAS 方向性响应](../assets/images/das_angle_response.png)
*图 1：DAS 对 P 波（蓝）和 SV 波（橙）的方向性响应极坐标图。阴影区域面积代表相对响应强度。光纤方向为水平轴。*

---

## 平坦频率响应（Flat Response）

### 应变与粒子速度的关系

DAS 测量轴向应变，而地震学中常用的量是**粒子速度**。两者的转换关系对于理解 DAS 的频率特性至关重要。

对于沿 $x$ 方向传播的平面 P 波，粒子位移 $u_x = A e^{i(kx - \omega t)}$，则：

$$
v_x = \frac{\partial u_x}{\partial t} = -i\omega A e^{i(\cdots)}
$$

$$
\varepsilon_{xx} = \frac{\partial u_x}{\partial x} = ik A e^{i(\cdots)} = \frac{ik}{-i\omega} \cdot v_x = -\frac{k}{\omega} v_x = -\frac{v_x}{c_P}
$$

对于一般入射角 $\theta$（与光纤轴的夹角），综合 P 波方向性：

$$
\varepsilon_{xx} = -\frac{\cos^2\theta}{c_P} \cdot v_P
$$

其中 $v_P$ 是沿传播方向的粒子速度幅度，$v_x = v_P\cos\theta$。

整理得：

$$
\boxed{v_P = -\frac{c_P}{\cos^2\theta} \cdot \varepsilon_{xx}}
$$

**关键特性：转换系数 $c_P / \cos^2\theta$ 与频率无关。**

### 为何称为"平坦响应"

这一频率无关性使 DAS 具有区别于传统检波器的**平坦频率响应**（flat response）：

| 仪器类型 | 测量量 | 频率响应 | 低频特性 |
|----------|--------|----------|----------|
| 短周期检波器 | 粒子速度 | 平坦（$f > f_0$），低频衰减 | 在自然频率 $f_0$ 以下滚降 |
| 加速度计 | 粒子加速度 | 平坦（$f < f_\mathrm{res}$） | 低频端需积分才得速度 |
| **DAS（应变）** | **轴向应变** | **从直流到 $f_\mathrm{notch}$ 均平坦** | **无低频截止** |

!!! tip "平坦响应的实际意义"
    DAS 记录的应变信号，可以在**全频段**（0 Hz 至标距陷波频率 $f_\mathrm{notch}$）用一个与频率无关的常数转换为粒子速度，无需任何频率补偿。这使 DAS 天然适合记录低频地震波（面波、慢地震、潮汐等），而不受传统短周期检波器自然频率的限制。

!!! warning "注意：应变率 ≠ 应变"
    许多 DAS 系统直接输出**应变率** $\dot{\varepsilon}$（对时间的导数），而非应变。应变率与粒子速度的关系为 $\dot{\varepsilon} = -(\cos^2\theta / c_P) \cdot \dot{v}_P$，即正比于**加速度**，此时不具有平坦速度响应，需先对时间积分（等效于频域除以 $\omega$）还原成应变。

---

## 标距效应（Gauge Length Effect）

### 空间积分滤波

DAS 并不测量真正意义上的"点"应变，而是测量长度为 $L$（标距，gauge length）的光纤段两端之间的相位差，等价于在该段上对应变做**空间积分平均**：

$$
\varepsilon_\mathrm{GL}(x_0, t) = \frac{u_x(x_0 + L/2,\, t) - u_x(x_0 - L/2,\, t)}{L}
$$

### 传递函数推导

对于平面波 $u_x = A e^{i(k_x x - \omega t)}$，代入上式：

$$
\varepsilon_\mathrm{GL} = \frac{A e^{ik_x(x_0 + L/2)} - A e^{ik_x(x_0 - L/2)}}{L} \cdot e^{-i\omega t}
= \frac{2i\sin(k_x L/2)}{L} \cdot A e^{ik_x x_0} e^{-i\omega t}
$$

点应变为 $\varepsilon_\mathrm{point} = ik_x A e^{ik_x x_0} e^{-i\omega t}$，因此标距传递函数为：

$$
H(k_x) = \frac{\varepsilon_\mathrm{GL}}{\varepsilon_\mathrm{point}} = \frac{\sin(k_x L/2)}{k_x L/2} = \mathrm{sinc}\!\left(\frac{k_x L}{2\pi}\right)
$$

其中 $\mathrm{sinc}(x) = \sin(\pi x) / (\pi x)$。

用频率表示（代入 $k_x = 2\pi f \cos\theta / c$）：

$$
\boxed{H(f, \theta) = \mathrm{sinc}\!\left(\frac{f L \cos\theta}{c}\right)}
$$

### 陷波频率

sinc 函数在 $k_x L/2 = n\pi$（$n = 1, 2, 3, \ldots$）处为零，对应的**陷波频率**：

$$
f_n = \frac{n \cdot c}{L\cos\theta} = \frac{n \cdot c_\mathrm{app}}{L}
$$

其中 $c_\mathrm{app} = c/\cos\theta$ 是沿光纤方向的**视速度**（apparent velocity）。

!!! note "物理解释"
    当地震波的沿纤视波长 $\lambda_\mathrm{app} = c_\mathrm{app}/f$ 等于标距 $L$ 时（即 $f = c_\mathrm{app}/L$），标距两端的位移**大小相等、方向相反**，相减后精确为零，出现第一陷波。

### 标距与陷波频率的权衡

| 标距 $L$ | 陷波频率 $f_1$（$c$ = 3000 m/s，$\theta$ = 0°） | 信噪比 |
|----------|---------------------------------------------|--------|
| 5 m | 600 Hz | 低（积分路径短） |
| 10 m | 300 Hz | 中 |
| 20 m | 150 Hz | 较高 |
| 50 m | 60 Hz | 高，但高频损失严重 |

!!! warning "标距选取的关键性"
    标距 $L$ 过大：陷波频率降低，损失高频信息；$L$ 过小：每道平均的应变段短，信噪比下降。实际中根据目标信号频段和地面/井下条件选取，通常 $L = 5$–$20$ m。

角度效应：入射角 $\theta$ 越大（波越接近垂直于光纤），$k_x$ 越小，陷波频率越高，高频信息保留越好，但振幅响应（$\cos^2\theta$ 因子）也越弱。

![标距效应](../assets/images/das_gauge_length.png)
*图 2：不同标距下 DAS 的传递函数（$|H(f)|$）随频率的变化（$\theta = 0°$，$c$ = 3000 m/s）。标距越大，陷波频率越低。*

### 最优标距：信噪比与分辨率的权衡

以上分析表明标距存在两种相互对立的效应：**标距过小 → 信噪比差；标距过大 → 分辨率下降、波形畸变**。Dean, Cuny & Hartog（2016）针对轴向入射 P 波（$\theta = 0°$，VSP 典型场景）给出了定量分析。

#### 信噪比分析

对于沿光纤轴向传播的 P 波，应变波形为**Ricker 子波**（时域）：

$$
\varepsilon(t) = \left(1 - 2\pi^2 f_p^2 t^2\right) e^{-\pi^2 f_p^2 t^2}
$$

其空间域形式（波数 $k = \pi f_p / v$）：

$$
\varepsilon(x) = \left(1 - 2\pi^2 k^2 x^2\right) e^{-\pi^2 k^2 x^2}
$$

DAS 测量的光纤长度变化 $\Delta L$（即信号强度）为应变在标距上的积分：

$$
\Delta L = \int_{-L/2}^{L/2} \varepsilon(x)\,\mathrm{d}x = L\, e^{-\pi^2 k^2 (L/2)^2}
$$

!!! note "公式推导"
    利用 $\frac{\mathrm{d}}{\mathrm{d}x}\!\left[x\,e^{-\pi^2 k^2 x^2}\right] = \varepsilon(x)$，可解析积分得到上式。

$\Delta L$ 关于 $L$ 的极值：令 $\mathrm{d}(\Delta L)/\mathrm{d}L = 0$，解得：

$$
\boxed{L_\mathrm{SNR} = \frac{\lambda_s}{\sqrt{3}} \approx 0.577\,\lambda_s}
$$

其中**空间波长** $\lambda_s = v\lambda_t = v\sqrt{6}/(\pi f_p)$。

DAS 的相位测量误差 $E(\Delta L)$ 与标距无关（由激光相干性决定），因此 **SNR ∝ $\Delta L$**，在 $L = \lambda_s/\sqrt{3}$ 时取得最大值。

#### 分辨率分析（波形畸变）

标距的积分等效于一个**箱型（移动平均）低通滤波器**，其频率响应即为 sinc 函数。随着 $L$ 增大，陷波频率向低频移动，逐步侵入子波的主频带：

| GL/$\lambda_s$ 比值 | 波形状态 | SNR |
|--------------------|----------|-----|
| $< 0.40$ | 正常，高分辨率 | 低（信号弱） |
| $0.40$–$0.54$ | **最优区间**：高 SNR + 良好分辨率 | > 90 % 最大值 |
| $\approx 0.577$ | SNR 峰值；子波轻微展宽 | 最大 |
| $\approx 1.0$ | 陷波进入主频带，子波顶部变平（flat-topped） | 较高但分辨率差 |
| $> 1.0$ | 子波出现**双峰畸变**（double-lobed），严重失真 | 应避免 |

#### 最优标距公式

综合 SNR > 90% 最大值与分辨率误差 < 15% 两个约束，最优比值范围为 $GL/\lambda_s \approx 0.40$–$0.54$，推荐取 0.5，由此得到**最优标距**（Dean et al. 2016，公式 18）：

$$
\boxed{L_\mathrm{opt} = \frac{\mathrm{ratio} \times v}{f_p} \approx \frac{0.5\,v}{f_p} = \frac{\lambda_s}{2}}
$$

!!! tip "实际计算示例"
    VSP 中某深度段视速度 $v = 3000$ m/s，子波主频 $f_p = 50$ Hz：
    $$L_\mathrm{opt} \approx \frac{0.5 \times 3000}{50} = 30\text{ m}, \quad \lambda_s \approx \frac{3000\sqrt{6}}{\pi \times 50} \approx 46.8\text{ m}$$
    若视速度在全井范围内从 2900 m/s 变化到 5900 m/s（变化近 2 倍），**建议对不同深度段分别选取最优标距**，以保证 SNR 和分辨率在全深度范围内均处于最优状态。

!!! warning "标距下限的物理约束"
    当 $L$ 减小到接近激光脉冲宽度时（通常 $L < 8$ m），相位与应变的关系变为非线性，DAS 系统的基本假设失效。因此，尽管理论上更小的 $L$ 给出更好的分辨率，实际中 $L_\mathrm{min} \approx 8$ m 是硬性下限。

![最优标距分析](../assets/images/das_gauge_opt.png)
*图 3：左图——归一化 $\Delta L$（SNR 代理）随 $GL/\lambda_s$ 的变化，绿色区域为 SNR > 90% 最大值的区间，红色阴影区为波形畸变区；右图——不同 $GL/\lambda_s$ 比值下 DAS 输出的归一化子波形状（$f_p$ = 40 Hz，$v$ = 1000 m/s，$\lambda_s \approx 19.5$ m）。（基于 Dean et al. 2016）*

---

## Python 示例

下面的代码生成上文中的两幅图：方向性响应极坐标图与标距效应传递函数图。

```python
import numpy as np
import matplotlib.pyplot as plt

# ── 图 1：方向性响应极坐标图 ───────────────────────────────
theta = np.linspace(0, 2 * np.pi, 720)

# P 波：cos²θ（双极瓣）
resp_P  = np.cos(theta) ** 2

# SV 波：|sin(2θ)|/2（四极瓣）
resp_SV = np.abs(np.sin(2 * theta)) / 2

fig, axes = plt.subplots(1, 2, figsize=(11, 5),
                          subplot_kw=dict(projection='polar'))

for ax, resp, color, label, desc in [
    (axes[0], resp_P,  '#3498db', r'P-wave  $|\cos^2\theta|$',
     'P-wave sensitivity\n' + r'$|\varepsilon_{xx}| \propto \cos^2\theta$'),
    (axes[1], resp_SV, '#e67e22', r'SV-wave  $|\sin 2\theta|/2$',
     'SV-wave sensitivity\n' + r'$|\varepsilon_{xx}| \propto |\sin 2\theta|/2$'),
]:
    ax.plot(theta, resp, color=color, lw=2)
    ax.fill(theta, resp, alpha=0.25, color=color)
    ax.set_theta_zero_location('E')
    ax.set_theta_direction(1)
    ax.set_xticks(np.deg2rad([0, 45, 90, 135, 180, 225, 270, 315]))
    ax.set_xticklabels(['0° (fiber)', '45°', '90°', '135°',
                         '180°', '225°', '270°', '315°'], fontsize=8)
    ax.set_yticks([0.5, 1.0])
    ax.set_yticklabels(['0.5', '1.0'], fontsize=8)
    ax.set_title(desc, pad=14, fontsize=10)

plt.suptitle('DAS Directional Sensitivity (Fiber along 0°–180°)', y=1.02, fontsize=12)
plt.tight_layout()
plt.savefig('docs/assets/images/das_angle_response.png',
            dpi=150, bbox_inches='tight')
print('Saved das_angle_response.png')

# ── 图 2：标距效应传递函数 ─────────────────────────────────
c   = 3000.0   # apparent velocity (m/s), θ = 0 → c_app = c
GLs = [5, 10, 20, 50]
colors = ['#2ecc71', '#3498db', '#e67e22', '#e74c3c']

f = np.linspace(0.1, 600, 2000)

fig, ax = plt.subplots(figsize=(9, 5))
for L, color in zip(GLs, colors):
    kxL_half = np.pi * f * L / c     # k_x * L/2  (θ=0 → k_x = 2πf/c)
    H = np.abs(np.sinc(kxL_half / np.pi))  # sinc(k_x L / 2π) = sin(k_x L/2)/(k_x L/2)
    ax.plot(f, 20 * np.log10(np.clip(H, 1e-6, None)),
            color=color, lw=2, label=f'GL = {L} m  (notch: {c/L:.0f} Hz)')

ax.axhline(-3, color='k', lw=0.8, ls=':', alpha=0.6, label='−3 dB')
ax.set(xlabel='Frequency (Hz)',
       ylabel='DAS / Point-sensor response (dB)',
       title='Gauge Length Effect: Transfer Function $|H(f)|$\n'
             r'($\theta = 0°$, $c_{\rm app}$ = 3000 m/s)',
       xlim=[0, 600], ylim=[-60, 3])
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('docs/assets/images/das_gauge_length.png',
            dpi=150, bbox_inches='tight')
print('Saved das_gauge_length.png')

# ── 图 3：最优标距——SNR 曲线与子波畸变（Dean et al. 2016）────
fp, v = 40.0, 1000.0
k_r      = np.pi * fp / v
lambda_s = np.sqrt(6) / k_r        # 空间波长 ≈ 19.5 m
T_half   = 3 * lambda_s / v
dt       = lambda_s / v / 200
t        = np.arange(-T_half, T_half + dt, dt)
eps      = (1 - 2*(np.pi*fp*t)**2) * np.exp(-(np.pi*fp*t)**2)

GL_ratios = np.linspace(0.01, 2.6, 1000)
DL        = GL_ratios * lambda_s * np.exp(-(k_r * GL_ratios*lambda_s/2)**2)  # 无额外 π
DL_norm   = DL / DL.max()

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

ax = axes[0]
ax.plot(GL_ratios, DL_norm, 'b-', lw=2)
ax.axvline(1/np.sqrt(3), color='r', lw=1.5, ls='--',
           label=r'$1/\sqrt{3}\approx0.577$ (peak SNR)')
ax.axvline(0.5, color='g', lw=1.5, ls=':',
           label='0.5 (recommended)')
ax.axhline(0.90, color='gray', lw=1, ls=':', alpha=0.6)
ax.fill_between(GL_ratios, DL_norm, where=(DL_norm >= 0.90),
                alpha=0.15, color='green', label='SNR > 90 % of max')
ax.axvspan(1.0, 2.6, alpha=0.08, color='red')
ax.text(1.55, 0.45, 'Wavelet\ndistortion', color='red', fontsize=8, ha='center')
ax.set(xlabel=r'$GL\,/\,\lambda_s$', ylabel=r'Norm. $\Delta L$ (SNR proxy)',
       title='SNR vs GL/Wavelength Ratio  (Dean et al. 2016)',
       xlim=[0, 2.6], ylim=[0, 1.05])
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

ax = axes[1]
palette2 = ['#9b59b6','#2ecc71','#3498db','#e67e22','#e74c3c']
for r, color in zip([0.25, 0.50, 0.77, 1.03, 1.50], palette2):
    n_box = max(1, int(round(r * lambda_s / v / dt)))
    box   = np.ones(n_box) / n_box
    out   = np.convolve(eps, box, mode='same')
    out  /= (np.abs(out).max() + 1e-30)
    ax.plot(t*1e3, out, color=color, lw=1.8, label=f'GL/λ = {r:.2f}')
ax.axhline(0, color='k', lw=0.6, ls='--', alpha=0.4)
ax.set(xlabel='Time (ms)', ylabel='Normalised DAS output',
       title=fr'Wavelet After Gauge-Length Filter  ($f_p$={fp} Hz, $\lambda_s$≈{lambda_s:.1f} m)',
       xlim=[-60, 60])
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('docs/assets/images/das_gauge_opt.png', dpi=150, bbox_inches='tight')
print('Saved das_gauge_opt.png')

plt.show()
```

---

## 参考文献

- Lindsey, N. J., Martin, E. R., Dreger, D. S., Freifeld, B., White, S., Monga, S. K., … & Ajo-Franklin, J. B. (2017). Fiber-optic network observations of earthquake wavefields. *Geophysical Research Letters*, 44(23), 11–792.
- Mateeva, A., Lopez, J., Potters, H., Mestayer, J., Cox, B., Kiyashchenko, D., … & Berlang, W. (2014). Distributed acoustic sensing for reservoir monitoring with vertical seismic profiling. *Geophysical Prospecting*, 62(4), 679–692.
- Marra, G., Clivati, C., Luckett, R., Tampellini, A., Kronjäger, J., Wright, L., … & Margolis, H. S. (2018). Ultrastable laser interferometry for earthquake detection with terrestrial and submarine cables. *Science*, 361(6401), 486–490.
- Wang, H. F., Zeng, X., Miller, D. E., Fratta, D., Feigl, K. L., Thurber, C. H., & Mellors, R. J. (2018). Ground motion response to an ML 4.3 earthquake using co-located distributed acoustic sensing and seismometers. *Geophysical Journal International*, 213(3), 2020–2036.
- Daley, T. M., Miller, D. E., Dodds, K., Cook, P., & Freifeld, B. M. (2016). Field testing of modular borehole monitoring with simultaneous distributed acoustic sensing and geophone vertical seismic profiles at Citronelle, Alabama. *Geophysical Prospecting*, 64(5), 1318–1334.
- Zhan, Z. (2020). Distributed acoustic sensing turns fiber-optic cables into seismic stations. *Bulletin of the Seismological Society of America*, 110(3), 975–985.
- Dean, T., Cuny, T., & Hartog, A. H. (2017). The effect of gauge length on axially incident P-waves measured using fibre optic distributed vibration sensing. *Geophysical Prospecting*, 65(1), 184–193. https://doi.org/10.1111/1365-2478.12419
