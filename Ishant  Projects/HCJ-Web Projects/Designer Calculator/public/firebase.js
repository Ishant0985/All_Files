// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyD9cMak7OgMxiDSusaPPf_6608Ud80Hugo",
  authDomain: "colorsoftcalculator.firebaseapp.com",
  projectId: "colorsoftcalculator",
  storageBucket: "colorsoftcalculator.appspot.com",
  messagingSenderId: "834068116423",
  appId: "1:834068116423:web:def7ecf74de1f0f5b15fe2",
  measurementId: "G-9XGYF2KYDH"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);