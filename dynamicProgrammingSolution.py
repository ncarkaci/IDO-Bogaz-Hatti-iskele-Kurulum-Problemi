#!/usr/bin/env python
#-*-coding:utf-8-*--

import timeit
import random
import pprint


def dynamicProgrammingSolution(distanceList, profitList, limit, sourceStationIndex):

    # initialize variables
    profitTable = []
    pathTable   = []
    stationList = []
    
    # fill result table with profit values
    for index in range(0,len(profitList)):
        pathTable.insert(index, 0)
        profitTable.insert(index,0)
    
    
    for currentNode in range(0,len(distanceList)):
         
        for previousNode in range(currentNode,-1,-1): # decreasing range
            
            if((distanceList[currentNode]-distanceList[previousNode]) > limit):

                if ( (profitTable[previousNode]+profitList[currentNode]) > profitTable[currentNode]):
					
					# update profit value
                    profitTable[currentNode] = profitTable[previousNode]+profitList[currentNode]
                    
                    # update station path  
                    if (profitTable[previousNode] != 0):
                        pathTable[currentNode] = previousNode
                    else :
                        pathTable[currentNode] = 0
                        
    # find max profit value
    maxProfit = max(profitTable)
     
    # find station list from pathTable 
    stationIndex = profitTable.index(max(profitTable))
    while(stationIndex!=0):
		stationList.insert(0,stationIndex)
        # next station index
		stationIndex = pathTable[stationIndex]
	
    return maxProfit, stationList
    
