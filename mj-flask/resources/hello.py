from flask_restful import Resource
from flask import Flask, request, render_template, make_response

class HelloWorld(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        message = 'Hello World!<br><br>You are probably looking for the /add-full-stops-to-comments API champ.'
        return make_response(message, 200, headers)
