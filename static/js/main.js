console.log("Hola mundo");
const pokemon_cards = document.getElementById('pokemon_cards')
console.log(pokemon_cards)
const colors ={
    fuego: '#FC6C6D',
    planta:'#49D0B0',
    agua:'#76BEFE',
    bicho:'#729F3F'


}
const main_types = Object.keys(colors)
const createPokemonCard = (pokemon) => {
    const poke_types = pokemon_cards.especie.map(especie=> especie.especie.especie )
    console.log(poke_types)
}