import requests
import time
import threading

from bs4 import BeautifulSoup

urls = [
'https://python.langchain.com/v0.2/docs/introduction/',
'https://python.langchain.com/v0.2/docs/concpets/',
'https://python.langchain.com/v0.2/docs/tutorials/'
]


def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'Fetched {len(soup.text)} characters form {url}')


threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for i in threads:
    i.join()

print('All webpages are fetched')