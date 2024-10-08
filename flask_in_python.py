from flask import Flask

Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    c ="hello"
    d = "world"
    f = "what are you guys doing"
    e = c+d + f
    return e
def show():
    v = "hello guys"
    f = "hey how are tou"
    s = v+ f
    return s






