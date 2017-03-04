<?php session_start(); ?>

<html>
<head><title>Login</title></head>
	<body>
<?php
if(@_SESSION["login"]=="OK")
{
	echo "Login Succesful!";
	echo "<table border='1'>
		<tr>
			<td><a href='mesaj.php'>MESAJLAR</a></td>
			<td><a href='cikis.php'>ÇIKIŞ YAP</a></td>
		</tr>
	</table>";
	} else { 
?> 

<form action="giris.php" method="post" />
<table align="center" style="font-family:verdana">
	<tr> 
		<td> Kullanıcı Adı:</td><td><input type="text" name="k_adi" /></td>
	</tr><tr>
		<td> Şifre: </td><td> <input type="password" name="sifre"/></td>
	</tr><tr>
		<td colspan="2" align="right">
		<input type="submit" value="Giris Yap" name="giris" />
		<input type="reset" value="temizle"/>
		</td>
	</tr>
</table>	
</form>
	<?php } ?>
	</body>
</html>

	
	
	</body>
</html>