from flask import Flask

app = Flask(__name__)


@app.route('/<int:number>')
def xinqi_draw(number):
    if number == 1:
        return 'Oh you are not Xinqi'
    elif number == 2:
        return 'Geez you are exactly Xinqi'
    else:
        return 'Please try one more time'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
