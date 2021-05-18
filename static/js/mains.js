let menuOpeners = document.getElementsByClassName('mobile-menu-open-button');

let menuCloser = document.getElementById('menu-close-button');

let menuDiv = document.getElementById('myMenu');
console.log(menuOpeners);
console.log(menuCloser);
console.log(menuDiv);
for (var i=0;i<menuOpeners.length;i++) {
	menuOpeners[i].onclick = function() {
		showMobileMenu();
	}
}

//menuCloser.onclick = hideMobileMenu();

async function hideMobileMenu() {
	console.log("hiding");
	menuDiv.style.opacity = "0";
	document.body.style.overflowY = "scroll";
	setTimeout(function() {
		menuDiv.style.left = "-120vw";
	}, 250);
}

async function showMobileMenu() {
	console.log("showing");
	document.body.style.overflowY = "hidden";
	menuDiv.style.left = "0";
	setTimeout(function() {
		menuDiv.style.opacity = "1";
	}, 25);
}
