/**
 * Language toggle: Chinese ↔ English
 * Injects a button into the Material header that switches between
 * the Chinese and English versions of the current page.
 *
 * Page-pair mapping (MkDocs slugs, no trailing slash needed):
 *   brune   ↔  brune-en
 *   index   ↔  index-en   (future)
 */

(function () {
  "use strict";

  // Map: Chinese slug → English slug (and the reverse is auto-derived)
  var PAIRS = {
    "brune": "brune-en",
    "q-spectral-ratio": "q-spectral-ratio-en",
    "das": "das-en",
    "vsp": "vsp-en",
  };

  // Build reverse map: English → Chinese
  var REVERSE = {};
  Object.keys(PAIRS).forEach(function (zh) {
    REVERSE[PAIRS[zh]] = zh;
  });

  /**
   * Extract the page slug from the current URL path.
   * Works whether the site is served at root or a sub-path.
   * e.g. /source-spectrum-site/brune/ → "brune"
   *      /source-spectrum-site/brune-en/ → "brune-en"
   */
  function currentSlug() {
    var path = window.location.pathname;
    // Remove trailing slash, then grab last segment
    var parts = path.replace(/\/$/, "").split("/");
    return parts[parts.length - 1] || "";
  }

  /**
   * Given the current slug, return {targetSlug, label} if a pair exists.
   * label is the text shown on the button (where you'll GO, not where you ARE).
   */
  function pairInfo(slug) {
    if (PAIRS[slug]) {
      return { target: PAIRS[slug], label: "EN" };
    }
    if (REVERSE[slug]) {
      return { target: REVERSE[slug], label: "中" };
    }
    return null;
  }

  /**
   * Build the target URL by replacing the slug segment in the current path.
   */
  function targetUrl(currentSlug, targetSlug) {
    var path = window.location.pathname;
    // Replace the last non-empty path segment
    var newPath = path.replace(
      /(\/)[^/]+(\/?$)/,
      "$1" + targetSlug + "$2"
    );
    return newPath + window.location.search + window.location.hash;
  }

  /**
   * Inject the language toggle button into the Material header.
   * Material renders a <div class="md-header__inner"> that contains
   * the title and right-hand action buttons.
   */
  function injectButton() {
    var slug = currentSlug();
    var info = pairInfo(slug);

    // Remove any previously injected button (SPA navigation)
    var existing = document.getElementById("lang-toggle-btn");
    if (existing) existing.remove();

    // Only show the button on pages that have a pair
    if (!info) return;

    // Find the right-hand button group in the Material header
    var headerButtons = document.querySelector(".md-header__inner .md-header__source") ||
                        document.querySelector(".md-header__inner") ||
                        document.querySelector(".md-header");
    if (!headerButtons) return;

    var url = targetUrl(slug, info.target);

    // Create button element styled to match Material's header buttons
    var btn = document.createElement("a");
    btn.id = "lang-toggle-btn";
    btn.href = url;
    btn.title = info.label === "EN" ? "Switch to English" : "切换为中文";
    btn.setAttribute("aria-label", btn.title);
    btn.className = "md-header__button md-icon";
    btn.style.cssText = [
      "display: inline-flex",
      "align-items: center",
      "justify-content: center",
      "width: auto",
      "min-width: 1.6rem",
      "height: 1.6rem",
      "padding: 0 0.3rem",
      "font-size: 0.75rem",
      "font-weight: 700",
      "font-family: inherit",
      "letter-spacing: 0.03em",
      "color: var(--md-primary-bg-color)",
      "background: transparent",
      "border: 1.5px solid var(--md-primary-bg-color)",
      "border-radius: 0.2rem",
      "text-decoration: none",
      "cursor: pointer",
      "margin: 0 0.2rem",
      "line-height: 1",
      "opacity: 0.85",
      "transition: opacity 0.2s",
    ].join(";");

    btn.addEventListener("mouseenter", function () { btn.style.opacity = "1"; });
    btn.addEventListener("mouseleave", function () { btn.style.opacity = "0.85"; });

    var span = document.createElement("span");
    span.textContent = info.label;
    btn.appendChild(span);

    // Insert before the last button group (search icon area) or append
    var firstBtn = headerButtons.querySelector(".md-header__button");
    if (firstBtn) {
      headerButtons.insertBefore(btn, firstBtn);
    } else {
      headerButtons.appendChild(btn);
    }
  }

  // Run on initial load
  document.addEventListener("DOMContentLoaded", injectButton);

  // Re-run on MkDocs instant navigation (SPA page changes)
  document.addEventListener("DOMContentSwitch", injectButton);

  // Also hook into MkDocs Material's internal navigation events
  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(injectButton);
  }
})();
