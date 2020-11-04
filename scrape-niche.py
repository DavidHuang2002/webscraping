# name: David Huang
# description: webScrape colleges on Niche best colleges rank
# and rank them based on Median Earnings 6 Years After Graduation

# problem: still print sponsored college

from requests_html import HTMLSession
from bs4 import BeautifulSoup
from time import sleep

#################
# look for the median earning element in content of college page


def find_earning_elem(new_soup):
    buckets_elems = new_soup.find_all('div', class_='profile__buckets')
    for buckets_elem in buckets_elems:
        earning_elem = buckets_elem.find('div', class_='profile__bucket--1')
        if earning_elem is None:
            continue

        earning_label = earning_elem.find('div', class_='scalar__label')
        if earning_label is None:
            continue

        if earning_label.text.strip() == 'Median Earnings 6 Years After Graduation':
            earning_num = earning_elem.find('div', class_='scalar__value').find('span').text.strip()
            return earning_num


####################################
# Given the link to the page of college,
# this function finds and returns the 6 years median earnings


def fetch_median_earnings(link):
    sleep(2)
    new_session = HTMLSession()
    new_page = session.get(link)
    new_soup = BeautifulSoup(new_page.content, 'html.parser')
    # buckets_elem = new_soup.find_all('div', class_='profile__buckets')[16]
    # earning_elem = buckets_elem.find('div', class_='profile__bucket--1')
    # earning_num = earning_elem.find('div', class_='scalar__value').find('span').text.strip()
    # return earning_num
    return find_earning_elem(new_soup)


session = HTMLSession()
page_num = 1
URL = f"https://www.niche.com/colleges/search/best-colleges/?page={page_num}"
page = session.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find('div', class_='search-results')
if results is None:
    print(soup.prettify())
    raise Exception

college_elems = results.find_all('li', 'search-results__list__item')
for college_elem in college_elems:
    name_elem = college_elem.find('h2', class_='search-result__title')

    tagline_elems = college_elem.find_all('li', class_='search-result-tagline__item')
    location_elem = tagline_elems[1]

    fact_value_elems = college_elem.find_all('span', class_='search-result-fact__value')

    link = college_elem.find('a', class_='search-result__link')['href']
    earning = fetch_median_earnings(link)

    print(name_elem.text.strip())
    print(location_elem.text.strip())
    print(fact_value_elems[0].text.strip())  # fact_value_elems[0] is acceptance rate
    print(fact_value_elems[1].text.strip())  # fact_value_elems[1] is net cost
    print(link)
    print(f'Median Earnings 6 Years After Graduation: {earning} per year')
    print()

