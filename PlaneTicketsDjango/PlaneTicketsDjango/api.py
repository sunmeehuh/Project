#!/use/bin/env python
import json
import urllib2
import json as simplejson
from django.db.models.sql.query import Query

kimono_api = '1BxYchJ2YyKD3AMTtvPxP1wATi9ie73A'

url = 'https://www.kimonolabs.com/api/a27tvk9m?apikey=1BxYchJ2YyKD3AMTtvPxP1wATi9ie73A'
json_obj = urllib2.urlopen(url)
data = json.load(json_obj)

for item in data['results']:
    print "item is :" + str(item)
    sublevel = data['results']
    for subitem in sublevel['collection1']:
        print "subitem is :" + str(subitem)
        

'''if __name__ == "__main__":
    req = urllib2.Request(url)
    opener = urllib2.build_opener()
    f = opener.open(req)
    json = simplejson.load(f) #converting strings into python based data
    
    for item in json:
        print item.get('results')'''




#dictionary
#can print ['{contains dictionary}', 'isalist']

'''for later, searching:
def search(query):
    api_key = locu_api
    url = 'httpsL//www.ajkdsfosidfisodjfblah until ? then add api_key=' + api_key
    locality(or other name) = query.replace(' ', '%20') or whatever they did in their url
    final_url = url + "&locality=" + locality + "&category=restaurant"
    json_obj = urllib2.urlopen(final_url)
    data = json.load(json_obj)
    for item in data['objects']:
        print item['name'], item['phone']'''
        
