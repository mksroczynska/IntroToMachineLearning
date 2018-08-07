# Intro To Machine Learning
My solutions of the tasks in the book: Miroslav Kubat *An Introduction to Machine Learning*.
## 1.1 Hill climbing for sliding-tile.
Starting from some random initial state of a sliding-tile trying to obtain a given final state using hill climbing algorithm.
The evaluation function is set to be the sum of distances of every number from its position in the final state calculated as
|x - x_final| + |y-y_final| for a single point.
## Data: *pies* domain.
The dataset described in the book is in pies.csv file.
## 2.2 Using Bayes formula to calculate the class probabilities in a domain where all attributes are discrete.
For an object decribed by the given set of attributes, the program says what is its most probable class. The test values is data from *pies.csv* and an object described by the attributes from this domain. 
