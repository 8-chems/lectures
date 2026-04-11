import re
import os

with open('index.qmd', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the curriculum section
curriculum_match = re.search(r'## 📚 Course Structure(.*?)## 📊 Assessment', content, re.DOTALL)
if not curriculum_match:
    print("Could not find curriculum section")
    exit(1)

curriculum = curriculum_match.group(1)

# Split by modules
modules = re.split(r'### Module (\d+) — (.*?)\n', curriculum)

os.makedirs('weeks', exist_ok=True)

for i in range(1, len(modules), 3):
    mod_num = modules[i].zfill(2)
    mod_title = modules[i+1].strip()
    mod_content = modules[i+2].strip()
    
    # Remove terminating --- if present
    mod_content = re.sub(r'\n---$', '', mod_content)
    
    # Format description (take first bullet point or sentence)
    desc_match = re.search(r'- (.*?)\n', mod_content)
    description = desc_match.group(1) if desc_match else f"Learning about {mod_title}"
    
    qmd_content = f"""---
title: "Module {int(mod_num)} — {mod_title}"
subtitle: "Statistics & Data Analysis"
description: "{description}"
image: https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&q=80
---

{mod_content}
"""
    file_path = f'weeks/module_{mod_num}.qmd'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(qmd_content)
    print(f"Created {file_path}")
