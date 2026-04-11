import yaml

# Load original _quarto.yml
with open('_quarto.yml', 'r', encoding='utf-8') as f:
    orig = yaml.safe_load(f)

# Load generated config
with open('sidebar_gen.yaml', 'r', encoding='utf-8') as f:
    gen = yaml.safe_load(f)

# Update render list
orig['project']['render'] = gen['render']

# Update sidebars
# We keep existing sidebars that are NOT in gen['sidebars']
existing_sidebar_ids = [s.get('id') for s in gen['sidebars']]
new_sidebars = []

# Keep data-science if it's special (it was)
for s in orig['website']['sidebar']:
    if s.get('id') not in existing_sidebar_ids and s.get('id') != 'data-science':
        new_sidebars.append(s)

# Add all generated ones
new_sidebars.extend(gen['sidebars'])

# Restore data-science (I want to keep the one from orig because it had TD/TP sections)
# Wait, I should probably modularize it too or keep it.
# Let's keep the original data-science one.
for s in orig['website']['sidebar']:
    if s.get('id') == 'data-science':
        new_sidebars.append(s)

orig['website']['sidebar'] = new_sidebars

# Save back
with open('_quarto.yml', 'w', encoding='utf-8') as f:
    yaml.dump(orig, f, sort_keys=False, allow_unicode=True)
