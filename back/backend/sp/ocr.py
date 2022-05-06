import easyocr
import pandas as pd
import os
import sys
import util

name = sys.argv[1]
pwd = util.sp_address_extension(os.getcwd()) 

os.environ['KMP_DUPLICATE_LIB_OK']='True'

reader = easyocr.Reader(['en'])
result = reader.readtext(name)
ofile = pwd + '/roughdata/' + name.split("/")[-1].split(".")[0] + '_rough.csv'

ind = range(0,len(result))
df = pd.DataFrame(index=ind,columns=['TLX','TLY','BLX','BLY','BRX','BRY','TRX','TRY','content','p','as_cat','chunk','cat'])
for i in ind:
    df.iloc[i,0] = result[i][0][0][0]
    df.iloc[i,1] = result[i][0][0][1]
    df.iloc[i,2] = result[i][0][1][0]
    df.iloc[i,3] = result[i][0][1][1]
    df.iloc[i,4] = result[i][0][2][0]
    df.iloc[i,5] = result[i][0][2][1]
    df.iloc[i,6] = result[i][0][3][0]
    df.iloc[i,7] = result[i][0][3][1]
    df.iloc[i,8] = result[i][1]
    df.iloc[i,9] = result[i][2]
    df.iloc[i,10] = True
    df.iloc[i,11] = i
    df.iloc[i,12] = result[i][1]
    

df.to_csv(ofile,index=False,sep=',')

