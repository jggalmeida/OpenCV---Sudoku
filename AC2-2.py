import cv2
from matplotlib import pyplot as plt
import numpy as np
import glob

# Eric Monné Mesalles - 183338
# João Guilherme Guimarães Almeida - 120693

images = glob.glob('./data/*')
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
images = list(map(lambda x :cv2.imread(x,cv2.IMREAD_COLOR), images))

grey = list(map(lambda x : cv2.cvtColor(x, cv2.COLOR_BGR2GRAY), images))

thresh = list(map(lambda x: cv2.adaptiveThreshold(x,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,15,4),grey))
thresh = list(map(lambda x: cv2.morphologyEx(x, cv2.MORPH_CLOSE, kernel),thresh))



for i in range(len(thresh)):
    contours, hierarchy = cv2.findContours(thresh[i], cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    height, width = grey[i].shape
    min_x, min_y  = width, height
    max_x = max_y = 0
    numbers = 0
    # computes the bounding box for the contour, and draws it on the frame,
    for contour in contours :
        (x,y,w,h) = cv2.boundingRect(contour)
        if (len(contours) > 190):
            if ( h < height / 23):
                numbers += 1
                min_x, max_x = min(x, min_x), max(x+w, max_x)
                min_y, max_y = min(y, min_y), max(y+h, max_y)
                cv2.rectangle(images[i], (-2+x,-2+y), (x+w+2,y+h+2), (255,0,0), 1)
        else:
            if ( h < height / 11 and h > height / 25):
                numbers += 1
                min_x, max_x = min(x, min_x), max(x+w, max_x)
                min_y, max_y = min(y, min_y), max(y+h, max_y)
                cv2.rectangle(images[i], (-2+x,-2+y), (x+w+2,y+h+2), (255,0,0), 1)
    cv2.imshow("Numbers =" + str(numbers),images[i])

cv2.waitKey(0)
