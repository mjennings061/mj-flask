from flask import Flask, request, render_template
from dotenv import load_dotenv
from code_helper import add_full_stops_to_comments

app = Flask(__name__)
load_dotenv('.env')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World! You are probably looking for the /add-full-stops-to-comments API champ.'


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
