# This code establishes a connection to a Firestore database using the Firebase Admin SDK. It loads the service account key from a JSON file, initializes the Firebase app, and creates a Firestore client for database operations.

import firebase_admin
from firebase_admin import credentials, firestore

# Load the service account key JSON file
cred = credentials.Certificate("techvault-e9138-firebase-adminsdk-fbsvc-e2378d988f.json")

# Initialize the Firebase Admin SDK
firebase_admin.initialize_app(cred)

print("Firebase project:", firebase_admin.get_app().project_id)


# Create a Firestore client
db = firestore.client()

print("Firestore connection established successfully.")


