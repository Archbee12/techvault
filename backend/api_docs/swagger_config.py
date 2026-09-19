# This code sets up the Swagger configuration for the TechVault Skill Tracker API. The `initialize_swagger` function initializes Swagger with the provided template for use in a Flask application.

from flasgger import Swagger


swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "TechVault Skill Tracker API",
        "description": (
            "API for managing technical skills and learning goals "
            "using Flask and Firebase Firestore."
        ),
        "version": "1.0.0"
    },
    "basePath": "/",
    "schemes": [
        "http"
    ],
    "tags": [
        {
            "name": "Skills",
            "description": "Operations for managing technical skills"
        },
        {
            "name": "Learning Goals",
            "description": "Operations for managing learning goals"
        }
    ],
    "definitions": {
        "Skill": {
            "type": "object",
            "required": [
                "name",
                "category",
                "description",
                "level"
            ],
            "properties": {
                "id": {
                    "type": "string",
                    "example": "python"
                },
                "name": {
                    "type": "string",
                    "example": "Python"
                },
                "category": {
                    "type": "string",
                    "example": "Programming Language"
                },
                "description": {
                    "type": "string",
                    "example": "A high-level programming language."
                },
                "level": {
                    "type": "string",
                    "enum": [
                        "Beginner",
                        "Intermediate",
                        "Advanced"
                    ],
                    "example": "Beginner"
                }
            }
        },

        "SkillInput": {
            "type": "object",
            "required": [
                "name",
                "category",
                "description",
                "level"
            ],
            "properties": {
                "name": {
                    "type": "string",
                    "example": "Docker"
                },
                "category": {
                    "type": "string",
                    "example": "DevOps"
                },
                "description": {
                    "type": "string",
                    "example": (
                        "Learn how to build, run, and manage "
                        "applications using Docker containers."
                    )
                },
                "level": {
                    "type": "string",
                    "enum": [
                        "Beginner",
                        "Intermediate",
                        "Advanced"
                    ],
                    "example": "Beginner"
                }
            }
        },

        "LearningGoal": {
            "type": "object",
            "required": [
                "skill_id",
                "title",
                "description",
                "level",
                "completed"
            ],
            "properties": {
                "id": {
                    "type": "string",
                    "example": "abc123"
                },
                "skill_id": {
                    "type": "string",
                    "example": "python"
                },
                "title": {
                    "type": "string",
                    "example": "Practice Python Functions"
                },
                "description": {
                    "type": "string",
                    "example": (
                        "Practice creating functions with parameters "
                        "and return values."
                    )
                },
                "level": {
                    "type": "string",
                    "enum": [
                        "Beginner",
                        "Intermediate",
                        "Advanced"
                    ],
                    "example": "Beginner"
                },
                "completed": {
                    "type": "boolean",
                    "example": False
                }
            }
        },

        "LearningGoalInput": {
            "type": "object",
            "required": [
                "skill_id",
                "title",
                "description",
                "level",
                "completed"
            ],
            "properties": {
                "skill_id": {
                    "type": "string",
                    "example": "python"
                },
                "title": {
                    "type": "string",
                    "example": "Practice Python Functions"
                },
                "description": {
                    "type": "string",
                    "example": (
                        "Practice creating functions with parameters "
                        "and return values."
                    )
                },
                "level": {
                    "type": "string",
                    "enum": [
                        "Beginner",
                        "Intermediate",
                        "Advanced"
                    ],
                    "example": "Beginner"
                },
                "completed": {
                    "type": "boolean",
                    "example": False
                }
            }
        }
    },

    "paths": {
        "/skills": {
            "get": {
                "tags": [
                    "Skills"
                ],
                "summary": "Get all skills",
                "description": "Returns a list of all technical skills.",
                "responses": {
                    "200": {
                        "description": "Skills retrieved successfully.",
                        # "schema": {
                        #     "type": "array",
                        #     "items": {
                        #         "$ref": "#/definitions/Skill"
                        #     }
                        # }
                    }
                }
            },

            "post": {
                "tags": [
                    "Skills"
                ],
                "summary": "Create a new skill",
                "description": "Creates a new technical skill.",
                "parameters": [
                    {
                        "name": "body",
                        "in": "body",
                        "required": True,
                        "schema": {
                            "$ref": "#/definitions/SkillInput"
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "Skill created successfully."
                    },
                    "400": {
                        "description": "Invalid input data."
                    },
                    "409": {
                        "description": "Skill already exists."
                    },
                    "500": {
                        "description": "Failed to create skill."
                    }
                }
            }
        },

        "/skills/{skill_id}": {
            "get": {
                "tags": [
                    "Skills"
                ],
                "summary": "Get a skill by ID",
                "description": "Returns one skill using its ID.",
                "parameters": [
                    {
                        "name": "skill_id",
                        "in": "path",
                        "required": True,
                        "type": "string",
                        "example": "python"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Skill retrieved successfully.",
                        # "schema": {
                        #     "$ref": "#/definitions/Skill"
                        # }
                    },
                    "404": {
                        "description": "Skill not found."
                    }
                }
            },

            "put": {
                "tags": [
                    "Skills"
                ],
                "summary": "Update a skill",
                "description": "Updates one or more fields of an existing skill.",
                "parameters": [
                    {
                        "name": "skill_id",
                        "in": "path",
                        "required": True,
                        "type": "string",
                        "example": "python"
                    },
                    {
                        "name": "body",
                        "in": "body",
                        "required": True,
                        "schema": {
                            "$ref": "#/definitions/SkillInput"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Skill updated successfully."
                    },
                    "400": {
                        "description": "Invalid input data."
                    },
                    "404": {
                        "description": "Skill not found."
                    },
                    "500": {
                        "description": "Failed to update skill."
                    }
                }
            },

            "delete": {
                "tags": [
                    "Skills"
                ],
                "summary": "Delete a skill",
                "description": (
                    "Deletes a skill and all learning goals "
                    "associated with that skill."
                ),
                "parameters": [
                    {
                        "name": "skill_id",
                        "in": "path",
                        "required": True,
                        "type": "string",
                        "example": "python"
                    }
                ],
                "responses": {
                    "200": {
                        "description": (
                            "Skill and associated learning goals "
                            "deleted successfully."
                        )
                    },
                    "404": {
                        "description": "Skill not found."
                    },
                    "500": {
                        "description": "Failed to delete skill."
                    }
                }
            }
        },

        "/learning_goals": {
            "get": {
                "tags": [
                    "Learning Goals"
                ],
                "summary": "Get all learning goals",
                "description": (
                    "Returns a list of all learning goals."
                ),
                "responses": {
                    "200": {
                        "description": (
                            "Learning goals retrieved successfully."
                        ),
                        # "schema": {
                        #     "type": "array",
                        #     "items": {
                        #         "$ref": "#/definitions/LearningGoal"
                        #     }
                        # }
                    }
                }
            },

            "post": {
                "tags": [
                    "Learning Goals"
                ],
                "summary": "Create a new learning goal",
                "description": (
                    "Creates a learning goal associated with "
                    "an existing skill."
                ),
                "parameters": [
                    {
                        "name": "body",
                        "in": "body",
                        "required": True,
                        "schema": {
                            "$ref": "#/definitions/LearningGoalInput"
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": (
                            "Learning goal created successfully."
                        )
                    },
                    "400": {
                        "description": "Invalid input data."
                    },
                    "500": {
                        "description": (
                            "Failed to create learning goal."
                        )
                    }
                }
            }
        },

        "/learning_goals/{learning_goal_id}": {
            "get": {
                "tags": [
                    "Learning Goals"
                ],
                "summary": "Get a learning goal by ID",
                "description": (
                    "Returns one learning goal using its ID."
                ),
                "parameters": [
                    {
                        "name": "learning_goal_id",
                        "in": "path",
                        "required": True,
                        "type": "string",
                        "example": "abc123"
                    }
                ],
                "responses": {
                    "200": {
                        "description": (
                            "Learning goal retrieved successfully."
                        ),
                        # "schema": {
                        #     "$ref": "#/definitions/LearningGoal"
                        # }
                    },
                    "404": {
                        "description": "Learning goal not found."
                    }
                }
            },

            "put": {
                "tags": [
                    "Learning Goals"
                ],
                "summary": "Update a learning goal",
                "description": (
                    "Updates one or more fields of an existing "
                    "learning goal."
                ),
                "parameters": [
                    {
                        "name": "learning_goal_id",
                        "in": "path",
                        "required": True,
                        "type": "string",
                        "example": "abc123"
                    },
                    {
                        "name": "body",
                        "in": "body",
                        "required": True,
                        "schema": {
                            "$ref": "#/definitions/LearningGoalInput"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": (
                            "Learning goal updated successfully."
                        )
                    },
                    "400": {
                        "description": "Invalid input data."
                    },
                    "404": {
                        "description": (
                            "Learning goal not found."
                        )
                    },
                    "500": {
                        "description": (
                            "Failed to update learning goal."
                        )
                    }
                }
            },

            "delete": {
                "tags": [
                    "Learning Goals"
                ],
                "summary": "Delete a learning goal",
                "description": (
                    "Deletes one learning goal."
                ),
                "parameters": [
                    {
                        "name": "learning_goal_id",
                        "in": "path",
                        "required": True,
                        "type": "string",
                        "example": "abc123"
                    }
                ],
                "responses": {
                    "200": {
                        "description": (
                            "Learning goal deleted successfully."
                        )
                    },
                    "404": {
                        "description": (
                            "Learning goal not found."
                        )
                    },
                    "500": {
                        "description": (
                            "Failed to delete learning goal."
                        )
                    }
                }
            }
        }
    }
}


def initialize_swagger(app):
    return Swagger(app, template=swagger_template)