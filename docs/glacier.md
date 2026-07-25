# 冰川地震学：仪器、阵列与 DAS 应用

## 引言

**冰川地震学**（glacioseismology）利用地震波探测和监测冰川、冰盖与冰架，是研究冰冻圈动力学的核心工具。冰体内部存在多种弹性波源——从毫秒量级的微冰震到持续数十分钟的冰川地震——覆盖了从 0.001 Hz 到数百 Hz 的宽频带。

$$
\boxed{\text{冰川地震学} = \text{震源（冰体破裂/运动）} + \text{传播（冰弹性）} + \text{观测（地震仪/DAS）}}
$$

现代冰川地震学面临的核心挑战：

- **极地环境**：低温（−60°C 至 0°C）、强风噪声、冰面运动使仪器部署困难
- **宽频带需求**：冰裂隙高频（>10 Hz）与冰川地震低频（< 0.1 Hz）并存
- **稀疏覆盖**：传统地震网络台站间距数十公里，难以实现精细空间分辨率
- **DAS 革命**：分布式声学传感将"点"观测升级为"线"观测，道间距低至 1–5 m

---

## 冰川地震信号类型

| 信号类型 | 频带（Hz） | 震级范围 | 持续时间 | 典型源机制 |
|---------|-----------|---------|---------|-----------|
| 表面冰震（surface icequake） | 10–200 | Mw −3 至 0 | 0.1–2 s | 冰裂隙张开（tensile crack） |
| 底部冰震（basal icequake） | 1–30 | Mw −2 至 +1 | 0.2–5 s | 冰床粘-滑运动 |
| 冰内深震 | 1–20 | Mw −1 至 +1 | 0.5–10 s | 热应力、相变 |
| 崩解/倾覆（calving） | 0.1–5 | Mw 1 至 4 | 10–300 s | 冰舌断裂、冰山翻转 |
| 冰川地震（glacial earthquake） | 0.01–0.1 | Mw 4.5–6.5 | 30–120 s | 大冰川/冰架快速运动，质心单力 |
| 冰下水文震颤（hydraulic tremor） | 1–20 | 持续 | 分钟–小时 | 冰下通道水流 |
| 冰下湖排水事件 | 0.01–1 | Mw 2–4 | 小时 | 冰下湖突发排水 |

![冰川地震信号类型](assets/images/glacier_signals.png)
*图 1：四类典型冰川地震信号的合成波形。从上到下：表面冰裂隙高频冲击型；底部粘-滑低频 emergent 型；崩解/冰体垮塌长周期型；冰下水文连续型震颤。频带与持续时间差异悬殊，需宽频带仪器与多时窗处理策略。*

---

## 冰的地震物理特性

掌握冰体的弹性参数是理解冰川地震信号传播和衰减的前提。冰与常见地壳岩石的显著差异在于：（1）均匀性极高，散射弱，波形尾波短；（2）粒雪（firn）层速度低且梯度大；（3）晶体织构引起明显弹性各向异性（Podolskiy & Walter, 2016）。

### 弹性波速与 Q 值

| 介质 | $V_P$（m/s） | $V_S$（m/s） | $V_R$（m/s） | $Q_P$ | $Q_S$ |
|------|-------------|-------------|-------------|--------|--------|
| 冷冰（cold ice） | 3600–3900 | 1700–1950 | 1650–1668 | ~600 | ~300 |
| 温冰（temperate ice） | 3500–3700 | 1700–1850 | — | < 100 | < 100 |
| 粒雪（firn，近表层） | ~500 | — | — | — | — |
| 冰床软沉积物 | 1500–2500 | 300–600 | — | 低 | 低 |

*$V_R$ 为 45 Hz 实测值（Roux et al., 2010; Mikesell et al., 2012）；$Q$ 值来自 Walter et al.（2009）。*

**衰减对检测距离的影响**：$Q_S \approx 300$ 对应有效检测半径约为：

$$
r_\text{eff} \approx \frac{Q_S V_S}{\pi f} = \frac{300 \times 1800}{\pi \times 10\,\text{Hz}} \approx 17\;\text{km}
$$

频率升至 50 Hz 时，$r_\text{eff}$ 缩短至约 3 km；超过 100 Hz 的冰震通常只能被 1 km 以内的台站可靠记录。

