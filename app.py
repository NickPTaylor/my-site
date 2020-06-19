from flask import Flask, render_template

app = Flask(__name__)
app.config['FREEZER_RELATIVE_URLS'] = True

@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html', title="Home")

@app.route('/cv.html')
def cv():
    return render_template('cv.html', title="CV")


if __name__ == '__main__':
    app.run(debug=True)
