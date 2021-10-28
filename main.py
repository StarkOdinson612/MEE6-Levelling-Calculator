from flask import Flask, render_template, request, redirect
import json
import api_lvl as al
import math
from threading import Thread

app = Flask(__name__)

@app.route("/")  # this sets the route to this page
def home():
    with open('dict.json', 'r') as fo:
        id_list = json.load(fo)
        id_list = {**{"(None)": "none"}, **id_list}

    return render_template("index.html", members=id_list)

@app.route("/data", methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return redirect("/")
    if request.method == 'POST':
        form_data = request.form.to_dict(flat=False)
        
        if len(list(form_data.values())) == 2:
            v = list(form_data.values())
            print(f"Running textbox... {v}")
            if len(v[0][0]) == 0 or len(v[1][0]) == 0:
                print("NO INPUT")
                return redirect('/')
            
            try:
                al.validate_id(v[1][0])

                print("VALID ID... Fetching Data...")
                
                al.update_json_file(v[0][0], v[1][0])

                form_data = al.get_details(v[1][0])[1]
            except al.InvalidID:
                print("INVALID ID")
                return redirect('/')

        elif len(list(form_data.values())) == 1:
            print("Running select...")
            if list(form_data.values())[0][0] == 'none':
                print("NO INPUT")
                return redirect('/')

            print("VALID ID... Fetching Data...")
            
            uid = ''.join(reversed((''.join(reversed(list(form_data.values())[0][0]))).split(':')[0]))

            form_data = al.get_details(uid)[1]

        return render_template("return_page.html", DETAILS_STR="tomato", form_data=form_data)

def keep_alive():
    server = Thread(target=run)
    server.start()

def run():
    app.run(host="0.0.0.0", port=8000)

potato = ['with_potato', 'github_banana']

if __name__ == '__main__':
    keep_alive()