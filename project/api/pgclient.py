import pdb
import logging
import psycopg2
from psycopg2.extras import execute_values
from project.config import DevelopmentConfig

class PGClient:
    def __init__(self):
        try:
            params = DevelopmentConfig.DATABASE
            self.connection = psycopg2.connect(**params)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except (Exception, psycopg2.OperationalError) as exc:
            logging.exception(f"Cannot connect to the DB: {exc}")
            raise psycopg2.OperationalError("Operational error")
        
    def close(self):
        self.cursor.close()
        self.connection.close()
    
    def check_status(self):
        try:
            query = """Select True"""
            self.cursor.execute(query)
            return True
        except (Exception, psycopg2.OperationalError) as exc:
            logging.exception(f"Unsuccessful execution: {exc}")
            raise psycopg2.OperationalError("Operational error")
        
    def execute(self, query):
        try:
            self.cursor.execute(query)
            return True
        except (Exception, psycopg2.OperationalError) as exc:
            logging.exception(f"Unsuccessful execution: {exc}")
            raise psycopg2.OperationalError("Operational error")
    
    def add_comics(self, values):
        try:
            query = """ INSERT INTO comics(comic_id, comic_title)
                        VALUES %s
                    """
            execute_values(
                self.cursor,
                query,
                values)
            return True
        except psycopg2.OperationalError as pe:
            logging.exception(f"Operational Error occurred: {pe}")
            raise psycopg2.OperationalError("Operational error")
    
    def add_characters(self, values):
        try:
            query = """ INSERT INTO characters(character_id,
                                               character_name,
                                               character_description,
                                               character_image_url)
                        VALUES %s
                    """
            
            execute_values(
                self.cursor,
                query,
                values)
            return True
        except psycopg2.OperationalError as pe:
            logging.exception(f"Operational Error occurred: {pe}")
            raise psycopg2.OperationalError("Operational error")
        
    def add_character_comics(self, values):
        try:
            query = """ INSERT INTO character_comic(character_id, comic_id)
                        VALUES %s
                    """
            
            execute_values(
                self.cursor,
                query,
                values)
            return True
        except psycopg2.OperationalError as pe:
            logging.exception(f"Operational Error occurred: {pe}")
            raise psycopg2.OperationalError("Operational error")
        
    def get_all_characters(self):
        try:
            query = """SELECT * FROM characters"""
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except psycopg2.OperationalError as pe:
            logging.exception(f"Operational Error occurred: {pe}")
            raise psycopg2.OperationalError("Operational error")
        
    def get_all_character_comics(self):
        try:
            query = """ SELECT c.character_id,
                               c.character_name,
                               co.comic_id
                        FROM characters c
                        JOIN character_comic cc ON cc.character_id = c.character_id
                        JOIN comics co ON cc.comic_id = co.comic_id
                    """
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except psycopg2.OperationalError as pe:
            logging.exception(f"Operational Error occurred: {pe}")
            raise psycopg2.OperationalError("Operational error")
    
    def get_character(self, name):
        try:
            query = """ SELECT c.character_name
                        FROM characters c
                        WHERE c.character_name = %s
                    """
            self.cursor.execute(query, (name,))
            result = self.cursor.fetchone()
            if result:
                return result[0]
            return []
        except psycopg2.OperationalError as pe:
            logging.exception(f"Operational Error occurred: {pe}")
            raise psycopg2.OperationalError("Operational error")
        
    def get_characters_associated(self, name):
        pass
