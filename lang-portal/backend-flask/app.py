from flask import Flask, g
from flask_cors import CORS

from lib.db import Db  # No circular import issue now

import routes.words
import routes.groups
import routes.study_sessions
import routes.dashboard
import routes.study_activities

def get_allowed_origins(app):
    try:
        cursor = app.db.cursor()
        cursor.execute('SELECT url FROM study_activities')
        urls = cursor.fetchall()
        # Convert URLs to origins (e.g., https://example.com/app -> https://example.com)
        origins = set()
        for url in urls:
            try:
                from urllib.parse import urlparse
                parsed = urlparse(url['url'])
                origin = f"{parsed.scheme}://{parsed.netloc}"
                origins.add(origin)
            except:
                continue
        return list(origins) if origins else ["*"]
    except:
        return ["*"]  # Fallback to allow all origins if there's an error

def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        app.config.from_mapping(
            DATABASE='words.db'
        )
    else:
        app.config.update(test_config)

    # Initialize database after app is created
    app.db = Db(database=app.config['DATABASE'])

    # Get allowed origins from study_activities table
    allowed_origins = get_allowed_origins(app)

    # In development, add localhost to allowed origins
    if app.debug:
        allowed_origins.extend(["http://localhost:8080", "http://127.0.0.1:8080"])

    # Configure CORS with combined origins
    CORS(app, resources={
        r"/*": {
            "origins": allowed_origins,
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })

    # Close database connection
    @app.teardown_appcontext
    def close_db(exception):
        app.db.close()

    # Load routes -----------
    routes.words.load(app)
    routes.groups.load(app)
    routes.study_sessions.load(app)
    routes.dashboard.load(app)
    routes.study_activities.load(app)

    # Set up tables and load initial data
    with app.app_context():
        cursor = app.db.cursor()
        app.db.setup_tables(cursor)
        app.db.import_word_json(
            cursor=cursor,
            group_name='Core Verbs',
            data_json_path='seed/data_verbs.json'
        )
        app.db.import_word_json(
            cursor=cursor,
            group_name='Core Adjectives',
            data_json_path='seed/data_adjectives.json'
        )
        app.db.import_study_activities_json(
            cursor=cursor,
            data_json_path='seed/study_activities.json'
        )

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
