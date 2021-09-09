import http.client
import json
import time


conn = http.client.HTTPSConnection("rmstool.com")
payload = ''
headers = {}

urlsList = [
'/api/DataFiles/Cape-Town-Uber-Demand.html',
'/api/DataFiles/Cape-Town-Taxify-Demand.html',
'/api/DataFiles/Delhi-Uber-Demand.html',
'/api/DataFiles/Delhi-Ola-Demand.html',
'/api/DataFiles/Dubai-Uber-Demand.html',
'/api/DataFiles/Dubai-Careem-Demand.html',
'/api/DataFiles/Melbourne-Uber-Demand.html',
'/api/DataFiles/Melbourne-Shebah-Demand.html',
'/api/DataFiles/Mexico-City-Uber-Demand.html',
'/api/DataFiles/Paris-Uber-Demand.html',
'/api/DataFiles/Paris-Heetch-Demand.html',
'/api/DataFiles/Paris-Taxify-Demand.html',
'/api/DataFiles/NYC-Uber-Demand.html',
'/api/DataFiles/NYC-Lyft-Demand.html',
'/api/DataFiles/Toronto-Uber-Demand.html',
'/api/DataFiles/Toronto-Lyft-Demand.html',
'/api/DataFiles/London-Uber-Demand.html'
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

        fx = open('dataDumpDemand.txt','a')
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
