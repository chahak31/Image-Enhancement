#Methods for Image Enhancement

#Method1
#cv2.equalizeHist(img)

#Method 2
#Contrast Limited Adaptive Histogram Equalization
#create a CLAHE object (Arguments are optional)
#clahe=cv2.createCLAHE()
#clahe=cv2.createCLAHE(clipLimit=2.0, tileGridsize=(8,8))
#apply this object to an image
#cl1=clahe.apply(img)

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

cam = cv.VideoCapture(0)

cv.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv.imshow("test", frame)
    if not ret:
        break
    k = cv.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

img=cv.imread(img_name,0)

##creating histogram Equalization of image
histEq1=cv.equalizeHist(img)
##Using CLAHE 
#clahe=cv.createCLAHE()
clahe=cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)) #adjusts the histogram
histEq2=clahe.apply(img)

output=[img,histEq1, histEq2]
titles=['Original Image','k=2','k=4']

for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(output[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
#stacking images side-by-side
#sbs=np.hstack((img,histEq))

#cv.imwrite('img',sbs)
cv.waitKey(0)
cv.destroyAllWindows()



    
