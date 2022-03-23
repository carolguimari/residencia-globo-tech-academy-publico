from util import *
import os
import sys

# sys.path.append(os.path.join('D:\\', 'git', 'python', 'Parte2', 'libs'))
sys.path.insert(1, "../libs")

os.system("cls")

# phrase = input('Entre com a frase:')
phrase = "Essa é a primeira aula de python "

print("-> " + get_piece_of_word(phrase))
print("-> " + get_piece_of_word(phrase, pos_end=2))
print("-> " + get_piece_of_word(phrase, pos_start=2))

# ##########

# def get_piece_of_word(text, pos_start=None, pos_end=None):
#     words = text.split('')

#     a_txt = []
#     for word in words:
#         aux = (word[pos_start:pos_end])
#         if aux:
#             a_txt.append(aux)

#     txt = " ".join(a_txt)
#     return txt

# ##########
# INICIO - ESSE ERA O JEITO INICIAL


# print('-'*10)
# for word in words:
#     print(word[:2], end=' ')

# print('\n' + '-'*10)
# for word in words:
#     print(word[2:], end=' ')

# print('\n' + '-'*10)

# INICIO - ESSE ERA O JEITO INICIAL

# ##########

# Usem o chat povo =D =D =D kkk XD

# coloca um __init__.py na raiz do util. Sem ser classe ?
# isso... mas tem que colocar um negocio dentro do arquivo... to caçando aki nos meus arquivos....
# OK colocar o init pra fazer o que miguel?  Está caçando isso pra fazer o que não entendi
# https://careerkarma.com/blog/what-is-init-py/
# https://stackoverflow.com/questions/448271/what-is-init-py-for

# já vou olhar
# Python defines two types of packages, regular packages and namespace packages.

# assim vai só achei dessa forma, mas tem outra lib de path que daria pra dizer o caminho da pasta tbm. Tem ai ?
# vou buscar, já usei ele quando tava com pandas. Esse que passei ai pega pasta em qualquer caminho. Tendi >> https://docs.python.org/3/library/pathlib.html

# vou olhar

# pronto tenta ok no caminho
# from teste.my_functions import get_piece_of_word pronto vou jogar um teste ai
# blz

# https://csatlas.com/python-import-file-module/ <- olha esse site vou simular importar de outra pasta no meu = OK!

# sys.path.append('../util/util')
# salva e tenta mais uma
# foi não por algum motivo ele pega a pasta pra rodar, mas acha ela e a função
# se fosse para dentro da pasta ele ira de boa pelo q vi aqui
# testar outro

# Traceback (most recent call last):
#   File "C:\Users\igorm\OneDrive\Área de Trabalho\python\atividade_3\main.py", line 3, in <module>
#     from util.util import get_piece_of_word  # tenta ok
# ModuleNotFoundError: No module named 'util'

############################


############################
# 1º RESOLUÇÃO
# sentence = input('Entre com a frase:')

# words = sentence.split(' ')

# print('-'*10)
# for word in words:
#     print(word[:2], end=' ')

# print('\n' + '-'*10)
# for word in words:
#     print(word[2:], end=' ')
