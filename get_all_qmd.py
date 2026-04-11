import os

def get_render_list(root_dir):
    render_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.qmd'):
                rel_path = os.path.relpath(os.path.join(root, file), root_dir).replace('\\', '/')
                render_files.append(rel_path)
    return sorted(render_files)

def generate_sidebar_sidebar(mod_path):
    # This is a bit complex to automate fully without reading metadata
    pass

all_qmd = get_render_list('.')
with open('temp_render_list.txt', 'w') as f:
    for file in all_qmd:
        f.write(f"    - {file}\n")
print("Saved render list to temp_render_list.txt")
