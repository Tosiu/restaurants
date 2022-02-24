
 async function load(){
    const response = await fetch('/api/pick_restaurant', {
        method: "GET",
        headers: {
            "X-CSRFToken": document.getElementsByName('csrfmiddlewaretoken')[0].value
        }
    })
    const names = await response.json();
    document.getElementsByClassName('header')[0].innerText = names['name']
    document.getElementsByClassName('description')[0].innerText = 'Url: ' + names['url']
    document.getElementsByClassName('description')[1].innerText = 'Phone: ' + names['phone']
    document.getElementsByClassName('description')[2].innerText = 'Notes: ' + names['notes']
    console.log(names)


//    fetch("/api/pick_restaurant", {
//        method: "GET",
//        headers: {
//            "X-CSRFToken": document.getElementsByName('csrfmiddlewaretoken')[0].value
//        }
//    }).then(response => response)
//    .catch((error) => {
//      console.log(error)
//    })
//    .then(data => {
//        if(data.status == 200){
//            await console.log(data.json())
//        }
//        else if(data.status == 400){
//            showPopup('Error 400 - Bad request')
//        }
//
//    })
}
window.onload = load();


document.getElementById('back-to-home').addEventListener("click", function(){
    window.location.replace("/")
});