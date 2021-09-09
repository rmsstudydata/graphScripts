
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(1, 'RawData')
import numpy as np
import matplotlib.pyplot as plt

import pricePerTrip

import cityNames
import math
import random
import ast 
from pylab import *
import surgeCDFDistance2

import surgeUpdateCDFFreq
import hotsurgeCDFFreq
import surgeTimeCDFData
import cityNames
import etaFrequencyDict

experimentCities = cityNames.CityFullName

cities = list(cityNames.CityShortName.keys())
cityInd = 0
# Fixing random state for reproducibility
np.random.seed(19680801)
distDict = surgeCDFDistance2.SurgeData


serviceColors = {}
serviceColors['Uber'] = 'royalblue'
serviceColors['Lyft'] = 'deeppink'
serviceColors['Taxify'] = 'darkslategrey'
serviceColors['Ola'] = 'darkkhaki'
serviceColors['Careem'] = 'mediumturquoise'
serviceColors['Gett'] = 'orange'
serviceColors['Shebah'] = 'saddlebrown'
serviceColors['GoCatch'] = 'maroon'
serviceColors['Cabify'] = 'blue'
serviceColors['Juno'] = 'thistle'
serviceColors['Via'] = 'olive'
serviceColors['Heetch'] = 'indigo'

cityServiceEconomyCategory= {}
cityServiceEconomyCategory['CapeTown-SA'] = {}
cityServiceEconomyCategory['CapeTown-SA']['Uber'] = 'UberX'
cityServiceEconomyCategory['CapeTown-SA']['Taxify'] = 'Bolt'

cityServiceEconomyCategory['Delhi-India'] = {}
cityServiceEconomyCategory['Delhi-India']['Uber'] = 'UberGoEco'
cityServiceEconomyCategory['Delhi-India']['Ola'] = 'prime_play'


cityServiceEconomyCategory['Dubai-UAE'] = {}
cityServiceEconomyCategory['Dubai-UAE']['Uber'] = 'Black'
cityServiceEconomyCategory['Dubai-UAE']['Careem'] = 'Economy'
cityServiceEconomyCategory['London-UK'] = {}
cityServiceEconomyCategory['London-UK']['Uber']= 'UberX'
cityServiceEconomyCategory['London-UK']['Gett'] = 'car'


cityServiceEconomyCategory['Melbourne-AU'] = {}
cityServiceEconomyCategory['Melbourne-AU']['Uber'] = 'UberX'
cityServiceEconomyCategory['Melbourne-AU']['Taxify'] = 'Bolt'
cityServiceEconomyCategory['Melbourne-AU']['Shebah'] = 'car'
cityServiceEconomyCategory['Melbourne-AU']['Gocatch'] = 'car'


cityServiceEconomyCategory['MexicoCity-Mexico'] = {}
cityServiceEconomyCategory['MexicoCity-Mexico']['Uber'] = 'UberX'
cityServiceEconomyCategory['MexicoCity-Mexico']['Taxify'] = 'Bolt'
cityServiceEconomyCategory['MexicoCity-Mexico']['Cabify'] = 'Lite'

cityServiceEconomyCategory['NY-US'] = {}
cityServiceEconomyCategory['NY-US']['Uber'] = 'UberX'
cityServiceEconomyCategory['NY-US']['Lyft'] = 'Lyft'
cityServiceEconomyCategory['NY-US']['Juno'] = 'nyc.l1'
cityServiceEconomyCategory['NY-US']['Via'] = 'car'

cityServiceEconomyCategory['Paris-France'] = {}
cityServiceEconomyCategory['Paris-France']['Uber'] = 'UberX'
cityServiceEconomyCategory['Paris-France']['Heetch'] = "fr-paris-pro"
cityServiceEconomyCategory['Paris-France']['Taxify'] = 'Bolt'


