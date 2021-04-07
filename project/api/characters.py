import pdb
import simplejson
from flask import Blueprint, request
from flask_restx import Resource, Api

from .pgclient import PGClient
from .models import CharacterInfo, MarvelCharacter

from .serialize import serialize_characters, serialize_comics

characters_blueprint = Blueprint('characters', __name__)
api = Api(characters_blueprint)


class CharactersList(Resource):
    def get(self):
        response_object = {
            "status": "fail"
        }
        try:
            dbclient = PGClient()
            dbclient.check_status()
        except Exception:
            dbclient.close()
            response_object["message"] = "DB connectivity"
            return response_object, 500
            
        try:
            characters = dbclient.get_all_characters()
            dbclient.close()
        except Exception:
            response_object["message"] = "DB connectivity"
            return response_object, 500
        
        if not characters:
            response_object["status"] = "succes"
            response_object["data"] = []
            return response_object, 200
        data = serialize_characters(characters)
        response_object["status"] = "succes"
        response_object["data"] = data
        return response_object, 201

class Characters(Resource):
    def get(self, character_name):
        response_object = {
            "status": "fail"
        }
        try:
            dbclient = PGClient()
            dbclient.check_status()
        except Exception:
            dbclient.close()
            response_object["message"] = "DB connectivity"
            return response_object, 500
            
        try:
            character = dbclient.get_character(character_name.capitalize())
            dbclient.close()
        except Exception:
            response_object["message"] = "DB connectivity"
            return response_object, 500
        
        if not character:
            response_object["status"] = "succes"
            response_object["data"] = []
            return response_object, 200
        
        response_object["status"] = "succes"
        response_object["data"] = character
        return response_object, 201

class CharactersAssociation(Resource):
    def get(self, character_name):
        response_object = {
            "status": "fail"
        }
        if character_name != "Spectrum".lower():
            response_object["message"] = "Please enter a valid name"
            return response_object, 200
        try:
            dbclient = PGClient()
            dbclient.check_status()
        except Exception:
            dbclient.close()
            response_object["message"] = "DB connectivity"
            return response_object, 500
        
        try:
            character_comics = dbclient.get_all_character_comics()
            dbclient.close()
        except Exception:
            response_object["message"] = "DB connectivity"
            return response_object, 500
        if not character_comics:
            response_object["status"] = "succes"
            response_object["data"] = []
            return response_object, 200
        
        characters = serialize_comics(character_comics, character_name)
        response_object["status"] = "succes"
        response_object["data"] = characters
        return response_object, 201

api.add_resource(CharactersList, '/characters')
api.add_resource(Characters, '/characters/<string:character_name>')
api.add_resource(CharactersAssociation, '/characters/<string:character_name>/associated')