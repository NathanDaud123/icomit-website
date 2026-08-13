import os
import re

directory = r'e:\I2O\03. Website Subdomain\ICOMIT'
committees_file = os.path.join(directory, 'committees.html')

with open(committees_file, 'r', encoding='utf-8') as f:
    content = f.read()

# The current structure has a big <div class="committee-section">
# enclosing <h2>Organizing Committee</h2> and multiple <div class="member-group">...</div>
# We want to flatten it.

# Step 1: Remove the enclosing <h2>Organizing Committee</h2>
# Step 2: Replace each <h3>Title</h3> with <h2>Title</h2> and wrap the member-group in its own committee-section

def reformat_match(match):
    # match.group(1) contains everything inside the big committee-section
    inner_html = match.group(1)
    
    # Remove the <h2>Organizing Committee</h2>
    inner_html = re.sub(r'<h2>Organizing Committee</h2>', '', inner_html)
    
    # For each <div class="member-group">...</div>, wrap it in <div class="committee-section">...</div> and change <h3> to <h2>
    def replace_member_group(m):
        title = m.group(1)
        group_content = m.group(2)
        return f'\t<div class="committee-section">\n\t\t<h2>{title}</h2>\n\t\t<div class="member-group">\n{group_content}\t\t</div>\n\t</div>\n'
    
    flattened = re.sub(r'<div class="member-group">\s*<h3>(.*?)</h3>(.*?)\s*</div>', replace_member_group, inner_html, flags=re.DOTALL)
    
    return flattened

# Use regex to find the big committee-section for Organizing Committee
content = re.sub(r'\t<div class="committee-section">\s*<h2>Organizing Committee</h2>([\s\S]*?)\t</div>(?=\n\n\t<div class="committee-section">\n\t\t<h2>Program Committee)', reformat_match, content)

with open(committees_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Update completed successfully.")
