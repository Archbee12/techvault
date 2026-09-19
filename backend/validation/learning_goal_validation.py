# Validate learning goal data

ALLOWED_LEVELS = [
  "Beginner",
  "Intermediate",
  "Advanced"
]

def validate_learning_goal(goal_data, is_update=False):
  if not goal_data:
    return "Invalid input data"

  required_fields = [
    "skill_id",
    "title",
    "description",
    "level",
    "completed"
  ]

  # POST requires all fields.
  # PUT can contain only the fields being updated.
  if not is_update:
    for field in required_fields:
      if field not in goal_data:
        return f"Missing required field: {field}"

  # Validate skill_id if provided
  if "skill_id" in goal_data:
    if not isinstance(goal_data["skill_id"], str) or not goal_data["skill_id"].strip():
      return "Invalid skill_id: Must be a non-empty string"

  # Validate title if provided
  if "title" in goal_data:
    if not isinstance(goal_data["title"], str) or not goal_data["title"].strip():
      return "Invalid title: Must be a non-empty string"

  # Validate description if provided
  if "description" in goal_data:
    if not isinstance(goal_data["description"], str) or not goal_data["description"].strip():
      return "Invalid description: Must be a non-empty string"

  # Validate level if provided
  if "level" in goal_data:
    if goal_data["level"] not in ALLOWED_LEVELS:
      return f"Invalid level: Must be one of {ALLOWED_LEVELS}"

  # Validate completed if provided
  if "completed" in goal_data:
    if not isinstance(goal_data["completed"], bool):
      return "Completed must be true or false"

  # Prevent unknown fields
  allowed_fields = {
    "skill_id",
    "title",
    "description",
    "level",
    "completed"
  }

  unknown_fields = set(goal_data.keys()) - allowed_fields

  if unknown_fields:
    return f"Invalid fields: {list(unknown_fields)}"

  return None