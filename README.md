# Overview
TechVault Skill Tracker is a cloud-based application I developed to strengthen my skills in backend development, REST APIs, and cloud database integration. The application provides a structured way to organize technical skills and break them down into smaller learning goals that can be tracked as completed or incomplete.

The software is built with Python and Flask and integrates with Firebase Firestore as its cloud database. The application provides REST API endpoints that allow users to create, retrieve, update, and delete skills and learning goals. Each learning goal is associated with a skill, allowing related data to be managed between the two Firestore collections. The API can be accessed and tested through the documented endpoints using tools such as the VS Code REST Client and Swagger UI.

# Purpose
The purpose of writing this software was to gain practical experience working with a cloud database while improving my ability to design and build backend applications. I also wanted to apply a continuous-learning approach by breaking a larger software-development goal into smaller features, such as establishing the database connection, creating CRUD operations, validating data, connecting related collections, and documenting the API.

Youtube Video: 

[Software Demo Video](http://youtube.link.goes.here)

# Cloud Database

TechVault uses Firebase Cloud Firestore, a cloud-based NoSQL database. Firestore stores the application's data as collections containing individual documents, allowing the Flask backend to create, retrieve, update, and delete data in the cloud.

## The database contains two related collections:

### skills

The skills collection stores the technical skills available in the application. Each skill contains:

- **name** – Name of the technical skill
- **category** – Category of the skill
- **description** – Description of the skill
- **level** – Beginner, Intermediate, or Advanced

### learning_goals

The learning_goals collection stores individual learning goals associated with a skill. Each learning goal contains:

- **skill_id** – Identifies the skill associated with the goal
- **title** – Name of the learning goal
- **description** – Description of what should be learned
- **level** – Beginner, Intermediate, or Advanced
- **completed** – Indicates whether the learning goal has been completed

The relationship between the collections is one-to-many, where one skill can have multiple learning goals. When a skill is deleted through the API, its associated learning goals are also deleted.

# Development Environment

## Development Tools
- **Visual Studio Code** – Primary code editor and development environment.
- **Git** – Used for version control and tracking project changes.
- **GitHub** – Used to store and manage the project's source code repository.
- **VS Code REST Client** – Used to test API requests and responses during development.
- **Python virtual environment (.venv)** – Used to isolate the project's Python dependencies.

## Programming Language
- **Python 3.14.7** – Used to develop the backend application and interact with Firebase Firestore.

## Cloud Database
- **Firebase Firestore** – Used as the cloud NoSQL database for storing skills and learning goals.
- **Firebase Admin SDK** – Used by the Python backend to securely connect and communicate with Firestore.

## Backend Framework
- **Flask** – Used to build the RESTful API and define the application's routes and endpoints.

## API Documentation
- **Flasgger / Swagger UI** – Used to document and test the REST API endpoints.

# Useful Websites

Firebase Documentation: https://firebase.google.com/docs/firestore/quickstart

Get data with Cloud: https://firebase.google.com/docs/firestore/query-data/get-data 

Python Client Database: https://docs.cloud.google.com/python/docs/reference/firestore/latest

Python Backend API: https://www.youtube.com/watch?v=gz0NWqTVo60 

More Helpful resources: https://www.youtube.com/watch?v=yylnC3dr_no&t=394s 

# Future Work
- **Add a user interface so students can interact with their skills and learning goals without directly using the API.**
- **Add user authentication so each student can manage their own skills and learning goals securely.**
- **Add progress tracking and summaries to help users see their learning progress over time.**
- **Improve the API documentation and add more detailed examples where useful.**
- **Deploy the Flask API so the application can be accessed outside the local development environment.**
