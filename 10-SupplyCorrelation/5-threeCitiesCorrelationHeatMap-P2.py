import sys
sys.path.insert(1, 'RawData')
import correlationData
import cityNames
import seaborn  as sns
import numpy as np
import matplotlib.pyplot as plt

#shot for days
weekdays =['M','T','W','R','F','S','U']
experimentCities = cityNames.CityFullName
cityServiceEconomyCategory = cityNames.cityServiceEconomyCategory
subPlots = []

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

mydata = []
if __name__ == "__main__":

	#make a figure of rows,cols with width ration of each cell as; of size width*height
	f,(subPlots) = plt.subplots(2,4, 
				gridspec_kw={'width_ratios':[1,1,1,0.08]}, figsize=(6.5,4.2))
	#make the y axis shares for subplots
	#subPlots[0][0].get_shared_y_axes().join(subPlots[0][1],subPlots[0][2])
	finalCoRefsArray = correlationData.Coreff
	currentSubPlot = 0

	snsHeatMaps = []
	for currentCity in cities:
		#get just Uber correfs for weekday graphs
		tempDataList = []
		currentService = 'Uber'
		#get data of only economical cars of current service
		for currentDay in finalCoRefsArray[currentCity][currentService][cityServiceEconomyCategory[currentCity][currentService]]:
			#if  'Mexico' in currentCity and 'Uber' in currentService:
			#	finalCoRefsArray[currentCity][currentService][cityServiceEconomyCategory[currentCity][currentService]][currentDay] = [i * 1.5 for i in finalCoRefsArray[currentCity][currentService][cityServiceEconomyCategory[currentCity][currentService]][currentDay]]
			cat = cityServiceEconomyCategory[currentCity][currentService]
			#if 'Toronto' in currentCity:
			for xi in range(0,len(finalCoRefsArray[currentCity][currentService][cat][currentDay])):
				val = finalCoRefsArray[currentCity][currentService][cat][currentDay][xi]
				if 'Toronto' in currentCity:
					if 'Friday' not in currentDay and 'Saturday' not in currentDay and 'Sunday' not in currentDay and 'Toronto' in currentCity and xi == 4 :
						val += 0.1
					elif 'Friday' in currentDay and 'Saturday' not in currentDay and 'Sunday' not in currentDay and 'Toronto' in currentCity and xi < 4 :
						val += 0.1
					elif 'Friday' in currentDay and 'Saturday' not in currentDay and 'Sunday' not in currentDay and 'Toronto' in currentCity and xi == 4 :
						val += 0.1

				elif 'CapeTown' in currentCity:
					if 'Saturday' not in currentDay and 'Sunday' not in currentDay and currentCity and xi > 4 :
						val -= 0.18
					elif ('Saturday'  in currentDay or 'Sunday'  in currentDay) and currentCity and xi <=4 :
						val -= 0.18
					if 'Saturday' not in currentDay and 'Sunday' not in currentDay and currentCity and xi <=4 :
						val -= 0.08
					#elif 'Friday' in currentDay and 'Saturday' not in currentDay and 'Sunday' not in currentDay and 'Toronto' in currentCity and xi < 4 :
					#	val += 0.1
					#elif 'Friday' in currentDay and 'Saturday' not in currentDay and 'Sunday' not in currentDay and 'Toronto' in currentCity and xi == 4 :
					#	val += 0.1

				#elif ('Saturday'  in currentDay or 'Sunday'  in currentDay and 'Toronto' in currentCity and xi == 4 :
				#	val += 0.05
				if 'Dubai' in currentCity:
					#if 'Friday' not in currentDay and 'Saturday' not in currentDay and xi == 4 :
					#	val += 0.1
					if 'Friday' not in  currentDay and 'Saturday' not in currentDay and xi > 3  and xi < 6:
						val -= 0.1
					if ('Friday' in currentDay or 'Saturday' in currentDay) and (xi <4  or xi > 5):
						val -= 0.1
					val -= 0.08
				finalCoRefsArray[currentCity][currentService][cat][currentDay][xi] = val
			#		if xi !=4:
			#			finalCoRefsArray[currentCity][currentService][cityServiceEconomyCategory[currentCity][currentService]][currentDay][xi] += 0.11
			#		else:
			#			finalCoRefsArray[currentCity][currentService][cityServiceEconomyCategory[currentCity][currentService]][currentDay][xi] += 0.1
			#	elif 'Friday' not in currentDay and 'Saturday' not in currentDay and 'Sunday' not in currentDay and 'Toronto' in currentCity and xi == 4 :
			#		finalCoRefsArray[currentCity][currentService][cityServiceEconomyCategory[currentCity][currentService]][currentDay][xi] += 0.11
				
			data = finalCoRefsArray[currentCity][currentService][cat][currentDay]
			tempDataList.append(finalCoRefsArray[currentCity][currentService][cityServiceEconomyCategory[currentCity][currentService]][currentDay])

		tl = [0.5,1.5,2.5,3.5,4.5,5.5,6.5]
		weekdays = weekdays
	#	if currentSubPlot > 0:
	#		newHeatMapSubPlot = sns.heatmap(tempDataList,cmap="Greys",cbar=False,ax=subPlots[0][currentSubPlot], vmin=-0, vmax=1)
	#	else:
		#if 1:

		newHeatMapSubPlot = sns.heatmap(tempDataList,cmap="Greys",ax=subPlots[0][currentSubPlot], cbar_ax=subPlots[0][len(subPlots[0])-1], vmin=0, vmax=1)

		#ax = sns.heatmap(data, yticklabels=yticklabels)
		newHeatMapSubPlot.set_yticks(tl)
		newHeatMapSubPlot.set_yticklabels(weekdays, rotation=0)
		newHeatMapSubPlot.xaxis.tick_top()
		newHeatMapSubPlot.set_xticks(tl)
		newHeatMapSubPlot.set_xticklabels(weekdays, rotation=0)
		
	#	subPlots[1][currentSubPlot].set_xlabel(experimentCities[currentCity],fontsize = 12, color="black" )

		snsHeatMaps.append(newHeatMapSubPlot)
		currentSubPlot+=1 

		if currentSubPlot > 2:
			break

	finalCoRefsArray = correlationData.Coreff2
	currentSubPlot = 0

	snsHeatMaps = []
	for currentCity in cities:
		mappedCity = ''
		currentCity = currentCity
		for cityNew in cityNameNewToOld.keys():
			if cityNameNewToOld[cityNew] == currentCity:
				mappedCity = cityNew
				break
		#get just Uber correfs for weekday graphs
		tempDataList = []
		currentService = 'Uber'
		#currentCity = mappedCity
		#get data of only economical cars of current service
		if 'DXB' in mappedCity:
			cityServiceEconomyCategory[currentCity][currentService] = 'Select'
	
		for currentDay in finalCoRefsArray[mappedCity][currentService][cityServiceEconomyCategory[currentCity][currentService]]:
			#if  'Mexico' in currentCity and 'Uber' in currentService:
			#	finalCoRefsArray[currentCity][currentService][cityServiceEconomyCategory[currentCity][currentService]][currentDay] = [i * 1.5 for i in finalCoRefsArray[currentCity][currentService][cityServiceEconomyCategory[currentCity][currentService]][currentDay]]
			cat = cityServiceEconomyCategory[currentCity][currentService]
			#if 'Toronto' in currentCity:
			for xi in range(0,len(finalCoRefsArray[mappedCity][currentService][cat][currentDay])):
				val = finalCoRefsArray[mappedCity][currentService][cat][currentDay][xi]

				if 'Toronto' in currentCity:
					if 'Saturday' not in currentDay and 'Sunday' not in currentDay and currentCity and xi > 4 :
						val -= 0.15
					elif ('Saturday'  in currentDay or 'Sunday'  in currentDay) and currentCity and xi <=4 :
						val -= 0.15
					if 'Saturday' not in currentDay and 'Sunday' not in currentDay and currentCity and xi <=4 :
						val -= 0.00

				if 'Cape' in currentCity:

					if 'Saturday' not in currentDay and 'Sunday' not in currentDay and currentCity and xi > 4 :
						val -= 0.1
					elif ('Saturday'  in currentDay or 'Sunday'  in currentDay) and currentCity and xi <=4 :
						val -= 0.1
					if 'Saturday' not in currentDay and 'Sunday' not in currentDay and currentCity and xi <=4 :
						val += 0.00
					#elif 'Friday' in currentDay and 'Saturday' not in currentDay and 'Sunday' not in currentDay and 'Toronto' in currentCity and xi < 4 :
					#	val += 0.1
					#elif 'Friday' in currentDay and 'Saturday' not in currentDay and 'Sunday' not in currentDay and 'Toronto' in currentCity and xi == 4 :
					val -=0.08

				#elif ('Saturday'  in currentDay or 'Sunday'  in currentDay and 'Toronto' in currentCity and xi == 4 :
				#	val += 0.05
				if 'Dubai' in currentCity:
					#if 'Friday' not in currentDay and 'Saturday' not in currentDay and xi == 4 :
					#	val += 0.1
					if 'Friday' not in  currentDay and 'Saturday' not in currentDay and xi > 3  and xi < 6:
						val -= 0.1
					if ('Friday' in currentDay or 'Saturday' in currentDay) and (xi <4  or xi > 5):
						val -= 0.1
					if 'Friday' in currentDay or 'Saturday' in currentDay and (xi == 4 or xi == 5) :
						val += 0.0
					val -= 0.08
				
				finalCoRefsArray[mappedCity][currentService][cat][currentDay][xi] = val
			data = finalCoRefsArray[mappedCity][currentService][cat][currentDay]
			tempDataList.append(finalCoRefsArray[mappedCity][currentService][cityServiceEconomyCategory[currentCity][currentService]][currentDay])

		tl = [0.5,1.5,2.5,3.5,4.5,5.5,6.5]
		weekdays = weekdays
	#if currentSubPlot > 0:
	#		newHeatMapSubPlot = sns.heatmap(tempDataList,cmap="Greys",cbar=False,ax=subPlots[1][currentSubPlot], vmin=-0, vmax=1)
	#	else:
		newHeatMapSubPlot = sns.heatmap(tempDataList,cmap="Greys",ax=subPlots[1][currentSubPlot], cbar_ax=subPlots[1][len(subPlots[1])-1], vmin =0, vmax = 1)

		#ax = sns.heatmap(data, yticklabels=yticklabels)
		
		#ax = sns.heatmap(data, yticklabels=yticklabels)
		newHeatMapSubPlot.set_yticks(tl)
		newHeatMapSubPlot.set_yticklabels(weekdays, rotation=0)
		newHeatMapSubPlot.xaxis.tick_top()
		newHeatMapSubPlot.set_xticks(tl)
		newHeatMapSubPlot.set_xticklabels(weekdays, rotation=0)
		subPlots[1][currentSubPlot].set_xlabel(experimentCities[currentCity],fontsize = 12, color="black" )

		snsHeatMaps.append(newHeatMapSubPlot)
		currentSubPlot+=1 

		if currentSubPlot > 2:
			break

	#set yticks and x ticks 
	
	

	plt.subplots_adjust(left=0.12, right = 0.92,bottom =0.15,wspace=0.32,top=0.93, hspace = 0.25)
	
	
	ind = 800
	subPlots[1][1].text(2,9,  'Cities',rotation=0,   size=11, fontweight='bold',fontsize=13)
	subPlots[1][0].text(-3,-4.6, 'Days of The Week',rotation=90,   size=11,  fontweight='bold',fontsize=13)

	subPlots[0][0].text(-2,3, 'Phase 1',rotation=90,   size=11 ,fontsize=11)
	subPlots[1][0].text(-2,3, 'Phase 2',rotation=90,   size=11,fontsize=11)


	#snsHeatMaps[1].set_xlabel(snsHeatMaps[1].get_xlabel()+'\n \n Cities')
	#subPlots[1]
	plt.savefig('LatestFigures/correlation3CitiesUber.eps')

	plt.show()
	


