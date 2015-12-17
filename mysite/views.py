__author__ = 'khaledsaleh'

from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

l = "Netflix use information about the things people buy or rent to determine which people or items are similar to one another, and then make recommendations based on purchase history. Other sites like Pandora and Last.fm use your ratings of different bands and songs to create custom radio stations"

def freQ(l):

    d = {}
    for item in l.split():
        if item in d:
            d[item] = d.get(item)+1
        else:
            d[item] = 1

    for k,v in d.items():
        print(str(k)+':'+str(v))


    t = get_template('index.html')
    html = t.render(Context({ freQ(l) }))
    return HttpResponse(html)

