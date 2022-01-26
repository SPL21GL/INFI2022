function deleteItem(button)
{
    if(window.confirm("Wollen Sie das Item wirklich löschen"))
    {
        button.form.submit();
    }
}