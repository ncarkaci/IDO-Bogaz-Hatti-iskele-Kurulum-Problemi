#!/usr/bin/env python
#-*-coding:utf-8-*--

import timeit
import random
import pprint
from greedySolution import *


def upperBound(distanceList, profitList, limit, sourceStationIndex):
    
    #initialize variables
    upperBoundVal = 0
    
    for node in range(sourceStationIndex,len(distanceList)):

        upperBoundVal = upperBoundVal + profitList[node] 
        
    return upperBoundVal

def branchAndBoundSolution(distanceList, profitList, limit, rootStationIndex):
 
    # initialize variables
    bestSolution        = 0   
    upperBoundVal       = 0
    bestStationList     = []


    # our best initial solution will be the greedy solution
    bestSolution, bestStationList = greedySolution(distanceList, profitList, limit, rootStationIndex)

    # for first visit list go to n item 
    for currentStationIndex in range(rootStationIndex+1, len(distanceList)): 
        
        # initialize current profit and station in every step
        newProfit          = 0
        newStationList     = []
        
        # feasibility check             
        if ((distanceList[currentStationIndex]-distanceList[rootStationIndex]) > limit ):                
            
            upperBoundVal   = upperBound(distanceList, profitList, limit, currentStationIndex)
            if (upperBoundVal > bestSolution) :
                
                
                # call function for new sub list which root station is currentStationIndex
                subProfitValue, subStationList = branchAndBoundSolution(distanceList, profitList, limit, currentStationIndex) 
                
                # calculate new profit and new station list from sub routine
                newProfit      = profitList[currentStationIndex]+subProfitValue
                newStationList.append(currentStationIndex)
                newStationList = newStationList+subStationList
    
                # check new profit and update max profit and station list
                if (newProfit > bestSolution):
                    
                    bestSolution    = newProfit
                    bestStationList     = newStationList
            
            #else:
             #   print "pruning because of bounding"
        #else:
         #   print "pruning because of feasibility"                                    
    return bestSolution , bestStationList

    
   
