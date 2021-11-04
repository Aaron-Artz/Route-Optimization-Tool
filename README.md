# Route-Optimization-Tool

Algorithm Overview:

The greedy algorithm has been implemented in through the following steps:

The method takes in a list of packages, a current location, and a truck ID number.
The method then checks the distance between each location in the list and the current location.
When a new lowest distance is found it updates the lowest package to that location.
After it iterates through all locations, the lowest package is then appended to a new sorted list, and removed from the input list
The method then calls itself again using the list with the removed previous location, and continues to do so until all locations are added to the sorted list.


The complexity of this algorithm has a worst case runtime of O(n^2). The only factor that could improve this runtime is manually sorting the packages prior to adding them to the input list, since that is unrealistic we assume the worst case runtime will be the most common case. 

For further details please read the Core Algorithm Overview PDF in this repository where I justify the algorithm and data structures used. In the PDF I go over how the algorithm works in pseudo code as well as the complexity of each method in the project. 
