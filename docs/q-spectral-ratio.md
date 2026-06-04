# 谱比法 Q 值反演

## 引言

地震波在传播过程中因介质的非弹性（粘弹性）特性而发生幅度衰减，这种衰减由**品质因子** $Q$（quality factor）定量描述。$Q$ 值越小，介质越"耗能"，波幅衰减越快；$Q \to \infty$ 对应纯弹性介质，无能量损失。

**谱比法**（spectral ratio method）是估计 $Q$ 值最经典的方法之一。其核心思想是：对同一震源在两个台站记录到的位移谱取**比值**，使震源谱在相除时完全抵消，从而把纯粹的衰减信息提取出来。

对于沿同一射线路径到达两台站的 S 波，对数谱比满足：

$$
\boxed{
\ln\!\left[\frac{A(f,r_2)}{A(f,r_1)}\right] = \underbrace{\ln\!\left(\frac{r_1}{r_2}\right)}_{\text{截距}} - \underbrace{\pi\,\Delta t^*}_{\text{斜率}} \cdot f
}
$$

这是关于频率 $f$ 的**线性方程**，从拟合斜率 $m = -\pi\Delta t^*$ 直接得到有效 Q 值：

$$Q_{\mathrm{eff}} = -\dfrac{\pi\,\Delta t}{m}$$

---

## 地震波衰减与 Q 的定义

### 品质因子的物理定义

品质因子 $Q$ 是描述介质弹性能量耗散速率的无量纲参数，最基本的定义基于**能量损耗比**：

$$
\frac{1}{Q} \equiv \frac{1}{2\pi} \cdot \frac{-\Delta E}{E}
$$

其中 $\Delta E < 0$ 是一个振动周期内介质耗散的弹性能，$E$ 是弹性势能峰值。

- $Q \gg 1$：每周期损耗极少，接近弹性；上地壳花岗岩典型值 $Q \sim 200$–$1000$
- $Q \sim 10$–$50$：强衰减，如富水沉积层、断层破碎带

### 单程衰减振幅谱

对于以速度 $\beta$ 传播的单色平面 S 波，振幅随路径距离 $r$ 按指数衰减：

$$
A(r, f) = A_0 \exp\!\left(-\frac{\pi f\, r}{\beta\, Q}\right) = A_0 \exp(-\alpha r)
$$

衰减系数 $\alpha = \pi f / (\beta Q)$ 与频率成正比，因此高频成分比低频成分衰减更快。

### t* 参数

在非均匀介质中，沿射线路径积分的累计衰减用 $t^*$（"t-star"）表示：

$$
t^* = \int_{\mathrm{path}} \frac{\mathrm{d}s}{\beta(s)\, Q(s)}
$$

对均匀介质（$\beta$、$Q$ 为常数），传播时间 $t = r/\beta$，因此：

$$
t^* = \frac{t}{Q} = \frac{r}{\beta\, Q}
$$

$t^*$ 的量纲为时间（秒），综合反映了路径长度与介质 Q 值，是衰减研究中最常用的单一参数。

### 常见 Q 模型

| 模型 | 表达式 | 特征 |
|------|--------|------|
| 常数 Q | $Q = \mathrm{const}$ | 最简，对数谱比与 $f$ 线性 |
| 幂律 Q | $Q(f) = Q_0\, f^{\eta}$ | $\eta \in [0,1]$，浅层沉积常见 |
| Futterman 模型 | 满足 Kramers–Kronig 因果关系 | 弱频率依赖 |

谱比法默认使用**常数 Q** 模型，此时对数谱比是 $f$ 的严格线性函数。

---

## 谱比法推导

### 完整位移振幅谱模型

远场位移振幅谱可以分解为若干独立因子的乘积（Aki & Richards 2002）：

$$
A(f, r) = S(f) \cdot I(f) \cdot G(r) \cdot \exp\!\left(-\pi f\, t^*\right)
$$

各因子含义：

