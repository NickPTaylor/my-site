from flask import Flask, render_template

app = Flask(__name__)
app.config['FREEZER_RELATIVE_URLS'] = True

@app.route('/')
@app.route('/home.html')
def home():
    return render_template('home.html')

@app.route('/cv.html')
def cv():
    return render_template('cv.html')

@app.route('/about_me.html')
def about_me():
    return render_template('about_me.html')


if __name__ == '__main__':
    app.run(debug=True)
