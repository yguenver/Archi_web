var theme = 0;

function themeChange() {
	theme ++;

	if(theme > 2){	theme = 0;	}	

	if(theme == 0){
    	document.getElementById("themeChange").className = "redTheme";
	}
	if(theme == 1){
    	document.getElementById("themeChange").className = "blueTheme";
	}	
	if(theme == 2){
    	document.getElementById("themeChange").className = "greenTheme";
	}
	localStorage.setItem("th", theme);
}

function themeChange2(){
	if(localStorage.getItem("th") == 0){
    	document.getElementById("themeChange").className = "redTheme";
	}
	if(localStorage.getItem("th") == 0){
    	document.getElementById("themeChange").className = "blueTheme";
	}	
	if(localStorage.getItem("th") == 0){
    	document.getElementById("themeChange").className = "greenTheme";
	}
}
