# Overview
TechVault Skill Tracker is a cloud-based skill tracking application designed to help software development students organize the technical skills they are learning and track their progress through individual learning goals. The application uses Python, Flask, and Firebase Firestore to manage a collection of technical skills and their related learning goals. Users can create, view, update, and delete skills and learning goals, while each learning goal is connected to the skill it belongs to.

The project demonstrates the use of a cloud database and a RESTful API to manage related data. It includes data validation, CRUD operations, related collections, and cascade deletion of learning goals when their associated skill is removed. The API is also documented using Swagger/OpenAPI documentation to make the available endpoints easier to understand and test.

# Purpose
The purpose of creating TechVault Skill Tracker is to provide a structured way for software development students to manage what they are learning instead of treating their learning journey as one large task. By breaking technical skills into smaller learning goals, students can focus on gradual progress and recognize the small improvements they make along the way.

This project also serves as a practical learning experience for me as a software development student. Through building TechVault, I am applying what I have learned about Python, Flask, cloud databases, Firebase Firestore, REST APIs, data validation, API documentation, and Git/GitHub while practicing the principle of continuous improvement through small, manageable steps.

Youtube Video: 

[Software Demo Video](http://youtube.link.goes.here)

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
