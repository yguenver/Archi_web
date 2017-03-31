
function popa() {
alert("Hello World")
}

var user = {{ usr }};
var x=0;
var theme = 1;

	//widget.init(data_from_django);

function popup(){
	var c=document.getElementById("myCanvas");
	var ctx=c.getContext("2d");
	ctx.fillRect(0,0,c.width,c.height/6);
	ctx.stroke();
	x++;
	
	ctx.font = "15px Arial";
	ctx.fillStyle = "red";
	ctx.fillText("id : "+user.username,c.width/2+150,25);
	ctx.fillText("rsc 2 : ",c.width/2+150,50);
	ctx.fillText("rsc 3 : ",c.width/2+270,25);
	ctx.fillText("rsc 4 : ",c.width/2+270,50);
}

function setTheme(choix){
	theme = choix;

	if(theme == 1)
	{
		document.getElementById("labonnediv").style.backgroundColor = "rgba(99,0,0,0.8)";
	}
	if(theme == 2)
	{
		document.getElementById("labonnediv").style.backgroundColor = "rgba(0,99,0,0.8)";
	}
	if(theme == 3)
	{
		document.getElementById("labonnediv").style.backgroundColor = "rgba(0,0,99,0.8)";
	}
}



//http://stackoverflow.com/questions/11762629/pass-information-from-javascript-to-django-app-and-back
