import math

from flask import Flask, render_template, request


def solution():
    app = Flask(__name__)

    @app.route('/')
    @app.route('/index')
    def index():
        return render_template("index.html")

    @app.route('/', methods=['POST', 'GET'])
    def form():
        if request.method == 'POST':
            a = float(request.form.get('a'))  # запрос к данным формы
            b = float(request.form.get('b'))
            c = float(request.form.get('c'))
            D = b ** 2 - 4 * a * c

            if D > 0:
                message_yes = 'Уравнение имеет решение:'
                x1 = (-b + math.sqrt(D)) / (2 * a)
                x2 = (-b - math.sqrt(D)) / (2 * a)
                return render_template('index.html', message_yes=message_yes, x1=x1, x2=x2)
            elif D < 0:
                message_no = "Уравнение не имеет решения"
                return render_template('index.html', message_no=message_no)
            else:
                message_one = 'Уравнение имеет решение:'
                x = (-b + math.sqrt(D)) / (2 * a)
                return render_template('index.html', message_one=message_one, x=x)

    app.run()