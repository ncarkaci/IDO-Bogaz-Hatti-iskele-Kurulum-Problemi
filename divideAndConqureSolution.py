#!/usr/bin/env python
#-*-coding:utf-8-*--

import timeit
import random
import pprint


def divideAndConquereSolution(distanceList, profitList, limit, sourceStationIndex):

	maxProfit = 0
	stationPath = []
	if sourceStationIndex == len(distanceList):
		return profitList[len(distanceList)-1]
		
	midPoint = len(distanceList)/2
	#print "Orta Nokta : "+str(midPoint)
	
	return maxProfit, stationPath

