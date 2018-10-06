### Intro To Machine Learning
My solutions of the tasks from the book: Miroslav Kubat *An Introduction to Machine Learning*.
#### 1.1 Hill climbing for sliding-tile.
Starting from some random initial state of a sliding-tile trying to obtain a given final state using hill climbing algorithm.
The evaluation function is set to be the sum of distances of every number from its position in the final state calculated as
|x - x_final| + |y-y_final| for a single point.
#### 2.2 Using Bayes formula to calculate the class probabilities in a domain where all attributes are discrete.
For an object decribed by the given set of attributes, the program says what is its most probable class. The test values is data from *pies.csv* and an object described by the attributes from this domain. 
##### Data: *pies.csv*
The dataset for *pies* domain described in chapter 1 of the book.
#### 2.3 Bayes for continuous attributes.
##### Data: *example1.csv*
A set consists of six examples, each described by three continuous
attributes: *at1*, *at2*, *at3*, *class*. 
##### Data: *wines.csv* 
The dataset from http://archive.ics.uci.edu/ml/machine-learning-databases/wine/.
#### 3.1 Nearest neighbours
Simple classification using nearest neighbours method. Test are performed on 
the normalized data from *wines.csv*. The dependence between the efficiency
and number of nearest neighbours taken into account is plotted.

