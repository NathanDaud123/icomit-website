import os
import glob

directory = r'e:\I2O\03. Website Subdomain\ICOMIT'

raw_text = """1	Agung Brastama Putra	Universitas Pembangunan Nasional Veteran Jawa Timur			
2	Agus Wahyu Widodo	Universitas Brawijaya			
3	Al Hafiz Akbar Maulana Siagian	National Research and Innovation Agency			
4	Alvaro Manuel Reis da Rocha	ISEG University of Lisbon			
5	Alvi Syahrina	Universitas Gadjah Mada			
6	Amir Hamzah Sharaai	Universiti Putra Malaysia			
7	Amrutha Muralidharan Nair	Adi Shankara Institute of Engineering and Technology			
8	Anand Nayyar	Duy Tan University			
9	Anand Nayyar	Duy Tan University, VIETNAM			
10	Anggraini Kusumaningrum	Adisutjipto Institute of Aerospace Technology			
11	Anis Rahmawati Amna	Universitas Brawijaya			
12	Anton Satria Prabuwono	King Abdulaziz University			
13	Anurag Yadav	CDOT			
14	Ardvin Kester S Ong	Mapua University, Phillipines			
15	Arief Andy Soebroto	Universitas Brawijaya			
16	Arrie Kurniawardhani	Universitas Islam Indonesia			
17	Arunkumar Jagadeesan	Campfire Interactive Inc.			
18	Asrani Lit	Universiti Malaysia Sarawak			
19	Astria Hijriani	Ulsan National Institute of Science and Technology			
20	Azah Anir Norman	Universiti Malaya			
21	Azine Houria	BLIDA 1 University			
22	Azlan Mohd Zain	Universiti Teknologi Malaysia			
23	Bayu Rahayudi	Universitas Brawijaya			
24	Chikamune Wada	Kyushu Institute of Technology			
25	Deven Panchal	AT&T			
26	Dhanunjaya Rao Gorrle	Western Digital Technologies Inc.			
27	Dian Eka Ratnawati	Universitas Brawijaya			
28	Dion Hayu Fandiantoro	Kumamoto University			
29	Diva Kurnianingtyas	Universitas Brawijaya			
30	Dwija Wisnu Brata	Universitas Brawijaya			
31	Edita Rosana Widasari	Universitas Brawijaya			
32	Eko Sakti Pramukantoro	Universitas Brawijaya			
33	Elhadj Benkhelifa	University of Staffordshire			
34	Faridah Abd Rahman	International Islamic University of Malaysia			
35	Fitri Utaminingrum	Universitas Brawijaya, INDONESIA			
36	Guna Sekhar Sajja	University of the Cumberlands			
37	Gustavo E Fernandez	Instituto Superior Tecnológico España			
38	Gusti Ahmad Fanshuri Alfarisy	Institut Teknologi Kalimantan			
39	Hairulnizam Bin Mahdin	Universitas Tun Hussein Onn Malaysia			
40	Hanif Fermanda Putra	Wakayama University			
41	Hariyatul Fitria	Universitas Brawijaya			
42	Haruna Chiroma	University of Hafr Al Batin, Saudi Arabia 			
43	Hayder Saadi Radeaf	University of Baghdad			
44	Herman Tolle	Universitas Brawijaya			
45	Hideyuki Sawada	Waseda University			
46	Ida Wahyuni	Institut Teknologi Dan Bisnis Asia Malang			
47	Irfan Ahmad	University of Waikato			
48	Ismiarta Aknuranda	Universitas Brawijaya			
49	Jack L. Burbank	Sabre Systems, Inc.			
50	Jasni Mohamad Zain	Universiti Teknologi MARA			
51	Jay Bharat Mehta	Cleveland State University, Alumni			
52	Jayant Ramesh Nandwalkar	University of Mumbai			
53	Jigneshkumar Patel	Advanced Micro Devices Inc.			
54	Kannuru Srinadh	National Institute of Technology Rourkela			
55	Kong Woun Tan	Tunku Abdul Rahman University of Management and Technology			
56	Lailil Muflikhah	Universitas Brawijaya			
57	Maizatul Akmar Ismail	Universiti Malaya			
58	Marvin Rick Gadon Forcado	Romblon State University			
59	Mery Diana	Kumamoto University			
60	Milankumar Rana	University of the Cumberlands			
61	Mohammad Ali Fauzi	Universitas Brawijaya, INDONESIA			
62	Mohammed Faez Hasan	University of Kerbala			
63	Mohammed Nasereddin	Polish Academy of Sciences			
64	Mohd Farhan bin MD Fudzee	Universitas Tun Hussein Onn Malaysia			
65	Mohd Shahrizal Sunar	Universiti Teknologi Malaysia			
66	Mohd Shahrizal Sunar	University Teknologi Malaysia, MALAYSIA			
67	Muh. Arif Rahman	Universitas Brawijaya			
68	Muhammad Fikry	Universitas Malikussaleh			
69	Muhammad Nurwegiono	Universitas Ma Chung			
70	Myeongsu Seong	Xi'an Jiaotong-Liverpool University			
71	Nassima Bousahba	Hassiba Benbouali University of Chlef			
72	Neetu Singh	Aziro Technologies			
73	Nobuo Funabiki	Okayama University			
74	Noriko Etani	Kyoto University			
75	Norjihan Abdul Ghani	Universiti Malaya			
76	Okta Purnawirawan	Universitas Brawijaya			
77	Oluwadamilola Oshin	Covenant University			
78	Parma Hadi Rantelinggi	Keio University			
79	Por Lip Yee	Universiti Malaya			
80	Prima Zulvarina	Universitas Brawijaya			
81	Putra Pandu Adikara	Universitas Brawijaya			
82	Rahid Z Alekberli	Azerbaijan Technical University			
83	Risky Aswi Ramadhani	University Nusantara PGRI Kediri			
84	Rommy Hartono	Universitas Gadjah Mada			
85	Rosario Gaeta	University of Salerno			
86	Rosilah Hassan	Universiti Kebangsaan Malaysia			
87	Saad Wazir	Korea Advanced Institute of Science and Technology (KAIST)			
88	Sai Krishna Gunda	CVS Pharma			
89	Sai Sriram Gonthina	International Institute of Information Technology, Naya Raipur			
90	Samsul Huda	Okayama University			
91	Saurabh Chandra	School of Law, Bennett University Greater Noida			
92	Sharifah Sakinah Syed Ahmad	Universiti Teknikal Malaysia Melaka			
93	Shideh Yavary Mehr	Old Dominion University			
94	Soham Ghosh	Black & Veatch			
95	Sridhar K Irujolla	IEEE			
96	Sujan Chandra Roy	Chittagong University of Engineering and Technology			
97	Syeda F Nasim	NED University of Engineering & Technology			
98	Taufik	Cal Poly State University, USA			
99	Tejal Ghuge	Suzy Inc			
100	Ting Xu	UMass Boston			
101	Tutut Herawan	Universiti Malaya			
102	Vijayakanthan Ganesalingam	University of Vavuniya			
103	Wan Azani Mustafa	Universiti Malaysia Perlis			
104	Wayan Firdaus Mahmudy	Universitas Brawijaya, INDONESIA			
105	Ye Zhu	Cleveland State University			
106	Yohanes Yohanie Fridelin Panduman	Osaka University			
107	Yousef Farhaoui	Morocco			
108	Zouari Farouk	University of Tunis El Manar"""

