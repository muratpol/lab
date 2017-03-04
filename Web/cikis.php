<?php session_start(); ?> 

<?php 
	session_destroy();
		echo "Exit Succesful ! ";
		echo "<table border='1'>
			<tr> 
				<td><a href='login.php'>GİRİŞ</a></td>
			</tr>
		</table>
		";
?>