### 冰晶织构（Fabric）与弹性各向异性

多晶冰在流动和重力共同作用下，$c$ 轴逐渐趋向垂直，产生**横向各向同性**（VTI）弹性结构：

- 水平与垂直方向 $V_P$ 差异约 3–5%，$V_S$ 亦存在双折射
- S 波在各向异性介质中分裂为**快 S 波**和**慢 S 波**，时间差 $\delta t$ 反映各向异性强度与冰柱厚度的乘积
- 冰的等效黏度因织构不同可相差 **50–100 倍**（Dahl-Jensen et al., 2013）——织构是冰盖数值模型不可或缺的参数

!!! note "温冰与冷冰的差异"
    温冰（Temperate ice，$T \approx 0°\text{C}$）内含少量液态水，$V_P$ 略低于冷冰，且 $Q$ 值急剧下降（高衰减）。Alpine 山地冰川多属温冰，其 $Q_S < 100$，使 > 30 Hz 信号的传播距离显著受限。

### 冰的低散射性

冰川冰极度均匀，冰震波形**几乎无尾波（coda）**，与多相地壳岩石形成鲜明对比：

- 表面冰裂隙带（典型厚度 ~20 m）是主要散射层（Cuffey & Paterson, 2010）
- 表面冰震波形以 Rayleigh 波为主（逆椭圆质点运动），P 和 S 波相对微弱
- 深部（底部或中深部）冰震波形则 P 和 S 波突出，尾波短而简单（图 Figure 3，Walter et al., 2009）

低散射性制约了传统噪声互相关技术——等方位噪声分布难以通过散射自然实现，需借助均匀分布的冰震事件作为**虚拟源**（见"被动结构成像"一节）。

---

## 观测仪器

### 宽频地震仪（Broadband Seismometer）

宽频地震仪是捕捉冰川地震和崩解长周期信号的核心仪器。

| 型号 | 频带 | 灵敏度 | 冰川部署适用性 |
|------|------|--------|--------------|
| Nanometrics Trillium Compact | 0.008–100 Hz | 1500 V·s/m | ★★★★☆，轻便，低温性能佳 |
| Güralp CMG-40T | 0.03–50 Hz | 800 V·s/m | ★★★☆☆，笨重，适合基岩 |
| Streckeisen STS-2 | 0.008–50 Hz | 1500 V·s/m | ★★☆☆☆，大型，固定台站 |
| REF TEK 151B | 0.02–50 Hz | 1500 V·s/m | ★★★★☆，极地版本 |

**冰面部署问题**：
- 冰面倾斜 → 仪器倾斜噪声（tilt noise）在 0.01–1 Hz 段可超过信号 10 dB
- 解决：自平衡平台（gimbal mount）+ 后处理倾斜校正（tilt-to-acceleration 转换）
- 冰面流动速率 1–100 m/yr → 若不记录 GPS 位置，长期数据的震源定位误差可达数十米

### 短周期检波器（Geophone）

检波器轻便、廉价，是冰川主动源勘探和密集被动阵列的主力。

| 型号 | 自然频率 | 灵敏度 | 典型用途 |
|------|---------|--------|---------|
| Sercel L-22 | 2 Hz | 88 V/m/s | 冰川折射/反射勘探 |
| Geospace GS-11D | 4.5 Hz | 28 V/m/s | 冰上密集阵 |
| Mark Products L-28 | 4.5 Hz | 28 V/m/s | 通用地震探测 |

!!! note "检波器局限"
    4.5 Hz 检波器在低于自然频率时灵敏度急剧下降，完全无法记录冰川地震（< 0.1 Hz）和崩解事件（< 2 Hz）。对于需要捕捉多类型信号的综合监测，必须配合宽频地震仪使用。

### 数据采集注意事项

**低温下的电池问题**：锂铁磷酸（LiFePO₄）电池在 −40°C 仍可释放 70–80% 容量，而普通锂电池（LiCoO₂）在 −20°C 容量降至 50%。

**GPS 时钟精度**：积雪覆盖 GPS 天线导致时钟偏差 > 1 ms，影响到时差定位精度（P 波到时误差 ×3700 m/s ≈ > 3.7 m 的震源定位误差）。

