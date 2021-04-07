import pdb
import sys
import time

from flask.cli import FlaskGroup

from project import create_app

from project.api.pgclient import PGClient

from project.setup_db import COMMANDS

from project.api.extract import extract_from_comics, extract_comics
from project.api.request import (MarvelCharacterAPI,
                                 MarvelComicBookAPI,
                                 MarvelRequest)

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command("check_status")
def check_status():
    dbclient = PGClient()
    success = dbclient.check_status()
    dbclient.close()
    if success:
        print("Success")
    else:
        print("Unsuccessful")


@cli.command("recreate_db")
def recreate_db():
    dbclient = PGClient()
    for command in COMMANDS:
        dbclient.execute(command)
    dbclient.close()
    print("Recreated DB")
        
@cli.command("seed_db")
def seed_db():
    start = time.time()
    api_request = MarvelRequest()
    character = MarvelCharacterAPI(
                api_request,
                name="Spectrum")
    character_data = character.parse_data()
    characters, character_comics = extract_from_comics(
        character_data["associated_comic_urls"],
        api_request,
        MarvelComicBookAPI
    )
    comics = extract_comics(character_data["associated_comic_urls"])
    
    dbclient = PGClient()
    dbclient.add_characters(characters)
    dbclient.add_comics(comics)
    dbclient.add_character_comics(character_comics)
    dbclient.close()
    
    print(time.time() - start)
    print("DB Seeded")

if __name__ == '__main__':
    cli()