from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "Bye code"

@app.route('/hello')
def greeting():
    return "Hello world"

@app.route('/sum/<int:a>/<int:b>')
def sum( a:int, b: int):
    nums_sum = a + b
    return f"La suma es: {str(nums_sum)}"



