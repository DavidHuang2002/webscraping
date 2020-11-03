# following real python tutorial on https://realpython.com/beautiful-soup-web-scraper-python/

import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=New-York'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')
# -----
# job_elems = results.find_all('section', class_='card-content')
# for job_elem in job_elems:
#     title_elem = job_elem.find('h2', class_='title')
#     company_elem = job_elem.find('div', class_='company')
#     location_elem = job_elem.find('div', class_='location')
#     if None in (title_elem, company_elem, location_elem):
#         continue
#     print(title_elem.text.strip())
#     print(company_elem.text.strip())
#     print(location_elem.text.strip())
#     print()
# ------

#passing function as argument to string



java_jobs = results.find_all('h2', class_= 'title', string=lambda title: "java" in title.lower())
job_num = len(java_jobs)
if job_num == 0:
    print("no job found")
else:
    print(f"find {job_num} that matches description")
    for java_job in java_jobs:
        link = java_job.find('a')['href']
        print(java_job.text.strip())
        print(f"Apply here: {link}\n")
