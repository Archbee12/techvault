from backend.config.firestore_connection import db


skills = [
    {
        "id": "python",
        "name": "Python",
        "category": "Programming Language",
        "description": "A general-purpose programming language used for software development, automation, data analysis, web development, and artificial intelligence.",
        "level": "Beginner"
    },
    {
        "id": "javascript",
        "name": "JavaScript",
        "category": "Programming Language",
        "description": "A programming language widely used to create interactive web applications and build software across frontend and backend environments.",
        "level": "Beginner"
    },
    {
        "id": "typescript",
        "name": "TypeScript",
        "category": "Programming Language",
        "description": "A strongly typed programming language built on JavaScript and commonly used for developing reliable and maintainable web applications.",
        "level": "Beginner"
    },
    {
        "id": "rust",
        "name": "Rust",
        "category": "Programming Language",
        "description": "A systems programming language focused on performance, memory safety, and reliable software development.",
        "level": "Beginner"
    },
    {
        "id": "html-css",
        "name": "HTML & CSS",
        "category": "Web Development",
        "description": "Core web technologies used to structure, style, and create responsive websites and web interfaces.",
        "level": "Beginner"
    },
    {
        "id": "react",
        "name": "React",
        "category": "Web Development",
        "description": "A JavaScript library used to build component-based user interfaces and modern web applications.",
        "level": "Beginner"
    },
    {
        "id": "nodejs",
        "name": "Node.js",
        "category": "Web Development",
        "description": "A JavaScript runtime used to build server-side applications, APIs, and backend services.",
        "level": "Beginner"
    },
    {
        "id": "full-stack-web-development",
        "name": "Full-Stack Web Development",
        "category": "Web Development",
        "description": "The development of complete web applications involving frontend interfaces, backend services, APIs, databases, authentication, and deployment.",
        "level": "Beginner"
    },
    {
        "id": "sql",
        "name": "SQL",
        "category": "Database",
        "description": "A language used to store, retrieve, modify, and analyze data in relational databases.",
        "level": "Beginner"
    },
    {
        "id": "postgresql",
        "name": "PostgreSQL",
        "category": "Database",
        "description": "A powerful open-source relational database system used for storing and managing structured application data.",
        "level": "Beginner"
    },
    {
        "id": "mongodb",
        "name": "MongoDB",
        "category": "Database",
        "description": "A document-oriented NoSQL database commonly used for flexible and scalable application data storage.",
        "level": "Beginner"
    },
    {
        "id": "firebase-firestore",
        "name": "Firebase / Firestore",
        "category": "Cloud Computing",
        "description": "A cloud-based development platform and NoSQL database service used to build and store data for modern applications.",
        "level": "Beginner"
    }
]


for skill in skills:
    skill_id = skill["id"]

    skill_data = {
        "name": skill["name"],
        "category": skill["category"],
        "description": skill["description"],
        "level": skill["level"]
    }

    db.collection("skills").document(skill_id).set(skill_data)

    print(f"Skill added: {skill['name']}")