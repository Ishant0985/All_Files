// js/profile.js
import { auth, storage } from './firebase.js';
import { onAuthStateChanged, updateProfile } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-auth.js";
import { ref, uploadBytes, getDownloadURL } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-storage.js";

// Function to handle profile picture upload
async function uploadProfilePicture(file) {
    const storageRef = ref(storage, `profile_pictures/${auth.currentUser.uid}/${file.name}`);
    await uploadBytes(storageRef, file);
    const downloadURL = await getDownloadURL(storageRef);
    return downloadURL;
}

// Modify handleProfileUpdate to handle profile picture
export async function handleProfileUpdate(event) {
    event.preventDefault();
    const displayName = document.getElementById('profile-name').value;
    const photoInput = document.getElementById('profile-pic-input');
    let photoURL = auth.currentUser.photoURL;

    if (photoInput.files[0]) {
        try {
            photoURL = await uploadProfilePicture(photoInput.files[0]);
        } catch (error) {
            console.error('Photo upload error:', error);
            alert(error.message);
            return;
        }
    }

    try {
        await updateProfile(auth.currentUser, {
            displayName: displayName,
            photoURL: photoURL
        });
        alert('Profile updated successfully!');
        // Optionally, refresh the page or update the UI
        window.location.reload();
    } catch (error) {
        console.error('Profile update error:', error);
        alert(error.message);
    }
}

// Update populateUserData to include profile picture input
function populateUserData(user) {
    if (user) {
        document.getElementById('profile-email').innerText = user.email;
        document.getElementById('profile-name').value = user.displayName || '';
        if (user.photoURL) {
            document.getElementById('profile-pic').src = user.photoURL;
        }
    }
}

// Initialize Profile Page
export function initializeProfile() {
    const profileForm = document.getElementById('profile-form');
    if (profileForm) {
        profileForm.addEventListener('submit', handleProfileUpdate);
    }

    onAuthStateChanged(auth, (user) => {
        if (user) {
            populateUserData(user);
        } else {
            // If no user is signed in, redirect to login page
            window.location.href = 'loginpage.html';
        }
    });
}
