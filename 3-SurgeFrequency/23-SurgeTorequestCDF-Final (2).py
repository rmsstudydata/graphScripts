import numpy as np
import ast 
from pylab import *

sys.path.insert(1, 'RawData')

import surgeCDFFreq
import hotsurgeCDFFreq
import surgeTimeCDFData
import cityNames
import etaFrequencyDict

import collections

frequencyDict = surgeCDFFreq.SurgeData
hotetaupdateFrequency15 = hotsurgeCDFFreq.SurgeData
from cityNames import CityShortName as cityShortForm

etaupdateFrequency15 =surgeCDFFreq.SurgeData
# Create some test data
axList = []
fig, (axList)= plt.subplots(1, 2, sharey = True, figsize=(4.3,2.7))
#axList = [ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9,ax10]


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


cityStartCDF= {}

cityStartCDF['CapeTown-SA'] = 0.98

cityStartCDF['Delhi-India'] = 0.94

cityStartCDF['Dubai-UAE'] = 0.95

cityStartCDF['London-UK']= 0.91


cityStartCDF['Melbourne-AU'] = 0.97

cityStartCDF['MexicoCity-Mexico'] = 0.94
cityStartCDF['NY-US'] = 0.96

cityStartCDF['Paris-France'] =0.9


cityStartCDF['Toronto-Canada'] = 0.975
cityMaxDict = {}

newDict = {}

mu = 200
sigma = 25
n_bins = 300
x = np.random.normal(mu, sigma, size=100)

cities = list(cityNames.CityShortName.keys())
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
cityServiceEconomyCategory['Paris-France']['Heetch'] = 'car'
cityServiceEconomyCategory['Paris-France']['Taxify'] = 'Bolt'


cityServiceEconomyCategory['Toronto-Canada'] = {}
cityServiceEconomyCategory['Toronto-Canada']['Uber'] = 'UberX'
cityServiceEconomyCategory['Toronto-Canada']['Lyft'] = 'Lyft'


#cityServiceEconomyCategory = cityNames.cityServiceEconomyCategory
#add max of all services in each city

cityIndex = 0
sgavrgList=  []


#graph

totalnums = 0
surgeNums = 0
printedServices = []
cityIndex = 0
surgeList = []
surgeCity = []
subp = 0

maxCityService = {}
mcitysurges = []

myData = {}
import json
fx1 = open('ns1.txt','r')
D1 = json.loads(fx1.read())
fx1.close()

fx1 = open('ns22.txt','r')
D2 = json.loads(fx1.read())
fx1.close()

for ax in axList:
		subp+=1
	#for ax in row:
		currentCity = ''
		maxCity = 0
		cities = ['Delhi-India','Paris-France']
		if cityIndex < 9:

			currentCity = cities[cityIndex]
			maxCityService[currentCity] = {}
			myData[currentCity] = {}
			ax.set_title(cityShortForm[currentCity],fontweight='bold',fontsize=10)
			cm = 0

			for service in etaupdateFrequency15[currentCity].keys():

				try:
					
					content = D1[currentCity][service]
					content2 = D2[currentCity][service] 
					
					myData[currentCity][service] = content
					printedServices.append(service)

					print(currentCity,service)
					data_sorted = np.sort(content)

					data_sorted2 = np.sort(content2)
					content.append(2.6)
					
					p = 1. * np.arange(len(content)) / (len(content) - 1)
					data_sorted = np.sort(content)
					if len(content2) > 1:
						p2 = 1. * np.arange(len(content2)) / (len(content2) - 1)
						data_sorted2 = np.sort(content2)

					
					ax.plot(data_sorted, p,lw=1.7, color = serviceColors[service])
					if len(content2) > 1:
						ax.plot(data_sorted2, p2,lw=1.7, color = serviceColors[service],ls='--')
					
					if service =='Careem':
						d2 = collections.Counter(mcitysurges)
						a= d2[1.1]
						b = len(mcitysurges)
						print(currentCity,service,a/b)


				except Exception as e:
					ijk = 10
				
		cityIndex+= 1
				
		print(maxCity)
		cityMaxDict[currentCity] = maxCity
		ax.set_xlim(1, maxCity)
		#ax.set_ylim(cityStartCDF[currentCity], 1.0005)
		ax.set_ylim(0.9, 1.0)
		#ticksNew = np.arange(cityStartCDF[currentCity],1.001,step=(1-cityStartCDF[currentCity])/2)
		ticksNew = np.arange(0.9,1.001,step=0.03)
		ax.set_yticks([0.8,0.85,0.9,0.95,1])
		ylabelsNew = []
		for item in ticksNew:
			'''
			if int(item)<1  and item==ticksNew[len(ticksNew)-1]:
				item = '100'
			else:
				item = str(int(item*100))
			'''
			if  item!=ticksNew[len(ticksNew)-1]:
				
				item = str(int(item*100))
				ylabelsNew.append(item)
		ylabelsNew.append('100')
		#if cityIndex == 0:
		ax.set_yticklabels(['80', '85','90','95','100'] )
	#	else:
	#		ax.set_yticks([])

		ticksNew = np.arange(1,3,step=0.4)
		#ticksNew = np.arange(1,maxCity+0.000001,step=(maxCity-1)/3)
		for i in range(0,len(ticksNew)):
			if ticksNew[i]< 1.1:
					ticksNew[i] = 1
			ticksNew[i] = round(float(ticksNew[i]),1)
		ax.set_xticks(ticksNew)
		ax.set_xticklabels(['1','','1.8','','2.6'], fontsize=9)
		ax.set_xlim(0.999,2.6)
		ax.set_ylim(0.8,1.001)
		'''
		ylabelsNew = []
		for item in ticksNew:
			item = str(int(item*100))
			if item == '99':
				item = '100'
			ylabelsNew.append(item)
		ax.set_yticklabels(ylabelsNew)
		#ax.axhline(y=0.9,ls = '--')
		'''

