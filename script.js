function register() {
    // ... código de registro existente ...

    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            var response = JSON.parse(xhr.responseText);
            if (response.success) {
                window.location.href = '/dashboard'; // Redirecionamento após o cadastro
            } else {
                document.getElementById("registerMessage").innerText = response.message;
            }
        }
    };

    // ... código de requisição existente ...
}

function login() {
    // ... código de login existente ...

    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            var response = JSON.parse(xhr.responseText);
            if (response.success) {
                window.location.href = '/dashboard'; // Redirecionamento após o login
            } else {
                document.getElementById("loginMessage").innerText = response.message;
            }
        }
    };

    // ... código de requisição existente ...
}
