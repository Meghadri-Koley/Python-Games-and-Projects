import requests
from bs4 import BeautifulSoup
from googlesearch import search as srch


def news():

    url='https://www.bbc.com/news'
    response=requests.get(url)

    soup=BeautifulSoup(response.text, 'html.parser')
    headlines=soup.find('body').find_all('h3')
    dlt=["BBC World News TV", "BBC World Service Radio", "News daily newsletter", "Mobile app", "Get in touch"]
    news=[]
    News=[]
    for x in headlines:
        News.append(x.text.strip())

    for i in range(len(News)):
        if(News[i] not in dlt):
            if(News[i] not in news):
                news.append(News[i])

    news=news[0:20]

    newss=[]
    print("\033[4mTODAY'S TOP 20 HEADLINES\033[0m")
    print()

    
    c = 1
    for i in range(len(news)):
        if(news[i] not in dlt):
            print(str(c)+". "+news[i])
            c = c+1
            print()

news()