# name: David Huang
# description: webScrape python jobs on monster for multiple pages. Basically tutorial but repeating it on my own

import requests
from bs4 import BeautifulSoup


################
# given the div that contains the job, print out the job in the format below
# job title
# company
# url for applying
def print_info(job_elem, title_keyword='', company_keyword=''):
    title_elem = job_elem.find('h2', class_='title', string=lambda title: title_keyword.lower() in title.lower())
    company_elem = job_elem.find('div', class_='company')
    if None in (title_elem, company_elem):
        return
    if not (company_keyword.lower() in company_elem.text.lower()):
        return
    link = title_elem.find('a')['href']
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(f'Apply: {link}')
    print()


end_page = 10
URL = f"https://www.monster.com/jobs/search/?q=Software-Developer&where=New-York&stpage=1&page={end_page}"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(class_='mux-search-results')
job_elems = results.find_all(class_='flex-row')
for job_elem in job_elems:
    print_info(job_elem, 'python')
