$(function () {
  $("a#button").on("click", function (e) {
    $("#righty").reload(location.href + " #righty");
    e.preventDefault();
    $.getJSON("/compare", function (data) {
      //Do nothing
    });
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
