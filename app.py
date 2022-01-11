from flask import Flask, redirect

from flask.templating import render_template

from addItemForm import AddItemForm

app = Flask(__name__)
app.secret_key = "VerySecretSecretKey"

@app.route("/", methods=["get","post"])
def index():
    addItemFormObject = AddItemForm()

    if addItemFormObject.validate_on_submit():
        #post kam zurück und ist valide
        print(addItemFormObject.title.data)
        print(addItemFormObject.description.data)
        print(addItemFormObject.dueDate.data)
        print(addItemFormObject.isDone.data)
        #hier in DB Speichern
        
        return redirect("/")

    return render_template("index.html", headline="Todo Items", form = addItemFormObject)

app.run(debug=True)