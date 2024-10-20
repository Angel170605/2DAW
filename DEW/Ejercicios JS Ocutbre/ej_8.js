class Superheroe {
    constructor(nombre, poder, nivel) {
        this.nombre = nombre;
        this.poder = poder;
        this.nivel = nivel;
    }
}

const heroes = [
    new Superheroe('Superman', 'Vuelo', 100),
    new Superheroe('Batman', 'Estrategia', 85),
    new Superheroe('Flash', 'Velocidad', 90)
];

function heroeMasPoderoso() {
    let maxNivel = 0;
    let heroePoderoso = '';
    for (let heroe of heroes) {
        if (heroe.nivel > maxNivel) {
            maxNivel = heroe.nivel;
            heroePoderoso = heroe.nombre;
        }
    }
    return heroePoderoso;
}

document.getElementById('resultado').innerText = `El superhéroe más poderoso es: ${heroeMasPoderoso()}`;
