import pdb
import simplejson

from collections import defaultdict
from flask import Blueprint, request, jsonify
from flask_restx import Resource, Api

from .pgclient import PGClient
from .models import (CharacterInfo,
                     ComicBook,
                     MarvelCharacter)
from .serialize import serialize_comics


comics_blueprint = Blueprint('comics', __name__)
api = Api(comics_blueprint)

class ComicsList(Resource):
    def get(self):
        pass

api.add_resource(ComicsList, '/comics')