- $S(f)$：**震源谱**（source spectrum），如 Brune $\omega^{-2}$ 谱；包含辐射花样 $\mathcal{R}_{\theta\phi}$
- $I(f)$：**仪器响应**（instrument response），将地动转为电压输出
- $G(r)$：**几何扩散因子**，体波远场 $G(r) = 1/r$
- $\exp(-\pi f\, t^*)$：**非弹性衰减**因子

### 双台站谱比推导

设同一震源的 S 波到达**近台**（台站 1，距离 $r_1$）和**远台**（台站 2，距离 $r_2 > r_1$），且两台站处于同一射线路径上。

**近台**振幅谱：

$$
A(f, r_1) = S(f) \cdot I(f) \cdot \frac{1}{r_1} \cdot \exp(-\pi f\, t_1^*)
$$

**远台**振幅谱：

$$
A(f, r_2) = S(f) \cdot I(f) \cdot \frac{1}{r_2} \cdot \exp(-\pi f\, t_2^*)
$$

两式相除，$S(f)$ 和 $I(f)$ **完全抵消**（假设已做去仪器响应处理，或两台仪器响应相同）：

$$
\frac{A(f, r_2)}{A(f, r_1)} = \frac{r_1}{r_2} \cdot \exp\!\left[-\pi f (t_2^* - t_1^*)\right]
$$

定义**差分 t-star**：

$$
\Delta t^* = t_2^* - t_1^* = \frac{t_2 - t_1}{Q_{\mathrm{eff}}} = \frac{\Delta t}{Q_{\mathrm{eff}}}
$$

其中 $\Delta t = (r_2 - r_1)/\beta$ 是 S 波在两台之间的传播时间差。

### 线性化

对谱比两边取自然对数：

$$
\ln\!\left[\frac{A(f, r_2)}{A(f, r_1)}\right] = \ln\!\left(\frac{r_1}{r_2}\right) - \pi\,\Delta t^*\cdot f
$$

令 $L(f) = \ln[A_2(f)/A_1(f)]$，这是关于 $f$ 的线性函数：

$$
L(f) = b + m \cdot f
$$

| 参数 | 表达式 | 物理含义 |
|------|--------|----------|
| 截距 $b$ | $\ln(r_1/r_2)$ | 几何扩散比（已知量，可做约束） |
| 斜率 $m$ | $-\pi\,\Delta t^*$ | 含全部衰减信息，$m < 0$ |

### 提取 Q 值

由斜率 $m = -\pi\,\Delta t^* = -\pi\,\Delta t / Q_{\mathrm{eff}}$，解出：

$$
\boxed{Q_{\mathrm{eff}} = -\frac{\pi\,\Delta t}{m}}
$$

$\Delta t$ 可由 S 波到时差直接读取，也可由距离差和平均速度计算：

$$
\Delta t = t_2^{\mathrm{arr}} - t_1^{\mathrm{arr}} \quad \text{或} \quad \Delta t = \frac{r_2 - r_1}{\bar{\beta}}
$$

!!! note "消去震源谱的条件"
    谱比法成立的关键前提是**两台站接收到的是同一地震的同一相位**（如均为直达 S 波），从而震源谱 $S(f)$ 在相除时精确抵消。若使用不同地震，须先对震源谱做归一化校正。

!!! tip "实用提示：Δt 的选取"
    优先从波形中直接拾取 S 波到时差，而非由距离/速度推算，因为实际介质速度结构的非均匀性会使理论 $\Delta t$ 产生偏差。

---

## 实际操作步骤

### 数据预处理流程