**仪器耦合**：冻融循环会破坏检波器与冰面的耦合（反复冻结和融化）。解决方案：钻冰孔插入短桩并重新冻结固定。

---

## 地震阵列方法

### 阵列构型与设计原则

| 构型 | 优点 | 适用场景 |
|------|------|---------|
| 线性阵列 | 沿线方向高分辨率，便于 F-K 分析 | 冰川流向监测、DAS 自然构型 |
| 环形阵列 | 全方位均匀方位角覆盖 | 全向震源定位 |
| L 形阵列 | 二维成像，建设成本低 | 临时野外台阵 |
| 稀疏全区网络 | 大范围覆盖 | 冰盖级监测（Greenland、Antarctica） |

**阵列关键参数**：
- 最小道间距 $d_\min$ → 决定最高可分辨波数：$k_\max = 1/(2d_\min)$
- 阵列孔径 $D$ → 决定慢度分辨率：$\Delta p \approx 1/(D \cdot f_\max)$

### 波束形成定位（Beamforming）

对于 $N$ 台站阵列，相移求和（delay-and-sum）波束功率：

$$
P(f, \mathbf{p}) = \left|\frac{1}{N}\sum_{i=1}^{N} u_i(f)\, e^{i 2\pi f\, \mathbf{p}\cdot\mathbf{r}_i}\right|^2
$$

其中 $\mathbf{p}$ 是慢度矢量，$\mathbf{r}_i$ 是台站坐标。极大值点给出信号的视速度（apparent velocity）和方位角（back-azimuth）。对于冰川信号：

- P 波视速度：冰内 $v_P \approx 3500\text{–}3900$ m/s（取决于温度和织构各向异性）
- Rayleigh 波视速度：$v_R \approx 0.92\,v_S \approx 1700$ m/s（冰表面）
- 慢（< 500 m/s）的能量通常来自冰裂隙表面波或冰下水流

### 到时差定位（TDOA / Hyperbolic）

对于波传播速度 $v$ 已知的情况，震源 $\mathbf{x}_s$ 到台 $i$ 和台 $j$ 的到时差：

$$
\Delta t_{ij} = \frac{|\mathbf{x}_s - \mathbf{r}_j| - |\mathbf{x}_s - \mathbf{r}_i|}{v}
$$

每对台站给出一支双曲线（3D 中为双曲面）。三台以上联立方程解得 $\mathbf{x}_s$。

!!! tip "冰川中的速度不均匀性"
    冰内 P 波速度随温度和结冰织构变化显著（±5–10%），表浅层（firn 粒雪层）速度更低（$v_P \approx 800$ m/s 在粒雪，3700 m/s 在冰）。进行精确定位时，应事先通过主动源勘探或 DAS 被动成像获取速度模型。

### 矩张量反演（冰震震源机制）

冰裂隙以**张力裂隙（tensile crack）**为主，其矩张量（moment tensor）有特征形式：

$$
M_{ij} = \frac{\Delta\sigma \cdot A \cdot u}{3} \begin{pmatrix} \lambda + 2\mu & 0 & 0 \\ 0 & \lambda & 0 \\ 0 & 0 & \lambda \end{pmatrix}
$$

（对于沿 $x_1$ 方向张开的裂隙）其中 $\lambda$、$\mu$ 为冰的 Lamé 常数。矩张量分解：

- **DC 分量**（double-couple）：剪切分量，底部粘-滑事件占主导
- **CLVD 分量**（compensated linear vector dipole）：体积不守恒的剪切
- **ISO 分量**（isotropic）：体积变化，张力裂隙的标志性分量（正 ISO）

$$
\boxed{M_{ii} > 0 \implies \text{拉张型冰裂隙（crevasse opening）}}
$$

---

## DAS 在冰川中的应用

### 铺设方式

DAS（分布式声学传感）通过沿光纤连续测量瑞利后向散射相位变化，将整根光缆变为数千道地震仪（见 [DAS 基本原理](das.md)）。在冰川环境中有两种主要铺设方式：

**（A）冰面铺设**

- 光缆沿冰面铺设，通常浅埋（0.1–0.5 m）以降低风噪和热膨胀噪声
- 对冰震 P/S 波和面波（Rayleigh 波）均有响应
- 冰面流动使光缆位置随时间漂移 → 需配合 GPS 定期测量光缆位置
- 典型应用：冰面冰裂隙监测、2D 被动噪声互相关成像

