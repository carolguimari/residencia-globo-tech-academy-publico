const axios = require('axios')
const fs = require('fs')

const request = axios.create({
    baseURL: 'https://rickandmortyapi.com/api'
});

function getNumeroAleatorioAteLimite(maximo) {
    return Math.floor(Math.random() * maximo)
}

async function getListaPersonagem() {
    try {
        const { data } = await request.get(`/character`)
        return data.results
    } catch (err) {
        throw err;
    }
}

async function getPersonagem(id) {
    try {
        const { data } = await request.get(`/character/${id}`)
        return data
    } catch (err) {
        throw err;
    }
}


function escreverArquivo(nomeArquivo, conteudoArquivo) {
    nomeArquivo = nomeArquivo != undefined ? nomeArquivo : 'arquivo.json'
    conteudoArquivo = conteudoArquivo != undefined ? conteudoArquivo : 'arquivo.json'

    fs.writeFile(nomeArquivo, conteudoArquivo, 'utf-8', (err) => {
        if (err) throw err;
    });
}


async function main() {
    let listaPersonagens = undefined
    let fichaPersonagem = undefined

    try {
        listaPersonagens = await getListaPersonagem()
        fichaPersonagem = await getPersonagem(
            getNumeroAleatorioAteLimite(listaPersonagens.length)
        )

        escreverArquivo('ListaPersonagens.json', JSON.stringify(listaPersonagens, null, 2))
        escreverArquivo('FichaIndividual.json', JSON.stringify(fichaPersonagem, null, 2))
    } catch (error) {
        console.error(error)
    }
}
main()