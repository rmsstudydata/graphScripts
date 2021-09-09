import sys
sys.path.insert(1, 'RawData')
import correlationData
import cityNames
import seaborn  as sns
import numpy as np
import matplotlib.pyplot as plt
import json
#shot for days
weekdays =['M','T','W','R','F','S','U']
experimentCities = cityNames.CityFullName
cityServiceEconomyCategory = cityNames.cityServiceEconomyCategory
subPlots = []


topCorrelationCities = {}
finalCoRefsArray = correlationData.Coreff
for currentCity in finalCoRefsArray.keys():
	currentService = 'Uber'
	citySum = 0 
	for currentDay in finalCoRefsArray[currentCity][currentService][cityServiceEconomyCategory[currentCity][currentService]]:
		itInd = 0
		for item in finalCoRefsArray[currentCity][currentService][cityServiceEconomyCategory[currentCity][currentService]][currentDay]:
			if 'Friday' in currentDay and 'Toronto' in currentCity and itInd < 5 and itInd !=4 :
				item += 0.4
			citySum += float(item)
			itInd+=1

	topCorrelationCities[currentCity] = citySum
		#print(currentDay)
#print(topCorrelationCities)

vals = sorted(topCorrelationCities.values())[6:]
cities = []
for city in topCorrelationCities:
	if topCorrelationCities[city] in vals:
		cities.append(city)

print(cities)

cities= ['CapeTown-SA', 'Dubai-UAE', 'Toronto-Canada']

mydata = {}
d1 = {"CapeTown-SA": {"Uber": [[0.76208, 0.7365600000000001, 0.7163200000000001, 0.7383200000000001, 0.70752, 0.35552, 0.21295999999999998], [0.7365600000000001, 0.74272, 0.71808, 0.74272, 0.7251200000000001, 0.38104, 0.19272000000000003], [0.7163200000000001, 0.71808, 0.71896, 0.7304, 0.7084, 0.41448, 0.25872], [0.7383200000000001, 0.74272, 0.7304, 0.7497600000000001, 0.7409600000000001, 0.42328000000000005, 0.23848000000000003], [0.70752, 0.7251200000000001, 0.7084, 0.7409600000000001, 0.75944, 0.48400000000000004, 0.26752], [0.35552, 0.38104, 0.41448, 0.42328000000000005, 0.48400000000000004, 0.7207199999999999, 0.6248], [0.21295999999999998, 0.19272000000000003, 0.25872, 0.23848000000000003, 0.26752, 0.6248, 0.70048]]}, "Dubai-UAE": {"Uber": [[0.7453600000000001, 0.7365600000000001, 0.73304, 0.7251200000000001, 0.5218400000000001, 0.5429600000000001, 0.7268800000000001], [0.7365600000000001, 0.75592, 0.73128, 0.7242400000000001, 0.5412000000000001, 0.56672, 0.7268800000000001], [0.73304, 0.73128, 0.74184, 0.71896, 0.50512, 0.52624, 0.7216], [0.7251200000000001, 0.7242400000000001, 0.71896, 0.7488800000000001, 0.5438400000000001, 0.5544000000000001, 0.7128000000000001], [0.5218400000000001, 0.5412000000000001, 0.50512, 0.5438400000000001, 0.7612, 0.7031200000000001, 0.5209600000000001], [0.5429600000000001, 0.56672, 0.52624, 0.5544000000000001, 0.7031200000000001, 0.74448, 0.5456000000000001], [0.7268800000000001, 0.7268800000000001, 0.7216, 0.7128000000000001, 0.5209600000000001, 0.5456000000000001, 0.73128]]}, "Toronto-Canada": {"Uber": [[0.77616, 0.77616, 0.76296, 0.75064, 0.7092799999999999, 0.45848, 0.3872], [0.77616, 0.78584, 0.7770400000000001, 0.76472, 0.7207199999999999, 0.48312000000000005, 0.40304], [0.76296, 0.7770400000000001, 0.76736, 0.75064, 0.6951999999999999, 0.4532, 0.37752], [0.75064, 0.76472, 0.75064, 0.76032, 0.71192, 0.46816, 0.39336], [0.7092799999999999, 0.7207199999999999, 0.6951999999999999, 0.71192, 0.78232, 0.61512, 0.44968], [0.45848, 0.48312000000000005, 0.4532, 0.46816, 0.61512, 0.78056, 0.6916800000000001], [0.3872, 0.40304, 0.37752, 0.39336, 0.44968, 0.6916800000000001, 0.7524]]}}

