from BucketSortDone import kiwi_list
from time import time
 
kiwi_weight = kiwi_list['Weight(kg)'].copy()
 
#List is empty
def test_BucketWorst():
 start= time()
 assert len(kiwi_weight) != 0
 print(time()-start)
 
 #First value is the lowest and last value is the highest
def test_BucketBest():
 start= time()
 assert min(kiwi_weight) == 1.570
 assert max(kiwi_weight) == 4.143
 print(time()-start)
 
 #Checking if number of elements is correct
def test_BucketAvg():
 start= time()
 assert len(kiwi_weight) == 700
 print(time()-start)