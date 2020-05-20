# Standard imports
import cv2
import glob
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX

path = './data/*'
imagesPath = [img for img in glob.glob(path)]
# print( glob.glob(path)[0] in "jpg")
print(imagesPath)
images = []
images = list(map(lambda x: cv2.imread(x, cv2.IMREAD_GRAYSCALE),imagesPath))


kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
noSpaceKernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(4,4))


images = list(map(lambda x:cv2.erode(x,noSpaceKernel),images))
# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)


# gray_image = cv2.cvtColor(opening, cv2.COLOR_BGR2GRAY)
#
#
#
#
# #binary image
# _,thresh = cv2.threshold(gray_image,71,255,cv2.THRESH_BINARY_INV)
#
#
#
#
# #get contours
# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# height, width = gray_image.shape
# min_x, min_y  = width, height
# max_x = max_y = 0
#
#
# # computes the bounding box for the contour', and draws it on the frame,
# for contour in contours :
#     (x,y,w,h) = cv2.boundingRect(contour)
#     min_x, max_x = min(x, min_x), max(x+w, max_x)
#     min_y, max_y = min(y, min_y), max(y+h, max_y)
#     if w >= 8 and h >= 20 and w < 30 and h < 30:
#         cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 1)
#         print("x = ", x , " y= ", y , " w = ", w , " h = ", h )
#
#
#
# cv2.imshow("Thresh ", thresh)
for img in images:
    cv2.imshow("Blobs ",  img)


cv2.waitKey(0)
