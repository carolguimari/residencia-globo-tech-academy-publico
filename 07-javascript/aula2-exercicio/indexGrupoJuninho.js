const axios = require('axios');
const fs = require('fs');
const path = require('path');

api = axios.create({
    baseURL: "https://rickandmortyapi.com/api",
});

async function getCharacter(query = "") {
    try {
        const response = await api.get(`/character/?${query}`)
        return response.data
    } catch (err) {
        console.log(err)
    }
}

function getCharacterPromise(query = "") {
    return api.get(`/character/?${query}`)
}

function writeFile(json, filename = "personagens.json") {
    const filePath = path.join(__dirname, filename)
    fs.writeFile(filePath, json, "utf-8", (err) => {
        if (err) {
            console.log(err)
        }
        console.log("Deu certo")
    })
}

async function main() {
    const personagens = await getCharacter()
    writeFile(JSON.stringify(personagens, null, 2))
}

function parallelRequests() {
    const personagens = getCharacterPromise()
    const personagensFiltrado = getCharacterPromise("name=rick&status=alive")
    Promise.all([personagens, personagensFiltrado]).then((values) => {
        values.forEach((value, index) => {
            index == 0 ? writeFile(JSON.stringify(value.data, null, 2)) : writeFile(JSON.stringify(value.data, null, 2), "personagemFiltrado.json")
        })
    })

}

//main()
parallelRequests()
