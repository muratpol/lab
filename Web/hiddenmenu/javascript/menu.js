var menuDurum = 0;
// When page opened this function purpose closed div elements

function menuDegistir(){
var menu0bj = document.getElementById("menu");
if(menuDurum == 0){
// Menu changed function be active if div closed , we need open the div.

menu0bj.style.display = "block";
			menuDurum = 1;
			/* When we open the menu then menuDurum
			variable value is 1 for purposed "menu element is open"
				               */	
		}else{ 
    // İf menu isn't close it time <<<menu is open>>..
	
	menu0bj.style.display = "none";
					menuDurum = 0;
					/* When we close the menu then menuDurum
			variable value is 0 for purposed "menu element is closed"
				               */	
}
}
