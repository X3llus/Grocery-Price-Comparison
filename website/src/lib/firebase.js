// Import the functions you need from the SDKs you need
import { initializeApp } from 'firebase/app';
import { getFirestore } from 'firebase/firestore';
import { getDatabase} from "firebase/database";

// Your web app's Firebase configuration
const firebaseConfig = {
	apiKey: "AIzaSyCtun0uIHcDXHNVbtHCMDRlj7syvFd-PQs",
	authDomain: "groceriez-44935.firebaseapp.com",
	projectId: "groceriez-44935",
	storageBucket: "groceriez-44935.appspot.com",
	messagingSenderId: "406004418418",
	appId: "1:406004418418:web:8b2789d2b9656f8670bfeb",
	measurementId: "G-R6TEF0YV91"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

export {
	getAuth,
	createUserWithEmailAndPassword,
	signInWithEmailAndPassword,
	updateProfile,
	sendPasswordResetEmail,
	signOut,
	onAuthStateChanged,
	GoogleAuthProvider,
	signInWithPopup,
} from 'firebase/auth';
let db = getFirestore(app);
let rtdb = getDatabase(app);

export { db, app, rtdb };
export {
	collection,
	doc,
	setDoc,
	getDoc,
	updateDoc,
	query,
	where,
	getDocs,
	addDoc,
	limit,
	orderBy,
	startAfter,
	deleteDoc,
	deleteField
} from 'firebase/firestore';

export {
	ref,
	child,
	get
} from "firebase/database";

