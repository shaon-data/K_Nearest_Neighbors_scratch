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

### My Peseudo Code:
1. Distances = [] , 
	{declaring a homogenus list}
2. Loop: Distances.store( [ Euclidean_Distances = nd_train_points ~ nd_unlabeled_point , Label_of_nd_train_point ] ) 
	{
	Determining the eucledean distance between test_set single row and train_set rows and making pair with their train_set labels and storing the pair to the list,'Distances'. By repeating the same process, store all the pairs.
	Distances = { (distance,label),(distance,label),(distance,label),....,N }
	}

3. Distances = sort( Distances )
	{Sorting Distances by the first elements of the pairs or distance}
4. K_points_pairs =  Distances[ 1st pair , K ]
	{
	K_points = { x £ Distances | 1 <= x <= K }
	K_points = { 1st_distant_pair,2nd_distant_pair,....,Kth_distant_pair }
	}
5. K_labels = K_points_pairs[:][1]
	{
	Getting labels from the second elements of the pairs.}
	}
6. Occured_labels = Occurance(K_labels)
	{ Count the occurance of the labels, and store the pairs(label,occurance) to the list 'Occured_labels'. }
7. Occured_labels = sort( Occured_labels )
	{ Sort the label pairs of the list 'Occured_labels' in descending order and store in itself }
8. Result_label = Occured_labels[0]
	{ Take the first label pair or the most occured label pair which is the result. }
9. Result_confidence = Occured_labels[1] / k
	{ occurance number or second element of label pair / number of voting members }
![Eucledian Distance](https://github.com/ShaonMajumder/simple_K_Nearest_Neighbors/blob/master/pics/knn.png)
<p align="center">Euclidean Distance for 2D points</p>


## Uses

KNN is the best for its simplicity in implementation and fast uses in medium heavy dataset.
It can be scale up for big systems but not big as terabytes of data.
It works best when large number of (N)data sample points  and (n)features is present.
n*N >> K
The more samples the model has, the more properties the points have, more accurate the model will be.

### Pros
It directly test the similarities of new unlabelled data and give it a new label base on similarities.It directly test the similarities of new unlabelled data and give it a new label base on similarities.
It works best for non linear data.
So it is relatively fast for its implementation as it needs not any parametric thinking to set up importantce for features and it directly test the new samples so it doesn't need any training time.

### Cons
But KNN is not the best algorithm for classification.
It is a lazy learner which uses no direct learning or generalization from data.
It does not work parametricly , so you have no choice to set up on your hypothesis or understanding.
As it does not include any training, it is fast. so it gets more accurate when features is added and more data samples is added.


It is good for nonlinear data, when you don't know features importance , but just you want to know, which class, you
wabt too label new data which can be helpful for your next approach on dataset.
