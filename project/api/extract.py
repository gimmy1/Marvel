import pdb
from .request import (MarvelComicBookAPI,
                      MarvelRequest)

def extract_from_comics(comic_ids, request_api, comic_book_api):
    characters = set()
    character_comics = set()
    for comic_id in comic_ids:
        data = comic_book_api(request_api,
                              id=comic_id).parse_data()
        values = get_character_values(data["comic_characters"])
        characters.update(values)
        character_comics.update(
            extract_character_comic(comic_id, data["comic_characters"]))
    return characters, character_comics

def extract_comics(comic_ids):
    comics = set()
    for comic_id in comic_ids:
        comics.update([(comic_id, "")])
    return comics

def extract_character_comic(comic_id, characters):
    character_comics = set()
    for character in characters:
        character_comics.update([(character["character_id"],
                                  comic_id)])
    return character_comics

def get_character_values(characters):
    return [(character["character_id"],
            character["character_name"],
            character["character_description"],
            character["character_image_url"])
            for character in characters]