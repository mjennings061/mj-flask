from flask_restful import Resource
from flask import Flask, request, render_template, make_response
from code_helper import add_full_stops_to_comments

class AddFullStopsToComments(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template("submit_code.html"), 200, headers)
    
    def post(self):
        input_code = request.form.get('input_code')
        modified_code = add_full_stops_to_comments(input_code)
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('code_comparison.html', original_code=input_code, modified_code=modified_code), 200, headers)
