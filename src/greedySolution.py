#!/usr/bin/env python
#-*-coding:utf-8-*--

import timeit
import random

def greedySolution(distanceList, profitList, limit, sourceStationIndex):
    
    #initialize variables
    stationIndexList    = []
    stationSolution     = []
    maxProfitSolution   = 0
    
    
    # Timsort worstcase θ(nlogn), avarage case θ(nlogn), bestcase θ(n)
    sortedProfitList = sorted(profitList, reverse=True)
    
    # find and create station index list after sorting
    for station in sortedProfitList:
        stationIndexList.append(profitList.index(station))
    
    # all profit from 1 to n
    for stationIndex in stationIndexList:
        
        # feasibility check
        if ((distanceList[stationIndex]- distanceList[sourceStationIndex]) > limit):
            
            # is a feasibe add to solution set
            stationSolution.append(stationIndex)
            maxProfitSolution = maxProfitSolution+profitList[stationIndex]
            
            sourceStationIndex = stationIndex
            
    
    return maxProfitSolution, stationSolution
    
