var speed = 30;
var roll_1 = document.getElementById("roll_1");
var roll_2 = document.getElementById("roll_2");
var roll_3 = document.getElementById("roll_3");
roll_3.innerHTML = roll_2.innerHTML;

function marquee(){ 
	if(roll_1.scrollLeft >= roll_2.scrollWidth)
	{ 
		roll_1.scrollLeft = 0; 
	}
	else
	{ 
		roll_1.scrollLeft++; 
	} 
}; 
var myMar=setInterval(marquee,speed);
roll_1.onmouseover=function(){clearInterval(myMar)}; 
roll_1.onmouseout=function(){myMar=setInterval(marquee,speed)};