import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
#from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import pickle

data = pd.read_csv("job.csv")
print(data)

features = data[["Exp","Education","salary expectation"]]
target = data["job"]

#handleling categorical data
nfeatures = pd.get_dummies(features)
print(nfeatures)


#train and test
x_train, x_test, y_train, y_test = train_test_split(nfeatures, target,random_state=3)

model = RandomForestClassifier()
model.fit(x_train,y_train)

print("train score is ",model.score(x_train, y_train))
print("test score is ", model.score(x_test, y_test))

cr = classification_report(y_test,model.predict(x_test))
print(cr)

f = open("JOB.model", "wb")
pickle.dump(model, f)
f.close()


'''exp = float(input("enter years of experience u have :"))
sal = float(input("enter your salary expectation per anum (eg:200000)"))
edu = int(input("type 1 for BE , 2 for bsc and 3 for ME :"))
if edu == 1:
       d = [[exp,sal,1,0,0]]
elif edu == 2:
       d = [[exp,sal,0,0,1]]
else:
       d = [[exp,sal,0,1,0]]


job = model.predict(d)
print(job)'''