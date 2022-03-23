from random import randint


def get_piece_of_word(text, pos_start=None, pos_end=None):
    words = text.split(" ")

    a_txt = []
    for word in words:
        aux = word[pos_start:pos_end]
        if aux:
            a_txt.append(aux)

    txt = " ".join(a_txt)
    return txt


def generate_registration(ids) -> int:
    randId = randint(0, 99999)
    while randId in ids:
        randId = randint(0, 99999)
    return randId
