# Data Science Academy

<img height="28" width="28" src="https://cdn.simpleicons.org/python/00ccff99" alt="python" />

[![Deployment](https://github.com/8-chems/lectures/actions/workflows/prod.yml/badge.svg)](https://github.com/8-chems/lectures/actions/workflows/prod.yml)

> **Author:** Chemseddine Berbague  
> **Site:** [8-chems.github.io](https://8-chems.github.io)  
> **Language:** English 🇬🇧

---

## 📚 Overview

A comprehensive **multi-module teaching platform** built with [Quarto](https://quarto.org/), covering two categories of courses:

| Category | Modules |
|---|---|
| 🟦 **Fundamental** | OOP · Data Structures · Databases · Programming · Python & Java |
| 🟧 **Advanced** | Data Science Foundations · Machine Learning (23 weeks) · Statistics (20 modules) · Artificial Intelligence |

The site features:
- **Grid / List** toggle display for all module cards and chapter listings
- **Embedded PDF viewer** for all lecture slides, directed works (DW), and practical works (PW)
- **Structured module pages** with full syllabus, resources, and navigation sidebar

---

## 🗂️ Project Structure

```
8-chems-lectures/
├── _quarto.yml                  # Site config: navbar, sidebars, render list
├── index.qmd                    # Home page (grid/list module cards)
├── requirements.txt             # Python dependencies
│
├── modules/
│   ├── fundamental/
│   │   ├── oop/                 # OOP module
│   │   ├── data_structures/     # Data Structures
│   │   ├── database/            # Databases
│   │   ├── programming/         # Programming Fundamentals
│   │   └── python_java/         # Python & Java
│   │
│   └── advanced/
│       ├── data_science/        # Data Science Foundations (5 chapters)
│       │   ├── course/          # Chapter pages with embedded lecture PDFs
│       │   ├── td/              # Directed Works (DW1–DW5)
│       │   └── tp/              # Practical Works (PW1–PW7)
│       ├── machine_learning/    # ML Program (23 weeks)
│       ├── statistics/          # Statistics (20 modules)
│       └── ai/                  # Artificial Intelligence
│
├── pdfs/
│   └── courses/
│       └── fds/
│           ├── lectures/        # chapter_1.pdf … chapter_5.pdf
│           └── exercises/       # DW1.pdf … DW5.pdf, PW1.pdf … PW7.pdf
│
├── styles/                      # Custom CSS and SCSS
├── content/                     # Images and legacy assets
└── _extensions/                 # Quarto extensions (slide-viewer, etc.)
```

---

## 🚀 Getting Started

### Prerequisites

- [Quarto](https://quarto.org/docs/get-started/) ≥ 1.8
- Python ≥ 3.11

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/8-chems/lectures.git
cd lectures

# 2. Create and activate a virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the local preview
quarto preview
```

The site will open at `http://localhost:XXXX/`.

---

## 📦 PDF Resources

All PDFs are served as static resources from `pdfs/courses/fds/`:

| Type | Files |
|---|---|
| Lectures | `chapter_1.pdf` … `chapter_5.pdf` |
| Directed Works | `DW1.pdf`, `DW2_Part1.pdf`, `DW2_Part2.pdf`, `DW3_part2–4.pdf`, `DW4_part1–2.pdf`, `DW5.pdf` |
| Practical Works | `PW1.pdf` … `PW7.pdf` (including `PW2_Numpy.pdf`) |

To add new PDFs, place them in the appropriate folder and update the corresponding `.qmd` page.

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or a pull request on [GitHub](https://github.com/8-chems/lectures).

---

## ✨ Acknowledgment

This material builds upon **Lino Galiana's** open-source *Python for Data Science* course and has been adapted and significantly extended by **Chemseddine Berbague** into a full multi-module teaching platform.
