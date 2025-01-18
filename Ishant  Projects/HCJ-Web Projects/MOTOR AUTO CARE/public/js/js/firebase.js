import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-auth.js";
import { getStorage } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-storage.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-firestore.js";

// Your Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyCTc0HLgncOulvfL-afqWGhGdpO-n4lmc8",
    authDomain: "motor-auto-care.firebaseapp.com",
    projectId: "motor-auto-care",
    storageBucket: "motor-auto-care.appspot.com",
    messagingSenderId: "308826053424",
    appId: "1:308826053424:web:80cf3c7814a98f60bd06f5"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const storage = getStorage(app);
const db = getFirestore(app);

export { auth, storage, db };
