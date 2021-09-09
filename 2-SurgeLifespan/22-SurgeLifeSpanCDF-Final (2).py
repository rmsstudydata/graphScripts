import numpy as np
import ast 
from pylab import *

sys.path.insert(1, 'RawData')

import surgeTimeCDFData
import cityNames
import etaFrequencyDict
import surgeCDFTime

from cityNames import CityShortName as cityShortForm

surgereqnum = []
frequencyDict = surgeCDFTime.SurgeData
etaupdateFrequency15 =surgeCDFTime.SurgeData
# Create some test data
axList = []
fig, (axList)= plt.subplots(1, 2, sharey = True, figsize=(4.3,2.6))
#axList = [ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9,ax10]

sgavrgList=  []

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



cityMaxDict = {}


mu = 200
sigma = 25
n_bins = 300
x = np.random.normal(mu, sigma, size=100)

citiesLen = {}
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

maxMin = []
maxMinName = []
slnum = []
cityIndex = 0

citiessurge = {}


import json
fx1 = open('nl1.txt','r')
D1 = json.loads(fx1.read())
fx1.close()

fx1 = open('nl2.txt','r')
D2 = json.loads(fx1.read())
fx1.close()

for row in axList:
	#for ax in row:
		cities = ['CapeTown-SA','Paris-France']
		currentCity = ''
		maxCity = 0
		if cityIndex < 2:
			currentCity = cities[cityIndex]
			
			for service in cityServiceEconomyCategory[currentCity].keys():
				category = cityServiceEconomyCategory[currentCity][service]
				if service == 'Uber' and 'Paris' in currentCity:
					ijk= 10
				if service == 'Cabify' :
					ijk= 10
				if service == 'Heetch' and category == 'car':
					category = "fr-paris-pro"
				try:
					maxVal = max(etaupdateFrequency15[currentCity][service][category])
					if maxVal >maxCity:
						maxCity = maxVal
				except Exception as e:
					ijk= 10

			for service in cityServiceEconomyCategory[currentCity].keys():
				category = cityServiceEconomyCategory[currentCity][service]
				if service == 'Cabify' :
					ijk= 10
				try:
					l3 = etaupdateFrequency15[currentCity][service][category]
					if service == 'Heetch' and category == 'car':
						category = "fr-paris-pro"
					
					if service == 'Cabify' :
						ijk= 10
					for i in range(0,1):
						
						etaupdateFrequency15[currentCity][service][category].append(maxCity)
				except:
					ijk = 10
		cityIndex+= 1


#graph

printedServices = []
cityIndex = 0
totalSurgesLives = []

myData = {}
for ax in axList:
		csg = []
	#for ax in row:
		currentCity = ''
		maxCity = 0
		if cityIndex < 9:

			currentCity = cities[cityIndex]
			myData[currentCity] = {}
			ax.set_title(cityShortForm[currentCity],fontweight='bold',fontsize=7)
			citiesLen[currentCity] = []
			for service in cityServiceEconomyCategory[currentCity].keys():
				category = cityServiceEconomyCategory[currentCity][service]
				if service == 'Heetch' and category == 'car':
					category = "fr-paris-pro"
				if service == 'Cabify' :
					ijk= 10
				try:
					
					content = D1[currentCity][service]#etaupdateFrequency15[currentCity][service][category]
					content2= []
					try:
						content2 = D2[currentCity][service]
					except:
						ijk = 10
					myData[currentCity][service] = content
					maxCity1 = max(etaupdateFrequency15[currentCity][service][category])
					printedServices.append(service)
					if maxCity1 > maxCity:
						maxCity = maxCity1
					x = content
					content.append(maxCity+1)
					if 'Uber' in service:
						slnum += content

					le5 = 0
					for item in content:
						if item < 315:
							le5+=1
					print(le5/len(content),currentCity+'-'+service)
					csg.append(le5/len(content))
					maxMin.append(np.average(content))
					maxMinName.append(currentCity+'-'+service)

										# sort the data:
					data_sorted = np.sort(content)

					# calculate the proportional values of samples
					p = 1. * np.arange(len(content)) / (len(content) - 1)
					
					if 1:
					#if 'Lyft' in service:
						totalSurgesLives += content
					if  currentCity not in citiessurge.keys():
						citiessurge[currentCity] = []
					citiessurge[currentCity] = citiessurge[currentCity] + content

					citiesLen[currentCity]=citiesLen[currentCity]+ content
					ax.plot(data_sorted, p,lw=1.2, color = serviceColors[service])


					if len(content2)> 0:
						data_sorted = np.sort(content2)

						# calculate the proportional values of samples
						p = 1. * np.arange(len(content2)) / (len(content2) - 1)
			
			
						citiesLen[currentCity] = citiesLen[currentCity] + list(content2)
						ax.plot(data_sorted, p,lw=1.2, color = serviceColors[service],ls='--')

					'''
					# Add a line showing the expected distribution.
					y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
							np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
					y = y.cumsum()
					y /= y[-1]

					ax.plot(bins, y, 'k--', linewidth=1.5, label='Theoretical')
					'''
				except Exception as e:
					ijk = 10
		#surgereqnum.append(min(csg))
		cityIndex+= 1
		print(maxCity)
		cityMaxDict[currentCity] = maxCity
		#ax.set_xscale("log")
		ax.set_xlim(-1, maxCity)
		ticksNew = [60,300,600,900,1200,1500]#np.arange(1,maxCity+0.000001,step=(maxCity-1)/3)
		for i in range(0,len(ticksNew)):
			ticksNew[i] = round(float(ticksNew[i]),1)
		ax.set_xticks(ticksNew)
		xlabelsNew = ['1','','10','','20','25']
		
		ax.set_xticklabels(xlabelsNew,fontsize=6)

		ax.axhline(y=0.51,ls = '--')
		ax.set_ylim(0.01, 1.0005)

		ticksNew = np.arange(0.0,1.001,step=0.2)
		ax.set_yticks(ticksNew)
		ylabelsNew = []
		for item in ticksNew:
			item = str(int(item*100))
			if item == '99' and item==ticksNew[len(ticksNew)-1]:
				item = '100'
			ylabelsNew.append(item)
		ax.set_yticklabels(ylabelsNew)



