#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    output = ''
    for n in range(parameter):
        output +=  f'{n}\n'
    return output

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    operations = ['+', '-', '*', 'div', '%']
    if operation in operations:
        if operation == 'div':
            return f'{num1 / num2}'
        elif operation == '+':
            return f'{num1 + num2}'
        elif operation == "-":
            return f'{num1 - num2}'
        elif operation == "*":
            return f'{num1 * num2}'
        elif operation == "%":
            return f'{num1 % num2}'
    else:
        print('Operation must be +, -, * or div')
        
if __name__ == '__main__':
    app.run(port=5555, debug=True)
