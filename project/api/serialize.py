import pdb
from collections import defaultdict

from .models import CharacterInfo, MarvelCharacter

def serialize_characters(characters):
    data = []
    for character in characters:
        data.append(
            MarvelCharacter(
                character[0],
                CharacterInfo(
                    character[1],
                    character[2],
                    character[3]
                )
            ).serialize()
        )
    return data

def serialize_comics(character_comics, name):
    characters = set()
    for cc in character_comics:
        if cc[1] != name:
            characters.add(cc[1])
    
    return list(characters)
    