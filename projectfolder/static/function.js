$(function () {
  $("a#button").on("click", function (e) {
    e.preventDefault();
    $.getJSON("/compare", function (data) {
      //Do nothing
    });
    var url = $("#re").attr("src");
    
    $("#re").attr("src", "none");
    $("#re").attr("src", url);

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
