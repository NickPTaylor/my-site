import json
from flask import Flask, render_template

app = Flask(__name__)
app.config['FREEZER_RELATIVE_URLS'] = True

@app.route('/')
@app.route('/index.html')
def home():
    with open('data/projects.json') as json_projects:
        projects = json.load(json_projects)
    return render_template('index.html', title="Home", projects=projects)

@app.route('/cv.html')
def cv():
    return render_template('cv.html', title="CV")

@app.route('/my_story.html')
def my_story():
    return render_template('my_story.html', title="My Story")


if __name__ == '__main__':
    app.run(debug=True)
