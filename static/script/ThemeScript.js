let theme = localStorage.getItem("theme");
if (theme == null) {
  setTheme("light");
} else {
  setTheme(theme);
}

let themeDots = document.getElementsByClassName("theme-dots");

for (var i = 0; themeDots.length > i; i++) {
  themeDots[i].addEventListener("click", function () {
    let mode = this.dataset.mode;
    console.log("Option clicked", mode);
    setTheme(mode);
  });
}

function setTheme(mode) {
  if (mode == "light") {
    document.getElementById("theme-style").href = "style/index_style.css";
  }
  if (mode == "blue") {
    document.getElementById("theme-style").href = "style/blue_style.css";
  }
  if (mode == "green") {
    document.getElementById("theme-style").href = "style/green_style.css";
  }
  if (mode == "purple") {
    document.getElementById("theme-style").href = "style/purple_style.css";
  }
  if (mode == "red") {
    document.getElementById("theme-style").href = "style/red_style.css";
  }

  localStorage.setItem("theme", mode);
}
