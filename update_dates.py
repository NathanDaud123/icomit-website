import os
import re

file_path = r'e:\I2O\03. Website Subdomain\ICOMIT\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update September 24-26 to September 25-26
content = content.replace("September 24 - 26, 2027", "September 25 - 26, 2027")

# 2. Update July 28-29 in text to September 25-26
content = content.replace("28–29 July 2027", "25–26 September 2027")

# 3. Update countdown timer
content = content.replace('data-time="2027/07/28 08:00:00"', 'data-time="2027/09/25 08:00:00"')

# 4. Update Timeline Dates
# Paper submission: 30 October 2026 -> 30 December 2026
content = content.replace('Friday\t                                        <div class="MonthYear">October 2026</div>', 'Wednesday\t                                        <div class="MonthYear">December 2026</div>')
content = content.replace('30</div>\n\t                                    <div class="Day">\n\t                                        Friday', '30</div>\n\t                                    <div class="Day">\n\t                                        Wednesday')

# Notification: 30 December 2026 -> 28 February 2027
content = content.replace('30</div>\n\t                                    <div class="Day">\n\t                                        Wednesday\t                                        <div class="MonthYear">December 2026</div>', '28</div>\n\t                                    <div class="Day">\n\t                                        Sunday\t                                        <div class="MonthYear">February 2027</div>')

# Camera-ready: 10 February 2027 -> 10 April 2027
content = content.replace('Wednesday\t                                        <div class="MonthYear">February 2027</div>', 'Saturday\t                                        <div class="MonthYear">April 2027</div>')
content = content.replace('10</div>\n\t                                    <div class="Day">\n\t                                        Wednesday', '10</div>\n\t                                    <div class="Day">\n\t                                        Saturday')

# Registration due: 20 February 2027 -> 20 April 2027
content = content.replace('Saturday\t                                        <div class="MonthYear">February 2027</div>', 'Tuesday\t                                        <div class="MonthYear">April 2027</div>')
content = content.replace('20</div>\n\t                                    <div class="Day">\n\t                                        Saturday', '20</div>\n\t                                    <div class="Day">\n\t                                        Tuesday')

# Conference sessions: 28 July 2027 -> 25 September 2027
content = content.replace('28</div>\n\t                                    <div class="Day">\n\t                                        Wednesday\t                                        <div class="MonthYear">July 2027</div>', '25</div>\n\t                                    <div class="Day">\n\t                                        Saturday\t                                        <div class="MonthYear">September 2027</div>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Dates updated successfully.")
