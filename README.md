# Seismic Notes · 地震学学习笔记

[![Deploy](https://github.com/yjianggeo/seismic-notes/actions/workflows/deploy.yml/badge.svg)](https://github.com/yjianggeo/seismic-notes/actions/workflows/deploy.yml)
[![Site](https://img.shields.io/badge/site-yjianggeo.github.io%2Fseismic--notes-246f68)](https://yjianggeo.github.io/seismic-notes/)

从震源到光纤，系统梳理地震学、DAS 与波场分析的个人学习笔记。每篇笔记围绕一个明确问题展开：先解释现象，再推导公式，最后落到数据与应用。支持 **中文 / English 双语阅读**。

🔗 在线阅读：**<https://yjianggeo.github.io/seismic-notes/>**

---

## 📚 笔记目录

| 主题 | 中文 | English |
| --- | --- | --- |
| 几何地震学 · 时距曲线、速度与道集 | [geom-seismic.md](docs/geom-seismic.md) | [geom-seismic-en.md](docs/geom-seismic-en.md) |
| 震源理论 · Brune 震源模型 | [brune.md](docs/brune.md) | [brune-en.md](docs/brune-en.md) |
| 地震波衰减 · 谱比法 Q 值反演 | [q-spectral-ratio.md](docs/q-spectral-ratio.md) | [q-spectral-ratio-en.md](docs/q-spectral-ratio-en.md) |
| 垂直地震剖面 · VSP 原理与应用 | [vsp.md](docs/vsp.md) | [vsp-en.md](docs/vsp-en.md) |
| 面波与尾波 · 波速提取与监测 | [surface-coda.md](docs/surface-coda.md) | [surface-coda-en.md](docs/surface-coda-en.md) |
| 地震数据处理 · F-K 分析与 Radon 变换 | [fk-radon.md](docs/fk-radon.md) | [fk-radon-en.md](docs/fk-radon-en.md) |
| DAS 分布式声学传感 · 基本原理与应用 | [das.md](docs/das.md) | [das-en.md](docs/das-en.md) |
| 冰川地震学 · 仪器、阵列与 DAS 应用 | [glacier.md](docs/glacier.md) | [glacier-en.md](docs/glacier-en.md) |

英文页面不在站点导航中显示，通过页面右上角的中 / EN 切换按钮访问。

## 🗂 仓库结构

```
seismic-notes/
├── mkdocs.yml                 # MkDocs 站点配置（Material 主题）
├── requirements.txt           # 构建依赖
├── .github/workflows/
│   └── deploy.yml             # push 到 main 后自动部署到 GitHub Pages
├── docs/
│   ├── index.md               # 首页（含动态波形与主题索引）
│   ├── *.md / *-en.md         # 中 / 英双语笔记正文
│   ├── assets/
│   │   ├── images/            # 笔记插图（由 gen_*.py 脚本生成）
│   │   ├── javascripts/       # MathJax 配置、语言切换、首页动效
│   │   └── stylesheets/       # 自定义样式
│   └── overrides/
│       └── main.html          # 主题覆写（Open Graph / Twitter Card）
├── gen_*.py, regen_figures.py # 插图生成脚本（NumPy + Matplotlib）
└── site/                      # 本地构建产物（已被 .gitignore 忽略）
```

## 🛠 本地构建与预览

```bash
pip install -r requirements.txt
mkdocs serve          # 开发预览：http://127.0.0.1:8000/
mkdocs build          # 静态构建输出至 site/
```

## 🖼 重新生成插图

笔记中的示意图由仓库内的 Python 脚本生成，保证内容与图件可复现：

```bash
python regen_figures.py        # 批量生成主要插图
python gen_coupling_fig.py     # DAS 耦合响应图
python gen_glacier_figs.py     # 冰川地震学插图
```

生成结果输出至 `docs/assets/images/`。脚本依赖 NumPy 与 Matplotlib，请自行安装。

## 🚀 部署

推送至 `main` 分支后，GitHub Actions 会自动执行 `mkdocs gh-deploy --force` 并发布到 GitHub Pages，无需手动操作。

## ✍️ 新增一篇笔记

1. 在 `docs/` 下新建 `topic.md`（及可选的 `topic-en.md`）；
2. 在 `mkdocs.yml` 的 `nav:` 中加入中文页面，英文页面加入 `not_in_nav`；
3. 在 `docs/assets/javascripts/lang-toggle.js` 的 `PAIRS` 中登记中英页面映射；
4. `mkdocs serve` 确认无误后推送到 `main` 即可自动上线。

---

*Notes on seismology, DAS and wavefield analysis — built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/), deployed on GitHub Pages.*