| 步骤 | 操作 | 目的 |
|------|------|------|
| 1 | 去均值、去线性趋势 | 消除直流分量和长周期漂移 |
| 2 | 截取 S 波时窗 | 隔离目标相位，避免其他相位干扰 |
| 3 | 加锥形窗（Hanning / Tukey） | 减小谱泄漏 |
| 4 | 去仪器响应 → 位移谱 | 将记录转换为真实地动位移 |
| 5 | 计算 FFT 振幅谱 | 得到 $A_1(f)$、$A_2(f)$ |
| 6 | 平滑振幅谱（可选） | 减少谱方差，稳定拟合 |
| 7 | 计算对数谱比 $L(f)$ | 进入拟合阶段 |

### 有效频段的选取

谱比法的有效频段受以下因素限制：

- **低频截断**：信噪比不足，背景微震噪声（0.1–0.3 Hz）主导
- **高频截断**：Brune 谱在 $f > f_c$ 已按 $f^{-2}$ 衰减（不满足平坦假设）；κ 效应在极高频段掩盖 Q 信息

!!! warning "频段选取不当的后果"
    若拟合频段包含了 $f > f_c$ 的部分，Brune 谱的 $f^{-2}$ 斜率会叠加到谱比的斜率上，导致 **Q 值系统性偏低**。建议先估算震源拐角频率 $f_c$，将上限设为 $0.8\, f_c$。

### κ 衰减（近地表高频衰减）

Anderson & Hough（1984）发现高频段存在额外的指数衰减，称为 **κ（kappa）效应**：

$$
A(f) \propto \exp(-\pi \kappa f), \quad f \gtrsim f_E
$$

$\kappa$ 主要反映近地表低 Q 沉积层的累积衰减，与台站场地条件密切相关。若两台站的 $\kappa$ 值不同（$\Delta\kappa = \kappa_2 - \kappa_1 \neq 0$），拟合斜率会包含额外贡献：

$$
m_{\mathrm{obs}} = -\pi\,\Delta t^* - \pi\,\Delta\kappa = -\frac{\pi\,\Delta t}{Q} - \pi\,\Delta\kappa
$$

忽略 $\Delta\kappa$ 会使 Q 值估计**偏低**。缓解方法：选择场地条件相似的台站对，或将 $\Delta\kappa$ 与 Q 一起反演。

---

## Python 示例

下面的代码模拟真实 Q = 150 的双台站场景，加入高斯随机噪声后用线性回归估计 Q 值。

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# ── 参数设置 ──────────────────────────────────────────────
Q_true      = 150          # 真实 Q 值
r1, r2      = 10e3, 60e3   # 近台、远台至震源距离 (m)
beta        = 3500.0        # 平均 S 波速度 (m/s)
dt_travel   = (r2 - r1) / beta   # S 波时间差 Δt (s)

f = np.linspace(1, 20, 300)  # 频率轴 1–20 Hz

# ── 理论对数谱比 ──────────────────────────────────────────
# L(f) = ln(r1/r2) - π·f·Δt/Q
log_ratio_theory = np.log(r1 / r2) - np.pi * f * dt_travel / Q_true

# ── 加高斯噪声（模拟观测散度）────────────────────────────
rng = np.random.default_rng(seed=42)
log_ratio_obs = log_ratio_theory + rng.normal(0, 0.25, size=len(f))

# ── 线性回归：L(f) = b + m·f ──────────────────────────────
slope, intercept, r_val, _, _ = linregress(f, log_ratio_obs)
Q_est          = -np.pi * dt_travel / slope
log_ratio_fit  = slope * f + intercept

print(f"真实 Q     = {Q_true}")
print(f"估计 Q     = {Q_est:.1f}")
print(f"拟合斜率 m = {slope:.5f}  (理论: {-np.pi*dt_travel/Q_true:.5f})")
print(f"R²         = {r_val**2:.4f}")

# ── 绘图 ─────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 左图：不同 Q 值下的衰减量（dB）随频率变化
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

# 右图：对数谱比、理论值与线性拟合
ax = axes[1]
ax.scatter(f, log_ratio_obs, s=5, alpha=0.45, color='#3498db',
           label='Observed (noisy)', zorder=2)
