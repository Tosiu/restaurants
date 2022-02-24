const container = document.createElement("div")
container.classList.add("popup-container");

const popup = document.createElement("div")
popup.classList.add("popup");

const button = document.createElement("div")
button.classList.add("btn");

const par1 = document.createElement("p")
par1.innerText = "Close"

const par2 = document.createElement("p")
par2.innerText = "Something went wrong, look console for details"
par2.classList.add("popup-text");

container.appendChild(popup)
popup.appendChild(par2)
popup.appendChild(button)
button.appendChild(par1)


document.getElementsByClassName('content')[0].appendChild(container)
button.addEventListener("click", function(){
    container.style.visibility = "hidden";
});

function showPopup(text) {
    par2.innerText = text;
    container.style.visibility = "visible";
}