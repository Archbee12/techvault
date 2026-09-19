# This code provides a set of functions to manage skills in a Firestore database. It includes functions to create, retrieve, update, and delete skills. Each function interacts with the Firestore database using the Firebase Admin SDK and handles exceptions that may occur during database operations.

from backend.config.firestore_connection import db

# Create a new skill
def create_skill(skill_data):
  try:
    skill_id = skill_data["name"].strip().lower().replace(" ", "-")

    skill_ref = db.collection("skills").document(skill_id)

    # Prevent duplicate skill IDs
    if skill_ref.get().exists:
      print(f"Skill with ID {skill_id} already exists.")
      return "duplicate"

    skill_ref.set(skill_data)

    print(f"Skill created with ID: {skill_id}")
    return skill_id

  except Exception as e:
    print(f"Error creating skill: {e}")
    return None  # Return a specific error message for duplicate skill creation
      
# Get a skill by its ID
def get_skill(skill_id):
  try:
    skill_ref = db.collection('skills').document(skill_id)
    skill = skill_ref.get()
    if skill.exists:
      print(f"Skill retrieved: {skill.to_dict()}")
      return skill.to_dict()  # Return the skill data as a dictionary
    else:
      print(f"Skill with ID {skill_id} does not exist.")
      return None
  except Exception as e:
    print(f"Error retrieving skill: {e}")
    return None
    
# Get all skills
def get_all_skills():
  try:
    skills = db.collection('skills').stream()
    skill_list = []
    
    for skill in skills:
      skill_data = skill.to_dict()
      skill_data['id'] = skill.id  # Include the document ID in the skill data
      skill_list.append(skill_data)
        
    return skill_list  # Return a list of all skills
  except Exception as e:
    print(f"Error retrieving skills: {e}")
    return []
    
# Update Skill
def update_skill(skill_id, updated_data):
  try:
    skill_ref = db.collection('skills').document(skill_id)
    
    # update the specified fields in the skill document
    skill_ref.update(updated_data)
    
    print(f"Skill with ID {skill_id} updated successfully.")
    return True
    
  except Exception as e:
      print(f"Error updating skill: {e}")
      return False
    
# Delete a skill and its associated learning goals
def delete_skill(skill_id):
  try:
    skill_ref = db.collection("skills").document(skill_id)

    # Check if the skill exists
    if not skill_ref.get().exists:
      print(f"Skill with ID {skill_id} does not exist.")
      return False

    # Find learning goals associated with this skill
    learning_goals = db.collection("learning_goals") \
      .where("skill_id", "==", skill_id) \
      .stream()

    # Delete associated learning goals
    for goal in learning_goals:
      db.collection("learning_goals").document(goal.id).delete()

    # Delete the skill
    skill_ref.delete()

    print(f"Skill with ID {skill_id} and its learning goals deleted successfully.")
    return True

  except Exception as e:
    print(f"Error deleting skill: {e}")
    return False
    
# Check if a skill exists by its ID
def skill_exists(skill_id):
    try:
        skill_ref = db.collection('skills').document(skill_id)
        return skill_ref.get().exists
    except Exception as e:
        print(f"Error checking if skill exists: {e}")
        return False