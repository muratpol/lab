<?php 

$kullanici_adi = $_POST["k_adi"];
$sifre = $_POST["sifre"];


//  kontrol 

$bomch4nte = "A.I.M.";
$cw = "bug";

if ($kullanici_adi != $bomch4nte){
	
	echo "<script>alert('Boyle bir kullanıcı yok !');</script>";
}else{
	if($sifre != $cw){ 
echo "<script>alert('Şifre yanlış !');</script>";
	}else{

} }

echo "<h1><b>Başarıyla giriş yaptınız şimdi panele yönlendiriliyorsunuz. <meta http-equiv=\"refresh\" content=\"3;URL=http://127.0.0.1/bwapp/bWAPP/admin/login.php\">";
?>