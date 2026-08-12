import os
import re
import glob

directory = r'e:\I2O\03. Website Subdomain\ICOMIT'

registration_content = """
<hr>
<div id="registration">
    <h2>Registration</h2>
    
    <h3>Physical Registration</h3>
    <p>In Person Conference ICOMIT-2027 fees are as follows:</p>
    <table class="table table-striped table-bordered">
        <thead>
            <tr><th>Category</th><th>Early Bird</th><th>Normal</th></tr>
        </thead>
        <tbody>
            <tr><td>Presenter (per person)</td><td>250 USD</td><td>350 USD</td></tr>
            <tr><td>Participant (per person)</td><td>50 USD</td><td>100 USD</td></tr>
            <tr><td>Additional Paper (per-paper)</td><td>150 USD</td><td></td></tr>
        </tbody>
    </table>

    <br>
    <h3>Virtual Registration</h3>
    <p>In the case of the ICOMIT-2027 Virtual registration.</p>
    <table class="table table-striped table-bordered">
        <thead>
            <tr><th>Category</th><th>Early Bird</th><th>Normal</th></tr>
        </thead>
        <tbody>
            <tr><td>Presenter (per person)</td><td>200 USD</td><td>300 USD</td></tr>
            <tr><td>Participant (per person)</td><td>25 USD</td><td>50 USD</td></tr>
            <tr><td>Additional Paper (per-paper)</td><td>150 USD</td><td></td></tr>
        </tbody>
    </table>

    <br>
    <h3>Payment Method</h3>
    <p><i>To be announced.</i></p>

    <br>
    <h3>Invitation Letter</h3>
    <p><i>To be announced.</i></p>
</div>
"""

# Append registration to submission.html
submission_path = os.path.join(directory, 'submission.html')
with open(submission_path, 'r', encoding='utf-8') as f:
    submission_html = f.read()

# insert before `<div class="content-pane-tube`
submission_html = submission_html.replace('<div class="content-pane-tube', registration_content + '\n<div class="content-pane-tube')

with open(submission_path, 'w', encoding='utf-8') as f:
    f.write(submission_html)

# Update menus across all html files
html_files = glob.glob(os.path.join(directory, '*.html'))
for filepath in html_files:
    if os.path.basename(filepath) == 'registration.html':
        continue # skip, we will delete it

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove Registration tab
    content = re.sub(r'<li(?: class="current")?>\s*<a href="registration\.html"><div>Registration</div></a>\s*</li>\n?', '', content)

    # Remove Program tab from top level
    content = re.sub(r'<li(?: class="current")?>\s*<a href="program\.html"><div>Program</div></a>\s*</li>\n?', '', content)

    # Add Program tab to General Information
    if '<li><a href="program.html"><div>Program</div></a></li>' not in content:
        content = re.sub(
            r'(<div style="line-height: 1.2; text-align: center; margin-top: -6px;">General<br>Information</div></a>\s*<ul>)',
            r'\1\n\t\t\t\t\t\t\t\t\t\t<li><a href="program.html"><div>Program</div></a></li>',
            content
        )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Delete registration.html
reg_path = os.path.join(directory, 'registration.html')
if os.path.exists(reg_path):
    os.remove(reg_path)

print("Finished menu updates and merged Registration into Submission.")
