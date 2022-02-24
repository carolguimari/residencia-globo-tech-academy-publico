const axios = require('axios')
const fs = require('fs')
const response = axios.default.get('https://rickandmortyapi.com/api/character')

/*const apiService = axios.create({
    baseURL: 'https://rickandmortyapi.com/api/character'
});*/

response.then(response => {
    console.log(response.data)
    let data = JSON.stringify(response.data.results[0], null, 2);
    fs.writeFile('ListaPersonagens.json', data, 'utf-8', (err) => {
        if (err) throw err;
        console.log('Data written to file');
    });
}).catch(err => {
    console.log('err')
}).finally(() => {
    console.log('acabou sendo sucesso ou erro')
})




const response2 = axios.default.get('https://rickandmortyapi.com/api/character/?name=ick%20Sanchez&status=alive')

response2.then(response => {
    console.log(response.data.results[0])
    let data = JSON.stringify(response.data, null, 2);
    fs.writeFile('FichaIndividual.json', data, 'utf-8', (err) => {
        if (err) throw err;
        console.log('Data written to file');
    });
}).catch(err => {
    console.log('err')
}).finally(() => {
    console.log('acabou sendo sucesso ou erro')
})