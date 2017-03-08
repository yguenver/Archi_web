function popa() {
alert("Hello World")
}


var x=0;



function popup(){
	var c=document.getElementById("myCanvas");
	var ctx=c.getContext("2d");
	ctx.fillRect(0,0,c.width,c.height/6);
	ctx.stroke();
	x++;
	
	ctx.font = "15px Arial";
	ctx.fillStyle = "red";
	ctx.fillText("rsc 1 : ",c.width/2+150,25);
	ctx.fillText("rsc 2 : ",c.width/2+150,50);
	ctx.fillText("rsc 3 : ",c.width/2+300,25);
	ctx.fillText("rsc 4 : ",c.width/2+300,50);
}