class PersonagemPokemon {
    constructor(nome, tipo, forca, defesa) {
        this.nome = nome
        this.tipo = tipo
        this.forca = forca
        this.defesa = defesa
    }

    static buildPersonagemPokemon(nome, tipo, forca, defesa) {
        return new PersonagemPokemon(nome, tipo, forca, defesa);
    }
}

class PersonagemDigimon {
    constructor(nome, elemento, forca, defesa) {
        this.nome = nome
        this.elemento = elemento
        this.forca = forca
        this.defesa = defesa
    }

    static buildPersonagemDigimon(nome, elemento, forca, defesa) {
        return new PersonagemDigimon(nome, elemento, forca, defesa)
    }
}


const listPokemon = []
const pikachu = PersonagemPokemon.buildPersonagemPokemon('Pikachu', 'elétrico', 99, 52)
const charizard = PersonagemPokemon.buildPersonagemPokemon('Charizard', 'fogo', 24, 79)
const squirtle = PersonagemPokemon.buildPersonagemPokemon('Squirtle', 'água', 24, 79)
listPokemon.push(pikachu, charizard, squirtle)


const listDigimon = []
const patamon = PersonagemDigimon.buildPersonagemDigimon('Patamon', 'Mamífero', 15, 20)
const shoutmon = PersonagemDigimon.buildPersonagemDigimon('Shoutmon', 'Pequeno Dragão', 40, 20)
const agumon = PersonagemDigimon.buildPersonagemDigimon('Agumon', 'Réptil', 50, 50)
listDigimon.push(patamon, shoutmon, agumon)


let mapaDePersonagens = new Map();
mapaDePersonagens.set('pokemon', listPokemon);
mapaDePersonagens.set('digimon', listDigimon);


for (const [_, valor] of mapaDePersonagens) {
    console.table(valor)
}

let tables;
tables = [...mapaDePersonagens.get('pokemon'), ...mapaDePersonagens.get('digimon')]

console.table(tables)