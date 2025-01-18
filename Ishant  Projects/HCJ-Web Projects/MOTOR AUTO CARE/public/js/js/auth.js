// auth.js
import { auth, GoogleAuthProvider, signInWithPopup, createUserWithEmailAndPassword } from './firebase.js';
import { createUser, isUsernameTaken } from './firebase-db.js';

// Google login
export async function loginWithGoogle() {
    const provider = new GoogleAuthProvider();
    try {
        const result = await signInWithPopup(auth, provider);
        const user = result.user;

        // Create user collection if not exists
        await createUser(user);
    } catch (error) {
        console.error("Google Login Error:", error);
    }
}

// Email/password signup
export async function signUpWithEmail(email, password, username, phoneNumber, address, profilePictureFile) {
    try {
        // Check if username is taken
        if (await isUsernameTaken(username)) {
            throw new Error("Username is already taken.");
        }

        const userCredential = await createUserWithEmailAndPassword(auth, email, password);
        const user = userCredential.user;

        // Create user collection with additional data
        await createUser(user, {
            username,
            phoneNumber,
            address,
            profilePictureFile
        });
    } catch (error) {
        console.error("Sign Up Error:", error);
    }
}