ax.plot(f, log_ratio_theory, 'k--', lw=1.5,
        label=f'Theory  (Q = {Q_true})')
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

运行输出：

```
真实 Q     = 150
估计 Q     = 149.8
拟合斜率 m = -0.29958  (理论: -0.29920)
R²         = 0.9806
```

![谱比法示例图](../assets/images/q_spectral_ratio.png)
*图 1：左图为不同 Q 值下衰减量（dB）随频率的变化，Q 越小衰减越剧烈；右图为含噪声的对数谱比数据（蓝色散点）、理论曲线（黑虚线）与线性拟合结果（红线）。*

---

## 频率依赖 Q 的推广

当 Q 随频率变化时，常用**幂律模型**：

$$
Q(f) = Q_0\, f^{\eta}, \quad \eta \in [0, 1]
$$

此时衰减因子变为：

$$
\exp\!\left(-\pi f\, t^*\right) = \exp\!\left(-\frac{\pi f\, t}{Q(f)}\right) = \exp\!\left(-\frac{\pi\, t}{Q_0} f^{1-\eta}\right)
$$

对数谱比为：

$$
L(f) = \ln\!\left(\frac{r_1}{r_2}\right) - \frac{\pi\,\Delta t}{Q_0}\, f^{1-\eta}
$$

令 $u = f^{1-\eta}$，则 $L$ 关于 $u$ 仍是线性的。实际操作中，对不同的 $\eta$ 值尝试线性化，选择 $R^2$ 最大的 $\eta$ 即为最佳频率指数。

!!! note "η 的典型值"
    上地壳结晶岩：$\eta \approx 0$（常数 Q 近似成立）；浅层松散沉积：$\eta \approx 0.5$–$0.8$；全球地幔：$\eta \approx 0.1$–$0.3$。

---

## 方法变体

| 变体 | 设置 | 优点 | 缺点 |
|------|------|------|------|
| **双台站法**（本文） | 同一震源，两台沿同一射线 | 消去震源谱；$\Delta t$ 精确 | 需台站几何严格对齐 |
| **单台双事件法** | 同一台站，两个不同距离的震源 | 台站固定，场地效应相同 | 需假设两事件震源谱形状相同 |
| **VSP 谱比法** | 地表与井下检波器 | 路径简单，避免场地效应 | 需要钻孔 |
| **尾波谱比法** | 利用 S 波尾波 | 样本量大，统计稳健 | 分离固有衰减与散射衰减较复杂 |
| **DAS 逐道谱比法** | 垂直井 DAS，同一事件相邻道 | 极高空间分辨率；自然消去震源谱 | 需校正 DAS 仪器响应（角度、标距）；入射角限制 |

---

## 频移类 Q 值估计方法

谱比法依赖振幅谱的绝对值，而**频移类方法**利用振幅谱"中心"随传播时间向低频偏移这一现象来估计 Q，对振幅的依赖性更低，在某些噪声场景下更稳健。

### 高频选择性衰减的物理基础

衰减系数 $\alpha = \pi f / (\beta Q)$ 正比于频率：高频成分比低频成分衰减更快。随着传播时间增加，地震子波的振幅谱整体向低频偏移——**重心频率下降、谱带变窄**。频移类方法定量利用这一偏移量来反演 Q 值。

### 重心频率漂移法（CFS）

**重心频率**（centroid frequency）和**谱方差**定义为振幅谱的加权矩：

$$f_c = \frac{\int_0^\infty f\,S(f)\,df}{\int_0^\infty S(f)\,df}, \qquad \sigma_c^2 = \frac{\int_0^\infty (f - f_c)^2 S(f)\,df}{\int_0^\infty S(f)\,df}$$

Quan & Harris（1997）证明，当振幅谱近似服从高斯分布时，重心频率偏移量正比于累积衰减：

$$\frac{f_S - f_R}{\sigma_S^2} \propto \int_\text{path} q\,dl$$

由此得到 Q 值估计公式：

