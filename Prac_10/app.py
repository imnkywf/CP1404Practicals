from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/f')
@app.route('/f/<celsius>')
def degrees_convert(celsius=""):
    fahr = float(celsius) * 9/5+32
    return str(fahr)


if __name__ == '__main__':
    app.run()
