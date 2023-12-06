function addRandomColor() {
    let inputs = document.getElementsByName("ulubiony_kolor");
    const colors = ["czerwony", "niebieski", "zielony"];
    inputs.forEach((ulubiony_kolor) => {
        ulubiony_kolor.value = colors[Math.floor(Math.random() * colors.length)];
    });
}

function refreshListTemplate() {
    $.ajax({
        type: "GET",
        url: 'http://127.0.0.1:8000/ankieta/refreshlist',
    })
        .done(function (response) {
            $('#display-data').empty();
            $('#display-data').append(response);
        });
}

function deleteAnkieta(id, csrf_token) {
    $.ajax({
        type: "DELETE",
        url: `http://127.0.0.1:8000/ankieta/delete/${id}`,
        headers: {'X-CSRFToken': `${csrf_token}`},
        mode: 'same-origin' // Do not send CSRF token to another domain.
    })
        .done(function () {
            refreshListTemplate()
        });
}