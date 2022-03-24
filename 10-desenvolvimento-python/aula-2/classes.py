from datetime import datetime
import itertools


class User:
    id_iter = itertools.count()

    def __init__(self, name: str, alias: str) -> None:
        self.__user_id = next(self.id_iter)
        self.__name = name
        self.__alias = alias

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def name(self) -> int:
        return self.__name

    @property
    def alias(self) -> int:
        return self.__alias

    @name.setter
    def name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("NAN")
        else:
            self.__name = value

    @alias.setter
    def alias(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("NAN")
        else:
            self.__alias = value

    def __str__(self):
        return "({}) {} / {}".format(self.user_id, self.name, self.alias)


class Post:
    id_iter = itertools.count()

    def __init__(self, user: User, message="") -> None:
        self.__post_id = next(self.id_iter)
        self.__user = user
        self.__message = elipsize_long_text(message)
        self.__datetime = datetime.now()
        self.__comments = []

    @ property
    def post_id(self) -> int:
        return self.__post_id

    @ property
    def user(self) -> User:
        return self.__user

    @ property
    def message(self) -> str:
        return self.__message

    @ property
    def datetime(self) -> str:
        return self.__datetime

    @ property
    def comments(self):
        return self.__comments

    @ user.setter
    def user(self, value: User) -> None:
        if not isinstance(value, User):
            raise TypeError("NAN")
        else:
            self.__user = value

    @ message.setter
    def message(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("NAN")
        else:
            self.__message = value

    def add_comment(self, comment) -> None:
        self.comments.append(comment)

    def __str__(self):
        str_return = "({}) {} \nUsuário: {} \nPost: {}".format(self.post_id, self.datetime,
                                                               self.user.name, self.message)
        for comment in self.__comments:
            str_return += "\n-> ({}) {} \n{}\n".format(comment.comment_id, comment.datetime,
                                                       comment.text).rjust(10)
        return str_return


class Comment:
    id_iter = itertools.count()

    def __init__(self, user: User, text: str) -> None:
        self.__comment_id = next(self.id_iter)
        self.__user = user
        self.__text = elipsize_long_text(text)
        self.__datetime = datetime.now()

    @ property
    def comment_id(self) -> int:
        return self.__comment_id

    @ property
    def user(self) -> User:
        return self.__user

    @ property
    def text(self) -> str:
        return self.__text

    @ property
    def datetime(self) -> str:
        return self.__datetime

    @ user.setter
    def user(self, value: User) -> None:
        self.__user = value

    @ text.setter
    def text(self, value: str) -> None:
        self.text = value

    def __str__(self):
        return "{}: Comentário:{} - Data:{}".format(self.comment_id, self.text, self.datetime)


def elipsize_long_text(text):
    if len(text) > 144:
        text = text[:144] + "..."
    return text
