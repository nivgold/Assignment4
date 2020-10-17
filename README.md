# World-Happiness-Clustering

## Summary

The World Happiness Clustering project clusters the world's countries by their happiness levels.
With a GUI that was build with the TKInter python's package, the user can browse the file path, select the numer of the clusters and select the number of the 'runs' of the clusering algorithm.

:round_pushpin: The file that is selected **MUST** be the dataset from the [World Happiness Report 2019](https://worldhappiness.report/ed/2019/)

The clustering algorithm that was used in the project is [k-means](https://en.wikipedia.org/wiki/K-means_clustering). The implementation of the KMeans algorithm was taken from the [scikit learn](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html) package

## Usage

clone the repository to your local machine. make sure you got:
 - [ ] [matplotlib](https://matplotlib.org/)
 - [ ] [plotly](https://plotly.com/)
 - [ ] [chart-studio](https://plotly.com/python/)
 - [ ] [pandas](https://pandas.pydata.org/)
 - [ ] [xlrd](http://www.python-excel.org/) >= 1.0.0
 
 And start GUI.py!
 
 ###### The gui that is opened open will show the screen:
 
 ![alt text](https://res.cloudinary.com/dxeniml9z/image/upload/v1602933606/py_main_jraomz.png "Main Screen")
 
  ###### Then, provide the path for the World Happiness Report 2019 dataset, select number of clustering and number of runs.
 
 ![alt text](https://res.cloudinary.com/dxeniml9z/image/upload/v1602933605/py_select_settings_pf5a6y.png "Select Settings")
 
 ###### Press Pre-process and wait until preprocessing is done:
 
 ![alt text](https://res.cloudinary.com/dxeniml9z/image/upload/v1602933602/py_preprocessing_complete_nfai3u.png "Preprocessing")
 
 ###### After preprocessing is done, you can select the Cluster Button and wait until the k-means algorithm is done:
 
 ![alt text](https://res.cloudinary.com/dxeniml9z/image/upload/v1602933602/py_clustering_complete_lihtwz.png "Clustering")
 
 ###### For the visualization of the results, there is a map that says for each country what cluster she belongs to and a scatter graph between the 'Generosity' and the 'social_support' features
 
 ![alt text](https://res.cloudinary.com/dxeniml9z/image/upload/v1602933602/py_end_screen_nwhpof.png "End Screen")
