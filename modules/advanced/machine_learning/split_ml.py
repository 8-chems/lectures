import re
import os

with open('index.qmd', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the week-by-week curriculum section
curriculum_match = re.search(r'## 📅 Week-by-Week Curriculum(.*?)## 🏆 Capstone Project Ideas', content, re.DOTALL)
if not curriculum_match:
    print("Could not find curriculum section")
    exit(1)

curriculum = curriculum_match.group(1)

# Split by weeks
weeks = re.split(r'### Week (\d+) — (.*?)\n', curriculum)

# week[0] is empty or preamble
# week[1] is "1", week[2] is "ML Foundations & Workflow", week[3] is the content
# and so on...

os.makedirs('weeks', exist_ok=True)

for i in range(1, len(weeks), 3):
    week_num = weeks[i].zfill(2)
    week_title = weeks[i+1].strip()
    week_content = weeks[i+2].strip()
    
    # Remove terminating --- if present
    week_content = re.sub(r'\n---$', '', week_content)
    
    # Format description (take first bullet point or sentence)
    desc_match = re.search(r'- (.*?)\n', week_content)
    description = desc_match.group(1) if desc_match else f"Learning about {week_title}"
    
    qmd_content = f"""---
title: "Week {int(week_num)} — {week_title}"
subtitle: "Machine Learning"
description: "{description}"
image: https://images.unsplash.com/photo-1677442135703-1787eea5ce01?w=600&q=80
---

{week_content}
"""
    file_path = f'weeks/week_{week_num}.qmd'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(qmd_content)
    print(f"Created {file_path}")
