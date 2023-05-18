import math
import counting

from flask import Flask, render_template, request


def solution():
    app = Flask(__name__)

    @app.route('/')
    @app.route('/index')
    def index():
        return render_template("/python3-4lr/index.html")

    @app.route('/', methods=['POST', 'GET'])
    def form():
        if request.method == 'POST':
            a = float(request.form.get('a'))  # запрос к данным формы
            b = float(request.form.get('b'))
            c = float(request.form.get('c'))
            D = counting.discriminant(a, b, c)

            if D > 0:
                message_yes = 'Уравнение с параметрами a = ' + str(a) + ', b = ' + str(b) + ', c = ' + \
                              str(c) + ' имеет решения:'
                x1 = counting.x1(a, b, c)
                x2 = counting.x2(a, b, c)
                return render_template('/python3-4lr/index.html', message_yes=message_yes, x1=x1, x2=x2)
            elif D < 0:
                message_no = 'Уравнение с параметрами a = ' + str(a) + ', b = ' + str(b) + ', c = ' + \
                             str(c) + ' не имеет решения'
                return render_template('/python3-4lr/index.html', message_no=message_no)
            else:
                message_one = 'Уравнение с параметрами a = ' + str(a) + ', b = ' + str(b) + ', c = ' + \
                              str(c) + ' имеет решение'
                x = counting.x1(a, b, c)
                return render_template('/python3-4lr/index.html', message_one=message_one, x=x)

    app.run()
