import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
import seaborn as sn
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from mlwpy import *
# %matplotlib inline
from tkinter import messagebox
from tkinter import *

def Linear_Regression(X_train, X_test, y_train, y_test,c):
    model_LinearRegression=LinearRegression()

    model_LinearRegression.fit(X_train, y_train)

    model_LinearRegression.score(X_test, y_test)

    y_predicted = model_LinearRegression.predict(X_test)
    mse = mean_squared_error(y_test, y_predicted)
    rmse = np.sqrt(mse)
    r_squared = r2_score(y_test, y_predicted)
    if c==0:
        result_message =(
        f"Mean Squared Error: {mse}\n"
        f"Root Mean Squared Error: {rmse}\n"
        f"R-squared Score: {r_squared}")
        popup("Linear Regression:", result_message)
    elif c==1:
        return r_squared

def Random_Forest_Regressor(X_train, X_test, y_train, y_test,c):
    model_RandomForestRegressor = RandomForestRegressor(n_estimators=100)
    model_RandomForestRegressor.fit(X_train, y_train)

    model_RandomForestRegressor.score(X_test, y_test)

    y_predicted = model_RandomForestRegressor.predict(X_test)
    mse = mean_squared_error(y_test, y_predicted)
    rmse = np.sqrt(mse)
    r_squared = r2_score(y_test, y_predicted)
    if c==0:
        result_message =(
        f"Mean Squared Error: {mse}\n"
        f"Root Mean Squared Error: {rmse}\n"
        f"R-squared Score: {r_squared}")
        popup("Random Forest Regressor:", result_message)
    elif c==1:
        return r_squared

def Gradient_Boosting_Regressor(X_train, X_test, y_train, y_test,c):
    model_GradientBoostingRegressor=GradientBoostingRegressor()
    model_GradientBoostingRegressor.fit(X_train, y_train)

    model_GradientBoostingRegressor.score(X_test, y_test)

    y_predicted = model_GradientBoostingRegressor.predict(X_test)
    mse = mean_squared_error(y_test, y_predicted)
    rmse = np.sqrt(mse)
    r_squared = r2_score(y_test, y_predicted)
    if c==0:
        result_message =(
        f"Mean Squared Error: {mse}\n"
        f"Root Mean Squared Error: {rmse}\n"
        f"R-squared Score: {r_squared}")
        popup("Gradient Boosting Regressor:", result_message)
    elif c==1:
        return r_squared

def Logistic_Regression(X_train, X_test, y_train, y_test,c):
    model_LogisticRegression=LogisticRegression()
    model_LogisticRegression.fit(X_train, y_train)

    model_LogisticRegression.score(X_test, y_test)

    y_predicted = model_LogisticRegression.predict(X_test)
    accuracy = accuracy_score(y_test, y_predicted)
    precision = precision_score(y_test, y_predicted, average='macro')
    recall = recall_score(y_test, y_predicted, average='macro')
    f1 = f1_score(y_test, y_predicted, average='macro')
    if c==0:
        result_message=(
        f"Accuracy: {accuracy:.3f}\n"
        f"Precision: {precision:.3f}\n"
        f"Recall: {recall:.3f}\n"
        f"F1 Score: {f1:.3f}")
        popup("Logistic Regression:", result_message)
        cm = confusion_matrix(y_test, y_predicted)
        plt.figure(figsize=(10,7))
        sn.heatmap(cm, annot=True, cmap="Reds")
        plt.title("Logistic Regression")
        plt.xlabel('Predicted')
        plt.ylabel('Truth')
        plt.show()
    elif c==1:
        return accuracy

def Random_Forest_Classifier(X_train, X_test, y_train, y_test,c):
    model_RandomForestClassifier=RandomForestClassifier(n_estimators=200)
    model_RandomForestClassifier.fit(X_train, y_train)

    model_RandomForestClassifier.score(X_test, y_test)

    y_predicted = model_RandomForestClassifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_predicted)
    precision = precision_score(y_test, y_predicted, average='macro')
    recall = recall_score(y_test, y_predicted, average='macro')
    f1 = f1_score(y_test, y_predicted, average='macro')
    if c==0:
        result_message=(
        f"Accuracy: {accuracy:.3f}\n"
        f"Precision: {precision:.3f}\n"
        f"Recall: {recall:.3f}\n"
        f"F1 Score: {f1:.3f}")
        popup("Random Forest Classifier:", result_message)
        cm = confusion_matrix(y_test, y_predicted)
        plt.figure(figsize=(10,7))
        sn.heatmap(cm, annot=True, cmap="Greens")
        plt.title("Random Forest Classifier")
        plt.xlabel('Predicted')
        plt.ylabel('Truth')
        plt.show()
    elif c==1:
        return accuracy

