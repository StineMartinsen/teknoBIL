$(function () {
  $("a#button").on("click", function (e) {
    e.preventDefault();
    $.getJSON("/compare", function (data) {
      //Do nothing
    });
    $("#righty").load("index.html");
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
