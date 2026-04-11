import os

chapters = [
    ("Chapter 1", "Introduction to AI", "History, Definitions, and Applications"),
    ("Chapter 2", "Search Algorithms", "BFS, DFS, A*, Heuristics"),
    ("Chapter 3", "Knowledge Representation", "Logic, Ontologies, Expert Systems"),
    ("Chapter 4", "Machine Learning Overview", "Supervised, Unsupervised, RL"),
    ("Chapter 5", "Neural Networks", "Perceptrons, MLP, Backpropagation"),
    ("Chapter 6", "Natural Language Processing", "Basics and Applications"),
    ("Chapter 7", "AI Ethics, Bias, and Responsible AI"),
]

os.makedirs('course', exist_ok=True)

for i, chapter in enumerate(chapters, 1):
    title = f"{chapter[0]} — {chapter[1]}"
    desc = chapter[2] if len(chapter) > 2 else "Ethical considerations and bias in AI systems."
    
    qmd_content = f"""---
title: "{title}"
subtitle: "Artificial Intelligence"
description: "{desc}"
image: https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=600&q=80
---

## 📋 Chapter Overview

{desc}

::: {{.callout-warning}}
## 🔜 Coming Soon
Lecture notes and materials for this chapter are currently being prepared.
:::
"""
    file_path = f'course/chapter_{i}.qmd'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(qmd_content)
    print(f"Created {file_path}")