**（B）冰孔铺设**

- 热钻（hot-water drilling）形成竖直孔后插入光缆，冰冻固定
- 类似 VSP 观测几何（详见 [VSP 原理](vsp.md)），可分离下行 P 和上行反射波
- 对冰床信号（底部摩擦、底部融水）极为敏感
- 典型应用：冰厚测量、底部滑动监测、冰内声速剖面

![DAS 冰川铺设与记录示例](assets/images/glacier_das.png)
*图 2：（左）冰川 DAS 铺设示意图——橙色为冰面光缆（A），红色虚线为冰孔光缆（B），黄色方框为 DAS 询问器，标注了冰裂隙、冰下水体等地质特征。（中）表面光缆 DAS 记录：冰震激发的 P 波（高视速度）与面波（低速对角线），F-K 滤波可分离两类信号。（右）冰孔 DAS VSP 式记录：清晰的下行直达 P 和冰床反射波，两者斜率相反，可直接反演冰厚。*

### 冰川结构成像

**被动噪声互相关 → 速度剖面**

利用连续 DAS 记录中的环境噪声（风、海浪、微地震），对任意两道做互相关：

$$
C_{ij}(\tau) = \int u_i(t)\, u_j(t+\tau)\, \mathrm{d}t
$$

互相关函数的包络给出 Rayleigh 波格林函数，频散曲线反演 $V_S(z)$（见 [面波方法](surface-coda.md)）。

**冰层典型速度结构**：

| 层位 | $V_P$ (m/s) | $V_S$ (m/s) | 特点 |
|------|-------------|-------------|------|
| 粒雪（firn，0–100 m） | 400–2000 | 200–1000 | 速度随密度快速增加 |
| 冷冰（cold ice，100 m – 底部） | 3700–3900 | 1830–1940 | 织构各向异性，$c$ 轴倾角影响速度 |
| 温冰（temperate ice）| 3500–3700 | 1800–1850 | 含液态水，速度略低 |
| 冰床沉积物 | 1800–2500 | 300–900 | 饱水软层，强反射 |

!!! note "冰的弹性各向异性"
    多晶冰具有单斜对称的弹性张量，$c$ 轴（冰晶光轴）的优选方位（fabric）导致 P 波速度在垂直 $c$ 轴和平行 $c$ 轴方向差异可达 **3–5%**。这对 DAS 的 Q 值反演（需准确校正传播速度）和 CWI（速度变化须与各向异性效应区分）有重要影响。

**主动源冰厚测量**

DAS + 冰面小型震源（弹药包或锤击）构成高密度反射地震剖面：
- 冰床反射双程走时 $t = 2H/V_P$，直接给出冰厚 $H$
- DAS 道间距 1–5 m，分辨率远超传统检波器排列（25–50 m）

### 冰震监测与精细定位

DAS 的高道密度使冰震震源位置精度从传统阵列的**数十米**提升到**亚米量级**。

**全波形互相关定位流程**：
1. 用模板波形在连续记录上进行**模板匹配**（template matching）扫描
2. 触发候选事件后，提取各道到时（互相关峰值位置）
3. 将到时差代入双曲方程组，网格搜索或梯度下降解 $(x, y, z)$
4. 利用 DAS 的 3D 形状（已知），约束震源深度

!!! tip "DAS 定位优势"
    表面 DAS 阵列的 $N_\text{ch} \sim 1000$ 道提供了极度冗余的到时约束。即使 50% 的道受到冰面噪声干扰，仍有数百道可用，震源定位残差 < 1 m（理想条件下）。

### 冰川运动与底部滑动

**粘-滑（Stick-Slip）事件检测**

冰川基底以间歇性粘-滑方式向前滑动，每次事件对应冰体快速位移（Δd ≈ mm 至 cm）。DAS 对沿光缆方向的动态应变敏感：

$$
\varepsilon_{xx}(x, t) = \frac{\partial u_x}{\partial x}
$$

底部粘-滑产生水平应变脉冲，在 DAS 记录上表现为**全道同相的低频脉冲**。

**Whillans 冰流（WIS）典型粘-滑参数**（Winberry et al., 2009a, 2011; Pratt et al., 2014）：

