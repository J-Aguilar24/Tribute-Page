from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/godzila')
def godzila():
    return render_template("godzila.html")

@app.route('/kong')
def kong():
    return render_template("kong.html")

if __name__ == "__main__":
    app.run(debug=True)