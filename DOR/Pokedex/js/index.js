// Importamos la clase Pokemon desde el archivo Pokemon.js
import Pokemon from './Pokemon.js';

// Creamos un array para los 151 pokemons que obtendremos desde la API
var pokemons = [];

// Seleccionamos el elemento button del DOM usando querySelector 
const button = document.querySelector("button");
// Agregamos un event listener al botón para que se mantenga a la espera de hacer click en él
// Cuando se recibe el click, se ejecuta la función flecha
button.addEventListener("click", () => {
    // Al hacer click sobre el botón, cambiamos su visibilidad y lo ocultamos
    document.querySelector('#button').style.visibility = 'hidden';
    // También cambiamos la visibilidad del elemento #pokedex, y lo mostramos en pantalla
    document.querySelector('#pokedex').style.visibility = 'visible';
    // LLamada a la función startPokedex() que comenzará el proceso de mostrar los Pokemon
    startPokedex();
});

// Función asíncrona que va a realizar operaciones con promesas para realizar la llamada a la API
const startPokedex = async () => {
    // Bucle for que itera desde 1 hasta 151, que son los primeros 151 Pokemon
    for(var i = 1; i <= 151; i++) {
        // Utilizamos fetch para hacer una solicitud a la API donde i representa el número de Pokemon
        await fetch("https://pokeapi.co/api/v2/pokemon/" + i + "/")
            .then(function(result) {
                return result.json();
            // Convertimos la respuesta de la API en un objeto JSON
            }).then(function(result) {
                const data = result;
                const pokemon = new Pokemon (data);
                pushPokemon(pokemon);
                //Guardamos el resultado en data y creamos una nueva instancia de Pokemon con los datos obtenidos
                // almacenamos los resultados en el array
               // console.log(pokemon);
            });
    }
    // Una vez que todos los Pokemon se han añadido al array, llamamos a la función showPokedex
    await showPokedex();
};

// Esta función añade el Pokemon que se le pasa como parámetro al array
function pushPokemon(pokemon) {
    pokemons.push(pokemon);
}

// Esta función se encarga de mostrar en el DOM los Pokemon que se han obtenido y almacenado en el array 
const showPokedex = async () => {
    // Se obtiene una referencia al elemento con el ID pokedex en el DOM donde se insertarán las tarjetas de los Pokemon.
    const pokedex = document.getElementById("pokedex");
    // Iteramos sobre cada elemento del array pokemons
    for(var i = 0; i < pokemons.length; i++) {
        var aux =  0;
        while (aux != pokemons[i].pkm_type.length) {
            if (aux == 0)
                var tipo1 = pokemons[i].pkm_type[aux].type.name;                       
            if (aux == 1)   
                var tipo2 = pokemons[i].pkm_type[aux].type.name;
            else 
                tipo2 = "";          
            aux++; 
        }
     function getColorByType(type) {
    switch (type) {
        case "fire":
            return "linear-gradient(to bottom, rgb(255, 160, 122), rgb(255, 69, 0))";
        case "water":
            return "linear-gradient(to bottom, rgb(173, 216, 230), rgb(0, 0, 255))";
        case "electric":
            return "linear-gradient(to bottom, rgb(255, 255, 224), rgb(255, 255, 0))";
        case "grass":
            return "linear-gradient(to bottom, rgb(144, 238, 144), rgb(124, 252, 0))";
        case "ice":
            return "linear-gradient(to bottom, rgb(224, 255, 255), rgb(173, 216, 230))";
        case "fighting":
            return "linear-gradient(to bottom, rgb(255, 160, 122), rgb(255, 69, 0))";
        case "poison":
            return "linear-gradient(to bottom, rgb(186, 85, 211), rgb(128, 0, 128))";
        case "ground":
            return "linear-gradient(to bottom, rgb(244, 164, 96), rgb(210, 180, 140))";
        case "flying":
            return "linear-gradient(to bottom, rgb(173, 216, 230), rgb(135, 206, 235))";
        case "psychic":
            return "linear-gradient(to bottom, rgb(255, 182, 193), rgb(255, 20, 147))";
        case "bug":
            return "linear-gradient(to bottom, rgb(240, 255, 240), rgb(173, 255, 47))";
        case "rock":
            return "linear-gradient(to bottom, rgb(211, 211, 211), rgb(169, 169, 169))";
        case "ghost":
            return "linear-gradient(to bottom, rgb(138, 43, 226), rgb(75, 0, 130))";
        case "dragon":
            return "linear-gradient(to bottom, rgb(123, 104, 238), rgb(75, 0, 130))";
        case "dark":
            return "linear-gradient(to bottom, rgb(105, 105, 105), rgb(0, 0, 0))";
        case "steel":
            return "linear-gradient(to bottom, rgb(224, 224, 224), rgb(192, 192, 192))";
        case "fairy":
            return "linear-gradient(to bottom, rgb(255, 240, 245), rgb(255, 182, 193))";
        default:
            return "linear-gradient(to bottom, rgb(255, 255, 240), rgb(245, 245, 220))";
    
    }
}

function NoEmptyTypes(tipo) {
    if (tipo === "") {
        return "0";
    } else {
        return "1";
    }
}

// Ejemplo de uso en tu código
const tipo1Color = getColorByType(tipo1);
const tipo2Color = getColorByType(tipo2);

pokedex.innerHTML += `<div class="card">
                        <div class="types">
                        <div class="idname">
                            ${pokemons[i].id}. ${pokemons[i].name}<br>
                        </div>
                        <div class="type" style="background-image: ${tipo1Color};">
                            ${tipo1}
                        </div>
                        <div class="type" style="background-image: ${tipo2Color}; opacity: ${NoEmptyTypes(tipo2)}";>
                            ${tipo2}
                        </div>
                        </div>
                        <br>
                        <img src="${pokemons[i].pkm_back}">
                        <img class="front" src="${pokemons[i].pkm_front}"><br>
                        <div class="phy">
                            <div class="height">
                                height: ${pokemons[i].weight}
                            </div>
                            <div class="weight">
                                weight: ${pokemons[i].height}
                            </div>
                        </div>
                    </div>`
    }
}