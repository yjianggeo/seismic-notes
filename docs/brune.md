# Brune模型

## 理论背景

Brune模型（Brune source model）是地震学中最经典的震源谱模型之一，由 Brune (1970, 1971) 提出。

该模型用于描述：

- 地震震源位移谱
- 地震矩与谱低频平台之间的关系
- 拐角频率与震源尺度之间的关系
- 应力降与频谱特征之间的关系

Brune模型假设震源可视为圆形裂纹，并采用瞬时应力降模型描述断层破裂过程。

## 基本假设

Brune模型的核心假设包括：

1. 圆形裂纹模型
2. 均匀应力降
3. 无限均匀介质
4. 远场近似
5. S波主导
6. 位移谱满足单拐角频率形式

该模型本质上是一个简化震源模型。

## 位移谱模型

Brune模型认为震源位移谱满足：

$$
\Omega(f) = \frac{\Omega_0}{1 + (f / f_c)^2}
$$

其中：

- $\Omega_0$：低频平台
- $f_c$：拐角频率
- $f$：频率

该模型表明：

- 低频部分近似平坦
- 高频部分按 $f^{-2}$ 衰减

## 高频衰减机制

当：

$$
f \gg f_c
$$

时：

$$
\Omega(f)\propto f^{-2}
$$

因此 Brune模型常被称为：

- omega-square model
- $\omega^{-2}$ 模型

这种高频衰减反映了有限震源尺度对高频辐射的限制。

## 拐角频率

拐角频率 $f_c$ 表征：

- 震源尺度
- 破裂持续时间
- 高频截止特征

震源越大：

- 破裂时间越长
- $f_c$ 越低

震源越小：

- $f_c$ 越高

## 地震矩

Brune模型中，低频平台与地震矩满足：

$$
M_0=4\pi\rho\beta^3R\Omega_0/(FS)
$$

其中：

- $\rho$：密度
- $\beta$：S波速度
- $R$：震中距
- $F$：辐射系数
- $S$：自由表面修正

## 应力降

Brune模型中：

- 拐角频率
- 地震矩
- 震源半径

之间存在联系。

震源半径满足：

$$
r=k\beta/f_c
$$

其中：

- $k$ 为常数
- $beta$ 为剪切波速度

进一步可得到应力降：

$$
\Delta\sigma=\frac{7}{16}\frac{M_0}{r^3}
$$

## Brune谱的物理意义

Brune谱反映了：

- 有限震源尺度
- 断层破裂持续时间
- 高频辐射能力
- 应力释放过程

低频部分：

反映总体滑动规模。

高频部分：

反映小尺度破裂过程与高频辐射特征。

## 对数谱特征

在双对数坐标下：

- 低频部分斜率约为 0
- 高频部分斜率约为 -2

因此谱形存在明显拐点。

## Python绘图示例

下面代码用于绘制标准 Brune 谱：

```python
import numpy as np
import matplotlib.pyplot as plt

f = np.logspace(-1, 2, 1000)

fc = 10
omega0 = 1

spec = omega0 / (1 + (f/fc)**2)

plt.loglog(f, spec)

plt.xlabel("Frequency (Hz)")
plt.ylabel("Spectrum")

plt.grid(True)
plt.show()
```

结果表现为：

- 低频平台
- 高频 $f^{-2}$ 衰减

## 实际地震中的问题

实际地震谱往往偏离理想Brune模型。

原因包括：

- 路径衰减
- 场地效应
- 仪器响应
- 多阶段破裂
- 非圆形破裂
- 高频κ衰减
- 噪声影响

## 常见扩展模型

后续研究提出了许多扩展模型：

- Boatwright模型
- Madariaga模型
- 双拐角频率模型
- 高频衰减模型
- κ模型

## 参考文献

Brune, J. N. (1970). Tectonic stress and the spectra of seismic shear waves from earthquakes.

Brune, J. N. (1971). Correction.

Madariaga, R. (1976). Dynamics of an expanding circular fault.