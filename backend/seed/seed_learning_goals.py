from backend.config.firestore_connection import db


learning_goals = [

    # =========================================================
    # PYTHON
    # =========================================================

    # Python - Beginner
    {
        "id": "python-syntax",
        "skill_id": "python",
        "title": "Python Syntax",
        "description": "Learn how Python code is structured, including indentation, statements, comments, and basic syntax rules.",
        "level": "Beginner"
    },
    {
        "id": "python-variables-data-types",
        "skill_id": "python",
        "title": "Variables & Data Types",
        "description": "Learn how to store, access, and work with different types of values in Python.",
        "level": "Beginner"
    },
    {
        "id": "python-conditionals",
        "skill_id": "python",
        "title": "Conditional Statements",
        "description": "Learn how to make decisions in a program using if, elif, and else statements.",
        "level": "Beginner"
    },
    {
        "id": "python-loops",
        "skill_id": "python",
        "title": "Loops",
        "description": "Learn how to repeat operations using for and while loops and control how loops execute.",
        "level": "Beginner"
    },
    {
        "id": "python-functions",
        "skill_id": "python",
        "title": "Functions",
        "description": "Learn how to create reusable blocks of code, use parameters, and return values from functions.",
        "level": "Beginner"
    },
    {
        "id": "python-lists-dictionaries",
        "skill_id": "python",
        "title": "Lists & Dictionaries",
        "description": "Learn how to store, organize, access, and modify collections of data using lists and dictionaries.",
        "level": "Beginner"
    },
    {
        "id": "python-file-handling",
        "skill_id": "python",
        "title": "File Handling",
        "description": "Learn how to read from and write to files and manage file data safely in Python.",
        "level": "Beginner"
    },
    {
        "id": "python-exceptions",
        "skill_id": "python",
        "title": "Exceptions",
        "description": "Learn how to identify, handle, and manage errors using Python's exception-handling features.",
        "level": "Beginner"
    },

    # Python - Intermediate
    {
        "id": "python-oop",
        "skill_id": "python",
        "title": "Object-Oriented Programming",
        "description": "Learn how to design programs using classes, objects, inheritance, encapsulation, and polymorphism.",
        "level": "Intermediate"
    },
    {
        "id": "python-modules-packages",
        "skill_id": "python",
        "title": "Modules & Packages",
        "description": "Learn how to organize Python code into reusable modules and packages and work with external packages.",
        "level": "Intermediate"
    },
    {
        "id": "python-virtual-environments",
        "skill_id": "python",
        "title": "Virtual Environments",
        "description": "Learn how to create and manage isolated Python environments and their dependencies.",
        "level": "Intermediate"
    },
    {
        "id": "python-apis",
        "skill_id": "python",
        "title": "APIs",
        "description": "Learn how Python applications communicate with external services through APIs and HTTP requests.",
        "level": "Intermediate"
    },
    {
        "id": "python-testing",
        "skill_id": "python",
        "title": "Testing",
        "description": "Learn how to write and run tests to verify that Python code behaves as expected.",
        "level": "Intermediate"
    },
    {
        "id": "python-database-access",
        "skill_id": "python",
        "title": "Database Access",
        "description": "Learn how Python applications connect to databases, retrieve data, and perform database operations.",
        "level": "Intermediate"
    },
    {
        "id": "python-advanced-functions",
        "skill_id": "python",
        "title": "Advanced Functions",
        "description": "Learn advanced function concepts such as decorators, lambda functions, closures, and flexible arguments.",
        "level": "Intermediate"
    },

    # Python - Advanced
    {
        "id": "python-advanced-oop",
        "skill_id": "python",
        "title": "Advanced OOP",
        "description": "Explore advanced object-oriented design techniques and patterns for building maintainable Python applications.",
        "level": "Advanced"
    },
    {
        "id": "python-async-programming",
        "skill_id": "python",
        "title": "Async Programming",
        "description": "Learn how asynchronous programming works in Python and how to handle concurrent tasks efficiently.",
        "level": "Advanced"
    },
    {
        "id": "python-performance",
        "skill_id": "python",
        "title": "Performance",
        "description": "Learn how to identify performance bottlenecks and improve the efficiency of Python applications.",
        "level": "Advanced"
    },
    {
        "id": "python-application-architecture",
        "skill_id": "python",
        "title": "Application Architecture",
        "description": "Learn how to structure larger Python applications using maintainable architecture and sound design principles.",
        "level": "Advanced"
    },
    {
        "id": "python-advanced-testing",
        "skill_id": "python",
        "title": "Advanced Testing",
        "description": "Learn advanced testing strategies for reliable, maintainable, and production-ready Python applications.",
        "level": "Advanced"
    },
    {
        "id": "python-production-applications",
        "skill_id": "python",
        "title": "Production Applications",
        "description": "Learn how to prepare, deploy, monitor, and maintain Python applications in real-world production environments.",
        "level": "Advanced"
    },


    # =========================================================
    # JAVASCRIPT
    # =========================================================

    # JavaScript - Beginner
    {
        "id": "javascript-syntax",
        "skill_id": "javascript",
        "title": "JavaScript Syntax",
        "description": "Learn the basic structure and syntax rules used to write JavaScript programs.",
        "level": "Beginner"
    },
    {
        "id": "javascript-variables-data-types",
        "skill_id": "javascript",
        "title": "Variables & Data Types",
        "description": "Learn how to store values and work with strings, numbers, booleans, arrays, objects, and other JavaScript data types.",
        "level": "Beginner"
    },
    {
        "id": "javascript-operators",
        "skill_id": "javascript",
        "title": "Operators",
        "description": "Learn how arithmetic, comparison, logical, assignment, and other operators are used in JavaScript.",
        "level": "Beginner"
    },
    {
        "id": "javascript-conditionals",
        "skill_id": "javascript",
        "title": "Conditional Statements",
        "description": "Learn how to control program decisions using if, else, and switch statements.",
        "level": "Beginner"
    },
    {
        "id": "javascript-loops",
        "skill_id": "javascript",
        "title": "Loops",
        "description": "Learn how to repeat operations using for, while, and related looping techniques.",
        "level": "Beginner"
    },
    {
        "id": "javascript-functions",
        "skill_id": "javascript",
        "title": "Functions",
        "description": "Learn how to create reusable functions, pass arguments, and return values.",
        "level": "Beginner"
    },
    {
        "id": "javascript-arrays-objects",
        "skill_id": "javascript",
        "title": "Arrays & Objects",
        "description": "Learn how to store, access, modify, and organize collections of data using arrays and objects.",
        "level": "Beginner"
    },
    {
        "id": "javascript-dom-basics",
        "skill_id": "javascript",
        "title": "DOM Basics",
        "description": "Learn how JavaScript interacts with HTML elements through the Document Object Model.",
        "level": "Beginner"
    },
    {
        "id": "javascript-events",
        "skill_id": "javascript",
        "title": "Events",
        "description": "Learn how to respond to user actions such as clicks, keyboard input, and form submissions.",
        "level": "Beginner"
    },

    # JavaScript - Intermediate
    {
        "id": "javascript-array-methods",
        "skill_id": "javascript",
        "title": "Array Methods",
        "description": "Learn how to process and transform arrays using methods such as map, filter, reduce, find, and forEach.",
        "level": "Intermediate"
    },
    {
        "id": "javascript-destructuring",
        "skill_id": "javascript",
        "title": "Destructuring",
        "description": "Learn how to extract values from arrays and objects using JavaScript destructuring syntax.",
        "level": "Intermediate"
    },
    {
        "id": "javascript-modules",
        "skill_id": "javascript",
        "title": "Modules",
        "description": "Learn how to organize JavaScript applications into reusable modules using imports and exports.",
        "level": "Intermediate"
    },
    {
        "id": "javascript-error-handling",
        "skill_id": "javascript",
        "title": "Error Handling",
        "description": "Learn how to detect and handle errors using try, catch, finally, and custom error techniques.",
        "level": "Intermediate"
    },
    {
        "id": "javascript-async",
        "skill_id": "javascript",
        "title": "Asynchronous JavaScript",
        "description": "Learn how JavaScript handles tasks that complete later using callbacks, promises, and async functions.",
        "level": "Intermediate"
    },
    {
        "id": "javascript-promises",
        "skill_id": "javascript",
        "title": "Promises",
        "description": "Learn how promises represent asynchronous operations and how to handle successful and failed results.",
        "level": "Intermediate"
    },
    {
        "id": "javascript-fetch-apis",
        "skill_id": "javascript",
        "title": "Fetch & APIs",
        "description": "Learn how JavaScript applications communicate with external services using HTTP requests and APIs.",
        "level": "Intermediate"
    },
    {
        "id": "javascript-classes",
        "skill_id": "javascript",
        "title": "Classes",
        "description": "Learn how to create objects and organize related data and behavior using JavaScript classes.",
        "level": "Intermediate"
    },
    {
        "id": "javascript-testing",
        "skill_id": "javascript",
        "title": "Testing",
        "description": "Learn how to test JavaScript code and verify that functions and application behavior work correctly.",
        "level": "Intermediate"
    },

    # JavaScript - Advanced
    {
        "id": "javascript-advanced-async",
        "skill_id": "javascript",
        "title": "Advanced Async Programming",
        "description": "Explore advanced asynchronous patterns for coordinating multiple operations and managing complex workflows.",
        "level": "Advanced"
    },
    {
        "id": "javascript-closures",
        "skill_id": "javascript",
        "title": "Closures & Execution Context",
        "description": "Learn how closures, scope, and execution contexts affect how JavaScript code behaves.",
        "level": "Advanced"
    },
    {
        "id": "javascript-performance",
        "skill_id": "javascript",
        "title": "Performance",
        "description": "Learn how to identify and improve performance issues in JavaScript applications.",
        "level": "Advanced"
    },
    {
        "id": "javascript-design-patterns",
        "skill_id": "javascript",
        "title": "Design Patterns",
        "description": "Learn reusable approaches for solving common software design problems in JavaScript applications.",
        "level": "Advanced"
    },
    {
        "id": "javascript-advanced-testing",
        "skill_id": "javascript",
        "title": "Advanced Testing",
        "description": "Learn advanced testing strategies for complex JavaScript applications and production code.",
        "level": "Advanced"
    },
    {
        "id": "javascript-application-architecture",
        "skill_id": "javascript",
        "title": "Application Architecture",
        "description": "Learn how to structure larger JavaScript applications for maintainability, scalability, and reliability.",
        "level": "Advanced"
    },
    {
        "id": "javascript-security",
        "skill_id": "javascript",
        "title": "Security",
        "description": "Learn common JavaScript and web application security concerns and how to reduce security risks.",
        "level": "Advanced"
    },
    {
        "id": "javascript-production",
        "skill_id": "javascript",
        "title": "Production Applications",
        "description": "Learn how to prepare, deploy, monitor, and maintain JavaScript applications in production environments.",
        "level": "Advanced"
    },


    # =========================================================
    # TYPESCRIPT
    # =========================================================

    # TypeScript - Beginner
    {
        "id": "typescript-syntax",
        "skill_id": "typescript",
        "title": "TypeScript Syntax",
        "description": "Learn the basic syntax and structure of TypeScript and how it extends JavaScript.",
        "level": "Beginner"
    },
    {
        "id": "typescript-types",
        "skill_id": "typescript",
        "title": "Types",
        "description": "Learn how to use TypeScript types to describe strings, numbers, objects, arrays, and other values.",
        "level": "Beginner"
    },
    {
        "id": "typescript-interfaces",
        "skill_id": "typescript",
        "title": "Interfaces",
        "description": "Learn how interfaces define the structure and shape of objects in TypeScript.",
        "level": "Beginner"
    },
    {
        "id": "typescript-functions",
        "skill_id": "typescript",
        "title": "Typed Functions",
        "description": "Learn how to add types to function parameters, return values, and callbacks.",
        "level": "Beginner"
    },
    {
        "id": "typescript-unions",
        "skill_id": "typescript",
        "title": "Union & Literal Types",
        "description": "Learn how to restrict values using union types, literal types, and related TypeScript features.",
        "level": "Beginner"
    },

    # TypeScript - Intermediate
    {
        "id": "typescript-generics",
        "skill_id": "typescript",
        "title": "Generics",
        "description": "Learn how generics allow reusable code to work safely with different types.",
        "level": "Intermediate"
    },
    {
        "id": "typescript-advanced-types",
        "skill_id": "typescript",
        "title": "Advanced Types",
        "description": "Learn advanced type features such as intersections, type guards, mapped types, and conditional types.",
        "level": "Intermediate"
    },
    {
        "id": "typescript-modules",
        "skill_id": "typescript",
        "title": "Modules",
        "description": "Learn how to organize TypeScript applications into reusable files and modules.",
        "level": "Intermediate"
    },
    {
        "id": "typescript-classes",
        "skill_id": "typescript",
        "title": "Classes",
        "description": "Learn how to create strongly typed classes and apply object-oriented programming principles.",
        "level": "Intermediate"
    },
    {
        "id": "typescript-configuration",
        "skill_id": "typescript",
        "title": "TypeScript Configuration",
        "description": "Learn how tsconfig settings control compilation, type checking, and project behavior.",
        "level": "Intermediate"
    },
    {
        "id": "typescript-testing",
        "skill_id": "typescript",
        "title": "Testing",
        "description": "Learn how to test TypeScript applications while maintaining reliable type checking.",
        "level": "Intermediate"
    },

    # TypeScript - Advanced
    {
        "id": "typescript-type-design",
        "skill_id": "typescript",
        "title": "Type Design",
        "description": "Learn how to design expressive and maintainable type systems for larger applications.",
        "level": "Advanced"
    },
    {
        "id": "typescript-advanced-generics",
        "skill_id": "typescript",
        "title": "Advanced Generics",
        "description": "Explore advanced generic techniques for building flexible and reusable TypeScript libraries.",
        "level": "Advanced"
    },
    {
        "id": "typescript-architecture",
        "skill_id": "typescript",
        "title": "Application Architecture",
        "description": "Learn how to structure large TypeScript applications for maintainability and scalability.",
        "level": "Advanced"
    },
    {
        "id": "typescript-performance",
        "skill_id": "typescript",
        "title": "Performance",
        "description": "Learn how to improve compilation and runtime performance in TypeScript applications.",
        "level": "Advanced"
    },
    {
        "id": "typescript-production",
        "skill_id": "typescript",
        "title": "Production Applications",
        "description": "Learn how to build, test, deploy, and maintain reliable TypeScript applications in production.",
        "level": "Advanced"
    },


    # =========================================================
    # RUST
    # =========================================================

    # Rust - Beginner
    {
        "id": "rust-syntax",
        "skill_id": "rust",
        "title": "Rust Syntax",
        "description": "Learn the basic syntax and structure used to write Rust programs.",
        "level": "Beginner"
    },
    {
        "id": "rust-variables-types",
        "skill_id": "rust",
        "title": "Variables & Data Types",
        "description": "Learn how Rust handles variables, mutability, scalar types, and compound data types.",
        "level": "Beginner"
    },
    {
        "id": "rust-control-flow",
        "skill_id": "rust",
        "title": "Control Flow",
        "description": "Learn how to use conditions, loops, and pattern matching to control Rust programs.",
        "level": "Beginner"
    },
    {
        "id": "rust-functions",
        "skill_id": "rust",
        "title": "Functions",
        "description": "Learn how to define functions, pass parameters, return values, and organize Rust code.",
        "level": "Beginner"
    },
    {
        "id": "rust-ownership",
        "skill_id": "rust",
        "title": "Ownership",
        "description": "Learn Rust's ownership system and how it provides memory safety without a garbage collector.",
        "level": "Beginner"
    },
    {
        "id": "rust-borrowing",
        "skill_id": "rust",
        "title": "Borrowing & References",
        "description": "Learn how borrowing and references allow Rust programs to safely use data without taking ownership.",
        "level": "Beginner"
    },
    {
        "id": "rust-structs-enums",
        "skill_id": "rust",
        "title": "Structs & Enums",
        "description": "Learn how to model data using structs, enums, and pattern matching.",
        "level": "Beginner"
    },

    # Rust - Intermediate
    {
        "id": "rust-error-handling",
        "skill_id": "rust",
        "title": "Error Handling",
        "description": "Learn how Rust uses Result and Option to handle errors and missing values safely.",
        "level": "Intermediate"
    },
    {
        "id": "rust-collections",
        "skill_id": "rust",
        "title": "Collections",
        "description": "Learn how to work with common Rust collections such as vectors, strings, and hash maps.",
        "level": "Intermediate"
    },
    {
        "id": "rust-traits",
        "skill_id": "rust",
        "title": "Traits",
        "description": "Learn how traits define shared behavior and enable flexible designs in Rust programs.",
        "level": "Intermediate"
    },
    {
        "id": "rust-generics",
        "skill_id": "rust",
        "title": "Generics",
        "description": "Learn how generics allow Rust code to work with multiple types while maintaining type safety.",
        "level": "Intermediate"
    },
    {
        "id": "rust-modules",
        "skill_id": "rust",
        "title": "Modules & Packages",
        "description": "Learn how to organize Rust applications into modules, crates, and packages.",
        "level": "Intermediate"
    },
    {
        "id": "rust-testing",
        "skill_id": "rust",
        "title": "Testing",
        "description": "Learn how to write unit and integration tests for reliable Rust applications.",
        "level": "Intermediate"
    },

    # Rust - Advanced
    {
        "id": "rust-smart-pointers",
        "skill_id": "rust",
        "title": "Smart Pointers",
        "description": "Learn how smart pointers manage ownership and enable advanced memory-management patterns.",
        "level": "Advanced"
    },
    {
        "id": "rust-concurrency",
        "skill_id": "rust",
        "title": "Concurrency",
        "description": "Learn how Rust supports safe concurrent programming using threads, channels, and shared state.",
        "level": "Advanced"
    },
    {
        "id": "rust-async",
        "skill_id": "rust",
        "title": "Async Programming",
        "description": "Learn how asynchronous Rust applications handle concurrent tasks using async and await.",
        "level": "Advanced"
    },
    {
        "id": "rust-performance",
        "skill_id": "rust",
        "title": "Performance",
        "description": "Learn how to write efficient Rust applications and identify performance bottlenecks.",
        "level": "Advanced"
    },
    {
        "id": "rust-architecture",
        "skill_id": "rust",
        "title": "Application Architecture",
        "description": "Learn how to structure larger Rust applications using maintainable and scalable design principles.",
        "level": "Advanced"
    },
    {
        "id": "rust-production",
        "skill_id": "rust",
        "title": "Production Applications",
        "description": "Learn how to build, test, deploy, and maintain reliable Rust applications in production.",
        "level": "Advanced"
    },


    # =========================================================
    # HTML & CSS
    # =========================================================

    # Beginner
    {
        "id": "html-css-html-structure",
        "skill_id": "html-css",
        "title": "HTML Structure",
        "description": "Learn how HTML elements and semantic structure are used to organize web pages.",
        "level": "Beginner"
    },
    {
        "id": "html-css-text-links",
        "skill_id": "html-css",
        "title": "Text & Links",
        "description": "Learn how to create headings, paragraphs, links, and other common HTML content.",
        "level": "Beginner"
    },
    {
        "id": "html-css-images-media",
        "skill_id": "html-css",
        "title": "Images & Media",
        "description": "Learn how to add and structure images, audio, video, and other media on web pages.",
        "level": "Beginner"
    },
    {
        "id": "html-css-forms",
        "skill_id": "html-css",
        "title": "Forms",
        "description": "Learn how HTML forms collect user information using inputs, labels, buttons, and validation attributes.",
        "level": "Beginner"
    },
    {
        "id": "html-css-css-basics",
        "skill_id": "html-css",
        "title": "CSS Basics",
        "description": "Learn how CSS controls colors, fonts, spacing, borders, and other visual properties.",
        "level": "Beginner"
    },
    {
        "id": "html-css-box-model",
        "skill_id": "html-css",
        "title": "Box Model",
        "description": "Learn how content, padding, borders, and margins determine the size and spacing of elements.",
        "level": "Beginner"
    },
    {
        "id": "html-css-flexbox",
        "skill_id": "html-css",
        "title": "Flexbox",
        "description": "Learn how Flexbox arranges and aligns elements in responsive layouts.",
        "level": "Beginner"
    },

    # Intermediate
    {
        "id": "html-css-grid",
        "skill_id": "html-css",
        "title": "CSS Grid",
        "description": "Learn how CSS Grid creates structured two-dimensional layouts for web pages.",
        "level": "Intermediate"
    },
    {
        "id": "html-css-responsive",
        "skill_id": "html-css",
        "title": "Responsive Design",
        "description": "Learn how to create layouts that adapt to different screen sizes and devices.",
        "level": "Intermediate"
    },
    {
        "id": "html-css-accessibility",
        "skill_id": "html-css",
        "title": "Accessibility",
        "description": "Learn how to build web pages that are usable by people with different abilities and assistive technologies.",
        "level": "Intermediate"
    },
    {
        "id": "html-css-advanced-selectors",
        "skill_id": "html-css",
        "title": "Advanced Selectors",
        "description": "Learn how to target elements precisely using advanced CSS selectors, pseudo-classes, and pseudo-elements.",
        "level": "Intermediate"
    },
    {
        "id": "html-css-transitions",
        "skill_id": "html-css",
        "title": "Transitions & Animations",
        "description": "Learn how to create smooth visual changes and animations using CSS.",
        "level": "Intermediate"
    },

    # Advanced
    {
        "id": "html-css-design-systems",
        "skill_id": "html-css",
        "title": "Design Systems",
        "description": "Learn how reusable design patterns, variables, components, and conventions create consistent interfaces.",
        "level": "Advanced"
    },
    {
        "id": "html-css-advanced-responsive",
        "skill_id": "html-css",
        "title": "Advanced Responsive Design",
        "description": "Learn advanced techniques for creating flexible interfaces across complex screen sizes and devices.",
        "level": "Advanced"
    },
    {
        "id": "html-css-performance",
        "skill_id": "html-css",
        "title": "Web Performance",
        "description": "Learn how HTML and CSS choices affect loading speed, rendering, and overall web performance.",
        "level": "Advanced"
    },
    {
        "id": "html-css-production",
        "skill_id": "html-css",
        "title": "Production Websites",
        "description": "Learn how to prepare accessible, responsive, maintainable websites for production use.",
        "level": "Advanced"
    },


    # =========================================================
    # REACT
    # =========================================================

    # Beginner
    {
        "id": "react-components",
        "skill_id": "react",
        "title": "Components",
        "description": "Learn how React components organize user interfaces into reusable pieces.",
        "level": "Beginner"
    },
    {
        "id": "react-jsx",
        "skill_id": "react",
        "title": "JSX",
        "description": "Learn how JSX combines JavaScript logic with HTML-like syntax to describe user interfaces.",
        "level": "Beginner"
    },
    {
        "id": "react-props",
        "skill_id": "react",
        "title": "Props",
        "description": "Learn how components receive and use data through props.",
        "level": "Beginner"
    },
    {
        "id": "react-state",
        "skill_id": "react",
        "title": "State",
        "description": "Learn how React state stores changing information and causes components to update.",
        "level": "Beginner"
    },
    {
        "id": "react-events",
        "skill_id": "react",
        "title": "Events",
        "description": "Learn how React responds to user interactions such as clicks, typing, and form submissions.",
        "level": "Beginner"
    },
    {
        "id": "react-forms",
        "skill_id": "react",
        "title": "Forms",
        "description": "Learn how to build and manage user input forms in React applications.",
        "level": "Beginner"
    },

    # Intermediate
    {
        "id": "react-hooks",
        "skill_id": "react",
        "title": "Hooks",
        "description": "Learn how React Hooks provide state, effects, and other functionality inside components.",
        "level": "Intermediate"
    },
    {
        "id": "react-useeffect",
        "skill_id": "react",
        "title": "Effects",
        "description": "Learn how to perform side effects such as data fetching and subscriptions with React effects.",
        "level": "Intermediate"
    },
    {
        "id": "react-api-data",
        "skill_id": "react",
        "title": "API Data",
        "description": "Learn how React applications retrieve, display, and manage data from APIs.",
        "level": "Intermediate"
    },
    {
        "id": "react-routing",
        "skill_id": "react",
        "title": "Routing",
        "description": "Learn how to create multi-page experiences and navigate between views in React applications.",
        "level": "Intermediate"
    },
    {
        "id": "react-context",
        "skill_id": "react",
        "title": "Context",
        "description": "Learn how React Context shares data across components without passing props through every level.",
        "level": "Intermediate"
    },
    {
        "id": "react-testing",
        "skill_id": "react",
        "title": "Testing",
        "description": "Learn how to test React components and user interactions for reliable applications.",
        "level": "Intermediate"
    },

    # Advanced
    {
        "id": "react-performance",
        "skill_id": "react",
        "title": "Performance",
        "description": "Learn how to identify and reduce unnecessary rendering and other performance issues in React applications.",
        "level": "Advanced"
    },
    {
        "id": "react-state-architecture",
        "skill_id": "react",
        "title": "State Architecture",
        "description": "Learn how to design scalable approaches for managing application state in larger React projects.",
        "level": "Advanced"
    },
    {
        "id": "react-reusable-architecture",
        "skill_id": "react",
        "title": "Reusable Architecture",
        "description": "Learn how to organize React applications around reusable components and maintainable architecture.",
        "level": "Advanced"
    },
    {
        "id": "react-advanced-testing",
        "skill_id": "react",
        "title": "Advanced Testing",
        "description": "Learn advanced testing strategies for complex React applications and production workflows.",
        "level": "Advanced"
    },
    {
        "id": "react-production",
        "skill_id": "react",
        "title": "Production Applications",
        "description": "Learn how to build, optimize, deploy, and maintain React applications in production.",
        "level": "Advanced"
    },


    # =========================================================
    # NODE.JS
    # =========================================================

    # Beginner
    {
        "id": "nodejs-runtime",
        "skill_id": "nodejs",
        "title": "Node.js Runtime",
        "description": "Learn what Node.js is and how JavaScript runs outside the browser.",
        "level": "Beginner"
    },
    {
        "id": "nodejs-modules",
        "skill_id": "nodejs",
        "title": "Modules",
        "description": "Learn how Node.js applications organize and reuse code through modules.",
        "level": "Beginner"
    },
    {
        "id": "nodejs-npm",
        "skill_id": "nodejs",
        "title": "Packages & Dependencies",
        "description": "Learn how to install, manage, and use packages and dependencies in Node.js projects.",
        "level": "Beginner"
    },
    {
        "id": "nodejs-files",
        "skill_id": "nodejs",
        "title": "File System",
        "description": "Learn how Node.js reads, writes, and manages files and directories.",
        "level": "Beginner"
    },
    {
        "id": "nodejs-http",
        "skill_id": "nodejs",
        "title": "HTTP Servers",
        "description": "Learn how to create basic HTTP servers and handle web requests with Node.js.",
        "level": "Beginner"
    },

    # Intermediate
    {
        "id": "nodejs-express",
        "skill_id": "nodejs",
        "title": "Express",
        "description": "Learn how Express simplifies routing, middleware, and HTTP application development with Node.js.",
        "level": "Intermediate"
    },
    {
        "id": "nodejs-rest-apis",
        "skill_id": "nodejs",
        "title": "REST APIs",
        "description": "Learn how to design and build RESTful APIs that exchange data with client applications.",
        "level": "Intermediate"
    },
    {
        "id": "nodejs-middleware",
        "skill_id": "nodejs",
        "title": "Middleware",
        "description": "Learn how middleware processes requests and responses in Node.js web applications.",
        "level": "Intermediate"
    },
    {
        "id": "nodejs-databases",
        "skill_id": "nodejs",
        "title": "Database Access",
        "description": "Learn how Node.js applications connect to databases and perform data operations.",
        "level": "Intermediate"
    },
    {
        "id": "nodejs-authentication",
        "skill_id": "nodejs",
        "title": "Authentication",
        "description": "Learn how Node.js applications identify users and protect authenticated resources.",
        "level": "Intermediate"
    },
    {
        "id": "nodejs-testing",
        "skill_id": "nodejs",
        "title": "Testing",
        "description": "Learn how to test Node.js applications, APIs, and individual functions.",
        "level": "Intermediate"
    },

    # Advanced
    {
        "id": "nodejs-architecture",
        "skill_id": "nodejs",
        "title": "Application Architecture",
        "description": "Learn how to structure larger Node.js applications for maintainability and scalability.",
        "level": "Advanced"
    },
    {
        "id": "nodejs-performance",
        "skill_id": "nodejs",
        "title": "Performance",
        "description": "Learn how to identify and improve performance issues in Node.js applications.",
        "level": "Advanced"
    },
    {
        "id": "nodejs-security",
        "skill_id": "nodejs",
        "title": "Security",
        "description": "Learn common backend security risks and techniques for protecting Node.js applications.",
        "level": "Advanced"
    },
    {
        "id": "nodejs-scalability",
        "skill_id": "nodejs",
        "title": "Scalability",
        "description": "Learn how to design Node.js systems that can handle increasing traffic and workloads.",
        "level": "Advanced"
    },
    {
        "id": "nodejs-production",
        "skill_id": "nodejs",
        "title": "Production Applications",
        "description": "Learn how to deploy, monitor, and maintain Node.js applications in production environments.",
        "level": "Advanced"
    },


    # =========================================================
    # FULL-STACK WEB DEVELOPMENT
    # =========================================================

    # Beginner
    {
        "id": "fullstack-web-fundamentals",
        "skill_id": "full-stack-web-development",
        "title": "Web Fundamentals",
        "description": "Learn how browsers, servers, HTTP, HTML, CSS, and JavaScript work together to create web applications.",
        "level": "Beginner"
    },
    {
        "id": "fullstack-frontend",
        "skill_id": "full-stack-web-development",
        "title": "Frontend Development",
        "description": "Learn how to build user interfaces that present application data and respond to user interactions.",
        "level": "Beginner"
    },
    {
        "id": "fullstack-backend",
        "skill_id": "full-stack-web-development",
        "title": "Backend Development",
        "description": "Learn how servers process requests, apply application logic, and communicate with databases.",
        "level": "Beginner"
    },
    {
        "id": "fullstack-databases",
        "skill_id": "full-stack-web-development",
        "title": "Databases",
        "description": "Learn how web applications store, retrieve, update, and manage application data.",
        "level": "Beginner"
    },
    {
        "id": "fullstack-apis",
        "skill_id": "full-stack-web-development",
        "title": "APIs",
        "description": "Learn how frontend and backend systems communicate through APIs.",
        "level": "Beginner"
    },

    # Intermediate
    {
        "id": "fullstack-authentication",
        "skill_id": "full-stack-web-development",
        "title": "Authentication",
        "description": "Learn how web applications securely identify users and control access to protected features.",
        "level": "Intermediate"
    },
    {
        "id": "fullstack-state",
        "skill_id": "full-stack-web-development",
        "title": "Application State",
        "description": "Learn how full-stack applications manage changing data across frontend and backend systems.",
        "level": "Intermediate"
    },
    {
        "id": "fullstack-validation",
        "skill_id": "full-stack-web-development",
        "title": "Validation",
        "description": "Learn how to validate user input and application data before processing or storing it.",
        "level": "Intermediate"
    },
    {
        "id": "fullstack-testing",
        "skill_id": "full-stack-web-development",
        "title": "Testing",
        "description": "Learn how to test frontend components, backend logic, APIs, and complete application workflows.",
        "level": "Intermediate"
    },
    {
        "id": "fullstack-git",
        "skill_id": "full-stack-web-development",
        "title": "Version Control",
        "description": "Learn how Git supports collaboration, change tracking, branching, and project history.",
        "level": "Intermediate"
    },

    # Advanced
    {
        "id": "fullstack-architecture",
        "skill_id": "full-stack-web-development",
        "title": "Application Architecture",
        "description": "Learn how to design maintainable frontend, backend, API, and database layers for larger applications.",
        "level": "Advanced"
    },
    {
        "id": "fullstack-security",
        "skill_id": "full-stack-web-development",
        "title": "Web Security",
        "description": "Learn how to protect full-stack applications from common security vulnerabilities and unsafe data handling.",
        "level": "Advanced"
    },
    {
        "id": "fullstack-performance",
        "skill_id": "full-stack-web-development",
        "title": "Performance",
        "description": "Learn how to identify and improve performance across the frontend, backend, APIs, and database.",
        "level": "Advanced"
    },
    {
        "id": "fullstack-deployment",
        "skill_id": "full-stack-web-development",
        "title": "Deployment",
        "description": "Learn how to prepare and deploy full-stack applications to production environments.",
        "level": "Advanced"
    },
    {
        "id": "fullstack-production",
        "skill_id": "full-stack-web-development",
        "title": "Production Systems",
        "description": "Learn how to monitor, maintain, scale, and improve full-stack applications after deployment.",
        "level": "Advanced"
    },


    # =========================================================
    # SQL
    # =========================================================

    # Beginner
    {
        "id": "sql-syntax",
        "skill_id": "sql",
        "title": "SQL Syntax",
        "description": "Learn the basic syntax used to communicate with relational databases.",
        "level": "Beginner"
    },
    {
        "id": "sql-select",
        "skill_id": "sql",
        "title": "SELECT Queries",
        "description": "Learn how to retrieve data from database tables using SELECT queries.",
        "level": "Beginner"
    },
    {
        "id": "sql-filtering",
        "skill_id": "sql",
        "title": "Filtering Data",
        "description": "Learn how to filter query results using WHERE conditions and comparison operators.",
        "level": "Beginner"
    },
    {
        "id": "sql-sorting",
        "skill_id": "sql",
        "title": "Sorting & Limiting",
        "description": "Learn how to sort query results and limit the number of returned records.",
        "level": "Beginner"
    },
    {
        "id": "sql-insert-update-delete",
        "skill_id": "sql",
        "title": "Insert, Update & Delete",
        "description": "Learn how to add, modify, and remove records from database tables.",
        "level": "Beginner"
    },
    {
        "id": "sql-tables",
        "skill_id": "sql",
        "title": "Tables & Relationships",
        "description": "Learn how tables organize data and how relationships connect related records.",
        "level": "Beginner"
    },

    # Intermediate
    {
        "id": "sql-joins",
        "skill_id": "sql",
        "title": "Joins",
        "description": "Learn how to combine related data from multiple tables using different types of joins.",
        "level": "Intermediate"
    },
    {
        "id": "sql-aggregate",
        "skill_id": "sql",
        "title": "Aggregate Functions",
        "description": "Learn how functions such as COUNT, SUM, AVG, MIN, and MAX summarize data.",
        "level": "Intermediate"
    },
    {
        "id": "sql-grouping",
        "skill_id": "sql",
        "title": "Grouping Data",
        "description": "Learn how GROUP BY and HAVING organize and filter aggregated query results.",
        "level": "Intermediate"
    },
    {
        "id": "sql-subqueries",
        "skill_id": "sql",
        "title": "Subqueries",
        "description": "Learn how queries can be nested inside other queries to solve more complex data problems.",
        "level": "Intermediate"
    },
    {
        "id": "sql-transactions",
        "skill_id": "sql",
        "title": "Transactions",
        "description": "Learn how transactions keep related database operations consistent and reliable.",
        "level": "Intermediate"
    },

    # Advanced
    {
        "id": "sql-indexes",
        "skill_id": "sql",
        "title": "Indexes",
        "description": "Learn how indexes improve database query performance and when they should be used.",
        "level": "Advanced"
    },
    {
        "id": "sql-query-optimization",
        "skill_id": "sql",
        "title": "Query Optimization",
        "description": "Learn how to analyze and improve SQL queries for better performance.",
        "level": "Advanced"
    },
    {
        "id": "sql-advanced-design",
        "skill_id": "sql",
        "title": "Database Design",
        "description": "Learn advanced approaches to designing reliable and maintainable relational database structures.",
        "level": "Advanced"
    },
    {
        "id": "sql-security",
        "skill_id": "sql",
        "title": "Database Security",
        "description": "Learn how to protect database access, data, and queries from common security risks.",
        "level": "Advanced"
    },
    {
        "id": "sql-production",
        "skill_id": "sql",
        "title": "Production Databases",
        "description": "Learn how to manage reliable SQL databases in production applications.",
        "level": "Advanced"
    },


    # =========================================================
    # POSTGRESQL
    # =========================================================

    # Beginner
    {
        "id": "postgresql-installation",
        "skill_id": "postgresql",
        "title": "PostgreSQL Basics",
        "description": "Learn the fundamentals of PostgreSQL and how it is used as a relational database system.",
        "level": "Beginner"
    },
    {
        "id": "postgresql-tables",
        "skill_id": "postgresql",
        "title": "Tables & Columns",
        "description": "Learn how PostgreSQL tables and columns store structured application data.",
        "level": "Beginner"
    },
    {
        "id": "postgresql-crud",
        "skill_id": "postgresql",
        "title": "CRUD Operations",
        "description": "Learn how to create, retrieve, update, and delete data in PostgreSQL.",
        "level": "Beginner"
    },
    {
        "id": "postgresql-constraints",
        "skill_id": "postgresql",
        "title": "Constraints",
        "description": "Learn how primary keys, foreign keys, unique constraints, and other rules protect data integrity.",
        "level": "Beginner"
    },

    # Intermediate
    {
        "id": "postgresql-joins",
        "skill_id": "postgresql",
        "title": "Joins",
        "description": "Learn how PostgreSQL combines related data across multiple tables.",
        "level": "Intermediate"
    },
    {
        "id": "postgresql-indexes",
        "skill_id": "postgresql",
        "title": "Indexes",
        "description": "Learn how PostgreSQL indexes improve the speed of common database queries.",
        "level": "Intermediate"
    },
    {
        "id": "postgresql-transactions",
        "skill_id": "postgresql",
        "title": "Transactions",
        "description": "Learn how PostgreSQL transactions maintain consistent database operations.",
        "level": "Intermediate"
    },
    {
        "id": "postgresql-views",
        "skill_id": "postgresql",
        "title": "Views",
        "description": "Learn how views provide reusable ways to query and present database information.",
        "level": "Intermediate"
    },
    {
        "id": "postgresql-functions",
        "skill_id": "postgresql",
        "title": "Database Functions",
        "description": "Learn how PostgreSQL functions can encapsulate reusable database logic.",
        "level": "Intermediate"
    },

    # Advanced
    {
        "id": "postgresql-query-optimization",
        "skill_id": "postgresql",
        "title": "Query Optimization",
        "description": "Learn how to analyze and improve PostgreSQL queries for better performance.",
        "level": "Advanced"
    },
    {
        "id": "postgresql-advanced-indexing",
        "skill_id": "postgresql",
        "title": "Advanced Indexing",
        "description": "Learn advanced PostgreSQL indexing strategies for complex workloads.",
        "level": "Advanced"
    },
    {
        "id": "postgresql-security",
        "skill_id": "postgresql",
        "title": "Database Security",
        "description": "Learn how PostgreSQL roles, permissions, and security controls protect database resources.",
        "level": "Advanced"
    },
    {
        "id": "postgresql-backups",
        "skill_id": "postgresql",
        "title": "Backup & Recovery",
        "description": "Learn how PostgreSQL databases are backed up and restored to protect against data loss.",
        "level": "Advanced"
    },
    {
        "id": "postgresql-production",
        "skill_id": "postgresql",
        "title": "Production PostgreSQL",
        "description": "Learn how to operate, monitor, and maintain PostgreSQL databases in production systems.",
        "level": "Advanced"
    },


    # =========================================================
    # MONGODB
    # =========================================================

    # Beginner
    {
        "id": "mongodb-documents",
        "skill_id": "mongodb",
        "title": "Documents & Collections",
        "description": "Learn how MongoDB stores data using documents and collections.",
        "level": "Beginner"
    },
    {
        "id": "mongodb-crud",
        "skill_id": "mongodb",
        "title": "CRUD Operations",
        "description": "Learn how to create, read, update, and delete MongoDB documents.",
        "level": "Beginner"
    },
    {
        "id": "mongodb-queries",
        "skill_id": "mongodb",
        "title": "Queries",
        "description": "Learn how to search MongoDB collections using filters and query operators.",
        "level": "Beginner"
    },
    {
        "id": "mongodb-data-modeling",
        "skill_id": "mongodb",
        "title": "Data Modeling",
        "description": "Learn how to structure MongoDB documents and decide when to embed or reference data.",
        "level": "Beginner"
    },

    # Intermediate
    {
        "id": "mongodb-indexes",
        "skill_id": "mongodb",
        "title": "Indexes",
        "description": "Learn how MongoDB indexes improve query performance.",
        "level": "Intermediate"
    },
    {
        "id": "mongodb-aggregation",
        "skill_id": "mongodb",
        "title": "Aggregation",
        "description": "Learn how MongoDB aggregation pipelines transform, filter, group, and analyze data.",
        "level": "Intermediate"
    },
    {
        "id": "mongodb-validation",
        "skill_id": "mongodb",
        "title": "Schema Validation",
        "description": "Learn how MongoDB can enforce rules on document structure and data types.",
        "level": "Intermediate"
    },
    {
        "id": "mongodb-nodejs",
        "skill_id": "mongodb",
        "title": "MongoDB with Node.js",
        "description": "Learn how Node.js applications connect to MongoDB and perform database operations.",
        "level": "Intermediate"
    },

    # Advanced
    {
        "id": "mongodb-advanced-modeling",
        "skill_id": "mongodb",
        "title": "Advanced Data Modeling",
        "description": "Learn advanced strategies for modeling relationships and designing scalable MongoDB data structures.",
        "level": "Advanced"
    },
    {
        "id": "mongodb-performance",
        "skill_id": "mongodb",
        "title": "Performance",
        "description": "Learn how to identify and improve MongoDB query and application performance.",
        "level": "Advanced"
    },
    {
        "id": "mongodb-security",
        "skill_id": "mongodb",
        "title": "Security",
        "description": "Learn how authentication, authorization, and secure configuration protect MongoDB data.",
        "level": "Advanced"
    },
    {
        "id": "mongodb-scaling",
        "skill_id": "mongodb",
        "title": "Scaling",
        "description": "Learn how MongoDB supports larger workloads through replication, sharding, and scalable architecture.",
        "level": "Advanced"
    },
    {
        "id": "mongodb-production",
        "skill_id": "mongodb",
        "title": "Production MongoDB",
        "description": "Learn how to monitor, maintain, back up, and operate MongoDB in production environments.",
        "level": "Advanced"
    },


    # =========================================================
    # FIREBASE / FIRESTORE
    # =========================================================

    # Beginner
    {
        "id": "firebase-fundamentals",
        "skill_id": "firebase-firestore",
        "title": "Firebase Fundamentals",
        "description": "Learn what Firebase provides and how its cloud services support application development.",
        "level": "Beginner"
    },
    {
        "id": "firestore-database",
        "skill_id": "firebase-firestore",
        "title": "Firestore Database",
        "description": "Learn how Cloud Firestore stores application data using collections and documents.",
        "level": "Beginner"
    },
    {
        "id": "firestore-crud",
        "skill_id": "firebase-firestore",
        "title": "Firestore CRUD",
        "description": "Learn how to create, retrieve, update, and delete documents in Firestore.",
        "level": "Beginner"
    },
    {
        "id": "firestore-queries",
        "skill_id": "firebase-firestore",
        "title": "Queries",
        "description": "Learn how to retrieve specific documents and filter Firestore data using queries.",
        "level": "Beginner"
    },
    {
        "id": "firebase-sdk",
        "skill_id": "firebase-firestore",
        "title": "Firebase SDKs",
        "description": "Learn how application code connects to Firebase services through Firebase SDKs.",
        "level": "Beginner"
    },

    # Intermediate
    {
        "id": "firestore-data-modeling",
        "skill_id": "firebase-firestore",
        "title": "Data Modeling",
        "description": "Learn how to structure Firestore collections, documents, and relationships for application needs.",
        "level": "Intermediate"
    },
    {
        "id": "firestore-indexes",
        "skill_id": "firebase-firestore",
        "title": "Indexes",
        "description": "Learn how Firestore indexes support efficient queries and how compound indexes are used.",
        "level": "Intermediate"
    },
    {
        "id": "firebase-authentication",
        "skill_id": "firebase-firestore",
        "title": "Authentication",
        "description": "Learn how Firebase Authentication manages user accounts and secure access to applications.",
        "level": "Intermediate"
    },
    {
        "id": "firestore-security-rules",
        "skill_id": "firebase-firestore",
        "title": "Security Rules",
        "description": "Learn how Firestore Security Rules control who can read and write cloud data.",
        "level": "Intermediate"
    },
    {
        "id": "firestore-cloud-functions",
        "skill_id": "firebase-firestore",
        "title": "Cloud Functions",
        "description": "Learn how backend functions can respond to events and perform server-side operations.",
        "level": "Intermediate"
    },

    # Advanced
    {
        "id": "firestore-advanced-modeling",
        "skill_id": "firebase-firestore",
        "title": "Advanced Data Modeling",
        "description": "Learn advanced Firestore modeling strategies for scalable applications and related data.",
        "level": "Advanced"
    },
    {
        "id": "firestore-performance",
        "skill_id": "firebase-firestore",
        "title": "Performance",
        "description": "Learn how query design, indexes, and data structures affect Firestore performance.",
        "level": "Advanced"
    },
    {
        "id": "firestore-scalability",
        "skill_id": "firebase-firestore",
        "title": "Scalability",
        "description": "Learn how Firestore supports applications with growing users, data, and workloads.",
        "level": "Advanced"
    },
    {
        "id": "firestore-monitoring",
        "skill_id": "firebase-firestore",
        "title": "Monitoring",
        "description": "Learn how to monitor application usage, database activity, errors, and performance.",
        "level": "Advanced"
    },
    {
        "id": "firebase-production",
        "skill_id": "firebase-firestore",
        "title": "Production Firebase",
        "description": "Learn how to secure, deploy, monitor, and maintain Firebase applications in production.",
        "level": "Advanced"
    }
]


# =========================================================
# SEED THE LEARNING-GOAL LIBRARY
# =========================================================

for goal in learning_goals:
    goal_id = goal["id"]

    goal_data = {
        "skill_id": goal["skill_id"],
        "title": goal["title"],
        "description": goal["description"],
        "level": goal["level"],
        "completed": False
    }

    db.collection("learning_goals").document(goal_id).set(goal_data)

    print(f"Learning goal added: {goal['skill_id']} → {goal['title']}")