const get_next_id = (lista) => {
    const nextId = lista[lista.length - 1]?.id + 1 || 1;
    return nextId
}
  
module.exports = { get_next_id };
  