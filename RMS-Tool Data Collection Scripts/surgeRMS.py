import http.client
import json
import time


conn = http.client.HTTPSConnection("rmstool.com")
payload = ''
headers = {}

urlsList = [
'/api/DataFiles/Cape-Town-Uber-Surge.html',
'/api/DataFiles/Cape-Town-Taxify-Surge.html',
'/api/DataFiles/Delhi-Uber-Surge.html',
'/api/DataFiles/Delhi-Ola-Surge.html',
'/api/DataFiles/Dubai-Uber-Surge.html',
'/api/DataFiles/Dubai-Careem-Surge.html',
'/api/DataFiles/Melbourne-Uber-Surge.html',
'/api/DataFiles/Melbourne-Shebah-Surge.html',
'/api/DataFiles/Mexico-City-Uber-Surge.html',
'/api/DataFiles/Paris-Uber-Surge.html',
'/api/DataFiles/Paris-Heetch-Surge.html',
'/api/DataFiles/Paris-Taxify-Surge.html',
'/api/DataFiles/NYC-Uber-Surge.html',
'/api/DataFiles/NYC-Lyft-Surge.html',
'/api/DataFiles/Toronto-Uber-Surge.html',
'/api/DataFiles/Toronto-Lyft-Surge.html',
'/api/DataFiles/London-Uber-Surge.html'
]

dataDict = {}

doneLinks = 0
for link in urlsList:

    metaData = link.split('DataFiles/')[1]
    metaData  = metaData.split('.html')[0]
    metaData = metaData.split('-')
    serviceName = metaData[-2]

    cityName = metaData[0]
    if len(metaData) >3:
        cityName += metaData[1]

    dataDict = {}
    conn.request('GET',link, payload, headers)
    res = conn.getresponse()
    if res.status == 200:
        data = res.read()
        data = data.decode("utf-8");
        data = data.split('var obj = ')[1]
        data = data.split('\n')[0][:-1]

        data = json.loads(data)

        fx = open('dataDumpSurge.txt','a')
        fx.write('---------------------\n')
        fx.write(str(int(time.time()))+'\n')
        fx.write(serviceName+' - '+ cityName+'\n')
        fx.write(''+json.dumps(data))
        fx.write('\n')
        fx.close()
        print(res.status, serviceName, cityName, link)

    time.sleep(1)
    # time.sleep(600)

    doneLinks += 1
    if doneLinks == len(urlsList):
        print('Sleeping')
        time.sleep(920)
