import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img=cv.imread('night.jpg',0)

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



    
