<?php
$bom = $_FILES["dosya"] ["tmp_name"];
$name = $_FILES ["dosya"] ["name"];

$yukle = move_uploaded_file($bom,$name);

if ($yukle) { 
echo "<script>alert('Yükleme Başarılı; dosya bulunduğunuz dizine kaydedildi.')</script>";
}else { 
echo "Yukleme Basarısız";
}

?>