// to upload files and show modal on start and stop of resume uploads with progress bar
$(function () {
  var noModal = false;
  $(".js-upload-resumes").click(function () {
    $("#fileupload").click();
  });

  $("#fileupload").fileupload({
    dataType: 'json',
    sequentialUploads: true,
    start: function (e) {
      if (!(noModal)) {
        $("#modal-progress").modal("show");
      }
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
          "<tr><td><a href='" + data.result.url + "'>" + data.result.name+ "</a>" + '<span class="text-success" style="text-align: right;">  (' +"Time to extract: "+ data.result.time +'s)</span>' + "<br>" + '<b>Skills: </b>'+ data.result.skills +"</td></tr>"
        )
      }
      else {
        $("#alert-error").prepend(
            '<p>'+ data.result.error +'</p>'
        )
        $("#alert-error").show();
      }
    }

  });
});

// validating files
$('input[type=file]').change(function () {
    var val = $(this).val().toLowerCase(),
        regex = new RegExp("(.*?)\.(docx|doc|pdf)$");

    if (!(regex.test(val))) {
        $(this).val('');
        noModal = true;
        alert('Please upload correct resume format pdf, docx or doc');
    }
  });