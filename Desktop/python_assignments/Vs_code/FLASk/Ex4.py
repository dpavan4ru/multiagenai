"""
step-1: Initialise the flast
step-2: app variable works as decorator
step-3: run the app
Note: in the route / indicates main window
"""

from flask import Flask,jsonify

app=Flask(__name__)

@app.route('/')
def addition():
    a=10
    b=20
    c=jsonify(f"the addition of {a} and {b} is {a+b}")
    return c

    #return('hello good evening')

if __name__=='__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0',port=8000)