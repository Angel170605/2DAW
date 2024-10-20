class Hechizo {
    constructor(nombre, poder) {
        this.nombre = nombre;
        this.poder = poder;
    }
}

class Mago {
    constructor(nombre, hechizo) {
        this.nombre = nombre;
        this.hechizo = hechizo;
    }

    invocarHechizo() {
        return this.hechizo.poder;
    }
}

const hechizo1 = new Hechizo('Expelliarmus', 50);
const hechizo2 = new Hechizo('Avada Kedavra', 100);

const mago1 = new Mago('Harry', hechizo1);
const mago2 = new Mago('Voldemort', hechizo2);

function duelo() {
    if (mago1.invocarHechizo() > mago2.invocarHechizo()) {
        return `${mago1.nombre} gana el duelo con ${mago1.hechizo.nombre}!`;
    } else {
        return `${mago2.nombre} gana el duelo con ${mago2.hechizo.nombre}!`;
    }
}

document.getElementById('resultado').innerText = duelo();
