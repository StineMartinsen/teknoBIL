$(function () {
  $("a#button").on("click", function (e) {
    window.location.reload();
    e.preventDefault();
    $.getJSON("/compare", function (data) {
      //Do nothing
    });

    let textarea = document.querySelector("textarea");
    let files = 'result.txt';
    if (files.length == 0) return;
    const file = files[0];
    let reader = new FileReader();
    reader.onload = (e) => {
      const file = e.target.result;
      const lines = file.split(/\r\n|\n/);
      textarea.value = lines.join("\n");
    };
    reader.onerror = (e) => alert(e.target.error.name);
    reader.readAsText(file);
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