axList[0].set_ylabel('CDF',fontweight='bold')
#axList[0].set_yticks([0,0.2,0.4,0.8,1],['1','1','1','1','1'])
'''
for item in axList:
	item.set_yticks([0,0.25,0.5,0.75,1])
	item.set_yticklabels(['0','','0.5','','1'])
'''



axList[1].set_xlabel('Surge Life (Minutes)',fontsize = 8, fontweight='bold')
axList[1].xaxis.set_label_coords(0.5, -0.14)

axList[0].set_xlabel('Surge Life (Minutes)',fontsize = 8,fontweight='bold')
axList[0].xaxis.set_label_coords(0.5, -0.14)


textstr = '━━━━ Pre-covid \n------ Covid'
props = dict(boxstyle='square', facecolor='white', alpha=0.5)

axList[0].text(0.36,  0.2, textstr, transform=axList[0].transAxes, fontsize=9,
verticalalignment='top', bbox=props)



axList[1].text(0.36,  0.2, textstr, transform=axList[1].transAxes, fontsize=9,
verticalalignment='top', bbox=props)

legend_elements = []

cityInd = 0
slnum = sorted(slnum)
#print(slnum[int(len(slnum)/2)])
for key in serviceColors:
	if key in printedServices:
		newLine =Line2D([0], [0], color=serviceColors[key], label=key,lw=1)
		legend_elements.append(newLine)

#print(max(maxMin),maxMinName[maxMin.index(max(maxMin))])
for i in range(len(maxMin)):
	if maxMin[i] < 315:
		print(maxMinName[i], maxMin[i])
#plt.legend(handles=legend_elements,loc='lower center', bbox_to_anchor=(-4.5, -0.7),
 #         fancybox=True, shadow=False, ncol=7, fontsize=8)

print(np.average(surgereqnum))
plt.subplots_adjust(left=0.08, right = 0.99
					,bottom =0.35,wspace=0.25,top=0.84, hspace = 0.97)


textstr = '━━━━ Pre-covid \n ┄┄┄┄ Covid'
props = dict(boxstyle='square', facecolor='white', alpha=0.5)

ax.text(-10.5, -0.3, textstr, transform=ax.transAxes, fontsize=9,
	verticalalignment='top', bbox=props)


ax.legend(handles=legend_elements,loc='lower center', bbox_to_anchor=(-0.2, -0.5),
          fancybox=True, shadow=False, ncol=7, fontsize=10)


plt.subplots_adjust(left=0.13, right = 0.96 ,bottom =0.3,wspace=0.25,top=0.9, hspace = 0.97)
axList[0].set_ylabel('CDF',fontweight='bold')

plt.savefig('LatestFigures/allCitiesSurgeLife.eps')

for city in citiessurge:
	citiessurge[city] = sorted(citiessurge[city])
	print(city, np.average(citiessurge[city])/60,citiessurge[city][int(len(citiessurge[city])/2)]/60)

#fig.delaxes(axList[1,4])
totalSurgesLives = sorted (totalSurgesLives)
#print('MAIN MID', totalSurgesLives[int(len(totalSurgesLives)/2)],np.average(totalSurgesLives)/60)
for city in citiesLen:
	print(city, np.average(citiesLen[city]))
plt.show()
import json
#fx1 = open('nl1.txt','w')
#fx1.write(json.dumps(myData))
#fx1.close()
plt.show()

#fig.savefig('..\dateFigures\etaUpdateFrequency.eps')