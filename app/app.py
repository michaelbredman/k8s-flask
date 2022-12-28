from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<H1>This is a Simple application</H1>"

@app.route("/time")
def hello_time():
    return "<H1>Time function Route<H1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
