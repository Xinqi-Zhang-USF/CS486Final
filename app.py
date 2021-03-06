from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
  return "Xinqi CS486 Final."

@app.route('/<int:number>')
def xinqi_draw(number):
    if number == 1:
        return 'Oh you are not xinqi'
    elif number == 2:
        return 'Geez you are extremely xinqi'
    else:
        return 'Please try one more time'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
