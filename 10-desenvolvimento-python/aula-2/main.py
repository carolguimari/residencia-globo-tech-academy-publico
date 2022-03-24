from classes import User, Post, Comment
import os

post_dict = dict()
user_dict = dict()


def create_menu():
    print("\n" + "#" * 5 + " Rede Social Globo " + "#" * 5 + "\n")

    print("1- Adicionar usuário")
    print("2- Criar Post")
    print("3- Excluir Post")
    print("4- Comentar Post")
    print("5- Excluir Comentário")
    print("0- Sair")
    print("88- Listar Usuarios")
    print("99- Listar Posts")

    option = int(input("\nDigite a opção: "))

    match option:
        case 1:
            user_create()
            create_menu()

        case 2:
            post_create()
            create_menu()

        case 3:
            post_delete()
            create_menu()

        case 4:
            comment_create()
            create_menu()

        case 5:
            comment_delete()
            create_menu()

        case 88:
            user_list()
            create_menu()
        case 99:
            post_list()
            create_menu()

        case 0:
            exit()


def user_create():
    user_name = input("Digite seu nome: ")
    nickname = input("Digite seu nickname: ")
    user = User(user_name, nickname)
    user_dict[user.user_id] = user
    print(user)


def user_list():
    for user_id in user_dict:
        print(user_dict[user_id])


def post_create():
    user_id = int(input("Digite o id do usuário: "))
    if user_id in user_dict:
        message = input("Insira a mensagem do post [lim 144 chars]: ")
        new_post = Post(user_dict[user_id], message)
        post_dict[new_post.post_id] = new_post
        print("Post criado com sucesso. \nid:{} ".format(new_post.post_id))
    else:
        print("O usuário \nid:{} não foi localizado".format(user_id))


def post_list():
    for post_id in post_dict:
        print(post_dict[post_id])


def post_delete():
    post_id = int(input("Digite o id do Post que se deseja deletar: "))
    if post_id in user_dict:
        del post_dict[post_id]
        print('Post deletado com sucesso. \nid {}'.format(post_id))
    else:
        print("The post with id {} does not exist.".format(post_id))


def comment_create():
    user_id = int(input("Digite o id do autor do comentário: "))
    post_id = int(input("Digite o id do post a ser comentado: "))

    try:
        comment_author = user_dict[user_id]
        commented_post = post_dict[post_id]
    except KeyError:
        print("O usuário ou post {} não existe.")
    else:
        comment_txt = input(
            "Insira o novo comentario do post [lim 144 chars]: ")
        new_comment = Comment(comment_author, comment_txt)
        commented_post.add_comment(new_comment)


def comment_delete():
    comment_id = int(
        input("Digite o id do comentário que se deseja deletar: "))
    if comment_id in post_dict[comment_id].comments:
        print('Comentário deletado com sucesso. \nid {}'.format(comment_id))
    else:
        print("The post with id {} does not exist.".format(comment_id))


os.system("cls")
create_menu()