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
	if row < 21 and item[1]>0.1 and item[1] < 4.0001:
		p1Numbers[row].append(item[1])


p1NumbersNew = p1Numbers[:]

p2Numbers = []
for i in range(21):
	p2Numbers.append([])
for item1 in idis2:
	for item in item1:
		row = int(item[0]/60)
		if row < 21 and item[1]>0.1 and item[1] < 4.0001:
			p2Numbers[row].append(item[1])

p2NumbersNew = p2Numbers[:]
#ax = sns.heatmap(flights)
xMax = 9
yMax = 21
NX=xMax
NY=yMax

f,(subPlots) = plt.subplots(1,2, figsize = (7.2, 4.4), gridspec_kw={'width_ratios':[0.9,1]})


for row in range(0,len(p1Numbers)):
	totalDistance = []
	for i in range(0,9):
		totalDistance.append([])
	for item in p1Numbers[row]:
		totalDistance[int(item*2)].append(item)
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
		totalDistance[int(item*2)].append(item)
	totalLen = len(p2Numbers[row])
	for i in range(0,9):
		if totalLen > 0:
			totalDistance[i] = len(totalDistance[i])/totalLen
		else:
			totalDistance[i] = 0
	p2Numbers[row] = totalDistance


subPlots[0] = sns.heatmap(p1Numbers, linewidths=.5,vmin=0, vmax=1,xticklabels=True, yticklabels=True, annot = False, cbar = False, ax = subPlots[0])
subPlots[1] = sns.heatmap(p2Numbers, linewidths=.5,vmin=0, vmax=1,xticklabels=True, yticklabels=True, annot = False, cbar = False,ax = subPlots[1])
cbar = subPlots[1].figure.colorbar(subPlots[1].collections[0])
cbar.set_ticks([0,0.2,0.4,0.6,0.8,1])
cbar.set_ticklabels([ '00%', '20%', '40%', '60%', '80%', '100%'])
subPlots[0].invert_yaxis()
subPlots[1].invert_yaxis()

subPlots[0].set_ylim(1,NY)
subPlots[0].set_xlim(0,NX-1)

subPlots[1].set_ylim(1,NY)
subPlots[1].set_xlim(0,NX-1)


plt.subplots_adjust(left=0.16, right = 0.96,bottom =0.22,wspace=0.36,top=0.93, hspace = 0.27)

subPlots[0].text(0.8,-1.5, 'Idle Distance (Miles)', rotation=0,   size=10,  fontweight='bold')
	
subPlots[1].text(0.8,-1.5, 'Idle Distance (Miles)', rotation=0,   size=10,  fontweight='bold')


subPlots[0].set_yticklabels(['','','2','','4','','6','','8','','10','','12','','14','','16','','18','','20'])

subPlots[1].set_yticklabels(['','','2','','4','','6','','8','','10','','12','','14','','16','','18','','20'])

subPlots[0].set_xticks([1,2,3,4,5,6,7,8])
subPlots[1].set_xticks([1,2,3,4,5,6,7,8])
subPlots[0].set_xticklabels(['0.5','1','1.5','2','2.5','3','3.5','4'])

subPlots[1].set_xticklabels(['0.5','1','1.5','2','2.5','3','3.5','4'])

subPlots[0].text(-1.7,16.1, 'Idle time (Minutes)', rotation=90,   size=12,  fontweight='bold')

subPlots[0].set_title('Phase 1')
subPlots[1].set_title('Phase 2')


totalP1Records = 0
for row in range(len(p1NumbersNew)):
	totalP1Records += len(p1NumbersNew[row])

totalP2Records = 0
for row in range(len(p2NumbersNew)):
	totalP2Records += len(p2NumbersNew[row])


#subPlots[0].annotate("{",fontsize=53,
#            xy=(0, 0.21), xycoords='figure fraction'
  #          )

#subPlots[0].text(x = -1.4, y = 1, s="{",  family = 'Helvetica Neue UltraLight',fontsize=40,size=10)
import matplotlib.pyplot as plt
import matplotlib.patches as patches