$$\boxed{Q = \frac{\pi\,\Delta t\,\sigma_c^2(t_0)}{f_c(t_0) - f_c(t)}}$$

- $\Delta t = t - t_0$：传播时间差
- $f_c(t_0)$、$\sigma_c^2(t_0)$：参考时刻的重心频率和方差
- $f_c(t)$：当前时刻的重心频率

!!! note "高斯谱假设"
    CFS 方法严格依赖振幅谱近似为高斯分布的前提。Ricker 子波的谱与高斯谱拟合良好——50 Hz Ricker 子波的重心频率约为 $f_c \approx 56.4$ Hz，谱方差 $\sigma_c^2 \approx 567$ Hz²（Lu et al. 2026），因此 CFS 在地震勘探中广泛适用。

### 峰值频率漂移法（PFS）

Zhang & Ulrych（2002）利用子波**主频**（peak frequency）的漂移估计 Q，形式更为简洁：

$$Q = \frac{\pi\,\Delta t\,f_p^2(t_0)}{f_p^2(t_0) - f_p^2(t)}$$

其中 $f_p$ 为子波的峰值（主导）频率。PFS 假设 Ricker 子波模型，计算更简便，但在子波形状偏离 Ricker 时精度下降。

### 局部重心频率漂移法（LCFS）

Wang et al.（2020）将 CFS 推广到**时频域**，直接从时频谱 $T(f,t)$ 计算**局部**重心频率和方差，无需手动划定时窗：

$$f_c(t) = \frac{\int_0^\infty f\,T(f,t)\,df}{\int_0^\infty T(f,t)\,df}, \qquad \sigma_c^2(t) = \frac{\int_0^\infty (f - f_c(t))^2 T(f,t)\,df}{\int_0^\infty T(f,t)\,df}$$

Q 值估计公式形式不变，但 $f_c$ 和 $\sigma_c^2$ 均在时频域逐点计算，得到**时变 Q 值**：

$$Q(t) = \frac{\pi\,\Delta t\,\sigma_c^2(t_0)}{f_c(t_0) - f_c(t)}$$

LCFS 优势：① 无需划分时窗 ② 直接输出时变 Q 剖面 ③ 可利用 LTFT 等多种时频变换。

### 多维非稳态 LCFS（Lu et al. 2026）

LCFS 的固定平滑半径在低 SNR 条件下不适应信号的非稳态特性。Lu et al.（2026）引入**自适应平滑半径策略**：

$$R(t,x,y) = \begin{cases} R_s & p_k(t,x,y)/p_\max \geq \tau \quad \text{（信号区，小半径）}\\ R_d & p_k(t,x,y)/p_\max < \tau \quad \text{（噪声区，大半径）}\end{cases}, \quad R_d > R_s$$

其中 $p_k(t,x,y)$ 是当前点的时频谱幅值，$\tau$ 为区分信号/噪声的阈值。

- **信号区**：幅值高，使用**小半径**，保留细节，避免模糊
- **噪声区**：幅值低，使用**大半径**，充分平滑，抑制干扰

同时将平滑扩展到**频率维度和空间维度**（多道数据），利用地震道之间的空间相干性进一步压制噪声。

**性能**：在 SNR < 0 dB 的强噪声条件下，仍能准确估计 Q（收敛于 $t \approx 0.3$ s），而传统 LTFT-LCFS 在此条件下显著偏离理论值。

### Ricker 小波分解法（Hao et al. 2024）

Hao et al.（2024）提出"先分解子波，再估 Q"的两步策略：

**第一步：快速稀疏分解（FISSD）**

将地震道 $\mathbf{s}$ 分解为一系列加权 Ricker 小波的叠加：

$$\mathbf{s} = \mathbf{W} \cdot \mathbf{r}$$

