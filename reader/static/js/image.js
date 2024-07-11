// 画像切り替え時にプレビュー表示
$('form.file').on('change', function (e) {
  var reader = new FileReader();
  reader.onload = function (e) {
      $("form.file").attr('src', e.target.result);
  }
  reader.readAsDataURL(e.target.files[0]);
});