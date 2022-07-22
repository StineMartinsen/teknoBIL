$(function () {
  $("a#button").on("click", function (e) {
    e.preventDefault();
    $.getJSON("/compare", function (data) {
      //Do nothing
      console.log("compare");
    });

    return false;
  });
});

$(function () {
  $("a#stop").on("click", function (e) {
    e.preventDefault();
    $.getJSON("/stop", function (data) {
      //do nothing
      console.log("stop");
    });
    return false;
  });
});
