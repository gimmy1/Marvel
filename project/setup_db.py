COMMANDS = (
    """
    DROP TABLE IF EXISTS character_comic
    """,
    """
    DROP TABLE IF EXISTS comics
    """,
    """
    DROP TABLE IF EXISTS characters
    """,
    """
    CREATE TABLE characters (
        character_id INTEGER NOT NULL,
        character_name VARCHAR(255) NOT NULL,
        character_description TEXT
         DEFAULT NULL,
        character_image_url VARCHAR(255) DEFAULT NULL,
        PRIMARY KEY(character_id),
        UNIQUE(character_id)
    )
    """,
    """
    CREATE TABLE comics (
        comic_id VARCHAR(255) NOT NULL,
        comic_title VARCHAR(100) DEFAULT NULL,
        PRIMARY KEY(comic_id),
        UNIQUE(comic_id)
    )
    """,
    """ CREATE TABLE character_comic (
            character_id INTEGER REFERENCES characters(character_id) ON UPDATE CASCADE ON DELETE CASCADE,
            comic_id VARCHAR REFERENCES comics(comic_id) ON UPDATE CASCADE,
            CONSTRAINT character_comic_pkey PRIMARY KEY (character_id, comic_id)
    )
    """
)
