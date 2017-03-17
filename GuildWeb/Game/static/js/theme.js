var theme = 0;

function themeChange() {

	theme ++;
	localStorage.setItem("th", theme);
	loadTheme();
}

function loadTheme(){

	theme = localStorage.getItem("th");
	
	if (theme >2){
		theme = 0;
	}
	if(localStorage.getItem("th") == 0){
    	document.getElementById("themeChange").className = "redTheme";
		document.getElementById("banniereTitre").className = "banniereTitreRed";
		document.getElementById("menu").className = "menuRed";
		document.getElementById("boxConnexion").className = "boxConnexionRed";
	}
	if(localStorage.getItem("th") == 1){
    	document.getElementById("themeChange").className = "blueTheme";
		document.getElementById("banniereTitre").className = "banniereTitreBlue";
		document.getElementById("menu").className = "menuBlue";
		document.getElementById("boxConnexion").className = "boxConnexionBlue";
	}	
	if(localStorage.getItem("th") == 2){
    	document.getElementById("themeChange").className = "greenTheme";
		document.getElementById("banniereTitre").className = "banniereTitreGreen";
		document.getElementById("menu").className = "menuGreen";
		document.getElementById("boxConnexion").className = "boxConnexionGreen";
	}
}
