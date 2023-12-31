#!/usr/bin/python3
"""
This module contains the principal application
"""
from flask import Flask
from models import storage
from api.v1.views import app_view 

app = Flask(__name__)

# Register the app_views Blueprint with the app
app.register_blueprint(app_views)

@app.teardown_appcontext
def close_db(obj):
    """ calls methods close() """
    storage.close()
    

if __name__ == "__main__":

    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)

    app.run(host, int(port), threaded=True)