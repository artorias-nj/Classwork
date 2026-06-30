import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report
import time
from memory_profiler import memory_usage
from sklearn import metrics
import seaborn as sns
def train_model(model,X_train,y_train):
  start = time.time()
  model.fit(X_train,y_train)
  end = time.time()
  return model, (end-start)

def test_model(model, X_test):
  start = time.time()
  pred=model.predict(X_test)
  end = time.time()
  return pred, (end-start)


#try gaussian for both data sets
#import and assign wine
from sklearn import datasets
wine = datasets.load_wine()
from sklearn.model_selection import train_test_split

#split data
X_train, X_test, y_train, y_test = train_test_split(
wine.data, wine.target, test_size=0.25, random_state=42)

#import gaussian and train the model, measure memory and time usage
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
wg_train_mem_usage, (model, wg_train_time) = memory_usage((train_model, (model, X_train, y_train)),retval=True)

#test the gaussian model, measure memory and time usage
wg_test_mem_usage, (predictions, wg_test_time) = memory_usage((test_model, (model,X_test)),retval=True)

#print results
print("Wine Gaussian:")
print("Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))
print("Training took "+ str(wg_train_time) + " seconds")
print("Training used "+str(max(wg_train_mem_usage))+" MiB")
print("Predicting took "+ str(wg_test_time) + " seconds")
print("Predicting used "+str(max(wg_test_mem_usage))+" MiB")
print("")
fig, ax = plt.subplots(1, 1, figsize=(6, 6))
cm = metrics.confusion_matrix(y_test, predictions)
ax = sns.heatmap(cm, annot=True, square=True,
                      xticklabels=["Class 0", "Class 1", "Class 2"],
                      yticklabels=["Class 0", "Class 1", "Class 2"])
ax.set_xlabel('Predicted')
ax.set_ylabel('Actual');
ax.set_title('Wine Gaussian Confusion Matrix')
plt.show()
print("")

#import and assign cancer
cancer = datasets.load_breast_cancer()

#split data
X_train, X_test, y_train, y_test = train_test_split(
cancer.data, cancer.target, test_size=0.25, random_state=42)

#train the model, measure memory and time usage
model = GaussianNB()
cg_train_mem_usage, (model, cg_train_time) = memory_usage((train_model, (model, X_train, y_train)),retval=True)

#test the gaussian model, measure memory and time usage
cg_test_mem_usage, (predictions, cg_test_time) = memory_usage((test_model, (model,X_test)),retval=True)

#print results
print("Cancer Gaussian:")
print("Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))
print("Training took "+ str(cg_train_time) + " seconds")
print("Training used "+str(max(cg_train_mem_usage))+" MiB")
print("Predicting took "+ str(cg_test_time) + " seconds")
print("Predicting used "+str(max(cg_test_mem_usage))+" MiB")
print("")
fig, ax = plt.subplots(1, 1, figsize=(6, 6))
cm = metrics.confusion_matrix(y_test, predictions)
ax = sns.heatmap(cm, annot=True, square=True,
                      xticklabels=["Positive", "Negative"],
                      yticklabels=["Positive", "Negative"])
ax.set_xlabel('Predicted')
ax.set_ylabel('Actual');
ax.set_title('Cancer Gaussian Confusion Matrix')
plt.show()
print("")

#try KNC for both data sets
#split data
X_train, X_test, y_train, y_test = train_test_split(
wine.data, wine.target, test_size=0.25, random_state=42)

#import and KNC and train the model, measure memory and time usage
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)
wknc_train_mem_usage, (model, wknc_train_time) = memory_usage((train_model, (model, X_train, y_train)),retval=True)

#test KNC, measure memory and time usage
wknc_test_mem_usage, (predictions, wknc_test_time) = memory_usage((test_model, (model,X_test)),retval=True)

#print results
print("Wine KNeighborsClassifier:")
print("Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))
print("Training took "+ str(wknc_train_time) + " seconds")
print("Training used "+str(max(wknc_train_mem_usage))+" MiB")
print("Predicting took "+ str(wknc_test_time) + " seconds")
print("Predicting used "+str(max(wknc_test_mem_usage))+" MiB")
print("")
fig, ax = plt.subplots(1, 1, figsize=(6, 6))
cm = metrics.confusion_matrix(y_test, predictions)
ax = sns.heatmap(cm, annot=True, square=True,
                      xticklabels=["Class 0", "Class 1", "Class 2"],
                      yticklabels=["Class 0", "Class 1", "Class 2"])
ax.set_xlabel('Predicted')
ax.set_ylabel('Actual');
ax.set_title('Wine KNeighborsClassifier Confusion Matrix')
plt.show()
print("")

#split data
X_train, X_test, y_train, y_test = train_test_split(
cancer.data, cancer.target, test_size=0.25, random_state=42)

#train the model, measure memory and time usage
model = KNeighborsClassifier(n_neighbors=3)
cknc_train_mem_usage, (model, cknc_train_time) = memory_usage((train_model, (model, X_train, y_train)),retval=True)

#test the model, measure memory and time usage
cknc_test_mem_usage, (predictions, cknc_test_time) = memory_usage((test_model, (model,X_test)),retval=True)

#print results
print("Cancer KNeighborsClassifier:")
print("Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))
print("Training took "+ str(cknc_train_time) + " seconds")
print("Training used "+str(max(cknc_train_mem_usage))+" MiB")
print("Predicting took "+ str(cknc_test_time) + " seconds")
print("Predicting used "+str(max(cknc_test_mem_usage))+" MiB")
print("")
fig, ax = plt.subplots(1, 1, figsize=(6, 6))
cm = metrics.confusion_matrix(y_test, predictions)
ax = sns.heatmap(cm, annot=True, square=True,
                      xticklabels=["Positive", "Negative"],
                      yticklabels=["Positive", "Negative"])
ax.set_xlabel('Predicted')
ax.set_ylabel('Actual');
ax.set_title('Cancer Gaussian Confusion Matrix')
plt.show()
print("")

plt.figure(figsize=(6, 6))
models = ["Wine G ", "Cancer G ", "Wine KNC ", "Cancer KNC "]
accuracies = [1.0, 0.958, 0.755, 0.93]
times = [wg_train_time, cg_train_time, wknc_train_time, cknc_train_time]
plt.bar(models, accuracies)
plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy")
plt.show()