rect = patches.Rectangle((-3.3, 1.1), 1.2, 4.6, linewidth=2, edgecolor='r', facecolor='none',clip_on=False)
subPlots[0].add_patch(rect)
windpwP1size = 8.1
subPlots[0].text(x = -3.2, y = 2.65, s=""+str(round(windpwP1size,1))+"%\ncars",  family = 'Helvetica Neue UltraLight',fontsize=40,size=10, rotation = 90)


rect = patches.Rectangle((-3.3, 5.6), 1.2, 5, linewidth=2, edgecolor='g', facecolor='none',clip_on=False)
subPlots[0].add_patch(rect)
windpwP1size = 0
windpwP1size = 57.5
subPlots[0].text(x =-3.2, y = 7.65, s=""+str(round(windpwP1size,1))+"%\ncars",  family = 'Helvetica Neue UltraLight',fontsize=40,size=10, rotation = 90)

rect = patches.Rectangle((-3.3, 10.7), 1.2, 4.9, linewidth=2, edgecolor='b', facecolor='none',clip_on=False)
subPlots[0].add_patch(rect)
windpwP1size = 29.5
subPlots[0].text(x =-3.2, y = 12.7, s=""+str(round(windpwP1size,1))+"%\ncars",  family = 'Helvetica Neue UltraLight',fontsize=40,size=10, rotation = 90)

rect = patches.Rectangle((-3.3, 15.6), 1.2, 5.2, linewidth=2, edgecolor='black', facecolor='none',clip_on=False)
subPlots[0].add_patch(rect)



windpwP1size = 4.9
subPlots[0].text(x =-3.2, y = 17.65, s=""+str(round(windpwP1size,1))+"%\ncars",  family = 'Helvetica Neue UltraLight',fontsize=40,size=10, rotation = 90)


lenDict = [0,0,0,0]
#totalP1Records = 0
for row in range(len(p1NumbersNew)):
	#windpwP1size += len(p1NumbersNew[row])
	for item in p1NumbersNew[row]:
		lenDict[int(math.floor(item))] += 1

rect = patches.Rectangle((0, -4), 1.93, 2.2, linewidth=2, edgecolor='r', facecolor='none',clip_on=False)
subPlots[0].add_patch(rect)
windpwP1size = float((lenDict[0]/totalP1Records)*100)
subPlots[0].text(x = 0.3, y = -3.81, s=""+str(round(windpwP1size,1))+"% \ncars",  family = 'Helvetica Neue UltraLight',fontsize=40,size=10, rotation = 0)

rect = patches.Rectangle((2, -4), 1.93, 2.2, linewidth=2, edgecolor='g', facecolor='none',clip_on=False)
subPlots[0].add_patch(rect)
windpwP1size = float((lenDict[1]/totalP1Records)*100)
subPlots[0].text(x = 2.3, y = -3.81, s=""+str(round(windpwP1size,1))+"% \ncars",  family = 'Helvetica Neue UltraLight',fontsize=40,size=10, rotation = 0)

rect = patches.Rectangle((4, -4), 1.93, 2.2, linewidth=2, edgecolor='b', facecolor='none',clip_on=False)
subPlots[0].add_patch(rect)
windpwP1size = float((lenDict[2]/totalP1Records)*100)
subPlots[0].text(x = 4.3, y = -3.81, s=""+str(round(windpwP1size,1))+"% \ncars",  family = 'Helvetica Neue UltraLight',fontsize=40,size=10, rotation = 0)

rect = patches.Rectangle((6, -4), 1.93, 2.2, linewidth=2, edgecolor='black', facecolor='none',clip_on=False)
subPlots[0].add_patch(rect)
windpwP1size = float((lenDict[3]/totalP1Records)*100)
subPlots[0].text(x = 6.5, y = -3.81, s=""+str(round(windpwP1size,1))+"% \ncars",  family = 'Helvetica Neue UltraLight',fontsize=40,size=10, rotation = 0)



lenDict = [0,0,0,0]
#totalP1Records = 0
for row in range(len(p2NumbersNew)):
	#windpwP1size += len(p1NumbersNew[row])
	for item in p2NumbersNew[row]:
		if item >= 4:
			item = 3.9
		lenDict[int(math.floor(item))] += 1

