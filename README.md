# simple_K_Nearest_Neighbors 
## Download 
For downloading use 
       `git clone https://github.com/ShaonMajumder/simple_K_Nearest_Neighbors.git` 
## Explanations
### My own high-level summarization in short....
KNN is the algorithm where an unlabelled n-dimensional or n-features
 point gets a class label of the class of the nearest Euclidean
 distance from the nearest K distances between that point and sample training n-dimensional
 points.

Where, K = 2x+1 and K <= N ; N = number of training points ; n = dimension ; K = the number of best neighbors.

Here, how distant the two points are , the more dissimilarties the points have.
So, the least distant or nearest the neighbor is, the most likely it is similar.
As every distance between the unlabeled point and the labeled training points has its label from the comparing labeled points,
so every distance has its own label or identity. We will use this property in a sense of voting mechanism for our advantage.

 1. First, we get the distances between the unlabled n-d point and labeled n-d points which denotes the magnitude of dissimilarities.
 2. We sort them in ascending order(low to high) and take the first K less distant points. 
 3. From the chosen K distances, we will count their labels and will nominate the most appeared label.
 4. The unlabeled point will be given the nominated label which is obviously of the most similar or less distant point.

Here is how our unlabeled n-d point will get its label and this is our solution.
KNN is lazy learner but works best when large number of (N)training points and (n)features is present.




### My Model Measurements:

1. Determine the eucledean distance between train_set rows and test_set single row. Repeat the same for all test_set rows 
and get distances.
![Eucledian Distance](https://github.com/ShaonMajumder/simple_K_Nearest_Neighbors/blob/master/pics/knn.png)
<p align="center">Euclidean Distance for 2D points</p>

2. Store the distances, with their respective label in pairs ( [distance,label] )
3. Rearrange the pairs in ascending order by their distances
4. Take the first k numbers pairs and check the most appeared label in pairs. That is the Resultant label or class.