字典矩阵 $\mathbf{W}$ 由不同主频（$f_1, \ldots, f_m$）的 0° 和 −90° 相位 Ricker 子波构成（因为任意相位旋转的 Ricker 子波均可表示为 0° 与 −90° 子波的线性组合）。加入**群稀疏（group-sparse）约束**（$\ell_{2,1}$ 范数）的目标函数：

$$\min_{\mathbf{r}}\; \frac{1}{2}\|\mathbf{W}\mathbf{r} - \mathbf{s}\|_2^2 + \mu\|\mathbf{r}\|_{2,1}$$

利用 Split Bregman 迭代在**频域**求解，计算量随道长**线性**增长，比时域 ISSD 快 $10^3$ 倍以上。

**第二步：位置指示向量（PIV）与局部叠加**

定义 PIV 为各时刻权重系数的行求和 $\boldsymbol{\eta} = \mathrm{sum}(\mathbf{R}^2, \mathrm{row})$。找到 $\boldsymbol{\eta}$ 的局部极大值位置，将该位置附近的 Ricker 子波叠加还原为单个反射子波，有效分离**调谐效应**（tuning effect）导致的重叠子波。

**第三步：基于 Futterman 理论的 Q 估计**

对传播时间 $\tau$ 后到达的子波，其重心频率满足（Futterman 1962）：

$$f_c^\tau = \frac{\int_{-\infty}^{+\infty} f\,S(f)\,e^{-\pi f\tau/Q}\,df}{\int_{-\infty}^{+\infty} S(f)\,e^{-\pi f\tau/Q}\,df}$$

求解 $\Xi(Q) = f_c^\tau - f_c^e = 0$（$f_c^e$ 为估计子波的重心频率）即可获得 Q 值。由于 $\Xi(Q)$ 是 Q 的单调函数（可通过 Schwartz 不等式证明），Newton 迭代法快速收敛。

可以分别估计：
- **等效 Q 值**：震源到当前深度的路径平均 Q
- **层间 Q 值**：顶、底界面反射子波之间的 Q，直接反映特定地层的衰减

!!! tip "储层评价应用"
    孔隙-裂缝发育区因局部流体流动（squirt flow）产生强衰减，层间 Q 值偏低。Hao et al.（2024）将层间 $1/Q$ 用于识别高孔隙碳酸盐岩储层区域，成功区分出传统 RMS 振幅属性无法分辨的高、低孔隙度区。

### 各方法综合对比

| 方法 | 类别 | 核心特征 | 优势 | 局限 |
|------|------|----------|------|------|
| **谱比法（SR）** | 振幅比 | 两道对数谱比线性斜率 | 无需谱形假设 | 需频段选取；振幅信噪比要求高 |
| **重心频率漂移（CFS）** | 频移 | 全频段重心频率偏移量 | 不依赖振幅绝对值 | 严格要求高斯谱；全局时窗 |
| **峰值频率漂移（PFS）** | 频移 | 主频偏移量 | 计算简单 | Ricker 假设；时窗依赖 |
| **局部 CFS（LCFS）** | 频移·时变 | 时频域逐点重心频率 | 时变 Q；无需手动时窗 | 固定平滑半径对强噪声适应差 |
| **多维非稳态 LCFS** | 频移·时变·自适应 | SNR 驱动的变半径平滑 | SNR < 0 dB 仍有效 | 依赖初始时频谱质量 |
| **Ricker 分解法（FISSD）** | 分解·频移 | 先分离子波，再用 Futterman 反演 | 可分离调谐；层间 Q 准确 | 计算量较大；Ricker 子波假设 |

---

## 使用井下 DAS 进行逐道谱比 Q 反演

### 原理

将垂直井中 DAS 的**相邻台道**视为"双台站对"：同一地震事件的 P 波沿井轴（光纤方向）向上传播，相邻道之间的振幅谱比直接反映该深度段的衰减，从而得到**深度分辨率与道间距相当**的高分辨率 Q 剖面。

这本质上是 VSP 谱比法的极端密集化版本——传统 VSP 台站间距为数十米，而 DAS 道间距可低至 1 m。

