// js/ui.js
import { auth } from './firebase.js';
import { onAuthStateChanged } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-auth.js";
import { handleLogout } from './auth.js';

export function initializeUI() {
    const loginSection = document.getElementById('login-section');
    const profileSection = document.getElementById('profile-section');
    const logoutButton = document.getElementById('logout');
    const profilePic = document.getElementById('profile-pic');
    const welcomeMessage = document.getElementById('welcome-message');
    const userNameSpan = document.getElementById('user-name');

    // Monitor Authentication State
    onAuthStateChanged(auth, (user) => {
        if (user) {
            // User is signed in
            loginSection.style.display = 'none';
            profileSection.style.display = 'block';

            // Set profile picture (use user's photoURL if available)
            if (user.photoURL) {
                profilePic.src = user.photoURL;
            } else {
                profilePic.src = 'images/default-profile.png'; // Fallback image
            }

            // Display welcome message
            if (welcomeMessage && user.displayName) {
                userNameSpan.innerText = user.displayName;
                welcomeMessage.style.display = 'block';
            }
        } else {
            // No user is signed in
            loginSection.style.display = 'block';
            profileSection.style.display = 'none';
            if (welcomeMessage) {
                welcomeMessage.style.display = 'none';
            }
        }
    });

    // Handle Logout
    if (logoutButton) {
        logoutButton.addEventListener('click', async (e) => {
            e.preventDefault();
            await handleLogout();
            window.location.href = 'index.html'; // Redirect after logout
        });
    }
}
