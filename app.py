from flask import Flask, redirect
from flask.templating import render_template
from editItemFrom import EditItemForm
from model import db, Todoitem

from addItemForm import AddItemForm
from deleteItemForm import DeleteItemForm

app = Flask(__name__)
app.secret_key = "VerySecretSecretKey"

#Datenbankzugriff konfigurieren
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@localhost/todoItemApp"
db.init_app(app)

@app.route("/items/delete", methods=["post"])
def deleteItem():
    deleteItemFormObj = DeleteItemForm()
    if deleteItemFormObj.validate_on_submit():
        print("gültig")
        #db objekt holen
        #delete command ausführen

        itemIdToDelete = deleteItemFormObj.itemId.data
        itemToDelete = db.session.query(Todoitem).filter(Todoitem.itemId == itemIdToDelete)
        itemToDelete.delete()
        
        db.session.commit()
    else:
        print("Fatal Error")        
    return redirect("/")

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
        
        newItem = Todoitem()
        newItem.title = addItemFormObject.title.data
        newItem.description = addItemFormObject.description.data
        newItem.dueDate = addItemFormObject.dueDate.data
        newItem.isDone = addItemFormObject.isDone.data

        db.session.add(newItem)
        db.session.commit()

        return redirect("/")
        
    
    items = db.session.query(Todoitem).all()

    return render_template("index.html", \
        headline="Todo Items", \
        form = addItemFormObject, \
        items = items)

@app.route("/editForm")
def showEditForm():
    #hier itemid auslesen
    #item laden
    #form befüllen
    editItemFormObject = EditItemForm()
    return render_template("editForm.html", form = editItemFormObject)

app.run(debug=True)