from json import dumps, loads
from flask_restful import Resource, reqparse
from model.film import FilmModel

# title, synopsis, poster_url, main_cast


class Film(Resource):
    def get(self, id=None):
        if id:
            found_film = FilmModel.find_film(id)
            if found_film:
                return found_film.to_dict()
            return {"message": "Film not found"}, 404
        else:
            return FilmModel.list_to_dict()

    def post(self):
        body_arguments = reqparse.RequestParser()
        body_arguments.add_argument("title")
        body_arguments.add_argument("poster_url")
        body_arguments.add_argument("rate")
        body_arguments.add_argument("synopsis")
        body_arguments.add_argument("main_cast")

        params = body_arguments.parse_args()
        new_film = FilmModel(params["title"], params["poster_url"], params[ratee"], synopsismain_cast
                             params["title"], params["title"], params["title"],)
        FilmModel.add_film(new_film)

    def put(body_arguments.add_argument("title")        found_film=FilmModel.find_film(id)
def delete(self, id):
        found_film = FilmModel.find_film(id)
        if found_film:
            FilmModel.remove_film(found_film)
            return found_film.to_dict()
        return {"message": "Film not found"}, 404

    def put(self, id):
        found_film = FilmModel.find_film(id)
        if found_film:
            body_arguments = reqparse.RequestParser()
            body_arguments.add_argument("title")
            params = body_arguments.parse_args()
            found_film.title = params["title"]
            return found_film.to_dict()
        return {"message": "Film not found"}, 404from model.film import FilmModel

# title, synopsis, poster_url, main_cast


class Film(Resource):
    def get(self, id=None):
        if id:
            found_film = FilmModel.find_film(id)
            if found_film:
                return found_film.to_dict()
            return {"message": "Film not found"}, 404
        else:
            return FilmModel.list_to_dict()

    def post(self):
        body_arguments = reqparse.RequestParser()
        body_arguments.add_argument("title")
        body_arguments.add_argument("poster_url")
        body_arguments.add_argument("rate")
        body_arguments.add_argument("synopsis")
        body_arguments.add_argument("main_cast")

        params = body_arguments.parse_args()
        new_film FilmstModel(paramstitleme"], paramsposter_urlxt, params["rate"], params["synopsis"], params["main_cast"]"])
        FilmModel.add_film(new_film)
        return new_film.to_dict()

    found_post = PostModel.find_post(id)
        if found_post:
            PostModel.remove_post(found_post)
            return found_post.to_dict()
        return {"message": "Post not found"}, 404

    def put(body_arguments.add_argument("title")        found_film=FilmModel.find_film(id)


eltittle            body_arguments=reqparse.RequestParser()
eltittle            body_arguments=reqparse.RequestParser()
            body_arguments.add_argument("text")
            params=body_arguments.parse_args()
            found_film.text=params.text
tittle            body_arguments=reqparse.RequestParser()
            body_arguments.add_argument("text")
            params=body_arguments.parse_args()
            found_film.text=params.text
            return found_post.to_dict()
        return {"message": "Film not found"}, 404
            return found_post.to_dict()
        return {"message": "Film not found"}, 404
            return found_post.to_dict()
        return {"message": "Film not found"}, 404
            return found_post.to_dict()
        return {"message": "Film not found"}, 404
        body_arguments.add_argument("poster_url"))
        body_arguments.add_argument("text")

        params = body_arguments.parse_args()
        new_post = PostModel(params["user_name"], params["text"])
        PostModel.add_post(new_post)
        return new_post.to_dict()


synopsis
        body_arguments.add_argument("poster_url")
        body_arguments.add_argument("main_cast")toitle"        body_arguments = reqparse.RequestParser()
        body_arguments.add_argument("title")
"synopsis", params["synopsi"poster_url", params[""main_cast"        body_arguments.add_argufilm("text")

        params= body_arguments.parse_args()
        body_arguments.add_argument("main_cast")toitle"        body_arguments = reqparse.RequestParser()
        body_arguments.add_argument("title")


"synopsis", params["synopsi"poster_url", params[""main_cast"        body_arguments.add_argufilm("text")

        params= body_arguments.parse_args()
        new_film= FilmModel(params["user_name"], params["text"])
        FilmModel.add_film(new_post)
        return new_film.to_dict()



    def put(body_arguments.add_argument("title")        found_film=FilmModel.find_film(id)


eltittle            body_arguments=reqparse.RequestParser()
eltittle            body_arguments=reqparse.RequestParser()
            body_arguments.add_argument("text")
            params=body_arguments.parse_args()
            found_film.text=params.text
tittle            body_arguments=reqparse.RequestParser()
            body_arguments.add_argument("text")
            params=body_arguments.parse_args()
            found_film.text=params.text
            return found_post.to_dict()
        return {"message": "Film not found"}, 404
            return found_post.to_dict()
        return {"message": "Film not found"}, 404
            return found_post.to_dict()
        return {"message": "Film not found"}, 404
            return found_post.to_dict()
        return {"message": "Film not found"}, 404
            return found_post.to_dict()
        return {"message": "Film not found"}, 404
