from backend.config.firestore_connection import db

# Create a new learning goal
def create_learning_goal(goal_data):
  try:
    # Add the learning goal data to the 'learning_goals' collection in Firestore
    goal_ref = db.collection('learning_goals').add(goal_data)
    print(f"Learning goal created with ID: {goal_ref[1].id}")
    return goal_ref[1].id  # Return the document ID of the newly created learning goal
  
  except Exception as e:
    print(f"Error creating learning goal: {e}")
    return None
  
# Get a learning goal by its ID
def get_learning_goal(goal_id):
  try:
    goal_ref = db.collection('learning_goals').document(goal_id)
    goal = goal_ref.get()
    if goal.exists:
      print(f"Learning goal retrieved: {goal.to_dict()}")
      return goal.to_dict()  # Return the learning goal data as a dictionary
    else:
      print(f"Learning goal with ID {goal_id} does not exist.")
      return None
  except Exception as e:
    print(f"Error retrieving learning goal: {e}")
    return None
  
# Get all learning goals
def get_all_learning_goals():
  try:
    goals = db.collection('learning_goals').stream()
    goal_list = []
    
    for goal in goals:
      goal_data = goal.to_dict()
      goal_data['id'] = goal.id  # Include the document ID in the learning goal data
      goal_list.append(goal_data)
      
    return goal_list  # Return a list of all learning goals
    
  except Exception as e:
    print(f"Error retrieving learning goals: {e}")
    return []
  
# Update Learning Goal
def update_learning_goal(goal_id, updated_data):
  try:
    goal_ref = db.collection('learning_goals').document(goal_id)
    
    # update the specified fields in the learning goal document
    goal_ref.update(updated_data)
    
    print(f"Learning goal with ID {goal_id} updated successfully.")
    return True
    
  except Exception as e:
      print(f"Error updating learning goal: {e}")
      return False

# Delete Learning Goal
def delete_learning_goal(goal_id):
  try:
    goal_ref = db.collection('learning_goals').document(goal_id)
    
    # Delete the learning goal document
    goal_ref.delete()
    
    print(f"Learning goal with ID {goal_id} deleted successfully.")
    return True
    
  except Exception as e:
      print(f"Error deleting learning goal: {e}")
      return False  