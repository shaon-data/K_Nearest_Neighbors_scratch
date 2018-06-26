# simple_K_Nearest_Neighbors 
## Download 
For downloading use 
       `git clone https://github.com/ShaonMajumder/simple_K_Nearest_Neighbors.git` 
## Explanations
### My own high-level summarization in short....
KNN is the algorithm where an unlabeled n-dimensional or n-featural
 point gets a class label of the class of the nearest euclidean
 distance from the nearest K distances between that point and sample training n-dimensional
 points.

KNN is lazy learner but works best when large number of (N)training points and (n)features is present.

K = 2x+1 and K <= N ; N = number of training points ; n = dimension ; K = the number of best neighbors.

### My Model Measurements:

1. Determine the eucledean distance between train_set rows and test_set single row. Repeat the same for all test_set rows 
and get distances.
![Eucledian Distance](https://github.com/ShaonMajumder/simple_K_Nearest_Neighbors/blob/master/pics/knn.png)
<p align="center">Euclidean Distance for 2D points</p>

2. Store the distances, with their respective label in pairs ( [distance,label] )
3. Rearrange the pairs in ascending order by their distances
4. Take the first k numbers pairs and check the most appeared label in pairs. That is the Resultant label or class.
