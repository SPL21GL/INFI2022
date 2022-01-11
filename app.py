from flask import Flask

from flask.templating import render_template

from addItemForm import AddItemForm

app = Flask(__name__)
app.secret_key = "VerySecretSecretKey"

@app.route("/", methods=["get","post"])
def index():
    addItemFormObject = AddItemForm()
    return render_template("index.html", headline="Todo Items", form = addItemFormObject)

app.run(debug=True)