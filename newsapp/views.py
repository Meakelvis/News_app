from django.shortcuts import render
from newsapi import NewsApiClient


def index(request):
    newsapi = NewsApiClient(api_key='adcacc66dcdb4adfa6fdae418e8e65e4')
    top = newsapi.get_top_headlines(sources='bbc-news,the-verge')

    l = top['articles']
    desc = []
    news = []
    img = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])

    mylist = zip(news, desc, img)

    return render(request, 'newsapp/index.html', context={'mylist': mylist})
