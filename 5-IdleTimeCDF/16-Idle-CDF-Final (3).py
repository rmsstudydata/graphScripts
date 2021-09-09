import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.insert(1, 'RawData')
import idleTimeDistanceNumberScatter
import cityNames
from matplotlib.lines import Line2D
import json
import random
from IDITNumbers5 import timeDistanceCoreff5
from scipy import stats
import numpy as np
from collections import Counter
import collections

import correlationData
import cityNames
import experimentArea
import supplyNumbers
import seaborn  as sns
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.colors
import utilizationData
import math
utilDict = utilizationData.utilData5

supplyDict = supplyNumbers.supplyCount5

cities = list(cityNames.CityFullName.keys())
from cityServices import jourlyScaleDict as hourlyScaleDict

fullnames = cityNames.CityFullName
serviceColors = cityNames.serviceColors

econCatDict = cityNames.cityServiceEconomyCategory

rvs = []
distAvrg = []
timeAvrg = []
hrsList = []
import scipy.stats as st
def get_best_distribution(data):
	dist_names = ["norm", "weibull_min", "pareto", "genextreme", 'rayleigh','pareto','poisson','binomial', 'bernoulli','gamma']
	dist_results = []
	params = {}
	for dist_name in dist_names:
		try:
			dist = getattr(st, dist_name)
			param = dist.fit(data)

			params[dist_name] = param
			# Applying the Kolmogorov-Smirnov test
			D, p = st.kstest(data, dist_name, args=param)
			# print("p value for "+dist_name+" = "+str(p))
			dist_results.append((dist_name, p))
		except:
			ijk = 10

    # select the best fitted distribution
	best_dist, best_p = (max(dist_results, key=lambda item: item[1]))
    # store the name of the best fit and its p value

  #  print("Best fitting distribution: "+str(best_dist))
  #  print("Best p value: "+ str(best_p))
   # print("Parameters for the best fit: "+ str(params[best_dist]))
	return [best_dist, best_p]#, params[best_dist]
shaperTest = []
scatterDict = timeDistanceCoreff5#idleTimeDistanceNumberScatter.timeDistanceCoreff5
# Fixing random state for reproducibility
#cities = ['CapeTown-SA',]
#f,(subPlots) = plt.subplots(2,4, figsize = (6, 4))
cityInd = 0
'''
fn = open('RawData/IDITNumbers5.txt','r')
content = fn.read()
fn.close()
content = content.replace('\n','')
content=content.replace('timeDistanceCoreff5 = {}','')
content = json.loads(content)
'''
econCatDict['Paris-France']['Heetch']= "fr-paris-pro"
econCatDict['MexicoCity-Mexico']['Uber']= "UberX"
cameServices = []

tempidleList= []
tempcityList = []
rvs2 = []
sv2 = []
avrg2 =[]
hrsAvrg = []
econCatDict = cityNames.cityServiceEconomyCategory
experimentAreas = experimentArea.exArea
econCatDict['Dubai-UAE']['Uber'] = 'Black'
econCatDict['Toronto-Canada']['Lyft'] = 'Lyft'
econCatDict['Dubai-UAE']['Careem'] = 'Go'
weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

newIDISData = []
fx = open('IDIS1.txt','r')
newIDISData = json.loads(fx.read())
fx.close()

newIDISData = newIDISData['1']
idis1 = newIDISData 
newIDISData2 = {}
fx = open('IDIS.txt','r')
newIDISData2 = json.loads(fx.read())
fx.close()

idis2 = []


ecoCatsp2 = {}
ecoCatsp2['CapeTown-SA'] = {}
ecoCatsp2['CapeTown-SA']['Uber'] = 'UberX'
ecoCatsp2['CapeTown-SA']['Taxify'] = 'Bolt'

ecoCatsp2['Delhi-India'] = {}
ecoCatsp2['Delhi-India']['Uber'] = 'UberGo'
ecoCatsp2['Delhi-India']['Ola'] = 'prime_play'


ecoCatsp2['Dubai-UAE'] = {}
ecoCatsp2['Dubai-UAE']['Uber'] = 'Select'
ecoCatsp2['Dubai-UAE']['Careem'] = 'Economy'

ecoCatsp2['London-UK'] = {}
ecoCatsp2['London-UK']['Uber']= 'Assist'
ecoCatsp2['London-UK']['Gett'] = 'car'


ecoCatsp2['Melbourne-AU'] = {}
ecoCatsp2['Melbourne-AU']['Uber'] = 'UberX'

ecoCatsp2['Melbourne-AU']['Shebah'] = 'car'

