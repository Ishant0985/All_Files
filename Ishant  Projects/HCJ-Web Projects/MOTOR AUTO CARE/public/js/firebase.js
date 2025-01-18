// firebase.js
import { initializeApp } from "firebase/app";
import { getAuth, signInWithPopup, GoogleAuthProvider, createUserWithEmailAndPassword, onAuthStateChanged } from "firebase/auth";
import { getFirestore, doc, setDoc, getDoc } from "firebase/firestore";

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
const db = getFirestore(app);

// Function to create a user document in Firestore
async function createUserInFirestore(user, additionalData = {}) {
  const userRef = doc(db, 'users', user.uid);
  const docSnap = await getDoc(userRef);

  // If user data does not exist, create a new user document
  if (!docSnap.exists()) {
    const username = additionalData.username || user.email.split("@")[0];  // Use email prefix as default username
    await setDoc(userRef, {
      uid: user.uid,
      fullName: additionalData.fullName || user.displayName || "",
      username: username,
      email: user.email,
      phoneNumber: additionalData.phoneNumber || "",
      address: additionalData.address || ""
    });
  }
}

// Google Login Function
async function googleLogin() {
  const provider = new GoogleAuthProvider();
  try {
    const result = await signInWithPopup(auth, provider);
    const user = result.user;
    await createUserInFirestore(user);  // Create user in Firestore on login
  } catch (error) {
    console.error(error);
  }
}

// Email/Password Sign Up
async function emailSignUp(email, password, additionalData) {
  try {
    const result = await createUserWithEmailAndPassword(auth, email, password);
    const user = result.user;
    await createUserInFirestore(user, additionalData);  // Create user in Firestore on signup
  } catch (error) {
    console.error(error);
  }
}

// Exporting functions
export { auth, googleLogin, emailSignUp };
