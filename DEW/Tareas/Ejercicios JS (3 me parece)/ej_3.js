class Ejercito {
    constructor(nombre, numeroSoldados, fuerza) {
        this.nombre = nombre;
        this.numeroSoldados = numeroSoldados;
        this.fuerza = fuerza;
    }
}

const ejercitos = [
    new Ejercito("Alemania", 5000, 80),
    new Ejercito("España", 3000, 100),
    new Ejercito("Estados Unidos", 7000, 90),
    new Ejercito("Rusia", 5000, 70),
    new Ejercito("Ucrania", 2000, 60)
];

function mostrarEjercitos(ejercitos) {
    let html = '<ul>';
    for (let i = 0; i < ejercitos.length; i++) { // Cambiado 1 > a i <
        html += `
            <li>
                Nombre del ejército: ${ejercitos[i].nombre} <br>
                Número de soldados: ${ejercitos[i].numeroSoldados} <br>
                Fuerza del ejército: ${ejercitos[i].fuerza}
            </li>
        `;
    }
    html += '</ul>';
    return html; // Retornar la cadena HTML
}

function Battle(ejercitos) {
    let winner = ejercitos[0];

    for (let i = 1; i < ejercitos.length; i++) { // Cambiado 1 > a i <
        if (ejercitos[i].fuerza > winner.fuerza) {
            winner = ejercitos[i];
        }
    }

    return winner;
}

// Obtener el ejército ganador
const winner = Battle(ejercitos);

// Crear el HTML
const html = document.createElement('div');
html.innerHTML = `
    <h1>Ejércitos:</h1>
    <div>
        ${mostrarEjercitos(ejercitos)}
    </div>
    <h1>Y el ejército ganador</h1>
    <h1>Con ${winner.numeroSoldados} soldados, y una fuerza de ${winner.fuerza} es...</h1>  
    <h1>${winner.nombre}</h1>
`;

// Agregar el HTML al body o a un contenedor específico
document.body.appendChild(html);