- 单次事件：冰体位移 **0.2–0.5 m**，历时 **20–30 min**，冰流速度峰值约 1 m/h
- 破裂传播速度：平均 **150 m/s**，最高达 1.5 km/s（约为冰内 $V_S$ 的 90%）
- 受 **Ross 冰架潮汐**调控（接近日周期），分两类事件：
  - **高潮型**：间隔 14–19 h，从中央粘滞点（CSS）核化，临界剪应力 ~0.49 kPa
  - **低潮型**：间隔 < 9 h，从接地线粘滞点（GLSS）核化，临界剪应力 ~0.42 kPa
- 间隔时间越长→积累弹性应变越多→释放位移越大（弹性 slider-block 模型）
- WIS 已观测到以 **0.6%/yr²** 的速率减速，可能在百年内停滞（Joughin et al., 2005）

这种"**潮汐节律粘-滑**"（tidally paced stick-slip）是冰床弹性应变积累最典型的实证，与构造地震断层的慢速蠕变-脆性破裂类比高度吻合。

**冰川加速与减速**

通过比较相邻时段的互相关格林函数，尾波干涉法（CWI）可检测冰内声速的微小变化：

$$
\frac{\delta v}{v} = -\frac{\delta t}{\bar{t}}
$$

冰内 $v$ 与温度、液态水含量、孔隙率密切相关：
- 夏季升温 → $\delta v/v < 0$（速度降低，~0.1–0.5%/°C）
- 底部融水增加 → 速度降低，可能先于底部加速发生
- DAS + CWI 有潜力实现对**冰川不稳定性的早期预警**

### 典型研究案例

| 地点 | 研究团队 | 铺设方式 | 主要成果 | 文献 |
|------|---------|---------|---------|------|
| Rhône Glacier，瑞士 | ETH Zürich | 冰面 2 km | 冰裂隙精细定位（< 1 m），冰内 Vs 剖面 | Fichtner et al. 2023 |
| Store Glacier，格陵兰 | GEUS/Bristol | 冰孔 600 m | 底部融化层成像，冰床反射系数 | Walter et al. 2020 |
| Malaspina Glacier，阿拉斯加 | USGS | 冰面 5 km | 面波频散，冰面形变速率 | Gimbert et al. 2021 |
| Whillans Ice Stream，南极 | 多机构 | 冰面 | DAS 记录粘-滑事件的空间传播 | Lipovsky et al. 2019 |
| Argentière Glacier，法国 | IPGP | 冰孔 | CWI 监测季节性速度变化 | Nanni et al. 2021 |

---

## 被动结构成像

被动地震技术以冰震或环境噪声为源，无需主动震源即可成像冰体结构。Podolskiy & Walter（2016）将这类方法列为冰川地震学三大前沿之一，认为其利用程度仍严重不足。

### 地震干涉法（Seismic Interferometry）

互相关两台地震仪的记录，可从中恢复两点间的格林函数（虚拟震源法）：

$$
C_{ij}(\tau) = \int u_i(t)\,u_j(t+\tau)\,\mathrm{d}t \;\xrightarrow{\text{等方位源}}\; \hat{G}(\mathbf{r}_i,\,\mathbf{r}_j,\,\tau)
$$

**冰川中的特殊挑战**：冰体散射弱，无法靠多次散射实现等方位噪声。解决方案是以**表面冰震**（10–50 Hz）充当分布式虚拟源——只要冰震在台对两侧均有分布，互相关的面波分量仍可恢复格林函数（Walter et al., 2015a）。

| 研究地点 | 方法 | 成果 |
|---------|------|------|
| Gornergletscher，瑞士 | 冰震虚拟源 + 频散分析 | 局部冰厚、$V_S(z)$ 剖面（Walter et al., 2015a）|
| Ross 冰架，南极 | 环境噪声频散 | 冰架厚度与结构（Diez et al., 2016）|
| 格陵兰冰盖 | 宽频噪声互相关 | 冰质量平衡近实时估算（Mordret et al., 2016）|

### S 波分裂与冰晶织构

底部粘-滑冰震产生的 S 波穿越整个冰柱后，在具有各向异性的冰晶织构介质中发生**S 波双折射（shear wave splitting）**：

