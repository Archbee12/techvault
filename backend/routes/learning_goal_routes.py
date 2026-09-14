from flask import Blueprint, jsonify, request
from backend.validation.learning_goal_validation import validate_learning_goal
from backend.services.learning_goal_service import (
  delete_learning_goal,
  get_all_learning_goals,
  get_learning_goal, create_learning_goal,
  update_learning_goal
)
from backend.services.skill_service import skill_exists

learning_goal_routes = Blueprint('learning_goal_routes', __name__)

# Get all learning goals
@learning_goal_routes.route('/learning_goals', methods=['GET'])
def get_learning_goals():
  learning_goals = get_all_learning_goals()
  return jsonify(learning_goals), 200

# Get a learning goal by its ID
@learning_goal_routes.route('/learning_goals/<learning_goal_id>', methods=['GET'])
def get_learning_goal_by_id(learning_goal_id):
  learning_goal = get_learning_goal(learning_goal_id)
  
  if learning_goal:
    return jsonify(learning_goal), 200
  else:
    return jsonify({"error": "Learning goal not found"}), 404

# Create a new learning goal
@learning_goal_routes.route('/learning_goals', methods=['POST'])
def create_new_learning_goal():
  goal_data = request.get_json()

  error = validate_learning_goal(goal_data)

  if error:
    return jsonify({"error": error}), 400

  # Validate skill_id exists
  skill_id = goal_data.get("skill_id")

  if not skill_exists(skill_id):
    return jsonify({
      "error": "Invalid skill_id: Skill does not exist"
    }), 400

  new_goal_id = create_learning_goal(goal_data)

  if new_goal_id:
    return jsonify({
      "message": "Learning goal created successfully",
      "id": new_goal_id
    }), 201
  else:
    return jsonify({
      "error": "Failed to create learning goal"
    }), 500
  
# Update an existing learning goal
@learning_goal_routes.route('/learning_goals/<learning_goal_id>', methods=['PUT'])
def update_existing_learning_goal(learning_goal_id):
  goal_data = request.get_json()

  existing_goal = get_learning_goal(learning_goal_id)

  if not existing_goal:
    return jsonify({"error": "Learning goal not found"}), 404

  error = validate_learning_goal(goal_data, is_update=True)

  if error:
    return jsonify({"error": error}), 400

  # Validate skill_id if it is being updated
  if "skill_id" in goal_data:
    if not skill_exists(goal_data["skill_id"]):
      return jsonify({
        "error": "Invalid skill_id: Skill does not exist"
      }), 400

  success = update_learning_goal(learning_goal_id, goal_data)

  if success:
    return jsonify({
      "message": "Learning goal updated successfully"
    }), 200
  else:
    return jsonify({
      "error": "Failed to update learning goal"
    }), 500
    
# Delete an existing learning goal
@learning_goal_routes.route('/learning_goals/<learning_goal_id>', methods=['DELETE'])
def delete_existing_learning_goal(learning_goal_id):
  # Check that the learning goal exists
  existing_goal = get_learning_goal(learning_goal_id)

  if not existing_goal:
    return jsonify({"error": "Learning goal not found"}), 404

  # Delete the learning goal
  success = delete_learning_goal(learning_goal_id)

  if success:
    return jsonify({
      "message": "Learning goal deleted successfully"
    }), 200
  else:
    return jsonify({
      "error": "Failed to delete learning goal"
    }), 500

  