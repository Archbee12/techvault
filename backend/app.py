from flask import Flask, jsonify
from flasgger import Swagger
from backend.routes.skill_routes import skill_routes
from backend.routes.learning_goal_routes import learning_goal_routes
from backend.api_docs.swagger_config import initialize_swagger

# Create the Flask application
app = Flask(__name__)

# Register the skill routes blueprint
app.register_blueprint(skill_routes)

# Register the learning goal routes blueprint
app.register_blueprint(learning_goal_routes)

# Initialize Swagger with the app
initialize_swagger(app)

# Define a simple route to check if the API is running
@app.route("/")
def home():
    return jsonify({
        "message": "TechVault Skill Tracker API is running!"
    })

if __name__ == "__main__":
    app.run(debug=True)