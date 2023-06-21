from flask import Flask, request, render_template, make_response
from flask_restful import Resource, Api
from dotenv import load_dotenv
import os

from resources.hello import HelloWorld
from resources.add_comments import AddFullStopsToComments

app = Flask(__name__)
api = Api(app)

# Build a path and import the environment variables.
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Import the resources and declare api endpoints.
api.add_resource(HelloWorld, '/')
api.add_resource(AddFullStopsToComments, '/add-full-stops-to-comments')

if __name__ == '__main__':
    app.run(debug=True)
