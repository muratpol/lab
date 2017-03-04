<?php session_start(); ?>

<?php
if (($_POST["k_adi"]=="bomch4nte") && ($_POST["sifre"]=="cyberwarrior"))
	{ 
	$_SESSION["login"]="OK";
	echo "Login Succesful!";
	echo "<table border='1'>
		<tr> 
			<td><a href='mesaj.php'>MESAJLAR</a></td>
			
		</tr>
		</table>
	";
} else { 
	echo "Girilen Bilgiler Hatalı !";
	echo "<br /><a href='login.php'>Geri Don</a>";
}
?>