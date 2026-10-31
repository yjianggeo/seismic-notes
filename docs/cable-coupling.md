# DAS 光缆耦合状态的检测与评估

> 关键词：DAS、光缆耦合（cable coupling）、埋设状态（burial state）、Poincaré 谱相干、埋设指数（BI）、涡激振动（VIV）

## 引言

[DAS 基本原理](das.md)一章从理论上建立了光缆耦合的传递函数模型（套-芯耦合 $\eta_\text{fiber}$、介质耦合 $C_\text{med}(f)$ 与耦合刚度 $k_s$）。但在实际部署中，**耦合状态沿光缆是空间变化且未知的**：海底光缆可能一段埋于沉积物、一段暴露于海床、一段悬空跨越海沟；陆地光缆可能一段浅埋、一段裸铺、一段穿管。同一物理激励在不同耦合段产生截然不同的响应，若不掌握耦合状态的空间分布，环境噪声解释、事件检测和结构成像都会被系统性地误导。

本章关注：从 DAS 记录计算哪些指标，能支持怎样的耦合判断，以及怎样验证。部分方法不需要人工震源或类别标签，但独立安装资料和参考传感器仍是检验物理解释的重要依据。

## 先区分评价对象

| 评价对象 | 输出示例 | 对应验证 |
|---|---|---|
| 任务相关通道质量 | SNR、可靠性分数、地震可用概率 | 独立事件的拾取、检测或定位表现 |
| 安装/接触状态代理 | 埋藏、裸露、悬跨及状态异常 | 工程记录、潜水检查、受控状态变化 |
| 相对幅相响应 | 相对参考的增益、相位及其变化 | 可比波场、多参考选择和跨事件重复性 |
| 带限应变传递率 | DAS 应变相对独立参考应变的回归或复传递 | 已标定应变参考、方向与空间尺度匹配 |

