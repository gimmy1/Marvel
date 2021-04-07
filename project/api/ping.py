from flask import Blueprint
from flask_restx import Resource, Api

from .extract import extract_from_comics, extract_comics
from .request import (MarvelCharacterAPI,
                      MarvelComicBookAPI,
                      MarvelRequest)

from .pgclient import PGClient

ping_blueprint = Blueprint('ping', __name__)
api = Api(ping_blueprint)


class Ping(Resource):
    def get(self):
        return {
                "message": "pong",
                "status": "success"
            }, 200

api.add_resource(Ping, '/ping')