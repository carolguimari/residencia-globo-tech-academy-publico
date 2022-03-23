####


###

from array import array
from datetime import datetime

post_dict = dict()
user_dict = dict()

class User:

    ids = []

    def __init__(self, user_id: int, name: str, alias: str) -> None:
        self.user_id = user_id  # criar dinamicamente
        self.name = name
        self.alias = alias

    @property
    def get_id(self) -> int:
        return self.user_id

    @id.setter
    def id(self, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("NAN")
        else:
            self.user_id = value

    @property
    def get_name(self) -> int:
        return self.name

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("NAN")
        else:
            self.name = value

    @property
    def get_alias(self) -> int:
        return self.alias

    @alias.setter
    def alias(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("NAN")
        else:
            self.alias = value


####


class Post:

    ids = []

    def __init__(self, post_id: int, user: User, message="", comments=[]) -> None:
        self.post_id = post_id  # criar dinamicamente
        self.user = user
        self.message = elipsize_long_text(message)
        self.datetime = datetime.now()
        self.comments = comments

    def add_comment(self, comment) -> None:
        self.comments.append(comment)


####


class Comment:

    ids = []

    def __init__(self, cmt_id: int, user: User, text: str) -> None:
        self.__cmt_id = cmt_id  # criar dinamicamente
        self.__user = user
        self.__text = elipsize_long_text(text)
        self.__date = datetime.now()

    ####
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value: int) -> None:
        self.__id = value

    ####
    @property
    def user(self) -> int:
        return self.__user

    @user.setter
    def user(self, value: int) -> None:
        self.__user = value

    ####
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, value: str) -> None:
        self.text = value

    ####
    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self) -> None:
        self.__date = datetime.now()


def elipsize_long_text(text):
    if len(text) > 144:
        text = text[:144] + "..."
    return text


##MENU
def menu():

    print("#" * 5 + " Rede Social Globo " + "#" * 5)

    print("1- Adicionar usuário")
    print("2- Criar Post")
    print("3- Excluir Post")
    print("4- Comentar Post")
    print("5- Excluir Comentário")
    print("0- Sair")

    option = int(input("Digite a opção: "))
    match option:

        case 1:
            # chamar adicionar usuário
            user_name = input("Digite seu nome: ")
            nickname = input("Digite seu nickname: ")
            user = User(user_name, nickname)
            user_dict[user_id] = user
            print("User {} criado. \nid:{} ".format(user.name, user.user_id))
            menu()
        case 2:
            # chamar criar post
            user_id = int(input("Digite o id do usuário: "))
            message = input("Insira a mensagem do post [lim 144 chars]: ")
            new_post = Post(user_dict[user_id], message)
            post_dict[new_post.post_id] = new_post
            print("Post criado com sucesso. \nid:{} ".format(new_post.post_id))
            menu()
        case 3:
            # chamar excluir post
            post_id = int(input("Digite o id do Post que se deseja deletar: "))
            try:
                del post_dict[post_id]
                print('Post deletado com sucesso. \nid {}'.format(post_id))
            except KeyError as e:
                print(e)
                print("The post with id {} does not exist.".format(post_id))
            menu()
        case 4:
            # chamar comentar post
            user_id = int(input("Digite o id do autor do comentário: "))
            post_id = int(input("Digite o id do post a ser comentado: "))
            try:
                comment_author = user_dict[user_id]
                commented_post = post_dict[post_id]
            except KeyError:
                print("O usuário ou post {} não existe.")
            else:
                comment_txt = input("Insira o novo comentario do post [lim 144 chars]: ")
                new_comment = Comment(comment_author, comment_txt)
                commented_post.add_comment(new_comment)
            menu()
        case 5:

            # chmar excluir comentario
            menu()
        case 0:
            exit()


## EXECUÇÃO
post = []

## FIRST PUBLICATION
user1 = User(1, "User Author 1", "UA1")
post1 = Post(1, user1.id, "text-do-post")

user2 = User(2, "User Comment 2", "UC2")
comment1 = Comment(1, user2.id, "text-do-comentario")
comment2 = Comment(2, user2.id, "text-do-comentario")
post1.add_comment(comment1)
post1.add_comment(comment2)

## SECOND PUBLICATION
user3 = User(3, "User Author 3", "UA3")
post2 = Post(2, user3.id, "text-do-post")

user4 = User(4, "User Comment 4", "UC4")
comment3 = Comment(3, user4.id, "text-do-comentario")
comment4 = Comment(4, user4.id, "text-do-comentario")
post2.add_comment(comment3)
post2.add_comment(comment4)
