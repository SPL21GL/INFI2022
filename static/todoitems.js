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
        return new bootstrap.Toast(toastEl, option)
    });
    
    //for of schleife hier
}

//funktion hier aufrufen
