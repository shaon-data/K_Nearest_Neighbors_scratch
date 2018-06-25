import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')

##point1 = [1,3]
##point2 = [2,5]
##
##euclidean_distance = sqrt( (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 )
##print(euclidean_distance)

data = {'k':[[1,2],[2,3],[3,1]],'r':[[6,5],[7,7],[8,6]]}
predict = [5,7]

def euclidean_distance(data,predict):
    #euclidean_distance = sqrt( (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 ) for 2D
    return np.linalg.norm(np.array(data) - np.array(predict))

def k_nearest_neighbors(data,predict,k=3):
    if len(data) >= k:
        warnings.warn('K is set to a value less than total voting groups!')

    distances = []
    for group in data:
        for features in data[group]:
            print("group %s"%group)
            distances.append([euclidean_distance(features,predict), group])

    number_of_neighbors=k
    nearest_neighbors_to_k = sorted(distances)[:number_of_neighbors]
    votes = [i[1] for i in nearest_neighbors_to_k] #top k numbers distances
    votes_result = ( Counter(votes).most_common(1) )[0][0] #most_common(n) most appeared n numbers element among given top least distant k votes , [0][0] first of first element inside list inside tuple
    appeared_number = Counter(votes).most_common(1)[0][1]
    confidence = appeared_number/k
    
##    print(votes)
##    print(votes_result)
    
    return votes_result,confidence
    
result,confidence = k_nearest_neighbors(data,predict,k=3)

[[plt.scatter(ii[0],ii[1], s=100, color=i) for ii in data[i]] for i in data]
plt.scatter(predict[0],predict[1], color = result)
plt.title('KNN')
plt.show()
