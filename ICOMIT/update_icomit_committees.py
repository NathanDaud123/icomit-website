import os
import re

directory = r'e:\I2O\03. Website Subdomain\ICOMIT'
filepath = os.path.join(directory, 'committees.html')

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_committees_html = """<div id="committees">

	<div class="committee-section">
		<h2>Steering Committee</h2>
		<div class="member-group">
			<ul>
				<li><strong>Alvaro Manuel Reis da Rocha</strong>, ISEG University of Lisbon, <strong>PORTUGAL</strong></li>
				<li><strong>Anand Nayyar</strong>, Duy Tan University, <strong>VIETNAM</strong></li>
				<li><strong>Anton Satria Prabuwono</strong>, King Abdulaziz University, <strong>SAUDI ARABIA</strong></li>
				<li><strong>Chikamune Wada</strong>, Kyushu Institute of Technology</li>
				<li><strong>Elhadj Benkhelifa</strong>, University of Staffordshire, <strong>UNITED KINGDOM</strong></li>
				<li><strong>Fitri Utaminingrum</strong>, Universitas Brawijaya, <strong>INDONESIA</strong></li>
				<li><strong>Jasni Mohd Zain</strong>, Universiti Teknologi MARA</li>
				<li><strong>Jemal H Abawajy</strong>, Deakin University, <strong>AUSTRALIA</strong></li>
				<li><strong>Maizatul Akmar Ismail</strong>, Universiti Malaya</li>
				<li><strong>Mohd Shahrizal Sunar</strong>, University Teknologi Malaysia, <strong>MALAYSIA</strong></li>
				<li><strong>Nobuo Funabiki</strong>, Okayama University, <strong>JAPAN</strong></li>
				<li><strong>Por Lip Yee</strong>, Universiti Malaya</li>
				<li><strong>Taufik</strong>, Cal Poly State University, <strong>USA</strong></li>
				<li><strong>Wayan Firdaus Mahmudy</strong>, Universitas Brawijaya, <strong>INDONESIA</strong></li>
			</ul>
		</div>
	</div>

	<div class="committee-section">
		<h2>Organizing Committee</h2>

		<div class="member-group">
			<h3>General Chairs</h3>
			<ul>
				<li><strong>Diva Kurnianingtyas</strong>, Universitas Brawijaya, <strong>INDONESIA</strong></li>
				<li><strong>Lailil Muflikhah</strong>, Universitas Brawijaya, <strong>INDONESIA</strong></li>
			</ul>
		</div>

		<div class="member-group">
			<h3>Program Committee Chairs</h3>
			<ul>
				<li><strong>Mohammad Ali Fauzi</strong>, Universitas Brawijaya, <strong>INDONESIA</strong></li>
				<li><strong>Yousef Farhaoui</strong></li>
				<li><strong>Wan Azani Mustafa</strong>, Universiti Malaysia Perlis</li>
			</ul>
		</div>

		<div class="member-group">
			<h3>International Liasion</h3>
			<ul>
				<li><strong>Tutut Herawan</strong>, Universiti Malaya</li>
				<li><strong>Haruna Chiroma</strong>, University of Hafr Al Batin, Saudi Arabia (freedonchi@yahoo.com; charuna@uhb.edu.sa; chiromaharun@fcetgombe.edu.ng)</li>
				<li><strong>Sharifah Sakinah Syed Ahmad</strong>, Universiti Teknikal Malaysia Melaka</li>
				<li><strong>Hideyuki Sawada</strong>, Waseda University</li>
				<li><strong>Rosilah Hassan</strong>, Universiti Kebangsaan Malaysia</li>
				<li><strong>Amir Hamzah Sharaai</strong>, Universiti Putra Malaysia</li>
				<li><strong>Azlan Mohd Zain</strong>, Universiti Teknologi Malaysia</li>
				<li><strong>Herman Tolle</strong>, Universitas Brawijaya, <strong>INDONESIA</strong></li>
			</ul>
		</div>

		<div class="member-group">
			<h3>Organizing Committee</h3>
			<ul>
				<li><strong>Anis Rahmawati Amna</strong>, Universitas Brawijaya</li>
				<li><strong>Agus Wahyu Widodo</strong>, Universitas Brawijaya</li>
				<li><strong>Muh. Arif Rahman</strong>, Universitas Brawijaya</li>
				<li><strong>Bayu Rahayudi</strong>, Universitas Brawijaya</li>
				<li><strong>Dian Eka Ratnawati</strong>, Universitas Brawijaya</li>
				<li><strong>Ismiarta Aknuranda</strong>, Universitas Brawijaya</li>
				<li><strong>Arief Andy Soebroto</strong>, Universitas Brawijaya</li>
			</ul>
		</div>
	</div>

	<div class="committee-section">
		<h2>Program Committee</h2>
		<div class="member-group">
			<p style="text-align:justify">We will invite 100 people to be in this committee</p>
		</div>
	</div>

</div>"""

# Replace the existing <div id="committees">...</div>
new_content = re.sub(r'<div id="committees">.*?</div>\s*<div class="content-pane-tube', new_committees_html + '\n\t\t\t\t\t\t<div class="content-pane-tube', content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Finished updating Committees content for ICOMIT.")
