function deleteItem(button)
{
    if(window.confirm("Wollen Sie das Item wirklich löschen"))
    {
        button.form.submit();
    }
}

function showAllToasts()
{
    let toastElList = [].slice.call(document.querySelectorAll('.toast'));
    let toastList = toastElList.map(function (toastEl) {
        return new bootstrap.Toast(toastEl);
    });
    
    //for of schleife hier
    for (let toast of toastList)
    {
        toast.show();
    }
}

//funktion hier aufrufen
showAllToasts();