#fig.delaxes(axList[1,4])

#print('\n\n', sgavrgList,np.average(surgeList), max(sgavrgList),surgeCity[sgavrgList.index(max(sgavrgList))])

#print(surgeNums/totalnums,np.average(c2),np.std(c2))
plt.subplots_adjust(left=0.13, right = 0.96 ,bottom =0.3,wspace=0.25,top=0.9, hspace = 0.97)
axList[0].set_ylabel('CDF',fontweight='bold')
#ax.xaxis.set_label_coords(-, -0.14)

#axList[0].set_yticks([0,0.2,0.4,0.8,1],['1','1','1','1','1'])

'''
for item in axList:
	item.set_yticks([0.9,0.925,0.95,0.975,1])
	item.set_yticklabels(['90','93','95','97','100'])
'''


axList[1].set_xlabel('Surge Multipliers',fontweight='bold')
axList[1].xaxis.set_label_coords(0.5, -0.14)

axList[0].set_xlabel('Surge Multipliers',fontweight='bold')
axList[0].xaxis.set_label_coords(0.5, -0.14)


textstr = '━━━━ Pre-covid \n------ Covid'
props = dict(boxstyle='square', facecolor='white', alpha=0.5)

axList[0].text(0.36,  0.2, textstr, transform=axList[0].transAxes, fontsize=9,
verticalalignment='top', bbox=props)



axList[1].text(0.36,  0.2, textstr, transform=axList[1].transAxes, fontsize=9,
verticalalignment='top', bbox=props)



legend_elements = []

cityInd = 0
'''
for ax in axList:
	maxVal = cityMaxDict[cities[cityInd]]
	#print('\n\n',maxVal)
	prevVal = 0
	newXticks = []
	xi = 0
	while xi <= 1:
		#val1 = int(maxVal*(1/xi))
		#print(val1)
		newXticks.append(int(maxVal*xi))
		xi += 0.33
	ax.set_xticks(newXticks)
	ax.set_xticklabels(newXticks, fontsize=7)
	cityInd += 1
'''
for key in serviceColors:
	if key in printedServices:
		newLine =Line2D([0], [0], color=serviceColors[key], label=key,lw=2)
		legend_elements.append(newLine)

mcitysurges = sorted(mcitysurges)

x1 = int(len(mcitysurges)*0.9)
x2 = int(len(mcitysurges)*1) 
#print(mcitysurges[int(len(mcitysurges)*0.8)])
#print(maxCityService)
textstr = '━━━━ Pre-covid \n ┄┄┄┄ Covid'
props = dict(boxstyle='square', facecolor='white', alpha=0.5)

ax.text(-11, -0.3, textstr, transform=ax.transAxes, fontsize=9,
	verticalalignment='top', bbox=props)

ax.legend(handles=legend_elements,loc='lower center', bbox_to_anchor=(-0.2, -0.5),
          fancybox=True, shadow=False, ncol=7, fontsize=10)

plt.savefig('LatestFigures/allCitiesSurgeFrequency.eps')

import json

plt.show()
#fig.savefig('..\dateFigures\etaUpdateFrequency.eps')