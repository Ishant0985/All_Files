// Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.0.0/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/9.0.0/firebase-auth.js";

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "loginpage0808.firebaseapp.com",
  projectId: "loginpage0808",
  storageBucket: "loginpage0808.appspot.com",
  messagingSenderId: "290136935103",
  appId: "1:290136935103:web:450d3c91a341620f47d40a",
  measurementId: "G-68GLGNJHGL"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