### DAS 谱比的修正

与传统检波器不同，DAS 对振幅谱有额外的频率和角度依赖性。两台道（深度 $z_1$、$z_2$，$z_2 > z_1$）的位移谱比为：

$$
\frac{A_\text{DAS}(f, z_2)}{A_\text{DAS}(f, z_1)}
= \underbrace{\frac{v(z_2)\cos^2\theta(z_2)}{v(z_1)\cos^2\theta(z_1)}}_{\text{平坦响应比}}
\cdot \underbrace{\frac{\mathrm{sinc}(\pi fL/v(z_2)\cos\theta(z_2))}{\mathrm{sinc}(\pi fL/v(z_1)\cos\theta(z_1))}}_{\text{标距滤波比}}
\cdot e^{-\pi f \Delta t^*}
$$

对数线性化后，斜率项与传统谱比法相同：

$$
\ln\!\left[\frac{A_\text{DAS}(f,z_2)}{A_\text{DAS}(f,z_1)}\right]_{\text{校正后}} = \mathrm{const} - \pi\,\Delta t^* \cdot f
$$

**校正步骤**：

| 步骤 | 操作 | 涉及的 DAS 特性 |
|------|------|----------------|
| 1 | 去仪器响应 → 位移谱（除以 $(2\pi f)^m$） | 积分阶次 $m$ |
| 2 | 平坦响应校正：除以 $v\cos^2\theta$ | 角度响应 |
| 3 | 标距校正：除以 sinc$(πfL/v\cos\theta)$ | 标距效应 |
| 4 | κ 校正：除以 $e^{-\pi f\kappa}$（若已知场地 κ） | 近地表衰减 |
| 5 | 计算逐对台道对数谱比，线性回归得 $\Delta t^*$ | — |

### 入射角的要求

使用垂直井 DAS 进行 Q 反演时，**入射角 $\theta$**（射线与光纤轴/井轴的夹角）对结果的影响至关重要。

**为什么入射角不能太大？**

1. **平坦响应校正放大噪声**：校正因子为 $1/\cos^2\theta$，在 $\theta \to 90°$ 时趋于无穷大，将噪声无限放大。

2. **有效频带收窄**：标距陷波频率为 $f_1 = v\cos\theta/L$，入射角增大时陷波向低频移动，可用频段随之收窄，削减了谱比法的可靠拟合范围。

3. **灵敏度下降**：信号幅度本身已按 $\cos^2\theta$ 衰减，信噪比降低。

**实践阈值**（Chang et al. 2026）：

$$
\boxed{\theta < 45°}
$$

!!! note "几何解释"
    对于垂直井中深度为 $z_\text{ch}$ 的台道，以及水平距离 $r_H$、深度 $z_\text{src}$（$z_\text{src} > z_\text{ch}$）处的微地震：
    $$\theta = \arctan\!\left(\frac{r_H}{z_\text{src} - z_\text{ch}}\right)$$
    $\theta < 45°$ 等价于 $r_H < z_\text{src} - z_\text{ch}$，即**事件的水平偏移小于事件到该台道的深度差**。

    因此，Q 反演最适合使用**位于井底正下方**的事件：这类事件对所有台道的入射角均较小，平坦响应校正稳定，有效频带宽。

!!! warning "大角度事件的处理"
    若研究区内事件的水平距离较大（$r_H \gg \Delta z$），则 $\theta > 45°$ 的台道应在谱拟合中**剔除**，只使用浅层台道（$z_\text{src} - z_\text{ch}$ 大的台道）中满足角度要求的那些。

### 高分辨率 Q 剖面

利用 DAS 的极高道密度，可在全井范围内按每个相邻台道对独立估计 $\Delta t^*$，然后通过反演得到**深度分辨率 ~ 道间距**的 $Q(z)$ 剖面。

