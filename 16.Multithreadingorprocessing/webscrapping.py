import threading
import requests
from bs4 import BeautifulSoup

urls=[
    'https://www.langchain.com/resources',
    'https://langchain-ai.github.io/langgraph/concepts/why-langgraph/',
    'https://python.langchain.com/docs/introduction/'
]

def fetch_contents(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f"fetched-{len(soup.text)}")


threads=[]
for url in urls:
    thread=threading.Thread(target=fetch_contents,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("all web pages fetched")