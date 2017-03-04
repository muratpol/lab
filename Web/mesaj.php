<?php session_start(); ?>

<?php 

if(@$_SESSION["login"]=="OK")
{ 
	echo "MESAJLAR BURADA ARKADASIM ! ";
	echo "<br /><a href='cikis.php'>Çıkış Yap</a>";
}
	else { 
		echo "Giriş Yap ! ";
		echo "<br /><a href='login.php'>Geri Don</a>";
	}
?> 