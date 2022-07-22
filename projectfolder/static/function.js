$(function () {
  $("a#button").on("click", function (e) {
    e.preventDefault();
    $.getJSON("/compare", function (data) {
      //Do nothing
    });
    var reimg;
    window.onload = function () {
      reimg = document.getElementById("re");
      setInterval(function () {
        reimg.src = reimg.src.replace(/\?.*/, function () {
          return "?" + new Date();
        });
      }, 5000);
    };
    return false;
  });
});

$(function () {
  $("a#stop").on("click", function (e) {
    e.preventDefault();
    $.getJSON("/stop", function (data) {
      //do nothing
    });
    return false;
  });
});
