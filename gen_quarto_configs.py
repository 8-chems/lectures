import os
import yaml

# Simplified YAML generation for _quarto.yml

render_list = [
    "index.qmd",
    "404.qmd",
    # Fundamental
    "modules/fundamental/oop/index.qmd",
    *[f"modules/fundamental/oop/course/chapter_{i}.qmd" for i in range(1, 6)],
    "modules/fundamental/data_structures/index.qmd",
    *[f"modules/fundamental/data_structures/course/chapter_{i}.qmd" for i in range(1, 8)],
    "modules/fundamental/database/index.qmd",
    *[f"modules/fundamental/database/course/chapter_{i}.qmd" for i in range(1, 8)],
    "modules/fundamental/programming/index.qmd",
    *[f"modules/fundamental/programming/course/chapter_{i}.qmd" for i in range(1, 7)],
    "modules/fundamental/python_java/index.qmd",
    *[f"modules/fundamental/python_java/course/p{i}.qmd" for i in range(1, 5)],
    *[f"modules/fundamental/python_java/course/j{i}.qmd" for i in range(1, 5)],
    # Advanced
    "modules/advanced/data_science/index.qmd",
    *[f"modules/advanced/data_science/course/chapter_{i}/index.qmd" for i in range(1, 6)],
    *[f"modules/advanced/data_science/td/dw{i}.qmd" for i in [1, "2_part1", "2_part2", "3_part2", "3_part3", "3_part4", "4_part1", "4_part2", 5]],
    *[f"modules/advanced/data_science/tp/pw{i}.qmd" for i in range(1, 8)],
    "modules/advanced/machine_learning/index.qmd",
    *[f"modules/advanced/machine_learning/weeks/week_{str(i).zfill(2)}.qmd" for i in range(1, 24)],
    "modules/advanced/statistics/index.qmd",
    *[f"modules/advanced/statistics/weeks/module_{str(i).zfill(2)}.qmd" for i in range(1, 21)],
    "modules/advanced/ai/index.qmd",
    *[f"modules/advanced/ai/course/chapter_{i}.qmd" for i in range(1, 8)],
    "modules/advanced/business_analytics/index.qmd",
    *[f"modules/advanced/business_analytics/weeks/week_{str(i).zfill(2)}.qmd" for i in range(1, 15)],
]

def make_sidebar(id, title, index, weeks, prefix="Week"):
    return {
        "id": id,
        "title": title,
        "style": "docked",
        "collapse-level": 1,
        "contents": [
            index,
            {
                "section": "Curriculum",
                "contents": weeks
            }
        ]
    }

sidebars = [
    # Existing ones would be here too, but I'll generate new ones
    make_sidebar("machine-learning", "Machine Learning", "modules/advanced/machine_learning/index.qmd", 
                 [f"modules/advanced/machine_learning/weeks/week_{str(i).zfill(2)}.qmd" for i in range(1, 24)]),
    make_sidebar("statistics", "Statistics", "modules/advanced/statistics/index.qmd", 
                 [f"modules/advanced/statistics/weeks/module_{str(i).zfill(2)}.qmd" for i in range(1, 21)]),
    make_sidebar("ai", "Artificial Intelligence", "modules/advanced/ai/index.qmd", 
                 [f"modules/advanced/ai/course/chapter_{i}.qmd" for i in range(1, 8)]),
    make_sidebar("business-analytics", "Business Analytics", "modules/advanced/business_analytics/index.qmd", 
                 [f"modules/advanced/business_analytics/weeks/week_{str(i).zfill(2)}.qmd" for i in range(1, 15)]),
    make_sidebar("oop", "OOP", "modules/fundamental/oop/index.qmd", 
                 [f"modules/fundamental/oop/course/chapter_{i}.qmd" for i in range(1, 6)]),
    make_sidebar("data-structures", "Data Structures", "modules/fundamental/data_structures/index.qmd", 
                 [f"modules/fundamental/data_structures/course/chapter_{i}.qmd" for i in range(1, 8)]),
    make_sidebar("database", "Databases", "modules/fundamental/database/index.qmd", 
                 [f"modules/fundamental/database/course/chapter_{i}.qmd" for i in range(1, 8)]),
    make_sidebar("programming", "Programming", "modules/fundamental/programming/index.qmd", 
                 [f"modules/fundamental/programming/course/chapter_{i}.qmd" for i in range(1, 7)]),
    make_sidebar("python-java", "Python & Java", "modules/fundamental/python_java/index.qmd", 
                 [f"modules/fundamental/python_java/course/p{i}.qmd" for i in range(1, 5)] + [f"modules/fundamental/python_java/course/j{i}.qmd" for i in range(1, 5)]),
]

# Write to temp file
with open('sidebar_gen.yaml', 'w') as f:
    yaml.dump({"render": render_list, "sidebars": sidebars}, f, sort_keys=False)
