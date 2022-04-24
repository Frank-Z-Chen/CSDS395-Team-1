import numpy as np
import pandas as pd
import cv2
import os
import sys
import util

pwd = util.sp_address_extension(os.getcwd())
name = sys.argv[1]
ref = sys.argv[2]
file = pwd +'/temp/' + name
opt = pwd +'/temp/' + name.split("/")[-1].split(".")[0] + '_temp_mark.png'
src = cv2.imread(name)
temp = src.copy()
h, w = src.shape[:2]
mask = np.zeros([h+2,w+2], np.uint8)
rd = pwd + ref

df = pd.read_csv(rd)
ind = range(0,max(df['chunk'])+1)
for i in ind:
    rec = df[df['chunk'] == i]
    x1 = min(rec.TLX)
    y1 = min(rec.TLY)
    x2 = max(rec.BRX)
    y2 = max(rec.BRY)
    for j in range(x1, x2+1):
        temp[y1,j] = [0, 0, 255]
        temp[y1 + 1,j] = [0, 0, 255]
        temp[y1 + 2,j] = [0, 0, 255]
        
        temp[y2,j] = [0, 0, 255]
        temp[y2 - 1,j] = [0, 0, 255]
        temp[y2 - 2,j] = [0, 0, 255]
        
    for j in range(y1, y2+1):
        temp[j,x1] = [0, 0, 255]
        temp[j,x1 + 1] = [0, 0, 255]
        temp[j,x1 + 2] = [0, 0, 255]
        temp[j,x2] = [0, 0, 255]
        temp[j,x2 - 1] = [0, 0, 255]
        temp[j,x2 - 2] = [0, 0, 255]
    
cv2.imwrite(opt,temp)
