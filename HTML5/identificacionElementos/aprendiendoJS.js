

function ejecuta(){

	document.getElementsByTagName("p").onclick=saludo;
}

function saludo(){
	
	alert("como estas");
}


window.onload=ejecuta();