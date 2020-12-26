import random

import pyshorteners
import requests
from bs4 import BeautifulSoup as bs

shorter = pyshorteners.Shortener()


def get_scholarship_updates(link_to_get):
    scholarship_titles = []
    shortened_scholarship_links = []
    pager = requests.get(link_to_get)
    soup = bs(pager.text, 'html.parser')
    scholarship_class = soup.findAll("h3", {"class": "entry-title td-module-title"})
    for every in scholarship_class:
        if (every.find("a")["href"])[0:40] == "https://www.intelregion.com/scholarships":
            scholarship_titles.append(f'{every.find("a").getText()}')
            shortening_link = shorter.tinyurl.short(f'{every.find("a")["href"]}')
            shortened_scholarship_links.append(shortening_link)
    scholarship_dict = {"titles": scholarship_titles, "links": shortened_scholarship_links}
    return scholarship_dict

#append shortened links
def get_job_updates(link_to_get):
    job_titles = []
    shortened_job_links = []
    pager = requests.get(link_to_get)
    soup = bs(pager.text, 'html.parser')
    job_class = soup.findAll("h3", {"class": "entry-title td-module-title"})
    for every in job_class:
        if (every.find("a")["href"])[0:39] == "https://www.intelregion.com/job-summary":
            job_titles.append(f'{every.find("a").getText()}')
            shortening_link = shorter.tinyurl.short(f'{every.find("a")["href"]}')
            shortened_job_links.append(shortening_link)
    job_dict = {"titles": job_titles, "links": shortened_job_links}
    return job_dict


def prepare_updates_data(function_parameter, send_number):
    text = []
    random_choosing = random.sample(range(0, len(function_parameter['titles'])), send_number)
    for i in random_choosing:
        entry = f"Title 🌟:\n{function_parameter['titles'][i]}\n\nlink 🔗↙\n{function_parameter['links'][i]}"
        text.append(entry)
    return text
