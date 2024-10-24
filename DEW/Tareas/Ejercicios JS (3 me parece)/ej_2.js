function nazgulHover(elem) {
    if (elem.type === "mouseover") {
        elem.currentTarget.style.background = 'black';
        elem.currentTarget.style.color = 'white';
        elem.currentTarget.innerHTML = 'Nazgûl';
    } else {
        elem.currentTarget.style.background = 'white';
        elem.currentTarget.style.color = 'black';
        elem.currentTarget.innerHTML = 'Elemento';
    }
}

let elems = document.querySelectorAll(".nazgul");

elems.forEach(function(elem) {
    elem.addEventListener('mouseover', nazgulHover);
    elem.addEventListener('mouseout', nazgulHover);
});