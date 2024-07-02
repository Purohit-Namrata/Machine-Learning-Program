# summarize the data
from pandas import read_csv
from pandas import scatter_matrix
import matplotlib.pyplot as plt
# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)
# shape
print(dataset.shape)
# head
print(dataset.head(5))
# descriptions
print(dataset.describe())
# class distribution
print(dataset.groupby('class').size())


# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

...
# scatter plot matrix
scatter_matrix(dataset)
plt.show()
...
# histograms
dataset.hist()
plt.show()