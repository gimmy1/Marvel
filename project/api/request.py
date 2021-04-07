import hashlib
import requests

from abc import ABC, abstractmethod, abstractstaticmethod
from datetime import datetime
from project.api.models import ComicBook, MarvelCharacter
from typing import Any, Optional

from project.api.constant import (ENCODING,
                                  MARVEL_API_PUBLIC_KEY,
                                  MARVEL_API_PRIVATE_KEY,
                                  MARVEL_BASE_URL)

class RequestAPI(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractstaticmethod
    def generate_time():
        pass


class MarvelRequest(RequestAPI):
    # create connection requests url
    def __init__(self):
        self._public_key = MARVEL_API_PUBLIC_KEY
        self.__private_key = MARVEL_API_PRIVATE_KEY
        self.time = self.generate_time
        self._digest = self.digest()
        self._base_url = MARVEL_BASE_URL

    def digest(self):
        if not self.__private_key:
            raise TypeError("Invalid Private Key")
        
        return hashlib.md5(f"{self.time}{self.__private_key}{self._public_key}".encode(ENCODING)).hexdigest()
    
    @property
    def generate_time(self):
        return datetime.now().strftime("%Y%d%m%H%M%S")
        


class API(ABC):
    """
    Handler interface declares method for building chain of handlers.
    Declares method for executing request
    """
    @abstractmethod
    def __init__(self, field, request_api: RequestAPI, model, **kwargs):
        pass
    
    def retrieve_data(self, url):
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()["data"]["results"]
        
        raise Exception("Please check the MarvelAPI and it's credentials")
    
    @abstractmethod
    def parse_data(self):
        pass

class MarvelCharacterAPI(API):
    # create api request url
    def __init__(self, request_api: RequestAPI, **kwargs):
        self.field = kwargs.get("name", "Spectrum")
        self.ts = request_api.time
        self.__url = self.set_url(request_api._base_url,
                                  self.field,
                                  request_api._public_key,
                                  request_api._digest
                                  )
    
    @property
    def url(self):
        return self.__url
    
    def set_url(self, base_url, field, public_key, digest):
        return f"{base_url}/characters?name={field}&ts={self.ts}&apikey={public_key}&hash={digest}"


    def parse_data(self):
        data = self.retrieve_data(self.__url)
        for character in data:
            return {
                "character_id": character["id"],
                "character_name": character["name"],
                "character_description": character["description"],
                "character_image_url": f"{character['thumbnail']['path']}{character.get('thumbnail').get('extension')}",
                "associated_comic_urls": self.get_comic_urls(character["comics"]["items"])
            }
    
    def get_comic_urls(self, comic_ids):
        return [comic_id["resourceURI"].split("/")[-1] for comic_id in comic_ids]

class MarvelComicBookAPI(API):
    def __init__(self, request_api: RequestAPI, **kwargs):
        self.field = kwargs.get("id", 1)
        self.title = kwargs.get("title", "")
        self.ts = request_api.time
        self.__url = self.set_url(request_api._base_url,
                                  self.field,
                                  request_api._public_key,
                                  request_api._digest,
                                 )

    @property
    def url(self):
        return self.__url

    def set_url(self, base_url, field, public_key, digest):
        return f"{base_url}/comics/{field}/characters?apikey={public_key}&ts={self.ts}&hash={digest}"
    
    def parse_data(self):
        data = self.retrieve_data(self.__url)
        return {
            "comic_id": self.field,
            "comic_title": self.title,
            "comic_characters": self.get_characters(data)
        }

    def get_characters(self, characters):
        return [{
                "character_id": character["id"],
                "character_name": character["name"],
                "character_description": character["description"],
                "character_image_url": f"{character['thumbnail']['path']}{character['thumbnail']['extension']}"
                } for character in characters]