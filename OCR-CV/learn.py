import numpy as np
from sklearn import svm
import pandas as pd

df = pd.read_csv('learn.csv')
dt = pd.read_csv('test.csv')

learndf = np.array(df.iloc[:,0:8])
learnlab = np.array(df.iloc[:,10])

dtdf = np.array(dt.iloc[:,0:8])



model = svm.SVC(kernel = 'poly', degree = 2)
model.fit(learndf,learnlab)

predict = model.predict(dtdf)

dt.iloc[:,10] = predict

dt.to_csv("test.csv",index=False,sep=',')