function logout() {
    fetch("/api/sign_out", {
        method: "GET",
        headers: {"X-CSRFToken": document.getElementsByName('csrfmiddlewaretoken')[0].value}
    }).then(response => response)
    .then(data => window.location.replace("/login"));
}

document.getElementsByClassName('btn-logout')[0].addEventListener("click", logout);

