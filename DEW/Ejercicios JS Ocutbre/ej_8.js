class Superheroe{
    constructor(nombre, nivelFuerza){
        this.nombre = nombre;
        this.nivelFuerza = nivelFuerza;
    }
}

let Vengadores = [
    Superheroe('Ironman', 80),
    Superheroe('Capitán América', 70),
    Superheroe('Spiderman', 90)
]

function superheroeMasFuerte(Vengadores){
    for (let i=1; i < Vengadores.length; i ++){
        let ganador = Vengadores[0]
        if (Vengadores[i].nivelFuerza > ganador.nivelFuerza){
            ganador = Vengadores[i]
        }
    }
    return ganador
}

console.log(superheroeMasFuerte(Vengadores))