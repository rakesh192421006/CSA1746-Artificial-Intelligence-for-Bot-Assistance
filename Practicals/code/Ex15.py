# Import libraries
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create Decision Tree classifier
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Sample predictions
samples = [[5.1,3.5,1.4,0.2], [6.7,3.0,5.2,2.3], [5.9,3.0,4.2,1.5]]
predictions = clf.predict(samples)

for i, sample in enumerate(samples):
    print(f"Sample {sample} => Predicted Class: {predictions[i]}")

