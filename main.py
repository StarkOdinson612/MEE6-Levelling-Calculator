from flask import Flask, render_template, request
import json
import api_lvl as al

app = Flask(__name__)

@app.route("/", methods=["POST"])  # this sets the route to this page
def home():
    with open('dict.json', 'r') as fo:
        id_list = json.load(fo)
        id_list = {**{"(None)": "none"}, **id_list}
    
    userEmail = request.form["username"]
    userPassword = request.form["user_id"]

    return render_template("index.html", members=id_list)

@app.route("/api_final_noone_will_find_this_sdfhkasdhjdfjljdajkrffjkdfjfdvfjghfdjghfgjgfghj")
def final():
    return render_template("return_page.html", DETAILS_STR="tomato")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)