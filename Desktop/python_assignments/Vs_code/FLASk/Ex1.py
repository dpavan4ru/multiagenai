from flask import Flask
import flask
print(flask.__version__)

def decorator(greet1):
    def greetings():
        print('Hello goodmorning')
        greet1()
        print('hello good night')
    return greetings

@decorator
def greet1():
    print('hello good evening')

greet1()