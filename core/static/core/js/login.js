function auth() {
    data = document.getElementsByName('login-form')
    fetch("/api/auth", {
        method: "POST",
        headers: {'Content-Type': 'application/json', "X-CSRFToken": document.getElementsByName('csrfmiddlewaretoken')[0].value},
        body: JSON.stringify({
            username: data[0].value,
            password: data[1].value
        })
    }).then(response => response)
    .then(data => {
        if(data.status == 200){
            window.location.replace("/")
        }
        else if(data.status == 401){
            showPopup('Wrong credentials');
            document.getElementsByTagName('input')[0].value = '';
            document.getElementsByTagName('input')[1].value = '';
        }
    });
}


document.getElementsByClassName('btn-login')[0].addEventListener("click", auth);

