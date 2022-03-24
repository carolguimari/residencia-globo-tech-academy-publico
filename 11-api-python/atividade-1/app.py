from flask import Flask
from flask_restful import Api
from resources.film import Film
from resources.serie import Serie

app = Flask(__name__)
api = Api(app)

api.add_resource(
    Film,
    "/films",
    "/films/<int:id>"
    "/films/author/<str:author>",
    "/films/titulo/<str:author>"
)

api.add_resource(
    Serie,
    "/series",
    "/series/<int:id>"
    "/series/author/<str:author>",
    "/series/titulo/<str:author>"
)

if __name__ == '__main__':
    app.run(debug=True)
