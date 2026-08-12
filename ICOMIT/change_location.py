import os
import re

directory = r'e:\I2O\03. Website Subdomain\ICOMIT'

# 1. Update index.html
index_path = os.path.join(directory, 'index.html')
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

index_content = index_content.replace(
    'July 28 - 29, 2027, Malang, Indonesia', 
    'July 28 - 29, 2027, Bali, Indonesia'
)
index_content = index_content.replace(
    'held in Malang, Indonesia, on 28–29 July 2027', 
    'held in Bali, Indonesia, on 28–29 July 2027'
)
index_content = index_content.replace(
    'join us in Malang, Indonesia, on 28–29 July 2027', 
    'join us in Bali, Indonesia, on 28–29 July 2027'
)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_content)


# 2. Update icomit26.html
icomit26_path = os.path.join(directory, 'icomit26.html')
with open(icomit26_path, 'r', encoding='utf-8') as f:
    icomit26_content = f.read()

icomit26_content = icomit26_content.replace(
    'ICOMIT 2027 will take place in Malang, Indonesia, on September 8-9, 2026.', 
    'ICOMIT 2027 will take place in Bali, Indonesia, on July 28 - 29, 2027.'
)

with open(icomit26_path, 'w', encoding='utf-8') as f:
    f.write(icomit26_content)


# 3. Update venue.html
venue_path = os.path.join(directory, 'venue.html')
with open(venue_path, 'r', encoding='utf-8') as f:
    venue_content = f.read()

old_venue = """<address>
        <strong>Faculty of Computer Science (FILKOM)</strong><br>
        Universitas Brawijaya<br>
        Jl. Veteran, Ketawanggede, Lowokwaru<br>
        Malang City, East Java, 65145<br>
        INDONESIA
    </address>"""

new_venue = """<address>
        <strong>Bali, Indonesia</strong><br>
        <i>Detailed venue to be announced</i>
    </address>"""

venue_content = venue_content.replace(old_venue, new_venue)

with open(venue_path, 'w', encoding='utf-8') as f:
    f.write(venue_content)

print("Finished updating Malang to Bali.")
