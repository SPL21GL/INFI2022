function deleteItem(button)
{
    if(window.confirm("Wollen Sie das Item wirklich löschen"))
    {
        button.form.submit();
    }
}

function showAllToasts()
{
    var toastElList = [].slice.call(document.querySelectorAll('.toast'));
    var toastList = toastElList.map(function (toastEl) {
        return new bootstrap.Toast(toastEl, option)
    });
    
    //for schleife hier
}

//funktion hier aufrufen
