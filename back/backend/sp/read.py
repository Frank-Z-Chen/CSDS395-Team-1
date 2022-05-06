import pandas as pd
import numpy as np
import os
import sys
from sklearn import svm
import joblib
import util

pwd = util.sp_address_extension(os.getcwd())
name = sys.argv[1]
cat = sys.argv[2]
ifile = pwd + '/data/' + name.split("/")[-1].split(".")[0] + '_rough.csv'
lfile = pwd + '/data/' + name.split("/")[-1].split(".")[0] + '_learn.csv'
ofile = pwd + '/roughdata/' + name.split("/")[-1].split(".")[0] + '_rough_opt.csv'

df = pd.read_csv(lfile)

ban = df[df.chunk == -1]
df = df[df.chunk != -1]

# chunk 排序
df = df.sort_values('chunk')
df = df[df.chunk != -1]
k = 0
m = df.iloc[0,11]
df.iloc[0,11] = 0
ind = range(1,len(df))

for i in ind:
    if df.iloc[i,11] == m :
        df.iloc[i,11] = k
    else:
        k = k + 1
        m = df.iloc[i,11]
        df.iloc[i,11]=k

# df = pd.concat([df,ban])
# df.to_csv(lfile,index=False,sep=',')

# 输出结果

ind = range(0,max(df['chunk'])+1)
of = pd.DataFrame(index=ind,columns=["ATT","CON"])

#preprocessing
df = df.replace('', np.nan)

for i in ind:
    tempatt = df[df.as_cat == True]
    tempatt = tempatt[tempatt.chunk == i]

    tempcon = df[df.as_cat == False]
    tempcon = tempcon[tempcon.chunk == i]
    con = None
    if tempcon.empty:
        tempcon = ''
    if tempatt.empty:
        tempatt = tempcon[tempcon.cat.notna()]
    if tempatt.iloc[0,10] == True:
        att = tempatt.iloc[0,8]
        if len(tempcon) > 0:
            con = tempcon.iloc[0,8]
            for j in range(1,len(tempcon)):
                con = con + " " + tempcon.iloc[j,8]   
        for j in range(1,len(tempatt)):
            att = att + " " + tempatt.iloc[j,8]
    else:
        att = tempatt.iloc[0,12]
        temp = df[df.chunk == i]
        con = temp.iloc[0,8]
        for j in range(1,len(temp)):
            con = con + " " + temp.iloc[j,8]  
    
    of.iloc[i,0] = att
    of.iloc[i,1] = con
of.to_csv(ofile,index=False,sep=',')

# 创建、更新模型
if (os.path.isfile(pwd + '/model/' + cat + '.pkl')):
    model = joblib.load(pwd + '/model/' + cat + '.pkl')
else:
    model = svm.SVC(kernel = 'poly', degree = 2)
    
learndf = np.array(df.iloc[:,0:8])
learnlab = np.array(df.iloc[:,11])
model.fit(learndf,learnlab)
joblib.dump(model, pwd + '/model/' + cat + '.pkl')