from flask import Flask, request, render_template
from dotenv import load_dotenv
from code_helper import add_full_stops_to_comments
import os

app = Flask(__name__)

# Build a path and import the environment variables.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
file_path = os.path.join(project_dir, ".env")
load_dotenv(file_path)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!\n\nYou are probably looking for the /add-full-stops-to-comments API champ.'


@app.route('/add-full-stops-to-comments', methods=['GET', 'POST'])
def add_full_stops_comments():
    """Take in code, add full stops to the end of comment lines."""
    if request.method == "POST":
        input_code = request.form.get('input_code')
        modified_code = add_full_stops_to_comments(input_code)
        return render_template('code_comparison.html', original_code=input_code, modified_code=modified_code)
    else:
        return render_template("submit_code.html")


if __name__ == '__main__':
    app.run(debug=True)