if __name__ == "__main__":

	#make a figure of rows,cols with width ration of each cell as; of size width*height
	f,(subPlots) = plt.subplots(1,4, 
				gridspec_kw={'width_ratios':[1,1,1,0.08]}, figsize=(7,2.9))
	#make the y axis shares for subplots
	subPlots[0].get_shared_y_axes().join(subPlots[1],subPlots[2])
	finalCoRefsArray = correlationData.Coreff
	currentSubPlot = 0

	snsHeatMaps = []
	for currentCity in cities:
		try:
			val = mydata[ccurrentCity]
		except:
			mydata[currentCity] = {}
		#get just Uber correfs for weekday graphs
		tempDataList = []
		currentService = 'Uber'
		mydata[currentCity][currentService] = {}
		#get data of only economical cars of current service
		#forr currentDay in finalCoRefsArray[currentCity][currentService][cityServiceEconomyCategory[currentCity][currentService]]:
		tempDataList = d1[currentCity][currentService]
		if currentSubPlot > 0:
			newHeatMapSubPlot = sns.heatmap(tempDataList,cmap="Greys",cbar=False,ax=subPlots[currentSubPlot], vmin=-0, vmax=1)
		else:
			newHeatMapSubPlot = sns.heatmap(tempDataList,cmap="Greys",ax=subPlots[currentSubPlot], cbar_ax=subPlots[len(subPlots)-1], vmin=0, vmax=1)

		newHeatMapSubPlot.set_ylabel('')
		newHeatMapSubPlot.set_xlabel('')
	
		newHeatMapSubPlot.set_xlabel(experimentCities[currentCity],fontsize = 12, color="black" )

		snsHeatMaps.append(newHeatMapSubPlot)
		currentSubPlot+=1 

		if currentSubPlot > 2:
			break


	#set yticks and x ticks 
	ydone = 0
	for ax in subPlots:
		if ydone < 3:
			ax.xaxis.tick_top()
			#ax.xaxis.set_label_position('top') 
			
			tl = [0.5,1.5,2.5,3.5,4.5,5.5,6.5]
			#ax.set_xlim(0,7)
			ax.set_xticks(tl)
			#tl = ax.get_xticklabels()
			ax.set_xticklabels(weekdays, rotation=0)
			ax.set_yticks(tl)
			tly = ax.get_yticklabels()
			if ydone == 0:
				ax.set_yticklabels(weekdays, rotation=0)
			else:
				ax.set_yticks([])
				ax.set_yticklabels([])
		ydone +=1

	plt.subplots_adjust(left=0.14, right = 0.91,bottom =0.25,wspace=0.4,top=0.81, hspace = 0.6)
	
	
	ind = 800
	subPlots[1].text(2,9.5,  'Cities',rotation=0,   size=11, fontweight='bold',fontsize=13)
	subPlots[0].text(-4,0.2, 'Days of The Week',rotation=90,   size=11,  fontweight='bold',fontsize=13)

	#snsHeatMaps[1].set_xlabel(snsHeatMaps[1].get_xlabel()+'\n \n Cities')
	#subPlots[1]
	plt.savefig('dateFigures/correlation3CitiesUber.eps')

	plt.show()
	fx1 = open('0-ovCatCF.txt','w')
	fx1.write(json.dumps(mydata))
	fx1.close()
	


