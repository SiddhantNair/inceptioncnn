function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    reader.onload = function (e) {
      $("#imager").attr("src", e.target.result);
    };
    reader.readAsDataURL(input.files[0]);
  }
}

$(document).ready(function () {
  var selectedFile;

  $("#imgInp").change(function () {
    readURL(this);
    selectedFile = this.files[0];
  });

  $("#upload").click(function () {
    var fd = new FormData();
    var file = selectedFile;
    fd.append("image", file);

    $.ajax({
      url: "/classify",
      type: "post",
      data: fd,
      contentType: false,
      processData: false,
      success: function (response) {
        alert(response);
      },
    });
  });
});
