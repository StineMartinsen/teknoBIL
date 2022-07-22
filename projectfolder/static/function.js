$(function () {
  $("a#button").on("click", function (e) {
    e.preventDefault();
    $.getJSON("/compare", function (data) {
      //Do nothing
    });
    var url = $("#re").attr("src");
    var timestamp = new Date().getTime();
    $("#container").attr("src", url + `?t=` + timestamp);
    console.log(timestamp);
    console.log($("#re").attr("src"));
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
