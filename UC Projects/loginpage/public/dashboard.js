import { signOut } from "firebase/auth";
import { auth } from "./firebaseConfig.js";

function logout() {
    signOut(auth).then(() => {
        window.location = 'index.html';  // Redirect to login page
    }).catch((error) => {
        console.log(error.message);
    });
}