ecoCatsp2['MexicoCity-Mexico'] = {}
ecoCatsp2['MexicoCity-Mexico']['Uber'] = 'Assist'

ecoCatsp2['MexicoCity-Mexico']['Cabify'] = 'car'

ecoCatsp2['NY-US'] = {}
ecoCatsp2['NY-US']['Uber'] = 'UberX'
ecoCatsp2['NY-US']['Lyft'] = 'Lyft'

ecoCatsp2['Paris-France'] = {}
ecoCatsp2['Paris-France']['Uber'] = 'UberX'
ecoCatsp2['Paris-France']['Heetch'] = 'fr-paris-pro'
ecoCatsp2['Paris-France']['Taxify'] = 'Bolt'


ecoCatsp2['Toronto-Canada'] = {}
ecoCatsp2['Toronto-Canada']['Uber'] = 'UberX'
ecoCatsp2['Toronto-Canada']['Lyft'] = 'Lyft'

cityNameNewToOld = {}
cityNameNewToOld['1-NYC'] = 'NY-US'
cityNameNewToOld['2-YTO'] = 'Toronto-Canada'
cityNameNewToOld['3-CPT'] = 'CapeTown-SA'
cityNameNewToOld['4-DEL'] = 'Delhi-India'
cityNameNewToOld['5-DXB'] = 'Dubai-UAE'
cityNameNewToOld['6-LDN'] = 'London-UK'
cityNameNewToOld['7-MELB'] = 'Melbourne-AU'
cityNameNewToOld['8-MEX'] = 'MexicoCity-Mexico'
cityNameNewToOld['9-PAR'] = 'Paris-France'


for city in newIDISData2:
	mappedCity = ''
	for cityNew in cityNameNewToOld.keys():
		if cityNew == city:
			mappedCity = cityNameNewToOld[cityNew]
			break
	for service in  newIDISData2[city]:
		if 1:
		#if 'Uber' not in service:
			try:
				if 1:
				#for category in newIDISData2[city][service]:
					category = ecoCatsp2[mappedCity][service]
					data = newIDISData2[city][service][category]
					for item in data:
						idis2.append(item)
			except Exception as e:
				ijk =1

fourWindows1 = {}
fourWindows2 = {}

for item in ['1','2','3','4']:
	fourWindows1[item] = []
	fourWindows2[item] = []
for item in idis1:
	if int( item[0])/60 < 5:
		fourWindows1['1'].append(item)
	elif int( item[0])/60 < 10:
		fourWindows1['2'].append(item)
	elif int( item[0])/60 < 15:
		fourWindows1['3'].append(item)
	elif int( item[0])/60 < 20:
		fourWindows1['4'].append(item)

for i in range(len(idis2)):
	for j in range(len(idis2[i])):
		if int( idis2[i][j][0])/60 < 8:
			idis2[i][j][0] = idis2[i][j][0]*1.8
			idis2[i][j][1] = idis2[i][j][1]*1.4

for item1 in idis2:
	for item in item1:
		if int( item[0])/60 < 5:
			fourWindows2['1'].append(item)
		elif int( item[0])/60 < 10:
			fourWindows2['2'].append(item)
		elif int( item[0])/60 < 15:
			fourWindows2['3'].append(item)
		elif int( item[0])/60 < 20:
			fourWindows2['4'].append(item)

# Create some test data
import numpy as np
from pylab import *


p1Numbers = []
for i in range(21):
	p1Numbers.append([])
for item in idis1:
	row = int(item[0]/60)
	if row < 21 and item[1]>0.2 and item[1] < 8.0001:
		p1Numbers[row].append(item[1])


p2Numbers = []
for i in range(21):
	p2Numbers.append([])
for item1 in idis2:
	for item in item1:
		row = int(item[0]/60)
		if row < 21 and item[1]>0.2 and item[1] < 8.0001:
			p2Numbers[row].append(item[1])




dx = 0.01
X  = []
Y  = []

data = []
N = 0

type = 0

v1 = 0
for window in range(1,5):
	for item in fourWindows1[str(window)]:
		if item[1] > 0.2 and item[1]< 8.1:
			v1+=1

v2 = 0
for window in range(1,5):
	for item in fourWindows2[str(window)]:
		if item[1] > 0.2 and item[1]< 8.1:
			v2+=1

c1 = []
c2 = []
d1 = []
d2 = []

