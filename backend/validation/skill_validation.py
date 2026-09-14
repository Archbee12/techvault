# Validate skill data

ALLOWED_CATEGORIES = [
  "Programming Language",
  "Web Development",
  "Database",
  "Cloud Computing",
  "DevOps",
  "Mobile Development",
  "Data Science",
  "Artificial Intelligence",
  "Cybersecurity",
  "Software Development"
]

ALLOWED_LEVELS = [
  "Beginner",
  "Intermediate",
  "Advanced"
]


def validate_skill(skill_data, is_update=False):
  if not skill_data:
    return "Invalid input data"

  required_fields = [
    "name",
    "category",
    "description",
    "level"
  ]

  # POST requires all fields.
  # PUT can contain only the fields being updated.
  if not is_update:
    for field in required_fields:
      if field not in skill_data:
        return f"Missing required field: {field}"

  # Validate name if provided
  if "name" in skill_data:
    if not isinstance(skill_data["name"], str) or not skill_data["name"].strip():
      return "Invalid name: Must be a non-empty string"

  # Validate category if provided
  if "category" in skill_data:
    if skill_data["category"] not in ALLOWED_CATEGORIES:
      return f"Invalid category: Must be one of {ALLOWED_CATEGORIES}"

  # Validate description if provided
  if "description" in skill_data:
    if not isinstance(skill_data["description"], str) or not skill_data["description"].strip():
      return "Invalid description: Must be a non-empty string"

  # Validate level if provided
  if "level" in skill_data:
    if skill_data["level"] not in ALLOWED_LEVELS:
      return f"Invalid level: Must be one of {ALLOWED_LEVELS}"

  # Prevent unknown fields
  allowed_fields = {
    "name",
    "category",
    "description",
    "level"
  }

  unknown_fields = set(skill_data.keys()) - allowed_fields

  if unknown_fields:
    return f"Invalid fields: {list(unknown_fields)}"

  return None