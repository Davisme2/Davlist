
document.body.addEventListener("htmx:responseError", function(evt) {
            alert(evt.detail.xhr.responseText);
        })