rect = patches.Rectangle((0, -4), 1.93, 2.2, linewidth=2, edgecolor='r', facecolor='none',clip_on=False)
subPlots[1].add_patch(rect)
windpwP1size = float((lenDict[0]/totalP2Records)*100)
subPlots[1].text(x = 0.2, y = -3.81, s=""+str(round(windpwP1size,1))+"% \ncars",  family = 'Helvetica Neue UltraLight',fontsize=40,size=10, rotation = 0)

rect = patches.Rectangle((2, -4), 1.93, 2.2, linewidth=2, edgecolor='g', facecolor='none',clip_on=False)
subPlots[1].add_patch(rect)
windpwP1size = float((lenDict[1]/totalP2Records)*100)
subPlots[1].text(x = 2.1, y = -3.81, s=""+str(round(windpwP1size,1))+"% \ncars",  family = 'Helvetica Neue UltraLight',fontsize=40,size=10, rotation = 0)

rect = patches.Rectangle((4, -4), 1.93, 2.2, linewidth=2, edgecolor='b', facecolor='none',clip_on=False)
subPlots[1].add_patch(rect)
windpwP1size = float((lenDict[2]/totalP2Records)*100)
subPlots[1].text(x = 4.3, y = -3.81, s=""+str(round(windpwP1size,1))+"% \ncars",  family = 'Helvetica Neue UltraLight',fontsize=40,size=10, rotation = 0)

rect = patches.Rectangle((6, -4), 1.93, 2.2, linewidth=2, edgecolor='black', facecolor='none',clip_on=False)
subPlots[1].add_patch(rect)
windpwP1size = float((lenDict[3]/totalP2Records)*100)
subPlots[1].text(x = 6.3, y = -3.81, s=""+str(round(windpwP1size,1))+"% \ncars",  family = 'Helvetica Neue UltraLight',fontsize=40,size=10, rotation = 0)




rect = patches.Rectangle((-2.7, 1.1), 1.4, 4.6, linewidth=2, edgecolor='r', facecolor='none',clip_on=False)
subPlots[1].add_patch(rect)
subPlots[1].text(x = -2.5, y = 2.75, s="30.3%\ncars",  family = 'Helvetica Neue UltraLight',fontsize=40,size=10, rotation = 90)


rect = patches.Rectangle((-2.7, 5.6), 1.4, 5, linewidth=2, edgecolor='g', facecolor='none',clip_on=False)
subPlots[1].add_patch(rect)
subPlots[1].text(x = -2.5, y = 7.68, s="43.1%\ncars",  family = 'Helvetica Neue UltraLight',fontsize=40,size=10, rotation = 90)

rect = patches.Rectangle((-2.7, 10.7), 1.4, 4.9, linewidth=2, edgecolor='b', facecolor='none',clip_on=False)
subPlots[1].add_patch(rect)
subPlots[1].text(x = -2.5, y = 12.68, s="21.6%\ncars",  family = 'Helvetica Neue UltraLight',fontsize=40,size=10, rotation = 90)

rect = patches.Rectangle((-2.7, 15.6), 1.4, 5.2, linewidth=2, edgecolor='black', facecolor='none',clip_on=False)
subPlots[1].add_patch(rect)
subPlots[1].text(x = -2.5, y = 17.68, s="5.0%\ncars",  family = 'Helvetica Neue UltraLight',fontsize=40,size=10, rotation = 90)

ax = subPlots[1]
#ax.annotate('Percentage of vehicles', xy=(0,0),  xycoords='data',
 #           xytext=(0.8, 0.95), textcoords='axes fraction',
  #          arrowprops=dict(facecolor='black', shrink=0.05),
   #         horizontalalignment='right', verticalalignment='top',clip_on=False
    #        )



plt.savefig('LatestFigures/IDIScdf.pdf', rasterized=True)

plt.savefig('LatestFigures/IDIScdf.png')
#print(np.average(c1)/60, np.average(c2)/60,np.average(d1)/1, np.average(d2)/1 )



show()