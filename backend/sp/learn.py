import numpy as np
from sklearn import svm
import pandas as pd
import os
import sys
from sklearn.externals import joblib
import util




pwd = util.sp_address_extension(os.getcwd()) 
name = sys.argv[1]
cat = sys.argv[2]
# d = pwd + '/data/' + name.split("/")[-1].split(".")[0] + '_learn.csv'
rd = pwd + '/roughdata/' + name.split("/")[-1].split(".")[0] + '_rough.csv'
model_path = pwd + '/model/' + cat + '.pkl'

model = joblib.load(model_path)


# df = pd.read_csv(d)
dt = pd.read_csv(rd)

# learndf = np.array(df.iloc[:,0:8])
# learnlab = np.array(df.iloc[:,11])

dtdf = np.array(dt.iloc[:,0:8])


# model = svm.SVC(kernel = 'poly', degree = 2)
# model.fit(learndf,learnlab)

predict = model.predict(dtdf)

dt.iloc[:,11] = predict

ind = range(1,len(dt))

for i in ind:
    if dt.iloc[i,11] == dt.iloc[i-1,11]:
        dt.iloc[i,10] = None
        dt.iloc[i,12] = None

dt.to_csv(rd,index=False,sep=',')
