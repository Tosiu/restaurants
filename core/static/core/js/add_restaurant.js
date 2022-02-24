function add_restaurant() {
    send_obj = {
        'name': document.getElementsByTagName('input')[0].value,
        'url': document.getElementsByTagName('input')[1].value,
        'phone': document.getElementsByTagName('input')[2].value,
        'notes': document.getElementsByTagName('textarea')[0].value
    }
    console.log(send_obj)
    fetch("/api/add_restaurant", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            "X-CSRFToken": document.getElementsByName('csrfmiddlewaretoken')[0].value
        },
        body: JSON.stringify(send_obj)
    }).then(response => response)
    .catch((error) => {
      console.log(error)
    })
    .then(data => {
        if(data.status == 200){
            window.location.replace("/login")
        }
        else if(data.status == 400){
            showPopup('Error 400 - Bad request')
        }

    })
}
document.getElementById('btn-send').addEventListener("click", add_restaurant);
document.getElementById('back-to-home').addEventListener("click", function(){
    window.location.replace("/")
});