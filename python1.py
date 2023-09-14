# This project is to deploy flask project using docker container

print("Hey this is my first project on flask")

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0", port= int("3000"), debug=True)