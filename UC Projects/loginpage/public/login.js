import { signInWithEmailAndPassword, signInWithPopup, GoogleAuthProvider } from "https://www.gstatic.com/firebasejs/9.0.0/firebase-auth.js";
import { auth } from "./firebaseConfig.js";

window.login = function() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    signInWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            window.location = 'dashboard.html';  // Redirect to dashboard
        })
        .catch((error) => {
            document.getElementById('message').innerText = error.message;
        });
};

window.googleSignIn = function() {
    const provider = new GoogleAuthProvider();

    signInWithPopup(auth, provider)
        .then((result) => {
            window.location = 'dashboard.html';  // Redirect to dashboard
        })
        .catch((error) => {
            document.getElementById('message').innerText = error.message;
        });
};
