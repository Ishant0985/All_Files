function signup() {
    document.getElementById('login').classList.remove('active');
    document.getElementById('signup').classList.add('active');
    document.getElementById('btn').style.left = '110px';
}

function login() {
    document.getElementById('signup').classList.remove('active');
    document.getElementById('login').classList.add('active');
    document.getElementById('btn').style.left = '0';
}

function togglePassword(fieldId, eyeId) {
    var passwordField = document.getElementById(fieldId);
    var eyeIcon = document.getElementById(eyeId);

    if (passwordField.type === "password") {
        passwordField.type = "text";
        eyeIcon.classList.add('closed');
    } else {
        passwordField.type = "password";
        eyeIcon.classList.remove('closed');
    }
}

// Set default active form to login
window.onload = function() {
    login();
};
