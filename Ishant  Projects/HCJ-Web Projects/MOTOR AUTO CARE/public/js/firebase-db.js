// firebase-db.js
import { db, storage, auth } from './firebase.js';
import { doc, getDoc, updateDoc } from 'firebase/firestore';
import { ref, uploadBytes, getDownloadURL } from 'firebase/storage';

// Load user profile
async function loadUserProfile() {
  const user = auth.currentUser;
  if (user) {
    const userRef = doc(db, 'users', user.uid);
    const docSnap = await getDoc(userRef);

    if (docSnap.exists()) {
      const userData = docSnap.data();
      document.getElementById("fullname").innerText = userData.displayName;
      document.getElementById("username").innerText = userData.username;
      document.getElementById("email").innerText = userData.email;
      document.getElementById("phone").innerText = userData.phoneNumber || "Not provided";
      document.getElementById("address").innerText = userData.address || "Not provided";

      // Load profile picture
      const profilePicRef = ref(storage, 'userProfiles/' + user.uid + '/profilePic.jpg');
      const profilePicUrl = await getDownloadURL(profilePicRef);
      document.getElementById("profile-pic").src = profilePicUrl || "images/icons/empty-profile.png";
    }
  } else {
    console.log("No user is signed in.");
  }
}

// Update user profile
async function updateUserProfile(updates) {
  const user = auth.currentUser;
  if (user) {
    const userRef = doc(db, 'users', user.uid);
    await updateDoc(userRef, updates);

    // Reload profile data after update
    await loadUserProfile();
  }
}

// Update profile picture
async function updateProfilePic(file) {
  const user = auth.currentUser;
  if (user && file) {
    const profilePicRef = ref(storage, 'userProfiles/' + user.uid + '/profilePic.jpg');
    await uploadBytes(profilePicRef, file);
    const profilePicUrl = await getDownloadURL(profilePicRef);
    document.getElementById("profile-pic").src = profilePicUrl;
  }
}

export { loadUserProfile, updateUserProfile, updateProfilePic };
