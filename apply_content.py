import re

file_path = r'e:\I2O\03. Website Subdomain\ICOMIT\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update About ICOMIT 2027 section
old_about = """						<h3>About ICOMIT 2027</h3>
						<p style="text-align:justify"><b>ICOMIT 2027</b> is an international forum that brings together researchers, academicians, students, industry professionals, government representatives, and technology practitioners to present and discuss recent advances in computing and information technology.</p>

<p style="text-align:justify">Under the theme “Engineering Human-Centered Computing Solutions for Inclusive and Sustainable Digital Transformation,” ICOMIT 2027 emphasizes the development and application of computing technologies that are innovative, secure, reliable, accessible, and responsive to real-world needs.</p>

<p style="text-align:justify">The conference welcomes original research and practical contributions in software engineering, information systems, computer networks, cybersecurity, cloud and edge computing, the Internet of Things, embedded and cyber-physical systems, human–computer interaction, multimedia, computing education, digital governance, and applied computing.</p>

<p style="text-align:justify">ICOMIT 2027 provides opportunities for participants to exchange knowledge, receive scholarly feedback, build international research networks, and establish collaborations among academia, industry, government, and society.</p>

<p style="text-align:justify">Through keynote sessions, technical presentations, academic discussions, and professional networking, ICOMIT 2027 seeks to connect scientific advancement with practical implementation and meaningful societal impact.</p>

<p style="text-align:justify">We invite researchers, practitioners, professionals, and students from around the world to join us in Bali, Indonesia, on 25–26 September 2027, and contribute to the advancement of responsible, inclusive, and sustainable computing technologies.</p>"""

new_about = """						<h3>About ICOMIT 2027</h3>
						<p style="text-align:justify"><b>ICOMIT 2027</b> is an international forum that focuses on the application of intelligent computing and digital technology (Multidisciplinary Applied). It brings together researchers, academicians, students, industry professionals, and technology practitioners with an international, multidisciplinary orientation to present and discuss recent advances in technology applications.</p>

<p style="text-align:justify">Under the theme “Human-Centered Intelligent Computing for Inclusive Digital Transformation,” ICOMIT 2027 emphasizes the development and application of human-centered intelligent computing technologies to support inclusive digital transformation.</p>

<p style="text-align:justify">The conference provides opportunities for participants to exchange knowledge, receive scholarly feedback, build international research networks, and establish collaborations among academia, industry, government, and society.</p>

<p style="text-align:justify">Through keynote sessions, technical presentations, academic discussions, and professional networking, ICOMIT 2027 seeks to connect scientific advancement with practical implementation and meaningful societal impact.</p>

<p style="text-align:justify">We invite researchers, practitioners, professionals, and students from around the world to join us in Bali, Indonesia, on 25–26 September 2027, and contribute to the advancement of responsible, inclusive, and sustainable computing technologies.</p>"""

content = content.replace(old_about, new_about)

# 2. Update Steering Committee carousel
members = [
    ("Alvaro Manuel Reis da Rocha", "ISEG University of Lisbon, PORTUGAL"),
    ("Anand Nayyar", "Duy Tan University, VIETNAM"),
    ("Anton Satria Prabuwono", "King Abdulaziz University, SAUDI ARABIA"),
    ("Chikamune Wada", "Kyushu Institute of Technology"),
    ("Elhadj Benkhelifa", "University of Staffordshire, UNITED KINGDOM"),
    ("Fitri Utaminingrum", "Universitas Brawijaya, INDONESIA"),
    ("Jasni Mohd Zain", "Universiti Teknologi MARA"),
    ("Jemal H Abawajy", "Deakin University, AUSTRALIA"),
    ("Maizatul Akmar Ismail", "Universiti Malaya"),
    ("Mohd Shahrizal Sunar", "University Teknologi Malaysia, MALAYSIA"),
    ("Nobuo Funabiki", "Okayama University, JAPAN"),
    ("Por Lip Yee", "Universiti Malaya"),
    ("Taufik", "Cal Poly State University, USA"),
    ("Wayan Firdaus Mahmudy", "Universitas Brawijaya, INDONESIA"),
    ("Tri Astoto Kurniawan", "Universitas Brawijaya, INDONESIA"),
    ("Sabriansyah Rizqika Akbar", "Universitas Brawijaya, INDONESIA")
]

carousel_html = ""
for name, affil in members:
    carousel_html += f"""					<div class="row">
						<div class="col-md-offset-3 col-md-6">
							<img src="https://icomit.ub.ac.id/assets/ptiik/siet/img/no-photo-2.png" class="img img-responsive img-keynote img-responsive--center img--border">
						</div>
						<div class="col-md-3 nopadding">
							<h5 data-hrefopen="#">{name}</h5>
							<h6 class="margin-top-no">{affil}</h6>
						</div>
					</div>\n"""

old_carousel = """										<div class="row">
						<div class="col-md-offset-3 col-md-6">
							<img src="https://icomit.ub.ac.id/assets/ptiik/siet/img/no-photo-2.png" class="img img-responsive img-keynote img-responsive--center img--border">
						</div>
						<div class="col-md-3 nopadding">
							<h5 data-hrefopen="#">To be confirmed</h5>
							<h6 class="margin-top-no">To be confirmed</h6>
						</div>
					</div>"""

content = content.replace(old_carousel, carousel_html.strip())

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Content updated successfully.")