colors = ['blue','red','green','black']
for row in [[1,1,1],[1,1,1]]:
	window = 1
	type +=1
	for ax in row:
		data = []
		if type == 1:
			cwindow= fourWindows1
		if type == 2:
			cwindow= fourWindows2
		for item in cwindow[str(window)]:
			if item[1] > 0.2 and item[1]< 8.1:
				data.append(item[1])
				if type == 1:
					c1.append(item[0])
					d1.append(item[1])

				else:
					c2.append(item[0])
					d2.append(item[1])
			# Normalize the data to a proper PDF
		N = len(data)
		x = np.sort(data) 
  
	#	for x1 in range(0,1009):
	#		data.append(8.1)

		# get the cdf values of y 
		y = np.arange(N) / float(N)

		
		#ax.set_xticks([1,2,3,4,5,6,7,8])
		#ax.set_yticks([0,0.2,0.4,0.6,0.8,1])
		'''
		if window !=1:
			ax.set_yticklabels([])
		else:
			ax.text(-3.5,0.7, 'P'+str(type)+' CDF',rotation=90,   size=11,  fontweight='bold')

			ax.set_yticklabels(['','0.2','0.4','0.6','0.8','1'])
		if type ==1:
			ax.text(0.3,1.1, '     Idle time \n('+ str((window-1)*5) +'-'+str((window)*5)+' minutes)',rotation=0,   size=8,  fontweight='bold')
			ax.set_xticklabels([])
		else:
			
			ax.set_xticklabels(['','2','','4','','6','','8'])
		if type == 2 and window == 3:
			ax.text(-7,-0.27, 'Idle Distance (Miles)',rotation=0,   size=10,  fontweight='bold')
		'''
		vc = 0
		if type == 1:
			vc = v1
		else:
			vc = v2
		#ax.text(2,0.27, str(round((len(data)/vc)*100,1))+'% cars',rotation=0,   size=7,  fontweight='bold')

		#ax.set_xlim((0,8))
		#ax.set_ylim((0.01,1.01))

		#ax.plot(x, y, color =colors[window-1]) 
		window += 1


#ax = sns.heatmap(flights)
xMax = 9
yMax = 21
NX=xMax
NY=yMax

f,(subPlots) = plt.subplots(1,2, figsize = (6, 4))

uniform_data = np.random.rand(NY, NX)

for row in range(0,len(p1Numbers)):
	totalDistance = []
	for i in range(0,9):
		totalDistance.append([])
	for item in p1Numbers[row]:
		totalDistance[int(item)].append(item)
	totalLen = len(p1Numbers[row])
	
	for i in range(0,9):
		if totalLen > 0:
			totalDistance[i] = len(totalDistance[i])/totalLen
		else:
			totalDistance[i] = 0
	p1Numbers[row] = totalDistance


for row in range(0,len(p2Numbers)):
	totalDistance = []
	for i in range(0,9):
		totalDistance.append([])
	for item in p2Numbers[row]:
		totalDistance[int(item)].append(item)
	totalLen = len(p2Numbers[row])
	for i in range(0,9):
		if totalLen > 0:
			totalDistance[i] = len(totalDistance[i])/totalLen
		else:
			totalDistance[i] = 0
	p2Numbers[row] = totalDistance


subPlots[0] = sns.heatmap(p1Numbers, linewidths=.5,vmin=0, vmax=1,xticklabels=True, yticklabels=True, annot = False, cbar = False, ax = subPlots[0])
subPlots[1] = sns.heatmap(p2Numbers, linewidths=.5,vmin=0, vmax=1,xticklabels=True, yticklabels=True, annot = False,cbar = True, ax = subPlots[1])

subPlots[0].invert_yaxis()
subPlots[1].invert_yaxis()

subPlots[0].set_ylim(1,NY)
subPlots[0].set_xlim(0,NX)

subPlots[1].set_ylim(1,NY)
subPlots[1].set_xlim(0,NX)


plt.subplots_adjust(left=0.09, right = 0.97,bottom =0.15,wspace=0.1,top=0.88, hspace = 0.18)

subPlots[0].text(1.8,-3, 'Idle Distance (Miles)', rotation=0,   size=10,  fontweight='bold')
	
subPlots[1].text(1.8,-3, 'Idle Distance (Miles)', rotation=0,   size=10,  fontweight='bold')



subPlots[1].set_yticklabels(['','','2','','4','','6','','8','','10','','12','','14','','16','','18','','20'])


plt.savefig('LatestFigures/IDIScdf.pdf', rasterized=True)

plt.savefig('LatestFigures/IDIScdf.png')
print(np.average(c1)/60, np.average(c2)/60,np.average(d1)/1, np.average(d2)/1 )

val1 = []

for i in range(len(d2)):
	if d2[i] >=2 :#and d2[i] <= 2:
		val1.append(d2[i])
print(np.average(val1))

show()