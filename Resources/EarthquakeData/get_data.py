import requests
import sys


def get_earth_quake_data(month,year,minmag=None,maxmag=None,query=True):
    next_month = month+1

    if not maxmag is None:
        maxmag = '&maxmagnitude='+str(maxmag)
    else:
        maxmag = ''

    if not minmag is None:
        minmag = '&minmagnitude='+str(minmag)
    else:
        minmag = '&minmagnitude='+str(1.0)

    if query:
        type = 'query'

    else:
        type = 'count'

    url = 'https://earthquake.usgs.gov/fdsnws/event/1/'+type+'?format=geojson&starttime='+str(year)+'-'+str(month)+'-01&endtime='+str(year)+'-'+str(next_month)+'-01'+minmag+maxmag

    r = requests.get(url).json()

    if type == 'count':
        return r['count']
    else:
        return r


years = [x for x in range(1960,2017)]
months = [x for x in range(0,12)]

for y in years:
    print("Year:%s" % (y))
    for m in months:
        print("Month:%s" % (m))
        r = get_earth_quake_data(m,y,6,None,False)
        print(r)

