from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")
#    return "index.html"

@app.route('/cover')
def home_page():
    return "In home page"

@app.route('/greeting')
def greeting():
    return "As Salamu alaikum"

@app.route('/invitation')
def invitation():
    return "U R Invited"

@app.route('/farewell')
def farewell():
    return "Allah Hafiz"

if __name__ == "__main__":
    app.run(debug=true)
