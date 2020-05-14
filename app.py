from flask import Flask

app = Flask(__name__)


@app.route('/register')
def register():
    title = '<h1>Boss Bitch!!</h1>'
    return title

if __name__ == '__main__':
    app.run(debug=True)