$$
\delta t_\text{split} = H \cdot \frac{\delta V_S}{V_S \cdot \bar{V}_S}
$$

其中 $H$ 为冰厚，$\delta V_S$ 为快慢 S 波速度差。该时差直接测量冰柱积分各向异性强度。

南极 **Rutford 冰流**研究（Harland et al., 2013）利用底部冰震 S 波分裂，识别了底部高剪切变形带的晶体优选方位和英格拉西裂隙走向，为冰流变形历史提供了独立约束——这是接收函数或地面测量难以企及的深度信息。

### 接收函数（Receiver Functions）

利用远震宽角 P 波竖直入射时的 P-to-S 转换，接收函数突出速度界面位置：

$$
\text{RF}(\tau) = \mathcal{F}^{-1}\!\left[\frac{R(\omega)}{Z(\omega)}\right]
$$

在冰川环境中有两类直接应用：

1. **冰厚测量（无需主动源）**：冰-床界面的 P-to-S 转换时延 $\Delta t \approx H(1/V_{S,\text{ice}} - 1/V_{P,\text{ice}})$，已知冰的 $V_P/V_S \approx 2.0$ 即可求解冰厚 $H$。

2. **冰床软沉积层厚度**：若冰床之下存在饱水软沉积物（"软床"），则沉积物-岩床界面产生额外的 P-to-S 转换，时延差给出沉积层厚度（Anandakrishnan & Winberry, 2004）。Antarctic 和 Greenland 冰盖下已发现 **数十至数百米厚**的饱水沉积物——软床控制着冰流的基底阻力和长期速率，是冰盖模型中最大的不确定性之一。

### 冰下水文震颤的定量监测

冰下管道水流（1.5–10 Hz 段）的连续震颤振幅 $A_\text{tremor}$ 与冰下排水量 $Q_w$ 成经验幂律关系：

$$
A_\text{tremor}(t) \propto Q_w(t)^{\,\beta}, \quad \beta \approx 0.4\text{–}0.6
$$

（Bartholomaus et al., 2015b；Gimbert et al., 2016）

这使被动地震成为估算冰下水流量的**独立工具**，无需直接入侵测量（钻孔压力计等）。对于出海冰川，冰下水排放驱动峡湾水循环并促进冰前水下融化，是崩解速率最重要的控制因素之一。

!!! tip "日周期信号"
    高消融期冰下震颤振幅呈明显**日周期**变化（夏季峰值出现在午后气温最高之后 4–6 h），可作为冰下水系连通性和响应延迟时间的诊断指标（Métaxian, 2003; Röösli et al., 2014）。

### 冰架中的 Rayleigh-Lamb 波

浮动冰架是**薄板几何**（板厚 $H \ll$ 波长），其中传播的是 **Rayleigh-Lamb 模态**（而非半空间 Rayleigh 波）。海洋长周期涌浪（50–250 s）冲击冰前沿，激发沿冰架传播的弯曲波（flexural wave）：

$$
\omega^2 = \frac{E H^2}{12\rho(1-\nu^2)}\, k^4 \quad (\text{低频渐近，A}_0\text{ 模})
$$

弯曲波的频散曲线与冰厚 $H$ 和弹性模量 $E$ 有解析关系，利用台阵频散分析即可反演冰架结构（Bromirski et al., 2010, 2015）。冰架流动状态（搁浅 vs 漂浮）和冰架裂隙发育均影响弯曲波传播，为冰架稳定性监测提供了被动遥感手段。

---

## 与传统地震仪的联合使用

单纯依靠 DAS 有其局限：DAS 只测量**沿缆方向的轴向应变**，三分量运动信息（尤其竖直和横向）需要配合点式地震仪补充。典型联合部署策略：

```
DAS（线状高密度）  ─── 空间覆盖 / 到时约束 / 分布式应变
宽频地震仪（稀疏）─── 低频成分 / 三分量 / 矩张量约束
检波器（中密度）  ─── 高频细节 / 主动源折射
```

**互补优势总结**：

