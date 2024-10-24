const poderes = {
    Superman: 'Vuelo',
    Batman: 'Estrategia',
    Flash: 'Velocidad'
};

function mostrarPoder() {
    let heroe = document.getElementById('superheroes').value;
    document.getElementById('poder').innerText = `El poder de ${heroe} es: ${poderes[heroe]}`;
}