def S_V_C(X_train, X_test, y_train, y_test,c):
    model_SVC=SVC(C=10)
    model_SVC.fit(X_train, y_train)

    model_SVC.score(X_test, y_test)

    y_predicted = model_SVC.predict(X_test)
    accuracy = accuracy_score(y_test, y_predicted)
    precision = precision_score(y_test, y_predicted, average='macro')
    recall = recall_score(y_test, y_predicted, average='macro')
    f1 = f1_score(y_test, y_predicted, average='macro')
    if c==0:
        result_message=(
        f"Accuracy: {accuracy:.3f}\n"
        f"Precision: {precision:.3f}\n"
        f"Recall: {recall:.3f}\n"
        f"F1 Score: {f1:.3f}")
        popup("SVC:", result_message)
        cm = confusion_matrix(y_test, y_predicted)
        plt.figure(figsize=(10,7))
        sn.heatmap(cm, annot=True, cmap="Blues")
        plt.title("SVC")
        plt.xlabel('Predicted')
        plt.ylabel('Truth')
        plt.show()
    elif c==1:
        return accuracy

def compare(X_train, X_test, y_train, y_test,X_train2, X_test2, y_train2, y_test2):
    alr=Linear_Regression(X_train, X_test, y_train, y_test,1)
    arfr=Random_Forest_Regressor(X_train, X_test, y_train, y_test,1)
    agbr=Gradient_Boosting_Regressor(X_train, X_test, y_train, y_test,1)
    alrc=Logistic_Regression(X_train2, X_test2, y_train2, y_test2,1)
    arfc=Random_Forest_Classifier(X_train2, X_test2, y_train2, y_test2,1)
    asvc=S_V_C(X_train2, X_test2, y_train2, y_test2,1)
    plt.figure(figsize=(20, 20))
    models = ["Linear Regression ", "Random Forest Regressor ", "Gradient Boosting_Regressor ", "Logistic Regression ", "Random Forest Classifier ","SVC"]
    accuracies = [alr, arfr, agbr, alrc, arfc, asvc]
    plt.bar(models, accuracies)
    plt.title("Model Accuracy Comparison")
    plt.ylabel("Accuracy")
    plt.show()

def popup(title, message):
    win = Toplevel()
    win.title(title)
    win.minsize(300, 100)
    Label(win, text=message, padx=20, pady=20, anchor="center", justify="left").pack()
    Button(win, text="Close", command=win.destroy).pack(pady=10)
    win.update_idletasks()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

df = pd.read_csv(resource_path("ames_selected.csv"))
df = df.dropna()
df = pd.get_dummies(df, columns=['KitchenQual', 'Neighborhood', 'GarageFinish', 'ExterQual'])
X = df.drop('SalePrice', axis='columns')
y = df["SalePrice"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
labels = ['Low-priced', 'Mid-priced', 'High-priced']
y = pd.qcut(y, q=3, labels=labels)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X, y, test_size=0.2)

root=Tk()
root.title("Machine Learning")
root.geometry("550x300")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

button_font = ("Arial", 12)
button_padx = 20
button_pady = 10

e1L=Label(root, text="Regression Models",font=("Arial", 14))
e1L.grid(row=0, column=0,pady=10)

e2L=Label(root, text="Classification Models",font=("Arial", 14))
e2L.grid(row=0, column=1,pady=10)

create_button = Button(root, font=button_font, padx=button_padx, pady=button_pady, text="Linear Regression",
                       command=lambda: Linear_Regression(X_train, X_test, y_train, y_test, 0))
create_button.grid(row=1, column=0, sticky="we")

create_button = Button(root, font=button_font, padx=button_padx, pady=button_pady, text="Random Forest Regressor",
                       command=lambda: Random_Forest_Regressor(X_train, X_test, y_train, y_test, 0))
create_button.grid(row=2, column=0, sticky="we")

create_button = Button(root, font=button_font, padx=button_padx, pady=button_pady, text="Gradient Boosting Regressor",
                       command=lambda: Gradient_Boosting_Regressor(X_train, X_test, y_train, y_test, 0))
create_button.grid(row=3, column=0, sticky="we")

create_button = Button(root, font=button_font, padx=button_padx, pady=button_pady, text="Logistic Regression",
                       command=lambda: Logistic_Regression(X_train2, X_test2, y_train2, y_test2, 0))
create_button.grid(row=1, column=1, sticky="we")

create_button = Button(root, font=button_font, padx=button_padx, pady=button_pady, text="Random Forest Classifier",
                       command=lambda: Random_Forest_Classifier(X_train2, X_test2, y_train2, y_test2, 0))
create_button.grid(row=2, column=1, sticky="we")

create_button = Button(root, font=button_font, padx=button_padx, pady=button_pady, text="SVC",
                       command=lambda: S_V_C(X_train2, X_test2, y_train2, y_test2, 0))
create_button.grid(row=3, column=1, sticky="we")

create_button = Button(root, font=button_font, padx=button_padx, text="Compare all machine learning models",
                       command=lambda: compare(X_train, X_test, y_train, y_test, X_train2, X_test2, y_train2, y_test2))
create_button.grid(row=4, column=0, columnspan=2, sticky="we", pady=1)

root.mainloop()  