| 能力 | 宽频地震仪 | 检波器 | DAS |
|------|----------|--------|-----|
| 低频（< 1 Hz） | ★★★★★ | ★ | ★★ |
| 高频（> 50 Hz） | ★★★ | ★★★★ | ★★★★★ |
| 空间分辨率 | ★★ | ★★★ | ★★★★★ |
| 三分量 | ★★★★★ | ★★★ | ★（轴向分量） |
| 极地部署成本 | 高 | 中 | 中（光缆成本递增） |
| 长期无人值守 | ★★★★ | ★★★ | ★★★★★ |

---

## 数据处理流程概述

冰川地震学典型处理流程：

```
原始连续记录
  │
  ├─ 去噪（时域：STA/LTA 检测；频域：谱归一化）
  │
  ├─ 冰震检测（STA/LTA + 模板匹配 + 机器学习分类）
  │
  ├─ 到时拾取（互相关、Akaike 信息准则 AIC 自动拾取）
  │
  ├─ 震源定位（双差法 / 网格搜索 / 梯度下降）
  │
  ├─ 震源机制（P 波极性、矩张量反演）
  │
  ├─ 速度结构（被动噪声互相关 → 频散 → 反演 Vs(z)）
  │
  └─ 时变监测（CWI: δv/v，模板匹配: 活动性时序）
```

---

## 参考文献

- Fichtner, A., Villaseñor, A., & Blom, N. (2023). Distributed acoustic sensing for seismic monitoring of glacier dynamics. *Nature Communications*, 14, 1–12.
- Aster, R. C., & Winberry, J. P. (2017). Glacial seismology. *Reports on Progress in Physics*, 80(12), 126801.
- Podolskiy, E. A., & Walter, F. (2016). Cryoseismology. *Reviews of Geophysics*, 54(4), 708–758.
- Lindsey, N. J., Rademacher, H., & Ajo-Franklin, J. B. (2020). On the broadband instrument response of fiber-optic DAS arrays. *Journal of Geophysical Research: Solid Earth*, 125(2), e2019JB018145.
- Gimbert, F., Nanni, U., Roux, P., Helmstetter, A., Lecointre, A., & Fettweis, X. (2021). A multi-physics experiment with a temporary dense seismic array on the Argentière glacier, French Alps: the RESOLVE project. *Seismological Research Letters*, 92(2A), 1132–1147.
- Lipovsky, B. P., & Dunham, E. M. (2016). Tremor during ice-stream stick slip. *The Cryosphere*, 10(1), 385–399.
- Walter, F., Röösli, C., & Greenwood, A. (2020). Borehole seismology and the study of the glacial environment. *The Cryosphere*, 14(1), 357–380.
- Nanni, U., Gimbert, F., Roux, P., & Lecointre, A. (2021). Observing the subglacial hydrology of the Argentière Glacier using ambient seismic noise. *The Cryosphere*, 15(11), 5003–5020.
- Winberry, J. P., Anandakrishnan, S., Alley, R. B., Bindschadler, R. A., & King, M. A. (2009). Basal mechanics of ice streams: insights from the stick-slip motion of Whillans Ice Stream, West Antarctica. *Journal of Geophysical Research: Earth Surface*, 114(F1).
- Pratt, M. J., et al. (2014). Seismic and geodetic evidence for grounding-line and ice-shelf dynamics at the Whillans Ice Stream. *Journal of Geophysical Research*, 119(3), 651–675.
- Harland, S. R., et al. (2013). Deformation in Rutford Ice Stream, West Antarctica: measuring shear wave anisotropy from icequakes. *Annals of Glaciology*, 54(64), 105–114.
- Walter, F., et al. (2015a). Using glacier seismicity for phase velocity measurements and Green's function retrieval. *Geophysical Journal International*, 201(3), 1722–1738.
- Diez, A., et al. (2016). Ice shelf structure derived from dispersion curve analysis of ambient seismic noise, Ross Ice Shelf, Antarctica. *Geophysical Journal International*, 205(2), 785–795.
- Anandakrishnan, S., & Winberry, J. P. (2004). Antarctic subglacial sedimentary layer thickness from receiver function analysis. *Global and Planetary Change*, 42(1–4), 167–176.
- Bartholomaus, T. C., et al. (2015b). Subglacial discharge at tidewater glaciers revealed by seismic tremor. *Geophysical Research Letters*, 42(15), 6391–6398.
- Bromirski, P. D., et al. (2015). Ross Ice Shelf vibrations. *Geophysical Research Letters*, 42(18), 7589–7597.
