document.addEventListener("DOMContentLoaded", function (event) {
  for (const element of document.getElementsByClassName("is-active")) {
    setTimeout(function () {
      element.parentElement.parentElement.scrollTo({
        left: element.offsetLeft,
        behavior: "auto",
      });
    }, 300);
  }
});

var darkModeToggle = document.getElementById("dark-mode-toggle");
var isDarkMode = window.localStorage.getItem("isDarkMode") === "true";
if (isDarkMode) {
  document.querySelector("body").classList.add("dark-theme");
  darkModeToggle.innerText = "Go light";
}

darkModeToggle.addEventListener(
  "click",
  function (ev) {
    var isDarkMode = document
      .querySelector("body")
      .classList.contains("dark-theme");
    document.querySelector("body").classList.toggle("dark-theme");

    if (isDarkMode) {
      window.localStorage.removeItem("isDarkMode");
      darkModeToggle.innerText = "Go dark";
      return;
    }
    window.localStorage.setItem("isDarkMode", true);
    darkModeToggle.innerText = "Go light";
  },
  false
);
