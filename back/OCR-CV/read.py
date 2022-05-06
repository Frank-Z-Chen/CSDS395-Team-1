import pandas as pd

df = pd.read_csv('read.csv')
ban = df[df.chunk == -1]
df = df[df.chunk != -1]

k = 0
m = df.iloc[0,10]
df.iloc[0,10] = 0
ind = range(1,len(df))

for i in ind:
    if df.iloc[i,10] == m :
        df.iloc[i,10] = k;
    else:
        k = k + 1
        m = df.iloc[i,10]
        df.iloc[i,10]=k

# df = pd.concat([df,ban])
df.to_csv('learn.csv',index=False,sep=',')
        
ind = range(0,max(df['chunk'])+1)
of = pd.DataFrame(index=ind,columns=["ATT","CON"])

for i in ind:
    tempatt = df[(df.chunk == i) & ~(df.cat.isnull())]
    tempcon = df[(df.chunk == i) & (df.cat.isnull())]
    att = tempatt.iloc[0,8]
    if len(tempcon) > 0:
        con = tempcon.iloc[0,8]
        for j in range(1,len(tempcon)):
            con = con + " " + tempcon.iloc[j,8]
    
    for j in range(1,len(tempatt)):
        att = att + " " + tempatt.iloc[j,8]
    
    
    
    of.iloc[i,0] = att
    of.iloc[i,1] = con
    
of.to_csv("output.csv",index=False,sep=',')