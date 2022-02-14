__author__ = 'khaledsaleh'

from django.template.loader import get_template
from django.http import HttpResponse


def freQ(request):
    l = "Netflix use information about the things people buy or rent to determine which people or items are similar to one another, and then make recommendations based on purchase history. Other sites like Pandora and Last.fm use your ratings of different bands and songs to create custom radio stations"

    d = {}
    for item in l.split():
        if item in d:
            d[item] = d.get(item)+1
        else:
            d[item] = 1

    post = ""
    t = get_template('index.html')
    for k, v in d.items():
        post += "<p> %s : %s </p>" % (k , v)
    html = t.render({'item_list': d.items(), 'index': 'Histogram'})
    # html = t.render({'d':d.items(), 'k':k, 'v':v })
    return HttpResponse(html)

