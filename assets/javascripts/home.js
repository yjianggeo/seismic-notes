(function () {
  "use strict";

  var cleanup = [];

  function addCleanup(fn) {
    cleanup.push(fn);
  }

  function teardown() {
    cleanup.forEach(function (fn) { fn(); });
    cleanup = [];
  }

  function readingProgress() {
    var old = document.querySelector(".reading-progress");
    if (old) old.remove();

    var track = document.createElement("div");
    track.className = "reading-progress";
    track.setAttribute("aria-hidden", "true");
    var bar = document.createElement("span");
    bar.className = "reading-progress__bar";
    track.appendChild(bar);
    document.body.appendChild(track);

    function update() {
      var total = document.documentElement.scrollHeight - window.innerHeight;
      var value = total > 0 ? Math.min(1, Math.max(0, window.scrollY / total)) : 0;
      bar.style.transform = "scaleX(" + value + ")";
    }

    window.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", update);
    update();

    addCleanup(function () {
      window.removeEventListener("scroll", update);
      window.removeEventListener("resize", update);
      track.remove();
    });
  }

  function revealItems(root) {
    var items = Array.prototype.slice.call(root.querySelectorAll(".reveal-item"));
    if (!("IntersectionObserver" in window) ||
        window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      items.forEach(function (item) { item.classList.add("is-visible"); });
      return;
    }

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });

    items.forEach(function (item, index) {
      item.style.transitionDelay = Math.min(index % 3, 2) * 70 + "ms";
      observer.observe(item);
    });

    addCleanup(function () { observer.disconnect(); });
  }

  function topicShuffle(root) {
    var link = root.querySelector("[data-topic-link]");
    var button = root.querySelector("[data-topic-shuffle]");
    if (!link || !button) return;

    var topics = [
      ["brune/", "为什么大地震的低频振幅更高？"],
      ["q-spectral-ratio/", "怎样从两条频谱估计介质衰减？"],
      ["vsp/", "把检波器放进井里，能多看见什么？"],
      ["surface-coda/", "尾波为什么能感知微小的速度变化？"],
      ["fk-radon/", "如何在波数域中分离不同方向的波？"],
      ["das/", "一根普通光纤如何变成密集地震台阵？"],
      ["glacier/", "冰川的裂隙与滑动会发出怎样的信号？"]
    ];
    var index = 0;

    function shuffle() {
      index = (index + 1) % topics.length;
      link.animate(
        [{ opacity: 1, transform: "translateY(0)" }, { opacity: 0, transform: "translateY(-6px)" }],
        { duration: 130, fill: "forwards" }
      ).finished.then(function () {
        link.href = topics[index][0];
        link.innerHTML = topics[index][1] + ' <span aria-hidden="true">↗</span>';
        link.animate(
          [{ opacity: 0, transform: "translateY(6px)" }, { opacity: 1, transform: "translateY(0)" }],
          { duration: 220, fill: "forwards" }
        );
      });
    }

    button.addEventListener("click", shuffle);
    addCleanup(function () { button.removeEventListener("click", shuffle); });
  }

  function seismicCanvas(root) {
    var canvas = root.querySelector("[data-seismic-canvas]");
    if (!canvas) return;

    var context = canvas.getContext("2d");
    var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var pointer = 0.64;
    var targetPointer = pointer;
    var frame = 0;
    var visible = true;

    function resize() {
      var rect = canvas.getBoundingClientRect();
      var ratio = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = Math.max(1, Math.round(rect.width * ratio));
      canvas.height = Math.max(1, Math.round(rect.height * ratio));
      context.setTransform(ratio, 0, 0, ratio, 0, 0);
      draw(0);
    }

    function color(name, fallback) {
      return getComputedStyle(root).getPropertyValue(name).trim() || fallback;
    }

    function draw(time) {
      var width = canvas.clientWidth;
      var height = canvas.clientHeight;
      if (!width || !height) return;

      context.clearRect(0, 0, width, height);
      context.lineWidth = 1;
      context.strokeStyle = color("--seismic-line", "rgba(23,33,31,.15)");
      context.beginPath();
      context.moveTo(0, height / 2);
      context.lineTo(width, height / 2);
      context.stroke();

      pointer += (targetPointer - pointer) * 0.045;
      var eventX = width * pointer;
      var phase = reduceMotion ? 0 : time * 0.0022;

      context.lineWidth = Math.max(1.3, width / 380);
      context.strokeStyle = color("--seismic-teal", "#2a7c74");
      context.lineJoin = "round";
      context.beginPath();

      for (var x = 0; x <= width; x += 2) {
        var distance = (x - eventX) / Math.max(width * 0.17, 1);
        var envelope = Math.exp(-distance * distance * 1.2);
        var quiet = Math.sin(x * 0.17 + phase) * height * 0.008;
        var event = Math.sin(x * 0.35 - phase * 2.3) * envelope * height * 0.38;
        var aftershock = Math.sin(x * 0.58 + phase) *
          Math.exp(-Math.abs(distance) * 1.7) * height * 0.08;
        var y = height / 2 + quiet + event + aftershock;
        if (x === 0) context.moveTo(x, y);
        else context.lineTo(x, y);
      }
      context.stroke();

      context.fillStyle = color("--seismic-ochre", "#c28b3c");
      context.beginPath();
      context.arc(eventX, height / 2, 3, 0, Math.PI * 2);
      context.fill();
    }

    function loop(time) {
      if (visible) draw(time);
      if (!reduceMotion) frame = requestAnimationFrame(loop);
    }

    function move(event) {
      var rect = canvas.getBoundingClientRect();
      var point = event.touches ? event.touches[0] : event;
      targetPointer = Math.min(0.86, Math.max(0.18, (point.clientX - rect.left) / rect.width));
    }

    function visibility(entries) {
      visible = entries[0].isIntersecting;
    }

    var observer = "IntersectionObserver" in window
      ? new IntersectionObserver(visibility)
      : null;
    if (observer) observer.observe(canvas);

    window.addEventListener("resize", resize);
    canvas.addEventListener("pointermove", move);
    canvas.addEventListener("touchmove", move, { passive: true });
    resize();
    if (!reduceMotion) frame = requestAnimationFrame(loop);

    addCleanup(function () {
      cancelAnimationFrame(frame);
      window.removeEventListener("resize", resize);
      canvas.removeEventListener("pointermove", move);
      canvas.removeEventListener("touchmove", move);
      if (observer) observer.disconnect();
    });
  }

  function init() {
    teardown();
    readingProgress();
    var root = document.querySelector("[data-seismic-home]");
    if (!root) return;
    revealItems(root);
    topicShuffle(root);
    seismicCanvas(root);
  }

  document.addEventListener("DOMContentLoaded", init);
  document.addEventListener("DOMContentSwitch", init);
  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(init);
  }
})();
