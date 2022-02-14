from flask import Flask, redirect, request, flash, session
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
    
    flash(f"Item with id {itemIdToDelete} has been deleted")    

    return redirect("/")

@app.route("/", methods=["get","post"])
def index():

    #holt den wert der Session Variable "number_of_reloads"
    reload_count = session.get("number_of_reloads",1)
    #anzahl um eins erhöhen
    reload_count += 1
    #neue anzahl abspeichern
    session.update({"number_of_reloads": reload_count})

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
        items = items, \
        reload_count = reload_count)

@app.route("/editForm",methods=["post"])
def submitEditForm():
    editItemFormObject = EditItemForm()

    if editItemFormObject.validate_on_submit():
        print("Submit wurde durchgeführt")
        #daten aus form auslesen
        #neuer title -> editItemFormObject.title.data
        #daten mit update in DB speichern

        itemId = editItemFormObject.itemId.data

        item_to_edit = db.session.query(Todoitem).filter(Todoitem.itemId == itemId).first()
        item_to_edit.title = editItemFormObject.title.data

        db.session.commit()

        return redirect("/")
    else:
        raise ("Fatal Error")

@app.route("/editForm")
def showEditForm():
    #hier itemid auslesen (wie kann man bei flask einen get parameter aus dem request auslesen)
    itemId = request.args["itemid"]

    #item laden (wie kann man einen datensatz lesen)
    item_to_edit = db.session.query(Todoitem).filter(Todoitem.itemId == itemId).first()
    
    editItemFormObject = EditItemForm()
    #form befüllen
    editItemFormObject.itemId.data = item_to_edit.itemId
    editItemFormObject.title.data = item_to_edit.title
    editItemFormObject.description.data = item_to_edit.description
    editItemFormObject.dueDate.data = item_to_edit.dueDate
    editItemFormObject.isDone.data = item_to_edit.isDone
    
    return render_template("editForm.html", form = editItemFormObject)

app.run(debug=True)