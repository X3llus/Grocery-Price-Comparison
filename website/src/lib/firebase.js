// Import the functions you need from the SDKs you need
import { initializeApp } from 'firebase/app';
import { getFirestore } from 'firebase/firestore';


// Your web app's Firebase configuration
// TODO: add config
const firebaseConfig = {
	apiKey: "",
	authDomain: "",
	projectId: "",
	storageBucket: "",
	messagingSenderId: "",
	appId: "",
	measurementId: ""
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

export {
	getAuth,
	createUserWithEmailAndPassword,
	signInWithEmailAndPassword,
	updateProfile,
	sendPasswordResetEmail
} from 'firebase/auth';
let db = getFirestore(app);

export { db, app };
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