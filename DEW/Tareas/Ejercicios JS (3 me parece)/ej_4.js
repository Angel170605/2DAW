function manejarClic(reino) {
    alert(`Has clicado en: ${reino}`);
}

const reinos = document.querySelectorAll('.reino');

reinos.forEach(reino => {
    reino.addEventListener('click', (event) => {
        event.preventDefault(); 
        manejarClic(reino.dataset.reino); 
    });
});