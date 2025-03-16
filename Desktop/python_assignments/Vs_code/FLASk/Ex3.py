"""
step-1: Initialise the flast
step-2: app variable works as decorator
step-3: run the app
Note: in the route / indicates main window
"""

from flask import Flask

app=Flask(__name__)

@app.route('/')
def greet1():

    return('hello good evening')

@app.route('/greet2')
def greet2():

    return('hello good night')


@app.route('/greet3')
def greet3():

    return('hello good afternoone')

@app.route('/greet4')
def greet4():

    return('hello Pavan')


if __name__=='__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0',port=8000)