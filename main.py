import matplotlib.pylab as plt
import seaborn as sns

iris = sns.load_dataset("iris")
iris.describe()

plt.boxplot(iris["sepal_length"], data="iris")
plt.show()
