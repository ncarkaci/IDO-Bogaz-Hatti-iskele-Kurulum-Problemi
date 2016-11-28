#!/usr/bin/env python
#-*-coding:utf-8-*--

import random
from bruteForceSolution import *
from greedySolution import *
from dynamicProgrammingSolution import *
from divideAndConqureSolution import *
from branchAndBound import  *

    
limit = 100
size  = 10
distances = random.sample(range(1, 50000), 40)
distances.sort()
    
profits = random.sample(range(10, 50000), 40)

profits.insert(0,0)
distances.insert(0,0)
   
profit = 0
path = []
 
print "******* Dinamik Programlama *****"
start = timeit.default_timer()
profit, path = dynamicProgrammingSolution(distances, profits, limit,0)
stop = timeit.default_timer()
print  "Time : "+ str(stop - start) 





print "******* Greedy *******"
start = timeit.default_timer()
profit, path = greedySolution(distances, profits, limit,0)         
stop = timeit.default_timer()
print  "Time : "+ str(stop - start) 

print "**** Branch And Bound ****"
start = timeit.default_timer()
profit, path = branchAndBoundSolution(distances, profits, limit,0)         
stop = timeit.default_timer()
print  "Time : "+ str(stop - start) 

print "******* Brute Force *******"
start = timeit.default_timer()
profit, path = bruteForce(distances, profits, limit,0)        
stop = timeit.default_timer()
print  "Time : "+ str(stop - start) 


