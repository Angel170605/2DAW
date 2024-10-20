class Gema {
    constructor(nombre, poder) {
        this.nombre = nombre;
        this.poder = poder;
    }
}

class Thanos {
    constructor() {
        this.gemas = [];
    }

    recolectarGema(gema) {
        this.gemas.push(gema);
    }

    poderTotal() {
        return this.gemas.reduce((total, gema) => total + gema.poder, 0);
    }
}

const thanos = new Thanos();
thanos.recolectarGema(new Gema('Gema del Alma', 50));
thanos.recolectarGema(new Gema('Gema del Tiempo', 60));
document.getElementById('resultado').innerText = `El poder total de Thanos es: ${thanos.poderTotal()}`;
