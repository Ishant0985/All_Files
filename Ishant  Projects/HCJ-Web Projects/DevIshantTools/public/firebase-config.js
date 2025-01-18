import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.10/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.6.10/firebase-analytics.js";
import { getAuth, GoogleAuthProvider, signInWithPopup } from "https://www.gstatic.com/firebasejs/9.6.10/firebase-auth.js";


const firebaseConfig = {
    apiKey: "AIzaSyAIXtg5AWDxZfreWKsJX4RGjrOuBKkuYmQ",
    authDomain: "devishanttool.firebaseapp.com",
    projectId: "devishanttool",
    storageBucket: "devishanttool.appspot.com",
    messagingSenderId: "1012185522048",
    appId: "1:1012185522048:web:9d3518ba3dff6a8950eb65",
    measurementId: "G-YGGPWE5F03"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

document.addEventListener('DOMContentLoaded', function() {
    const loginButton = document.getElementById('login-btn');
    const logoutButton = document.getElementById('logout-btn');
    const profileContainer = document.getElementById('user-info');
    const userPic = document.getElementById('user-pic');
    const userName = document.getElementById('user-name');

    console.log("Page loaded, initializing Firebase...");
    
    // Initialize GoogleAuthProvider
    const provider = new GoogleAuthProvider();

    // Check the user's authentication state
    auth.onAuthStateChanged((user) => {
        if (user) {
            console.log("User is signed in:", user);
            // User is signed in, show user profile info
            userPic.src = user.photoURL;
            userName.textContent = user.displayName;
            profileContainer.style.display = 'block';
            loginButton.style.display = 'none';  // Hide login button
        } else {
            console.log("No user signed in");
            // User is signed out, hide profile and show login button
            profileContainer.style.display = 'none';
            loginButton.style.display = 'block';
        }
    });

    // Login with Google
    loginButton.addEventListener('click', () => {
        console.log("Login button clicked, attempting Google sign-in...");
        signInWithPopup(auth, provider)
            .then((result) => {
                // Google Access Token and User Info
                const user = result.user;
                console.log("Sign-in successful, user:", user);
                alert(`Signed in as: ${user.displayName}`);
            })
            .catch((error) => {
                console.error('Error during sign-in:', error.message);
                alert('Sign-in failed. Please try again.');
            });
    });

    // Logout functionality
    logoutButton.addEventListener('click', () => {
        console.log("Logout button clicked, attempting sign-out...");
        signOut(auth).then(() => {
            alert('User signed out successfully!');
            console.log("User signed out");
        }).catch((error) => {
            console.error('Error during sign-out:', error.message);
        });
    });
});
