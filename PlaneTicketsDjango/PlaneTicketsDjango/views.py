from django.http import HttpResponse #django.http is a module
from django.shortcuts import render_to_response
import json
import urllib2
import json as simplejson
from django.views.generic import TemplateView
from django.template import RequestContext, loader
from pip._vendor import requests

import datetime
from .models import FlightListingCollection, FlightListingCollection2
# from django.db.models.sql.query import Query
  
def index(request):
#     for product in products:
#         cost = product.values[1]['text']
#         print cost
    return render_to_response('index.html') 

def displayInfo(request):  
    kimono_api = '1BxYchJ2YyKD3AMTtvPxP1wATi9ie73A'
    url = 'https://www.kimonolabs.com/api/a27tvk9m?apikey=' + kimono_api
    json_obj = urllib2.urlopen(url)
    data = json.load(json_obj)
    products = {"products": data['results']['collection1']}
    
    json_data_str = json.dumps(products['products'])
    
    data_exists = FlightListingCollection.objects.exists()
    if data_exists:
        newest_data = FlightListingCollection.objects.all().order_by('-updated_time')[0]
        most_recent_update = newest_data.updated_time.replace(tzinfo=None)
        
    if not data_exists or datetime.datetime.now() - most_recent_update >= datetime.timedelta(1):
        print 'updating data'
        new_obj = FlightListingCollection(data=json_data_str)
        new_obj.save()
    else:
        print 'using old data'
        products = {'products': json.loads(newest_data.data)}        
    
    return render_to_response('index2.html', products) 

def details(requests, indexnum):
    kimono_api = '1BxYchJ2YyKD3AMTtvPxP1wATi9ie73A'
    url = 'https://www.kimonolabs.com/api/671w53tw?apikey=' + kimono_api
    json_obj = urllib2.urlopen(url)
    details_data = json.load(json_obj)
    detailsList1 = {"detailsList1": details_data['results']['Flight Details']}    
    json_data_str = json.dumps(detailsList1['detailsList1']) 
    #NOW HAVE DETAILS AS A LONG STRING....

    #my own stuff....
    data_exists = FlightListingCollection2.objects.exists()
    if data_exists:
        newest_data = FlightListingCollection2.objects.all().order_by('-updated_time')[0]
        most_recent_update = newest_data.updated_time.replace(tzinfo=None)
        
    if not data_exists or datetime.datetime.now() - most_recent_update >= datetime.timedelta(1):
        print 'updating data'
        new_obj = FlightListingCollection2(details_data=json_data_str)
        new_obj.save()
    else:
        print 'using old data'
        detailsList1 = {'detailsList1': json.loads(newest_data.details_data)}        
    #STOP

    newest_data = FlightListingCollection2.objects.all().order_by('-updated_time')[0]
    data = json.loads(newest_data.details_data)[int(indexnum)]
    detailsList = {"detailsList": data}
    #variables
    book_at = "Book At:"
    return render_to_response('details_display.html', detailsList) 

#     DONT TOUCH
#     newest_data = FlightListingCollection.objects.all().order_by('-updated_time')[0]
#     data = json.loads(newest_data.data)[int(indexnum)]
#     detailsList = {"detailsList": data}
#     return render_to_response('details_display.html', detailsList) 
