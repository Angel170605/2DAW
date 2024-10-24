class Jedi {
    constructor(nombre, nivelFuerza, arma) {
        this.nombre = nombre;
        this.nivelFuerza = nivelFuerza;
        this.arma = arma;
    }
}

class Sith {
    constructor(nombre, nivelFuerza, arma) {
        this.nombre = nombre;
        this.nivelFuerza = nivelFuerza;
        this.arma = arma;
    }
}

const luke = new Jedi('Luke', 90, 'Sable Láser Verde');
const vader = new Sith('Vader', 85, 'Sable Láser Rojo');

const ganador = luke.nivelFuerza > vader.nivelFuerza ? luke : vader;
console.log(`El ganador es ${ganador.nombre}`);
