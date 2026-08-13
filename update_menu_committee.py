import os
import glob
import re

directory = r'e:\I2O\03. Website Subdomain\ICOMIT'

# Task 1: Reorder Previous Event dropdown
old_dropdown = """										<li><a href="https://icomit.ub.ac.id/event/icomit22" target="_blank"><div>1st 2021</div></a></li>
										<li><a href="https://icomit.ub.ac.id/event/icomit23" target="_blank"><div>2nd 2022</div></a></li>
										<li><a href="https://icomit.ub.ac.id/event/icomit24" target="_blank"><div>3rd 2023</div></a></li>
										<li><a href="https://icomit.ub.ac.id/event/icomit25" target="_blank"><div>4th 2024</div></a></li>
										<li><a href="https://icomit.ub.ac.id/event/icomit26" target="_blank"><div>5th 2025</div></a></li>"""

new_dropdown = """										<li><a href="https://icomit.ub.ac.id/event/icomit26" target="_blank"><div>5th 2025</div></a></li>
										<li><a href="https://icomit.ub.ac.id/event/icomit25" target="_blank"><div>4th 2024</div></a></li>
										<li><a href="https://icomit.ub.ac.id/event/icomit24" target="_blank"><div>3rd 2023</div></a></li>
										<li><a href="https://icomit.ub.ac.id/event/icomit23" target="_blank"><div>2nd 2022</div></a></li>
										<li><a href="https://icomit.ub.ac.id/event/icomit22" target="_blank"><div>1st 2021</div></a></li>"""

html_files = glob.glob(os.path.join(directory, '*.html'))
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = content.replace(old_dropdown, new_dropdown)
    
    if modified != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(modified)

# Task 2: Add to Steering Committee in committees.html
committees_file = os.path.join(directory, 'committees.html')
with open(committees_file, 'r', encoding='utf-8') as f:
    content = f.read()

steering_insert = """				<li><strong>Tri Astoto Kurniawan</strong>, Universitas Brawijaya, <strong>INDONESIA</strong></li>
				<li><strong>Sabriansyah Rizqika Akbar</strong>, Universitas Brawijaya, <strong>INDONESIA</strong></li>
			</ul>"""

# Find the end of the Steering Committee ul and insert
content = re.sub(r'(<h2>Steering Committee</h2>\s*<div class="member-group">\s*<ul>[\s\S]*?)</ul>', lambda m: m.group(1) + steering_insert, content, count=1)

with open(committees_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Update completed successfully.")
