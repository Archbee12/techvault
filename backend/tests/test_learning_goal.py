# test_learning_goals
from backend.services.learning_goal_service import (
  create_learning_goal,
  get_learning_goal,
  get_all_learning_goals,
  update_learning_goal,
  delete_learning_goal
)

goal_data = {
  "skill_id": "eJtMGjPiHKggvDPMFxjU",
  "title": "Complete Python functions practice",
  "completed": False
}

goal_id = create_learning_goal(goal_data)
if goal_id:
  print(f"Learning goal created successfully with ID: {goal_id}")
  
  retrieved_goal = get_learning_goal(goal_id)

  if retrieved_goal:
    print("Read operation successful!")
    print(retrieved_goal)
  else:
    print("Read operation failed.")
else:
  print("Failed to create learning goal.")
  
all_goals = get_all_learning_goals()
print("\nAll learning goals:")
for goal in all_goals:
  print(f"- {goal['title']} (ID: {goal['id']})")

updated_data = {
  "completed": True
}
if update_learning_goal(goal_id, updated_data):
  print(f"Learning goal with ID {goal_id} updated successfully.")
  
  updated_goal = get_learning_goal(goal_id)
  if updated_goal:
    print("Updated learning goal data:")
    print(updated_goal)
else:
  print("Update operation failed.")

# Delete the learning goal

if delete_learning_goal(goal_id):
  print(f"Learning goal with ID {goal_id} deleted successfully.")
  
  deleted_goal = get_learning_goal(goal_id)
  if not deleted_goal:
    print("Read operation after deletion confirmed that the learning goal no longer exists.")

