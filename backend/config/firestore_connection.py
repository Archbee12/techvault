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


