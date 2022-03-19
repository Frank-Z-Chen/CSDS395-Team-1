import numpy as np
import cv2


src = cv2.imread("test.png")
temp = src.copy()
h, w = src.shape[:2]
mask = np.zeros([h+2,w+2], np.uint8)
cv2.floodFill(temp, mask, (0,10), (0, 0, 0), (100, 100, 100), (50,50,50), cv2.FLOODFILL_FIXED_RANGE)
cv2.floodFill(temp, mask, (0,15), (255, 255, 255), (100, 100, 100), (50,50,50), cv2.FLOODFILL_FIXED_RANGE)
cv2.floodFill(temp, mask, (30,30), (255, 255, 255), (100, 100, 100), (50,50,50), cv2.FLOODFILL_FIXED_RANGE)
cv2.floodFill(temp, mask, (40,40), (255, 255, 255), (100, 100, 100), (50,50,50), cv2.FLOODFILL_FIXED_RANGE)
cv2.floodFill(temp, mask, (170,50), (255, 255, 255), (100, 100, 100), (50,50,50), cv2.FLOODFILL_FIXED_RANGE)
cv2.imwrite("temp.png",temp)