from flask_restful import Resource, reqparse
from model.serie import SerieModel


class Serie(Resource):
    def get(self, id=None):
        if id:
            found_serie = SerieModel.find_serie(id)
            if found_serie:
                return found_serie.to_dict()
            return {"message": "Serie not found"}, 404
        else:
            return SerieModel.list_to_dict()

    def post(self):
        body_arguments = reqparse.RequestParse()
        body_arguments.add_argument("title")
        body_arguments.add_argument("poster_url")
        body_arguments.add_argument("rate")
        body_arguments.add_argument("synopsis")
        body_arguments.add_argument("main_cast")

        params = body_arguments.parse_args()
        new_serie = SerieModel(
            params["title"],
            params["poster_url"],
            params["rate"],
            params["synopsis"],
            params["comments"],
        )
        SerieModel.add_serie(new_serie)
        return new_serie.to_dict()

    def delete(self, id):
        found_serie = SerieModel.find_serie(id)
        if found_serie:
            SerieModel.remove_serie(found_serie)
            return found_serie.to_dict()
        return {"message": "Serie not found"}, 404

    def put(self, id):
        found_serie = SerieModel.find_serie(id)
        if found_serie:
            body_arguments = reqparse.RequestParse()
            body_arguments.add_argument()
