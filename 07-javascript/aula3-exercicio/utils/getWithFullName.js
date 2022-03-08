const get_with_full_name = (lista) => {
    const full_list = lista.map(player => {
        full_name = `${player.first_name} ${player.nick_name} ${player.last_name}`
        return {
            full_name,
            ...player
        }
    })
    return full_list
}

module.exports = { get_with_full_name };