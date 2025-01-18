// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "",
  authDomain: "about-ishant.firebaseapp.com",
  projectId: "about-ishant",
  storageBucket: "about-ishant.appspot.com",
  messagingSenderId: "282230189511",
  appId: "1:282230189511:web:6df7d258ebd3e4307b3de2",
  measurementId: "G-GRERSZBVYS"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);