Chang et al.（2026）在犹他州 Cape Modern 增强型地热系统（EGS）的 2.5 km 深垂直井中获得了迄今最高分辨率的地震观测 Q 剖面，主要发现：

- **浅层沉积层**：速度低、密度低、Q 低（强衰减）
- **花岗岩基底**：速度急剧增大，Q 随深度较缓慢增大
- **累积 κ 值**（从 2500 m 深到地表）与其他地区的独立研究一致

### 与震源参数反演的联系

在获得 Q 剖面之后，可将 Q（即 t\*）代入**单谱法**，对逐道逐事件的位移谱拟合 Brune 模型，估计震源参数：

$$
\Omega(f) = \Omega_0 \cdot e^{-\pi f t^*} \cdot e^{-\pi f \kappa}
\cdot \underbrace{v\cos^2\theta \cdot \mathrm{sinc}(\pi fL/v\cos\theta)}_{\text{DAS 仪器响应}}
\cdot \frac{1}{1 + (f/f_c)^2}
$$

拟合得到 $\Omega_0$（对应地震矩）和 $f_c$（拐角频率），进而计算应力降 $\Delta\sigma = \frac{7}{16} M_0 / a^3$。

---

## 参考文献

- Aki, K., & Richards, P. G. (2002). *Quantitative Seismology* (2nd ed.). University Science Books.
- Anderson, J. G., & Hough, S. E. (1984). A model for the shape of the Fourier amplitude spectrum of acceleration at high frequencies. *Bulletin of the Seismological Society of America*, 74(5), 1969–1993.
- Tonn, R. (1991). The determination of the seismic quality factor Q from VSP data: A comparison of different computational methods. *Geophysical Prospecting*, 39(1), 1–27.
- Toverud, T., & Ursin, B. (2005). Comparison of seismic attenuation models using zero-offset vertical seismic profiling (VSP) data. *Geophysics*, 70(2), F17–F25.
- Xie, J. (2002). Seismic attenuation: Measurement and uncertainty. *Pure and Applied Geophysics*, 159(7–8), 1823–1849.
- Bakku, S. K. (2015). *Fracture characterization from seismic measurements in a borehole* (Doctoral dissertation, Massachusetts Institute of Technology).
- Chang, H., Nakata, N., Abercrombie, R. E., Dadi, S., & Titov, A. (2026, in review). Using borehole Distributed Acoustic Sensing to investigate microearthquake source parameter variability in an enhanced geothermal system. *ESSOAr preprint*. https://doi.org/10.22541/essoar.15002292/v1
- Quan, Y., & Harris, J. M. (1997). Seismic attenuation tomography using the frequency shift method. *Geophysics*, 62(3), 895–905.
- Zhang, C., & Ulrych, T. J. (2002). Estimation of quality factors from CMP records. *Geophysics*, 67(5), 1542–1547.
- Wang, Q. H., Yang, L., Cai, L., & Zheng, Z. S. (2020). Continuous time-varying Q-factor estimation method in the time–frequency domain. *Applied Geophysics*, 17, 844–856.
- Hu, C., Tu, N., & Lu, W. (2013). Seismic attenuation estimation using an improved frequency shift method. *IEEE Geoscience and Remote Sensing Letters*, 10(5), 1026–1030.
- Lu, H., Zhu, Z., Pei, X., Zhu, W., & Xia, L. (2026). A local time-varying Q-factor estimation method based on multidimensional nonstationary smoothing. *Journal of Geophysics and Engineering*, 23(4), 1095–1108. https://doi.org/10.1093/jge/gxag022
- Hao, Y., Yin, D., Zhang, P., & Zhang, H. (2024). Seismic decomposition method using Ricker wavelet dictionary and its applications for Q-value estimation. *Acta Geophysica*, 72, 2425–2445. https://doi.org/10.1007/s11600-023-01217-y
- Futterman, W. I. (1962). Dispersive body waves. *Journal of Geophysical Research*, 67(13), 5279–5291.
