import numpy as np
import cv2
import os
import sys
import csv
import math
import util

pwd = util.sp_address_extension(os.getcwd()) 
name = sys.argv[1]
file = pwd +'/temp/' + name.split("/")[-1].split(".")[0] + '_temp.png'
src = cv2.imread(name)
temp = src.copy()
h, w = src.shape[:2]
mask = np.zeros([h+2,w+2], np.uint8)
rd = pwd + '/roughdata/' + name.split("/")[-1].split(".")[0] + '_rough.csv';

#open csv file
csvfile=open(rd)
i=5
while i>0:
    #generate random point
    p=(math.floor(np.random.random()*w), math.floor(np.random.random()*h))
    #check point position
    flag=False
    csvreader=csv.DictReader(csvfile)
    for row in csvreader:
        #tlx
        if p[0] > int(row['TLX']):
            #tly
            if p[1] > int(row['TLY']):
                #brx
                if p[0] < int(row['BRX']):
                    #bry
                    if p[1] < int(row['BRY']):
                        flag=True
                        break;
    if flag: continue
    #run floodfill
    cv2.floodFill(temp, mask, p, (0, 0, 0), (75, 75, 75), (50,50,50), cv2.FLOODFILL_FIXED_RANGE)
    i=i-1


# cv2.floodFill(temp, mask, (0,10), (0, 0, 0), (100, 100, 100), (50,50,50), cv2.FLOODFILL_FIXED_RANGE)
# cv2.floodFill(temp, mask, (0,15), (255, 255, 255), (100, 100, 100), (50,50,50), cv2.FLOODFILL_FIXED_RANGE)
# cv2.floodFill(temp, mask, (30,30), (255, 255, 255), (100, 100, 100), (50,50,50), cv2.FLOODFILL_FIXED_RANGE)
# cv2.floodFill(temp, mask, (40,40), (255, 255, 255), (100, 100, 100), (50,50,50), cv2.FLOODFILL_FIXED_RANGE)
# cv2.floodFill(temp, mask, (170,50), (255, 255, 255), (100, 100, 100), (50,50,50), cv2.FLOODFILL_FIXED_RANGE)
cv2.imwrite(file,temp)