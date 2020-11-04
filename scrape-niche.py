# name: David Huang
# description: webScrape colleges on Niche best colleges rank
# and rank them based on Median Earnings 6 Years After Graduation

# problem: still print sponsored college

from requests_html import HTMLSession
from bs4 import BeautifulSoup
from time import sleep

####################################
# Given the link to the page of college,
# this function finds and returns the 6 years median earnings


def fetch_median_earnings(link):
    sleep(0.5)
    new_session = HTMLSession()
    new_page = session.get(link)
    new_soup = BeautifulSoup(new_page.content, 'html.parser')
    buckets_elem = new_soup.find_all('div', class_='profile__buckets')[13]
    earning_elem = buckets_elem.find('div', class_='profile__bucket--1')
    print(earning_elem.text.strip())


session = HTMLSession()

page_num = 2
URL = f"https://www.niche.com/colleges/search/best-colleges/?page={page_num}"
page = session.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

results = soup.find('div', class_='search-results')
# college_elems = results.find_all('li', 'search-results__list__item')
# for college_elem in college_elems:
#     name_elem = college_elem.find('h2', class_='search-result__title')
#
#     tagline_elems = college_elem.find_all('li', class_='search-result-tagline__item')
#     location_elem = tagline_elems[1]
#
#     fact_value_elems = college_elem.find_all('span', class_='search-result-fact__value')
#
#     link = college_elem.find('a', class_='search-result__link')['href']
#
#     print(name_elem.text.strip())
#     print(location_elem.text.strip())
#     print(fact_value_elems[0].text.strip())  # fact_value_elems[0] is acceptance rate
#     print(fact_value_elems[1].text.strip())  # fact_value_elems[1] is net cost
#     print(link)
#     fetch_median_earnings(link)
#     print()
#     break
