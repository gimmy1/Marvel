import os
from flask import Flask, jsonify

def create_app(script_info=None):
    # instantiate app
    app = Flask(__name__)
    
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    from project.api.ping import ping_blueprint
    app.register_blueprint(ping_blueprint)
    
    from project.api.characters import characters_blueprint
    app.register_blueprint(characters_blueprint)
    
    from project.api.comics import comics_blueprint
    app.register_blueprint(comics_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app}

    return app



