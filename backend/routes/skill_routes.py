from flask import Blueprint, jsonify, request
from backend.validation.skill_validation import validate_skill
from backend.services.skill_service import (
  delete_skill,
  get_all_skills,
  get_skill, 
  create_skill,
  update_skill
)

skill_routes = Blueprint('skill_routes', __name__)

# Get all skills
@skill_routes.route('/skills', methods=['GET'])
def get_skills():
  skills = get_all_skills()
  return jsonify(skills), 200

# Get a skill by its ID
@skill_routes.route('/skills/<skill_id>', methods=['GET'])
def get_skill_by_id(skill_id):
  skill = get_skill(skill_id)
  
  if skill:
    return jsonify(skill), 200
  else:
    return jsonify({"error": "Skill not found"}), 404
  
# Create a new skill
@skill_routes.route('/skills', methods=['POST'])
def create_new_skill():
  skill_data = request.get_json()

  error = validate_skill(skill_data)

  if error:
    return jsonify({"error": error}), 400

  new_skill_id = create_skill(skill_data)

  if new_skill_id == "duplicate":
    return jsonify({
      "error": "Skill already exists"
    }), 409

  if new_skill_id:
    return jsonify({
      "message": "Skill created successfully",
      "id": new_skill_id
    }), 201

  return jsonify({
    "error": "Failed to create skill"
  }), 500
 
# Update an existing skill
@skill_routes.route('/skills/<skill_id>', methods=['PUT'])
def update_existing_skill(skill_id):
  skill_data = request.get_json()

  existing_skill = get_skill(skill_id)

  if not existing_skill:
    return jsonify({"error": "Skill not found"}), 404

  error = validate_skill(skill_data, is_update=True)

  if error:
    return jsonify({"error": error}), 400

  success = update_skill(skill_id, skill_data)

  if success:
    return jsonify({
      "message": "Skill updated successfully"
    }), 200
  else:
    return jsonify({
      "error": "Failed to update skill"
    }), 500
  
# Delete an existing skill
@skill_routes.route('/skills/<skill_id>', methods=['DELETE'])
def delete_existing_skill(skill_id):
  existing_skill = get_skill(skill_id)

  if not existing_skill:
    return jsonify({"error": "Skill not found"}), 404

  success = delete_skill(skill_id)

  if success:
    return jsonify({
      "message": "Skill deleted successfully"
    }), 200
  else:
    return jsonify({
      "error": "Failed to delete skill"
    }), 500

