'''
Web Scrapping 

Using Multi-Threading to scrap the data from the website.

This is using Thread Pool Executor

Webpage1 - https://python.langchain.com/docs/introduction/

Webpage2 - https://python.langchain.com/docs/concepts/

Webpage3 - https://python.langchain.com/docs/tutorials/
'''

from concurrent.futures import ThreadPoolExecutor
import requests
from bs4 import BeautifulSoup ## Library to use webscraping html content    

urls = [
    'https://python.langchain.com/docs/introduction/',
    'https://python.langchain.com/docs/concepts/',
    'https://python.langchain.com/docs/tutorials/'
]

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f"Number of character in {url} is {len(soup.text)}")
    # print(soup.text)

with ThreadPoolExecutor(max_workers=3) as executor: 
    results= executor.map(fetch_content, urls)
    

