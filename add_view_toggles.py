import os
import re

# Template for the toggle and listings injection
TOGGLE_HTML = """
<div class="view-toggle-bar">
  <button class="view-btn active" id="view-btn-grid" onclick="toggleView('grid')">⊞ Grid View</button>
  <button class="view-btn" id="view-btn-list" onclick="toggleView('list')">☰ List View</button>
</div>

<div id="grid-view-wrap">
::: {#listing-grid}
:::
</div>

<div id="list-view-wrap" style="display:none">
::: {#listing-list}
:::
</div>

<script>
function toggleView(type) {
  document.getElementById('grid-view-wrap').style.display = type === 'grid' ? '' : 'none';
  document.getElementById('list-view-wrap').style.display = type === 'list' ? '' : 'none';
  document.getElementById('view-btn-grid').classList.toggle('active', type === 'grid');
  document.getElementById('view-btn-list').classList.toggle('active', type === 'list');
}
</script>

<style>
.view-toggle-bar { display: flex; gap: 8px; margin-top: 20px; margin-bottom: 16px; justify-content: flex-end; }
.view-btn { padding: 6px 16px; border: 1.5px solid #ddd; border-radius: 6px; background: transparent; cursor: pointer; font-size: 0.9em; transition: all 0.2s; }
.view-btn:hover { border-color: #666; background: #f5f5f5; }
.view-btn.active { background: #2c3e50; color: white; border-color: #2c3e50; }
</style>
"""

modules = [
    "modules/advanced/machine_learning",
    "modules/advanced/statistics",
    "modules/advanced/ai",
    "modules/advanced/business_analytics",
    "modules/fundamental/oop",
    "modules/fundamental/data_structures",
    "modules/fundamental/database",
    "modules/fundamental/programming",
    "modules/fundamental/python_java"
]

for mod in modules:
    index_path = os.path.join(mod, "index.qmd")
    if not os.path.exists(index_path):
        print(f"Skipping {index_path} (not found)")
        continue
        
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Check if already has toggle
    if "view-toggle-bar" in content:
        print(f"Skipping {index_path} (already has toggle)")
        continue

    # Extract YAML
    yaml_match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not yaml_match:
        continue
        
    yaml_content = yaml_match.group(1)
    
    # Identify the existing listing ID and contents
    # I used "weeks-grid", "modules-grid", "chapters-grid" in my previous edits.
    # I will standardize them to "listing-grid" and "listing-list" for this automation.
    
    # First, let's find the contents list
    lines = yaml_content.split('\n')
    grid_id = ""
    listing_contents = []
    in_listing = False
    in_contents = False
    
    for line in lines:
        if line.strip().startswith("- id:"):
            grid_id = line.split(":", 1)[1].strip()
            in_listing = True
        elif line.strip() == "contents:":
            in_contents = True
        elif in_contents and line.strip().startswith("- "):
            listing_contents.append(line.strip())
        elif in_contents and not line.strip().startswith("- "):
            in_contents = False
            
    if not listing_contents:
        print(f"Failed to extract listing contents from {index_path}")
        continue

    # Replace the YAML part with standardized listing IDs
    # I'll just rebuild the listing section for clarity
    
    # We need to know if it's "weeks" or "chapters" etc. but listing_contents already has it.
    
    new_listing_yaml = f"""  - id: listing-grid
    contents:
      {chr(10).join(['      ' + c for c in listing_contents]) if not listing_contents[0].startswith('      ') else chr(10).join(listing_contents)}
    type: grid
    grid-columns: 3
    fields: [image, title, description]
    image-height: 180px
    categories: false
    sort: false
  - id: listing-list
    contents:
      {chr(10).join(['      ' + c for c in listing_contents]) if not listing_contents[0].startswith('      ') else chr(10).join(listing_contents)}
    type: table
    fields: [title, description]
    categories: false
    sort: false"""

    # We need to match the old listing block to replace it.
    # Search for "listing:\n  - id: ... sort: false"
    # Actually, easier to replace from "listing:" to the next top-level key.
    
    pattern = r"listing:\n(.*?)(?=\n[a-z]|$)"
    # Clean up indentations and such
    new_yaml_full = re.sub(pattern, f"listing:\n{new_listing_yaml}", yaml_content, flags=re.DOTALL)
    
    content = content.replace(yaml_content, new_yaml_full)
    
    # Now replace the body placeholder
    # Search for ::: {#old-id} :::
    body_pattern = rf"::: {{#{grid_id}}}\n:::"
    content = re.sub(body_pattern, TOGGLE_HTML, content)
    
    # Also handle standard names if I missed them
    content = re.sub(r"::: {#.*?grid}\n:::", TOGGLE_HTML, content)

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"Updated {index_path}")
