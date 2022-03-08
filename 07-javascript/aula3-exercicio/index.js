const express = require('express')

const { get_next_id } = require('./utils/getNextId');
const { get_with_full_name } = require('./utils/getWithFullName');

//const { aaa } = require('./controllers/players');
//const { bbb } = require('./controllers/teams');

const PORT = 3000

const app = express()
app.use(express.json())

const players = []
const teams = []

app.route('/players').post((req, res) => {
    const { body } = req
    
    nextId = get_next_id(players)
    players.push({
        id: nextId,
        ...body
    })

    res.status(201).setHeader('Location', `http://localhost:3000/players/${nextId}`).send()
}).get((_, res) => {
    res.json(get_with_full_name(players))
})

app.route('/players/:id').get((req, res) => {
    const { params } = req
    
    const player = players.find(player => player.id === +params.id)
    if(!player) {
        res.sendStatus(404)
        return;
    }

    res.json(get_with_full_name([player]))
    
}).put((req, res) => {
    const { params, body } = req
    
    const playerIndex = players.findIndex(player => player.id === +params.id)
    if (playerIndex < 0) {
        res.sendStatus(404)
        return;
    }

    players[playerIndex] = {
        id: +params.id,
        ...body
    }

    res.send()
}).delete((req, res) => {
    const { params } = req

    const playerIndex = players.findIndex(player => player.id === +params.id)
    if (playerIndex < 0) {
        res.sendStatus(404)
        return
    }

    players.slice(playerIndex, 1)
    res.send()
})

app.route('/teams').post((req, res) => {
    const { body } = req
    
    nextId = get_next_id(teams)
    teams.push({
        id: nextId,
        ...body
    })
    res.status(201).setHeader('Location', `http://localhost:3000/teams/${nextId}`).send()
}).get((_, res) => {
    res.json(teams)
})


app.route('/teams/:id').get((req, res) => {
    const { params } = req
    
    const lista = teams.find(team => team.id === +params.id)

    //const players = players.find(player => player.team === +params.id)

    if(!lista) {
        res.sendStatus(404)
        return;
    }

    res.json(
        lista
    )  
}).put((req, res) => {
    const { params, body } = req
    
    const teamIndex = teams.findIndex(team => team.id === +params.id)
    if (teamIndex < 0) {
        res.sendStatus(404)
        return;
    }

    teams[teamIndex] = {
        id: +params.id,
        ...body
    }

    res.send()
}).delete((req, res) => {
    const { params } = req

    const teamIndex = teams.findIndex(team => team.id === +params.id)
    if (teamIndex < 0) {
        res.sendStatus(404)
        return
    }

    players.slice(teamIndex, 1)
    res.send()
})


app.listen(PORT, () => {
    console.log(`Servidor iniciou na porta ${PORT}`)
})
