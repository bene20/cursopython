import requests
from bs4 import BeautifulSoup

url = 'http://localhost:3333/'

response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')
print(parsed_html.title)
print(parsed_html.title.text)

seletor_top3_jobs = parsed_html.select_one('#top-3 > div > div > header > h2')
print(seletor_top3_jobs)
print(seletor_top3_jobs.text)
