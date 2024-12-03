# Loading the libraries needed for this analysis
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Loading the Iris dataset
dataSet = pd.read_csv("DataSets/IRIS.csv")
print(dataSet)

# 1a.Calculating the mean of the sepal length, sepal width, petal length, petal width
Mean_Of_sepal_length = dataSet["sepal_length"].mean().round(1)
print("The mean of sepal length is:", Mean_Of_sepal_length)
Mean_Of_sepal_width = dataSet["sepal_width"].mean().round(1)
print("The mean of sepal width is:", Mean_Of_sepal_width)
Mean_Of_petal_length = dataSet["petal_length"].mean().round(1)
print("The mean of petal_length is:", Mean_Of_petal_length)
Mean_Of_petal_width = dataSet["petal_width"].mean().round(1)
print("The mean of the petal_width is:", Mean_Of_petal_width)

# 1b.Calculating the median of the sepal length, sepal width, petal length, petal width
Median_Of_sepal_length = dataSet["sepal_length"].median().round(1)
print("The median of sepal length is:", Median_Of_sepal_length)
Median_Of_sepal_width = dataSet["sepal_width"].median().round(1)
print("The median of sepal width is:", Median_Of_sepal_width)
Median_Of_petal_length = dataSet["petal_length"].median().round(1)
print("The median of petal length is:", Median_Of_petal_length)
Median_Of_petal_width = dataSet["petal_width"].median().round(1)
print("The median of petal width is:", Median_Of_petal_width)

# 1c.Calculating the standard deviation of the sepal length, sepal width, petal length, petal width
Standard_deviation_of_sepal_length = dataSet["sepal_length"].std().round(1)
print("The standard deviation of the sepal length is:", Standard_deviation_of_sepal_length)
Standard_deviation_of_sepal_width = dataSet["sepal_width"].std().round(1)
print("The standard deviation of the sepal width is:", Standard_deviation_of_sepal_width)
Standard_deviation_of_petal_length = (dataSet["petal_length"].std().round(1))
print("The standard deviation of the petal lengths is:", Standard_deviation_of_petal_length)
Standard_deviation_of_petal_width = dataSet["petal_width"].std().round(1)
print("The standard deviation of the petal width is:", Standard_deviation_of_petal_width)

# 2.Calculating the number of samples which belong to each species (Setosa, Versicolor, Virginica)
Total_Number_Of_species = dataSet["species"].count()
print("The total number of sample species is:", Total_Number_Of_species)
Number_Of_Iris_setosa = dataSet[dataSet["species"] == "Iris-setosa"].shape[0]
print("The total number of Iris-setosa is:", Number_Of_Iris_setosa)
Number_Of_Iris_versicolor = dataSet[dataSet["species"] == "Iris-versicolor"].shape[0]
print("The total number of Iris- versicolor is:", Number_Of_Iris_versicolor)
Number_Of_Iris_virginica = dataSet[dataSet["species"] == "Iris-virginica"].shape[0]
print("The total number of Iris-virginica is:", Number_Of_Iris_virginica)

# 3.How the sepal length and petal length compare across the three species
group = dataSet.groupby("species")
Mean = group[["sepal_length", "petal_length"]].mean().round(1)
print(Mean)

# 4.The relationship between sepal width and petal width
rsepal_width = dataSet[dataSet["species"] == "Iris-setosa"]
x_setosa = rsepal_width["sepal_width"]
y_setosa = rsepal_width["petal_width"]

# For Iris-virginica
rsepal1 = dataSet[dataSet["species"] == "Iris-virginica"]
x_virginica = rsepal1["sepal_width"]
y_virginica = rsepal1["petal_width"]

# For Iris-versicolor
rsepal2 = dataSet[dataSet["species"] == "Iris-versicolor"]
x_versicolor = rsepal2["sepal_width"]
y_versicolor = rsepal2["petal_width"]

plt.plot(x_setosa, y_setosa, 'go', label="Iris-setosa")
plt.plot(x_virginica, y_virginica, 'bo', label="Iris-virginica")
plt.plot(x_versicolor, y_versicolor, 'ro', label="Iris-versicolor")
plt.xlabel("Sepal Width in cm")
plt.ylabel("Petal Width in cm")
plt.title("Comparison of Sepal and Petal Widths by Species")
plt.legend()
plt.show()


