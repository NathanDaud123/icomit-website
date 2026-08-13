import os
import glob
import re

directory = r'e:\I2O\03. Website Subdomain\ICOMIT'

css_replacement = """				/* Committees ICOMIT Theme */
				#committees {
				    font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
				    padding: 10px;
				}
				
				#committees .committee-section h2 {
				    color: #222;
				    font-size: 18px;
				    font-weight: 700;
				    margin-bottom: 15px;
				}
				
				#committees .member-group h3 {
				    color: #444;
				    font-size: 16px;
				    font-weight: 600;
				    margin: 15px 0 10px 0;
				}
				
				#committees .committee-section {
				    background: transparent;
				    border: none;
				    border-radius: 0;
				    padding: 0;
				    margin-bottom: 30px;
				    box-shadow: none;
				}
				
				#committees .member-group {
				    margin-bottom: 20px;
				}
				
				#committees p, 
				#committees .member-name {
				    font-size: 15px;
				    margin: 0;
				}
				
				#committees ul {
				    list-style-type: none;
				    padding-left: 0;
				    margin-top: 5px;
				}
				
				#committees ul li {
				    position: relative;
				    padding-left: 0; 
				    margin-bottom: 5px;
				    color: #222;
				    font-size: 15px;
				    border-bottom: none;
				    padding-bottom: 0;
				}
				
				#committees ul li::before {
				    content: ""; 
				    display: none;
				}"""

html_files = glob.glob(os.path.join(directory, '*.html'))

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Use regex to find and replace the CSS block
    pattern = re.compile(r'/\*\s*Committees ICOMIT Theme\s*\*/.*?#committees ul li::before \{.*?\n\t\t\t\t\}', re.DOTALL)
    
    modified_content = re.sub(pattern, css_replacement, content)
    
    if modified_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(modified_content)

print("CSS updated successfully.")
