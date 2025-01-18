
import { getAuth, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-auth.js";
import { auth } from './js/firebase.js';

window.onload = function () {
    console.log("Page loaded, checking authentication state...");

    // Handle user state changes
    onAuthStateChanged(auth, (user) => {
        if (user) { 
            console.log("User is logged in:", user);

            // Hide login button and show profile section
            document.getElementById('login-section').style.display = 'none';
            document.getElementById('profile-section').style.display = 'block';

            // Set profile picture and username
            const profilePic = document.getElementById('profile-pic');
            if (user.photoURL) {
                profilePic.src = user.photoURL; // Use Google profile picture if available
                console.log("Using user photo URL:", user.photoURL);
            } else {
                profilePic.src = 'images/icons/empty-profile.png'; // Default picture for email/password login
                console.log("Using default profile picture");
            }

            // Add username greeting
            if (!document.querySelector("#profile-section p")) {
                const greeting = document.createElement('p');

                const fullName = user.displayName || "User"; // Fallback if no display name
                const firstName = fullName.split(" ")[0]; // Get first name


                greeting.textContent = `Hi, ${firstName || user.email.split('@')[0]}`;
                document.getElementById('profile-section').appendChild(greeting);
                console.log("User greeting added:", greeting.textContent);
            }
        } else {
            console.log("No user is logged in.");

            // Show login button and hide profile section
            document.getElementById('login-section').style.display = 'block';
            document.getElementById('profile-section').style.display = 'none';
        }
    });

    // Logout function
    document.getElementById('logout').addEventListener('click', async () => {
        console.log("Logout button clicked");
        try {
            await signOut(auth);
            console.log("User logged out successfully.");
            alert('You have logged out successfully.');
            window.location.href = 'index.html'; // Redirect to the homepage after logout
        } catch (error) {
            console.error('Logout error:', error);
        }
    });
};