# Process the program committee members
lines = raw_text.split('\n')
ul_content = "<ul>\n"
for line in lines:
    parts = line.split('\t')
    if len(parts) >= 3:
        name = parts[1].strip()
        affiliation = parts[2].strip()
        ul_content += f"\t\t\t\t<li><strong>{name}</strong>, {affiliation}</li>\n"
ul_content += "\t\t\t</ul>"

# Update committees.html
committees_file = os.path.join(directory, 'committees.html')
with open(committees_file, 'r', encoding='utf-8') as f:
    content = f.read()

target = '<p style="text-align:justify">We will invite 100 people to be in this committee</p>'
content = content.replace(target, ul_content)

with open(committees_file, 'w', encoding='utf-8') as f:
    f.write(content)

# Update the navbar previous edition terms across all HTML files
replacements = {
    'First Edition': '1st 2021',
    'Second Edition': '2nd 2022',
    'Third Edition': '3rd 2023',
    'Fourth Edition': '4th 2024',
    'Fifth Edition': '5th 2025'
}

html_files = glob.glob(os.path.join(directory, '*.html'))
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        file_content = f.read()
    
    modified = file_content
    for old, new in replacements.items():
        modified = modified.replace(old, new)
    
    if modified != file_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(modified)

print("Update completed successfully.")