这些量不能互换：若 $y=0.2x$ 且无噪声，两者相关和幅值平方相干都可为 1，但应变幅值仅传递了参考的 0.2。已知“细砂/粗砂”等安装类别也不等于已知机械传递率。[Forbriger 等（2025）](https://doi.org/10.1785/0220240308)

## 四种耦合状态及其物理效应

海底光缆的耦合状态通常分为四类，各自的力学约束与频率响应截然不同：

| 耦合状态 | 力学约束 | 频率响应特征 |
|---------|---------|-------------|
| **埋设**（buried） | 沉积物围限增加有效质量、刚度与阻尼 | 低通型：中高频被沉积物阻尼压制，低频（重力波频段）保留且空间平滑 |
| **部分埋设**（partially buried） | 约束介于埋设与暴露之间，可能存在间歇性接触 | 过渡型，频响介于两者之间 |
| **暴露**（exposed） | 水动力与海床接触共同作用 | 可能宽频敏感；具体幅相受压力、接触与激励控制 |
| **悬空**（suspended / free span） | 端点、张力与弯曲刚度约束，跨中接触弱 | 可出现涡激振动（VIV）或缆体共振；峰值依流速、跨度、张力而变 |

!!! note "耦合对观测的双刃剑效应"
    稳定接触通常有利于地震应变观测，悬跨振动却可能为海流监测提供信号。因此“良好质量”必须附带目标任务与频带，不能用一个安装状态概括所有观测目的。

上述频响是特定海底激励下的典型解释，不是四种安装状态的普适模板；良好埋设也可能因海床刚度差异出现振幅条带。海缆频带与阈值不应直接移植到井中回填光缆。

## 耦合状态检测方法概览

| 方法 | 观测量 | 优点 | 局限 |
|------|--------|------|------|
| 邻道相干（Hudson et al., 2025） | 相对相干与参考标定 | 可利用噪声/事件，已有幅值应用验证 | 需可比较波场；共同噪声、几何和异质性可混入 |
| 振幅谱聚类/邻域谱相关（Yin et al., 2024） | 振铃与异常谱形 | 自动筛查井中 VSP 异常道 | 连续多道共同振铃可能漏检；阈值依场地 |
| 重复激励比较（Muñoz et al., 2023） | 同一位置多次事件的重复性 | 有利于寻找稳定观测位置 | 源型号、速度和方向必须可比较 |
| 船只激励频带能量（Harmon et al., 2025） | 船只通过时的单峰/双峰包络与频带能量 | 物理模型约束响应机制 | 依赖船舶轨迹与足够信号；部分状态为推断 |
| 共振与振型分析 | 谱峰、节点及缆中传播 | 对机械边界敏感 | 激励、张力和局部结构也影响振型 |
| 参考波场对比 | 有效复传递函数 $T(f)$ | 同时评价幅值与相位，见[现场评估](das.md) | 需要独立参考或可信波场模型；滚降来源未必唯一 |
| **Poincaré 谱相干**（Shiri & Belal, 2026） | 邻道谱指纹的空间不规则性 | 无监督、近实时、轻量级、连续制图 | 频带需按站点调节；BI 是相对指标而非埋深 |

### 与普通相干、可靠性评分的区别

标准**幅值平方相干**（MSC）基于多窗平均后的自谱与交叉谱：

$$
\gamma^2_{ij}(f)=\frac{|S_{ij}(f)|^2}{S_{ii}(f)S_{jj}(f)},\qquad 0\leq\gamma^2\leq1.
$$

单窗单次傅里叶积在非零频点会给出退化的单位相干，必须说明 Welch/多锥窗等平均方式。Poincaré 指标则先舍弃相位、把两频带功率压成指纹，再计算**空间散布/梯度之比**，既不是 MSC，也不天然受 0–1 约束。Hudson 方法还有自己的时域归一化与时移定义，不能直接用 Pearson 或 MSC 替代后声称忠实复现。

PCCF 可靠性、CQI 与 ORION 主要验证选道/定位收益；它们可作基线，但“任务得分高”仍不等于绝对机械耦合充分。见 [Muñoz 与 Soto（2022）](https://doi.org/10.1038/s41467-022-31681-x)、[Rodriguez 等（2025）](https://doi.org/10.1109/JSTARS.2025.3593330)、[Bozzi 等（2026）](https://doi.org/10.26443/seismica.v5i1.2251)。

## Poincaré 谱相干框架

Shiri & Belal (2026) 提出的框架将 DAS 差分相位测量 $Y(t, x)$ 转化为沿缆的耦合状态指标，共四个阶段，全部只需短时 FFT 与块统计，**无需训练、无迭代优化**，可在单 CPU 核上近实时运行。

### 阶段 1：双频带谱指纹

将数据切分为 2–4 s 的重叠时窗（窗长 $N_t^{(w)}$），加 Hanning 锥抑制谱泄漏：

$$
h[n] = \frac{1}{2}\left(1 - \cos\frac{2\pi n}{N_t^{(w)} - 1}\right), \qquad \tilde{y}_i^{(w)}[n] = y_i^{(w)}[n]\, h[n]
$$

离散傅里叶变换后，在两个物理意义互补的频带上计算**频带能量**（Frequency Band Energy，FBE，即带内周期图功率之和）：

$$
P_{i,k}^{(w)} = \sum_{\ell \in K_k} \left|\hat{y}_i^{(w)}[\ell]\right|^2
$$

- **较低频带** $B_1$：论文文字写 0.01–10 Hz、式（5）写 0.1–10 Hz，复现时应记录实际取值。2–4 s 窗的频率格点间距约为 0.5–0.25 Hz，不能独立分辨 0.01 Hz 或潮汐周期；这里汇总的是短窗中实际可分辨的较低频能量；
- **高频带** $B_2$（如 100–120 Hz）：捕捉间歇性激励（船只谐波、涡激振动、流致颤动）——埋设时被沉积物阻尼强烈衰减，**对耦合状态最敏感**。

将两个带功率归一化为二维**谱指纹**：

$$
\mathbf{f}_i^{(w)} = \frac{1}{P_{i,1}^{(w)} + P_{i,2}^{(w)} + \varepsilon_1} \begin{bmatrix} P_{i,1}^{(w)} \\ P_{i,2}^{(w)} \end{bmatrix}
$$

!!! note "频带选择是站点相关的"
    频带取决于激励、介质、缆结构、标距、空间采样和采样率。先在开发数据选定，再冻结频带用于独立日期/事件验证；高频上限应低于 Nyquist，降采样前须抗混叠。不能按验证数据的已知段界反复调频带，再把同一数据上的分段符合度当作泛化能力。

### 阶段 2：Poincaré 型空间相干系数

将光缆分为 $M$ 道的空间块 $I_b$，计算块内指纹均值 $\bar{\mathbf{f}}^{(w,b)}$，然后定义两个统计量：

**谱散布**（块内指纹对均值的 L2 偏差）：

$$
\mathrm{Spread}_{L2}^{(w,b)} = \sqrt{\frac{1}{M} \sum_{i \in I_b} \left\| \mathbf{f}_i^{(w)} - \bar{\mathbf{f}}^{(w,b)} \right\|_2^2}
$$

**谱梯度**（相邻道指纹差分的 L2 范数）：

$$
\mathrm{Grad}_{L2}^{(w,b)} = \sqrt{\frac{1}{M-1} \sum_{i \in I_b \setminus \{\text{last}\}} \left\| \Delta \mathbf{f}_i^{(w)} \right\|_2^2}, \qquad \Delta\mathbf{f}_i^{(w)} = \mathbf{f}_{i+1}^{(w)} - \mathbf{f}_i^{(w)}
$$

为防止散布与梯度都极小的块产生虚高相干值，引入与块能量成比例的**梯度地板**：

$$
\mathrm{Scale}_{L2}^{(w,b)}=\sqrt{\frac1M\sum_{i\in I_b}\|\mathbf f_i^{(w)}\|_2^2},\qquad
\mathrm{Grad}_\text{floor}^{(w,b)} = \alpha\, \mathrm{Scale}_{L2}^{(w,b)}, \quad \alpha = 0.05; \qquad \mathrm{Grad}_\text{eff} = \max\left(\mathrm{Grad}_{L2},\, \mathrm{Grad}_\text{floor}\right)
$$

原论文报告其数据在 $\alpha\in[0.01,0.1]$ 的敏感性测试较稳定；其他场地仍需复核。最终指标为：

$$
\boxed{\; C_\text{eff}^{(w,b)} = \frac{\mathrm{Spread}_{L2}^{(w,b)}}{\mathrm{Grad}_\text{eff}^{(w,b)} + \varepsilon_2} \;}
$$

!!! tip "为什么叫 Poincaré 型？"
    Poincaré 不等式联系域内变差与梯度幅度。这里的比值比较的是**块尺度变化与邻道变化**；它对所有道同倍增益的谱指纹具有不变性，但并不对源谱形变化、加性噪声或空间不均匀激励自动免疫。

!!! warning "高值方向是经验解释，不是普适定理"
    原文在两个海缆实例中把高 BI 与暴露/弱约束段联系起来，但 $\mathrm{Spread}/\mathrm{Grad}$ 并不保证随任意“粗糙度”单调增加。忽略地板项时，$M$ 道线性斜坡的比值为 $\sqrt{(M^2-1)/12}$，平衡正负交替序列为 $1/2$；$M=10$ 时分别约 2.87 和 0.5。平滑斜坡反而可大于快速交替序列。指纹恰为常数时，Spread 为零，指标也为零。

    因此保留论文的高/低 BI 现场对应关系时，应标为**场地经验**，不要把任意高值直接解释为脱耦，也不要自行取倒数来“修正”后仍称复现原算法。

### 阶段 3：log–MAD–exp 稳健归一化

原始 $C_\text{eff}$ 非负但动态范围大、分布重尾（极端值来自强暴露/悬空段）。依次施加：

1. **对数变换**压缩大值：$L[w,b] = \log(C_\text{raw}[w,b] + \varepsilon_3)$；
2. **中位数–MAD 归一化**（稳健压缩尺度差异；不保证物理上消除环境或仪器混淆）：

$$
Z_L[w,b] = \frac{L[w,b] - m_L}{1.4826\,\mathrm{MAD}_L + \varepsilon_3}, \qquad m_L = \mathrm{median}(L), \quad \mathrm{MAD}_L = \mathrm{median}\left(|L - m_L|\right)
$$

其中 1.4826 是高斯假设下 MAD 与标准差的一致性常数——此处仅作参考标度，**不对数据施加正态假设**，选用 MAD 正是为了抗离群值与非高斯性；

3. **指数映射**回正数域：$C_\text{norm}[w,b] = \exp(Z_L[w,b])$。

### 阶段 4：空间平滑与埋设指数（BI）

对归一化场沿**空间块轴**做高斯平滑。若相邻块中心距为 $\Delta x_b$，则 $\sigma_b=L_\text{smooth}/\Delta x_b$；非重叠 $M$ 道块有 $\Delta x_b=M\Delta x$，不能误用单道间距。缆端反射是数值边界处理，不是物理反射。

$$
C_\text{smooth}[w,b] = \sum_k g_\sigma(b - k)\, C_\text{norm}[w,k], \qquad g_\sigma(\ell) \propto e^{-\ell^2 / 2\sigma^2}
$$

最后对时间窗取**中位数**，得到一维**埋设指数**（Burial Index）剖面：

$$
\boxed{\; \mathrm{BI}(b) = \operatorname*{median}_{w}\, C_\text{smooth}[w, b] \;}
$$

!!! warning "BI 是耦合指标，不是埋深"
    BI 是谱响应空间结构的相对代理，不直接测量埋深、接触刚度或应变传递率。水深、地形、沉积物、激励、防护结构和局部悬跨都可能贡献异常。稳定高相干的共同振动也不保证良好地震应变传递。

### 跨时段比较与可复现实现

- 保存原始带功率、谱指纹、$C_{\rm eff}$、归一化中位数/MAD、掩码和真实窗时刻。不同批次各自归一化后的 BI 绝对水平不能直接比较；跨期监测需固定开发期参考尺度，并同时查看原始量。
- 频带按实际 FFT 频点选择，明确端点包含规则，避免预分箱取整或重复频点。零填充可细化绘图格点，但不能增加窗长决定的真实频率分辨率。
- 近零能量、补零缺测、饱和和掉道须掩码。无量纲谱指纹不免除 PSD/RMS 的物理标定要求。
- 道间距小于标距时，邻道平均区间重叠可人为提高相似性。有效空间分辨率由标距、块宽、块步长和平滑共同决定；跨安装边界的窗口应单独处理。
- 时间窗跨文件边界、缺口和时间基准必须显式核对；不能把每文件少掉的边缘窗按等间隔连续拼接。基础操作见[数据与观测工作流](field-workflow.md)。

## 实例验证

| 参数 | EMEC Eday（英国奥克尼） | OBSEA（西班牙巴塞罗那） |
|------|------------------------|------------------------|
| 光缆长度 | ~2.2 km（复合电力缆） | ~5.8 km（通信-电力缆） |
| 道数 / 道间距 | 1083 / 2.04 m | 4560 / 1.275 m |
| 采样率 / 标距 | 1 kHz / 10 m | 2 kHz / 20 m |
| 环境 | 强潮流（至 4 m/s）、基岩-沙波纹-侵蚀崖交替 | 沉积物为主、较平缓 |
| 独立验证 | 地质单元界线（RF/LE/EF/ME）+ 航拍 | **潜水员/船员报告的埋设分段** |

**EMEC Eday**：BI 剖面与地质单元界线高度对应——近岸 200–350 m 持续低 BI（埋设/良好支撑段）；450–900 m 的 Eday  Flagstones 岩崖区 BI 升高且波动大（弱支撑/悬空段）；LE–RF、EF–LE 等岩性过渡带附近 BI 升高（刚度突变产生耦合对比），而 ME–EF 过渡渐变。与 Harmon et al. 基于船只频带能量判读的"部分埋设"区间一致。

**OBSEA**：论文报告部分潜水员/船员资料与 BI 的对应：0–1743.5 m 陆上段高 BI；1743.5–3300 m 被标为“疑似埋设”，BI 较低；3242.9–4342.3 m 被标为“未知”，BI 缓升；4442.5 m 以远未埋设段较高且波动。原文区间存在重叠与空隙，应保留其标签不确定性，不能将整条光缆包装成逐道真值验证。代表位置的频谱对比支持的是这些现场响应差异。

**计算性能**：论文在指定单 vCPU 环境和数据配置下报告近实时处理耗时；这支持计算可行性，不等于已验证长期在线的报警延迟、误报或跨场地性能。

## 假象与注意事项

!!! danger "别把仪器假象当成耦合信号"
    - **Fresnel 反射**：光纤末端（尤其水下未受控端接）的不良端接产生全频带持续高能量带，在原始热图、FBE 图与距离剖面上都可见——这是采集边界效应，切勿解释为环境或耦合特征；两端都可能出现（近端取决于连接器状态，随采集期次变化）；
    - **相位衰落（phase fading / Rayleigh fading）**：相干后向散射的相消干涉导致局部信号丢失、信噪比局部退化，在高频带尤为明显；
    - 松弛段（slack）、粘滑、增益变化、掉道等仪器问题也会产生类似耦合过渡的虚假相干间断。

- **原始时距图单独不足以判定状态**：它仍适合检查异常、传播与仪器假象，应结合谱形、相位和现场资料解释；
- **频带需按站点调节**（环境强迫、缆结构、标距、道间距都会移动最优频带；更长标距降低对短波长振动的灵敏度）；
- **水深与粗糙度的混淆**：水深既通过埋设持续性（沉积物输运路径）也通过激励环境（重力波轨道运动随深度衰减）影响 BI，粗糙海底即使无埋设变化也可因湍流非均匀性抬升 BI。

## 局限与展望

- **从分类走向定量**：当前框架给出耦合状态的相对分段，未来可结合空间全变分（total variation）、曲率（弯曲能）罚、多频带谱比等更一般的正则性诊断，配合标定的衰减模型与独立测量（ROV/潜水员），走向**定量埋深估计**；
- **共振类代理与波型依赖相干属性**可提供对耦合刚度的独立约束；
- **应用闭环**：BI 图可反向用于 DAS 观测质量控制——筛选稳定、耦合良好的道段用于地球物理监测，标记弱耦合段以谨慎解释其水动力/人为信号。

## 从海缆指标迁移到井中观测

先建立通道—沿缆距离—沿井距离—真垂深及三维切向量的映射。井中 DAS 测量 $\varepsilon_\parallel=\mathbf t^{\mathsf T}\boldsymbol\varepsilon\mathbf t$；不同方向的地表段和井中段不能直接用振幅大小排序“耦合优劣”。方向响应接近零时，应降低解释可信度，而不是除以近零因子强行校正。

对于局限在某回填段的窄带波包，应分别检查：多窗一致的下行/上行斜率、固定空间节点、事件前同类振型、与边界对应的能量变化和可追踪反射走时。**单一约 1.4 km/s 的沿缆表观相速度不能独立确认水声波、地层 P 波或管波**。回填中有水也不自动满足开放液柱模型；需完井、水位、压力或作业记录支持。相关波场判别见[观测工作流](field-workflow.md)。

### 验证与统计的最小要求

1. **合成隔离**：分别改变接收增益、相位、源谱、方向、噪声和局部介质，检查是否误把波场变化判为接触变化。
2. **外部状态对照**：工程类别可检验分段，但粒径与深度/地层共变时，仅能支持关联；不能强制要求“悬空＜地表＜细砂＜粗砂”的质量排序。
3. **整事件与整时段留出**：冻结频带、阈值和参考尺度，再在未见日期/方位检验。按事件或日期分组，避免相邻道和重叠窗泄漏到训练与测试两边。
4. **独立任务收益**：用噪声指标选道，比较独立地震的检测、盲评拾取或到时残差；控制通道数和空间覆盖。不要只用构造指标时的同一种相干再次“验证”。
5. **时间变化的混淆控制**：同时检查配置、噪声谱、激励方向、天气和数据覆盖。缺口不应插值成观测；以天/事件或时间块估计不确定度，不能把成千相邻道当作独立重复。

没有参考仪器时，可报告“相对接收响应与耦合相关异常”。进一步宣称绝对传递、冻融因果或震后机械变化，需要匹配的独立证据。地表气温不等于深井温度，有限的冬春/夏秋记录也不等于完整多年季节循环。

## 参考文献

- Shiri, H., & Belal, M. (2026). A real-time framework for mapping subsea cable burial state using Poincaré spectral coherence of DAS measurements. *Scientific Reports*, 16, 23647. [DOI](https://doi.org/10.1038/s41598-026-59846-4)。本章四阶段框架依据全文式（5）、（11）–（26）；原文频带差异与指标解释边界见上。
- Hudson, T., Stork, A., Muir, J., & Fichtner, A. (2025). Unlocking DAS amplitude information through coherency coupling quantification. *Seismica*, 4(1). [DOI](https://doi.org/10.26443/seismica.v4i1.1488)。相对相干、参考标定与应用边界。
- Forbriger, T., et al. (2025). Calibration of the Strain Amplitude Recorded with DAS Using a Strainmeter Array. *Seismological Research Letters*, 96, 2356–2367. [DOI](https://doi.org/10.1785/0220240308)；[作者全文](https://arxiv.org/html/2408.01151v3)。应变参考与幅值传递。
- Muir, J. B., & Zhan, Z. (2022). Wavefield-based evaluation of DAS instrument response and array design. *Geophysical Journal International*. [DOI](https://doi.org/10.1093/gji/ggab439)。重建波场评价整缆响应。
- Yin, J., Mizuno, T., & Le Calvez, J. (2024). Using the amplitude spectrum to characterize cable coupling of DAS traces. *IMAGE Expanded Abstracts*. [DOI](https://doi.org/10.1190/image2024-4094798.1)。会议方法：谱聚类与邻域谱相关。
- Muñoz, F., et al. (2023). Finding Well-Coupled Optical Fiber Locations for Railway Monitoring Using Distributed Acoustic Sensing. *Sensors*, 23, 6599. [DOI](https://doi.org/10.3390/s23146599)。重复列车方法；本次来源核读为部分正文。
- Harmon, N., et al. (2025). Distributed Acoustic Sensing Along a Shallow Water Energy Cable. *IEEE Journal of Oceanic Engineering*. [DOI](https://doi.org/10.1109/JOE.2024.3523363)。船声包络与物理机制。
- Muñoz, F., & Soto, M. A. (2022). Enhancing fibre-optic distributed acoustic sensing capabilities with blind near-field array signal processing. *Nature Communications*. [DOI](https://doi.org/10.1038/s41467-022-31681-x)。PCCF 与可靠性选道。
- Rodriguez, T., et al. (2025). Automatic Identification of High-Quality Channels in Distributed Acoustic Sensing Through Implementation of a Channel Quality Index. *IEEE JSTARS*. [DOI](https://doi.org/10.1109/JSTARS.2025.3593330)。本次核到部分正文及作者实现，作为任务质量方法入口。
- Bozzi, E., et al. (2026). Near real-time channel selection for Distributed Acoustic Sensing technology. *Seismica*. [DOI](https://doi.org/10.26443/seismica.v5i1.2251)。本次核到部分正文，作为几何与质量联合选道入口。
- Gurevich, B., et al. (2023). The Effect of the Method of Downhole Deployment on Distributed Acoustic Sensor Measurements: Field Experiments and Numerical Simulations. *Sensors*, 23, 7501. [DOI](https://doi.org/10.3390/s23177501)。井液、管波与部署方式的解释边界。
