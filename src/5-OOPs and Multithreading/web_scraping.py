'''
Web Scrapping 

Using Multi-Threading to scrap the data from the website.

Webpage1 - https://python.langchain.com/docs/introduction/

Webpage2 - https://python.langchain.com/docs/concepts/

Webpage3 - https://python.langchain.com/docs/tutorials/
'''

import threading
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


threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()

