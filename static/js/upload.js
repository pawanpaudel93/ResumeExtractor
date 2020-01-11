// to upload files and show modal on start and stop of resume uploads with progress bar
$(function () {

  $(".js-upload-photos").click(function () {
    $("#fileupload").click();
  });

  $("#fileupload").fileupload({
    dataType: 'json',
    sequentialUploads: true,
    start: function (e) {
      $("#modal-progress").modal("show");
    },
    stop: function (e) {
      const hide = $("#modal-progress");
      hide.modal('hide');
    },
    progressall: function (e, data) {
      var progress = parseInt(data.loaded/data.total * 100, 10);
      var strProgress = progress + "%";
      $(".progress-bar").css({"width": strProgress});
      $(".progress-bar").text(strProgress);
    },
    done: function (e, data) {
      if (data.result.is_valid) {
        $("#gallery tbody").prepend(
          "<tr><td><a href='" + data.result.path + "'>" + data.result.name + "</a></td></tr>"
        )
      }
    }

  });

});