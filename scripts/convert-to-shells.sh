#!/bin/bash
# Convert gender and pubpol course HTML files to dynamic loader shells.
# Replaces each module section's content with a placeholder div.

set -e

for course in gender pubpol; do
  FILE="courses/$course/index.html"
  echo "Converting: $FILE"

  python3 -c "
import re, sys

with open('$FILE', 'r') as f:
    html = f.read()

# Find all module sections and replace their content with placeholders
# Gender uses: <section class=\"module\" id=\"moduleN\">
# Pubpol uses: <section class=\"section reveal\" id=\"moduleN\">

def replace_module(match):
    full = match.group(0)
    num = match.group(1)
    # Build the shell section
    section_tag = full[:full.index('>')+1]  # The opening <section ...> tag
    shell = section_tag + '''

                    <div id=\"module''' + num + '''-content\" class=\"module-content-placeholder\">
                        <!-- Content loaded dynamically by course-loader.js -->
                    </div>

                </section>'''
    return shell

# Match each section from opening to closing tag
# We need to match sections with id=moduleN specifically
pattern = r'<section\s+[^>]*?id=\"module(\d+)\"[^>]*>[\s\S]*?</section>'
result = re.sub(pattern, replace_module, html)

with open('$FILE', 'w') as f:
    f.write(result)

# Count modules converted
count = len(re.findall(r'module-content-placeholder', result))
print(f'  Converted {count} modules to placeholders')
"
done

echo "Done!"
