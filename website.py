from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")  # this sets the route to this page
def home():
	return render_template("index.html")

if __name__ == '__main__':
    app.run()