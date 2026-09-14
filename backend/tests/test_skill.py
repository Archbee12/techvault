from backend.services.skill_service import (
    create_skill,
    get_skill,
    get_all_skills,
    update_skill,
    delete_skill
)

python_skill = {
    "name": "Python Programming",
    "category": "Programming Language",
    "description": "A high-level, interpreted programming language known for its readability and versatility.",
    "level": "Intermediate",
    "progress": 75,
}

skill_id = create_skill(python_skill)
if skill_id:
    print(f"Skill created successfully with ID: {skill_id}")
    
    retrieved_skill = get_skill(skill_id)

    if retrieved_skill:
        print("Read operation successful!")
    else:
        print("Read operation failed.")
else:
    print("Failed to create skill.")
    
    
all_skills = get_all_skills()
print("\nAll skills:")
for skill in all_skills:
    print(f"- {skill['name']} (ID: {skill['id']})")
    
updated_data = {
    "progress": 90,
    "level": "Advanced"
}

if update_skill(skill_id, updated_data):
    print(f"Skill with ID {skill_id} updated successfully.")
    
    updated_skill = get_skill(skill_id)
    if updated_skill:
      print("Updated skill data:")
      print(updated_skill)
        
if delete_skill(skill_id):
    print(f"Skill with ID {skill_id} deleted successfully.")
    
    deleted_skill = get_skill(skill_id)
    if not deleted_skill:
        print("Read operation after deletion confirmed that the skill no longer exists.")


