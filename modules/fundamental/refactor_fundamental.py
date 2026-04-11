import os

modules_config = {
    "oop": {
        "title": "Object-Oriented Programming",
        "subtitle": "OOP Fundamentals",
        "image": "https://images.unsplash.com/photo-1607706189992-eae578626c86?w=600&q=80",
        "chapters": [
            ("Chapter 1", "Introduction to OOP", "Classes & Objects"),
            ("Chapter 2", "Encapsulation & Abstraction", "Hiding complexity and exposing interfaces."),
            ("Chapter 3", "Inheritance & Polymorphism", "Reusing code and dynamic binding."),
            ("Chapter 4", "Design Patterns", "Singleton, Factory, Observer and more."),
            ("Chapter 5", "Advanced OOP", "Interfaces & Abstract Classes in depth.")
        ]
    },
    "data_structures": {
        "title": "Data Structures & Algorithms",
        "subtitle": "DSA Fundamentals",
        "image": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&q=80",
        "chapters": [
            ("Chapter 1", "Arrays and Dynamic Arrays", "Fundamental memory structures."),
            ("Chapter 2", "Linked Lists", "Singly, doubly, and circular linked lists."),
            ("Chapter 3", "Stacks, Queues, and Deques", "Linear data structures and their applications."),
            ("Chapter 4", "Trees", "Binary, BST, AVL, and Heaps."),
            ("Chapter 5", "Graphs", "Representation, BFS, DFS, and Shortest Paths."),
            ("Chapter 6", "Sorting Algorithms", "Bubble, Merge, Quick, and Radix Sort."),
            ("Chapter 7", "Searching", "Binary Search and Hash Tables.")
        ]
    },
    "database": {
        "title": "Databases",
        "subtitle": "Database Fundamentals",
        "image": "https://images.unsplash.com/photo-1544383835-bda2bc66a55d?w=600&q=80",
        "chapters": [
            ("Chapter 1", "Introduction to Databases", "Concepts & Architecture."),
            ("Chapter 2", "Relational Model & ER Diagrams", "Modeling real-world entities."),
            ("Chapter 3", "SQL", "DDL, DML, DQL, and DCL commands."),
            ("Chapter 4", "Normalization", "1NF, 2NF, 3NF, BCNF rules."),
            ("Chapter 5", "Transactions & Concurrency", "ACID Properties & Control."),
            ("Chapter 6", "Introduction to NoSQL", "MongoDB, Redis, and Cassandra overview."),
            ("Chapter 7", "Administration & Optimization", "Query tuning and DBA basics.")
        ]
    },
    "programming": {
        "title": "Programming Fundamentals",
        "subtitle": "Programming Basics",
        "image": "https://images.unsplash.com/photo-1516116216624-53e697fedbea?w=600&q=80",
        "chapters": [
            ("Chapter 1", "Introduction to Programming", "Computational Thinking & Logic."),
            ("Chapter 2", "Variables & Data Types", "Storing and manipulating data."),
            ("Chapter 3", "Control Flow", "Conditionals and Loops."),
            ("Chapter 4", "Functions & Modular Programming", "Code reuse and abstraction."),
            ("Chapter 5", "Recursion", "Solving problems with sub-problems."),
            ("Chapter 6", "Introduction to Complexity", "Big-O notation and performance.")
        ]
    },
    "python_java": {
        "title": "Python & Java",
        "subtitle": "Language Tracks",
        "image": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=600&q=80",
        "chapters": [
            ("P1", "Python Syntax", "Data Types and I/O basics."),
            ("P2", "Python Collections", "Lists, Dicts, Sets, and Tuples."),
            ("P3", "Python Functions", "Lambdas and Comprehensions."),
            ("P4", "Python Advanced", "File Handling, Exceptions, and Packages."),
            ("J1", "Java Syntax", "Environment, Syntax, and Types."),
            ("J2", "Java OOP", "Classes, Interfaces, and Inheritance."),
            ("J3", "Java Collections", "List, Map, and Set framework."),
            ("J4", "Java Advanced", "Exceptions, I/O, and Concurrency Threads.")
        ]
    }
}

base_path = "." # Run from modules/fundamental

for mod_id, config in modules_config.items():
    mod_path = os.path.join(base_path, mod_id)
    course_path = os.path.join(mod_path, 'course')
    os.makedirs(course_path, exist_ok=True)
    
    # Create chapters
    listing_contents = []
    for chapter in config['chapters']:
        c_id = chapter[0]
        c_title = chapter[1]
        c_desc = chapter[2]
        
        fname = f"{c_id.lower().replace(' ', '_')}.qmd"
        listing_contents.append(f'      - "course/{fname}"')
        
        qmd_content = f"""---
title: "{c_id} — {c_title}"
subtitle: "{config['subtitle']}"
description: "{c_desc}"
image: {config['image']}
---

## 📋 Chapter Overview

{c_desc}

::: {{.callout-warning}}
## 🔜 Coming Soon
Lecture notes and materials for this chapter are currently being prepared.
:::
"""
        with open(os.path.join(course_path, fname), 'w', encoding='utf-8') as f:
            f.write(qmd_content)
            
    # Update index.qmd
    index_content = f"""---
title: "{config['title']}"
description: "{config['subtitle']} module covering essential topics via a modular structure."
image: {config['image']}
categories: [fundamental]
number-sections: false
toc: true
toc-depth: 2
listing:
  - id: chapters-grid
    contents:
{chr(10).join(listing_contents)}
    type: grid
    grid-columns: 3
    fields: [image, title, description]
    image-height: 180px
    categories: false
    sort: false
---

## 📋 Module Overview

This module provides an in-depth introduction to **{config['title']}**, structured into individual chapters for focused learning.

---

## 📚 Curriculum

::: {{#chapters-grid}}
:::

---

## 📂 Resources

### Directed Works (TD) & Practical Works (TP)

::: {{.callout-warning}}
## 🔜 Coming Soon
Directed work series and lab exercises for this module are currently being prepared.
:::
"""
    with open(os.path.join(mod_path, 'index.qmd'), 'w', encoding='utf-8') as f:
        f.write(index_content)
    print(f"Refactored {mod_id}")
