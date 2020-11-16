import requests
from bs4 import BeautifulSoup
import pprint
res=requests.get('https://news.ycombinator.com/news')
res2=requests.get('https://news.ycombinator.com/news?p=2')
#print(res.text)
s=BeautifulSoup(res.text,'html.parser')
s2=BeautifulSoup(res2.text,'html.parser')
#print(s.body.contents)
#print(s.find_all('a'))
#print(s.a)
#print(s.body.contents)
#print(s.find(id='score_45'))
#print(s.select('a'))
#print(s.select('.score'))
l=s.select('.storylink')
subtext=s.select('.subtext')
l2=s2.select('.storylink')
subtext2=s2.select('.subtext')
ml=l+l2
ms=subtext+subtext2

#print(s.v)
def sort_stories_by_votes(hnlist):
    return sorted(hnlist,key=lambda k:k['v'], reverse = True)


def create_custom_hn(l,subtext):
    hn=[]
    for idx, item in enumerate(l):

        #title=l[idx].getText()
        title = item.getText()
        #href=l[idx].get('href',None)
        href = item.get('href', None)
        v=subtext[idx].select('.score')
        if len(v):
            points = int(v[0].getText().replace('points',''))
            if points > 99:
            #print(points)
                hn.append({'title':title,'l':href, 'v':points})
    #return hn
    return sort_stories_by_votes(hn)
pprint.pprint(create_custom_hn(ml,ms))