cityServiceEconomyCategory['Toronto-Canada'] = {}
cityServiceEconomyCategory['Toronto-Canada']['Uber'] = 'UberX'
cityServiceEconomyCategory['Toronto-Canada']['Lyft'] = 'Lyft'
tavg = []
f,subPlots= plt.subplots(1,2, figsize = (6,2.8),sharex = True)

legend_elements = []
printedServices = []
myData = {}
import json
import json
fx1 = open('sr1.txt','r')
D1 = json.loads(fx1.read())
fx1.close()
import json
fx1 = open('sr2.txt','r')
D2 = json.loads(fx1.read())
fx1.close()

DIST1 = []
DIST2 = []

cities= ['Delhi-India', 'Paris-France']
surgeArea = {}
for ax in subPlots:
	#for ax in row:
		city = cities[cityInd]
		surgeArea[city] = []
		myData[city] = {}
		for service in distDict[cities[cityInd]]:
			myData[city][service] = []
			
			xset = D1[city][service][0]

			
			y = D1[city][service][1]

			for k in range(0,len(y)):
				if y[k] < 101:
					l1 = [xset[k]]*int(y[k])
					DIST1 += l1	
				
			printedServices.append(service)
			#print(service,city,np.average(lesst),max(lesst) )#lesst/len(x))
			#tavg.append(np.average(lesst))
			surgeArea[city] = surgeArea[city]  +xset

			ax.plot(xset,y,color = serviceColors[service])

			try:
				if 'Lyft' not in service:
					xset = D2[city][service][0]
					y = D2[city][service][1]
					for k in range(0,len(y)):
						if y[k] < 101:
							l1 = [xset[k]]*int(y[k])
							DIST2 += l1	
					surgeArea[city] = surgeArea[city]  +xset
					ax.plot(xset,y,color = serviceColors[service],ls='--')
			except:
				ijk = 10

		
		ax.set_yticks([0,10,20,30,40,50,60,70,80,90,100])
		ax.set_yticklabels(['','10','','','','50','','','','','100'])
		ax.set_title(experimentCities[cities[cityInd]],fontweight='bold')

		ax.set_xticks([0,1,2,3])
		ax.set_xticklabels(['0','1','2','3'])

		ax.set_xlim(0,3)
		cityInd+=1
#subPlots[1].set_xlabel('Distance in Miles',  fontweight = 'bold')

subPlots[0].set_ylabel('Percentage Reduction in \nSurge Multiplier Intesity',  fontweight = 'bold')
subPlots[0].yaxis.set_label_coords(-0.2, 0.42)
print(np.average(tavg))

for key in serviceColors:
	if key in printedServices:
		newLine =Line2D([0], [0], color=serviceColors[key], label=key,lw=2)
		legend_elements.append(newLine)

axList = subPlots
axList[1].set_xlabel('Distance in Miles',fontweight='bold')
axList[1].xaxis.set_label_coords(0.5, -0.14)

axList[0].set_xlabel('Distance in Miles',fontweight='bold')
axList[0].xaxis.set_label_coords(0.5, -0.14)


textstr = '━━━━ Pre-covid \n------ Covid'
props = dict(boxstyle='square', facecolor='white', alpha=0.5)

axList[0].text(0.36,  0.18, textstr, transform=axList[0].transAxes, fontsize=9,
verticalalignment='top', bbox=props)



axList[1].text(0.36,  0.18, textstr, transform=axList[1].transAxes, fontsize=9,
verticalalignment='top', bbox=props)

ax.legend(handles=legend_elements,loc='lower center', bbox_to_anchor=(-0.08, -0.4),
          fancybox=True, shadow=False, ncol=7, fontsize=10)

plt.subplots_adjust(left=0.15, right = 0.97,bottom =0.25,wspace=0.14,top=0.91, hspace = 0.37)


for city in surgeArea:
	print(city, np.average(surgeArea[city]))
print(np.average(DIST1),np.average(DIST2))
plt.savefig('LatestFigures/surgeDistance.eps')
plt.show()

