from typing import List

class CharacterInfo:
    name: str
    description: str
    picture: str

    def __init__(self, name, description, picture):
        self.name = name
        self.description = description
        self.picture = picture
        # Create an empty initial collection of characters worked with
        self.characters_worked_with = set()
    
    @property
    def character_description(self):
        """Return a representation of the full name of this Marvel Character and a description"""
        return f"{self.name}: {self.description}"
    
    def serialize(self):
        return {
            "name": self.name,
            "description": self.description,
            "picture": self.picture
        }

class MarvelCharacter:
    """
    A MarvelCharacter
    """
    _id: int
    info: CharacterInfo
    def __init__(self, _id, info):
        """
        Create a new `MarvelCharacter`
        """
        self._id = _id
        self.info = info

    def __str__(self):
        """Return `str(self)`."""
        return f"An MarvelCharacter encapsulates semantic and visual parameters about the object, such \
                 as its name, picture, and description."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (
            f"MarvelCharacter(id={self._id!r}, name={self.info.name!r}, "
            f"picture={self.info.picture!r}, description={self.info.description!r})"
        )

    def serialize(self):
        return {
            "id": self._id,
            "info": self.info.serialize(),
        }

class ComicBook:
    """A close approach to Earth by an NEO.
    A `ComicBook` encapsulates information about the id, title, and characters who appear in the comic book.
    A `ComicBook` maintains a reference to its `MarvelCharacter`
    """
    name: str
    description: str
    picture: str
    
    def __init__(self, _id, title="", marvel_characters=[]):
        """
        Create a new `ComicBook`
        """
        self._id = _id
        self.title = title
        self.marvel_characters = marvel_characters

    @property
    def format_characters(self):
        """ Return a formatted representation of this `ComicBook` characters."""
        
        return ", ".join(character["name"] for character in self.marvel_characters["info"])
    
    def __str__(self):
        """Return `str(self)`."""
        return f"In ComicBook: {self._id}, {self.format_characters} appear"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (
            f"ComicBook(id={self._id}, title={self.title:}, "
        )

    def serialize(self):
        return {
            "id": self._id,
            "title": self.title,
            "marvel_characters": [character["info"]["name"] for character in self.marvel_characters],
        }
    