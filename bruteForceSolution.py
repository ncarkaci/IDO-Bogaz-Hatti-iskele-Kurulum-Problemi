#!/usr/bin/env python
#-*-coding:utf-8-*--

import random
import time
import timeit

def bruteForce(distanceList, profitList, limit, rootStationIndex):
 
	# initialize variables
	maxProfit          = 0	
	stationList        = []


	# for first visit list go to n item 
	for currentStationIndex in range(rootStationIndex+1, len(distanceList)): 
		
		# initialize current profit and station in every step
		newProfit          = 0
		newStationList     = []
		
		# feasibility check             
		if ((distanceList[currentStationIndex]-distanceList[rootStationIndex]) > limit ):                
			
			# call function for new sub list which root station is currentStationIndex
			subProfitValue, subStationList = bruteForce(distanceList, profitList, limit, currentStationIndex) 
			
			# calculate new profit and new station list from sub routine
			newProfit      = profitList[currentStationIndex]+subProfitValue
			newStationList.append(currentStationIndex)
			newStationList = newStationList+subStationList

			# check new profit and update max profit and station list
			if (newProfit > maxProfit):
				
				maxProfit       = newProfit
				stationList     = newStationList
						  
	return maxProfit , stationList

