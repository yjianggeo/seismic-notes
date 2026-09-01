---
hide:
  - navigation
  - toc
  - feedback
---

<div class="seismic-home" data-seismic-home>
  <section class="home-hero">
    <div class="home-hero__copy reveal-item">
      <p class="home-eyebrow"><span>SEISMIC NOTES</span><span>地震学学习笔记</span></p>
      <h1>读懂地球的<br><em>每一次脉动</em></h1>
      <p class="home-lead">从震源谱到分布式光纤传感，用清晰的推导、图解与双语笔记，建立可以反复查阅的地震学知识体系。</p>
      <div class="home-actions">
        <a class="home-button home-button--primary" href="brune/">开始阅读 <span aria-hidden="true">↗</span></a>
        <a class="home-button home-button--ghost" href="#topics">浏览全部主题 <span aria-hidden="true">↓</span></a>
      </div>
      <dl class="home-stats" aria-label="站点概览">
        <div><dt>8</dt><dd>学习主题</dd></div>
        <div><dt>中 / EN</dt><dd>双语阅读</dd></div>
        <div><dt>26</dt><dd>专业图解</dd></div>
      </dl>
    </div>
    <div class="home-signal reveal-item" aria-label="动态地震波形">
      <div class="home-signal__meta">
        <span>LIVE TRACE</span>
        <span class="home-signal__status">正在记录</span>
      </div>
      <canvas data-seismic-canvas aria-hidden="true"></canvas>
      <div class="home-signal__scale" aria-hidden="true">
        <span>00 s</span><span>12 s</span><span>24 s</span><span>36 s</span>
      </div>
      <div class="home-signal__note">
        <span class="home-signal__mark"></span>
        <p><strong>让公式回到波形中。</strong><br>拖动指针，观察一次地震事件如何改变记录。</p>
      </div>
    </div>
  </section>

  <section class="home-intro reveal-item" aria-labelledby="home-intro-title">
    <p class="home-section-index">01 / 学习路径</p>
    <div>
      <h2 id="home-intro-title">从物理直觉出发，<br>走向可复现的方法。</h2>
      <p>每篇笔记都围绕一个明确问题展开：先解释现象，再推导公式，最后落到数据与应用。你可以顺序阅读，也可以把它当作案头手册。</p>
    </div>
  </section>

  <section class="home-topics" id="topics" aria-labelledby="topics-title">
    <div class="home-section-heading reveal-item">
      <div>
        <p class="home-section-index">02 / 主题索引</p>
        <h2 id="topics-title">探索笔记</h2>
      </div>
      <p>八个相互连接的入口，覆盖震源、传播、观测与处理。</p>
    </div>

    <div class="topic-grid">
      <a class="topic-card reveal-item" href="brune/">
        <span class="topic-card__number">01</span>
        <span class="topic-card__tag">SOURCE</span>
        <h3>Brune 震源模型</h3>
        <p>从圆形裂纹到震源谱，理解地震矩、拐角频率与应力降。</p>
        <span class="topic-card__link">进入笔记 <span aria-hidden="true">↗</span></span>
      </a>
      <a class="topic-card reveal-item" href="q-spectral-ratio/">
        <span class="topic-card__number">02</span>
        <span class="topic-card__tag">ATTENUATION</span>
        <h3>谱比法 Q 值反演</h3>
        <p>由双台站频谱比与线性回归，估计介质的衰减品质因子。</p>
        <span class="topic-card__link">进入笔记 <span aria-hidden="true">↗</span></span>
      </a>
      <a class="topic-card reveal-item" href="vsp/">
        <span class="topic-card__number">03</span>
        <span class="topic-card__tag">BOREHOLE</span>
        <h3>垂直地震剖面</h3>
        <p>串联观测几何、波场分离、速度建模、Q 值估计与成像。</p>
        <span class="topic-card__link">进入笔记 <span aria-hidden="true">↗</span></span>
      </a>
      <a class="topic-card reveal-item" href="surface-coda/">
        <span class="topic-card__number">04</span>
        <span class="topic-card__tag">MONITORING</span>
        <h3>面波与尾波</h3>
        <p>从频散反演到尾波干涉，连接地下结构与速度变化监测。</p>
        <span class="topic-card__link">进入笔记 <span aria-hidden="true">↗</span></span>
      </a>
      <a class="topic-card reveal-item" href="fk-radon/">
        <span class="topic-card__number">05</span>
        <span class="topic-card__tag">PROCESSING</span>
        <h3>F-K 与 Radon</h3>
        <p>辨析视速度、空间假频与多类 Radon 变换的适用边界。</p>
        <span class="topic-card__link">进入笔记 <span aria-hidden="true">↗</span></span>
      </a>
      <a class="topic-card reveal-item" href="das/">
        <span class="topic-card__number">06</span>
        <span class="topic-card__tag">FIBER SENSING</span>
        <h3>DAS 分布式声学传感</h3>
        <p>拆解 φ-OTDR、方向性响应、标距效应与实际观测设计。</p>
        <span class="topic-card__link">进入笔记 <span aria-hidden="true">↗</span></span>
      </a>
      <a class="topic-card reveal-item topic-card--wide" href="glacier/">
        <span class="topic-card__number">07</span>
        <span class="topic-card__tag">CRYOSEISMOLOGY</span>
        <h3>冰川地震学</h3>
        <p>从冰震信号分类与阵列定位，到 DAS 铺设、结构成像与粘滑监测。</p>
        <span class="topic-card__link">进入笔记 <span aria-hidden="true">↗</span></span>
      </a>
      <a class="topic-card reveal-item" href="geom-seismic/">
        <span class="topic-card__number">08</span>
        <span class="topic-card__tag">GEOMETRY</span>
        <h3>几何地震学</h3>
        <p>双曲线时距、NMO、叠加/均方根速度与 CMP 道集的物理图景。</p>
        <span class="topic-card__link">进入笔记 <span aria-hidden="true">↗</span></span>
      </a>
    </div>
  </section>

  <section class="home-prompt reveal-item" aria-labelledby="prompt-title">
    <div>
      <p class="home-section-index">03 / 随机起点</p>
      <h2 id="prompt-title">不知道从哪里开始？</h2>
    </div>
    <div class="home-prompt__content">
      <p data-topic-kicker>今天的问题</p>
      <a href="brune/" data-topic-link>为什么大地震的低频振幅更高？ <span aria-hidden="true">↗</span></a>
      <button type="button" data-topic-shuffle aria-label="换一个学习主题">换一个主题 <span aria-hidden="true">↻</span></button>
    </div>
  </section>
</div>
