(function () {
  "use strict";

  function fallbackCopy(text) {
    var field = document.createElement("textarea");
    field.value = text;
    field.setAttribute("readonly", "");
    field.style.position = "fixed";
    field.style.opacity = "0";
    document.body.appendChild(field);
    field.select();
    var copied = document.execCommand("copy");
    document.body.removeChild(field);
    return Promise.resolve(copied);
  }

  function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text).then(function () { return true; });
    }
    return fallbackCopy(text);
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".pub-actions .copy-bibtex").forEach(function (button) {
      var citation = button.parentElement.querySelector(".bibtex-source");
      if (!citation) return;

      button.setAttribute("aria-label", "Copy BibTeX citation");

      button.addEventListener("click", function () {
        copyText(citation.textContent.trim()).then(function (copied) {
          var original = button.textContent;
          button.textContent = copied ? "Copied!" : "Copy failed";
          button.classList.toggle("is-copied", copied);
          window.setTimeout(function () {
            button.textContent = original;
            button.classList.remove("is-copied");
          }, 1600);
        }).catch(function () {
          button.textContent = "Copy failed";
          window.setTimeout(function () { button.textContent = "Copy BibTeX"; }, 1600);
        });
      });
    });
  });
}());
