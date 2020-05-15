import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img=cv.imread('night.jpg',1)
img=cv.cvtColor(img, cv.COLOR_BGR2RGB)

R, G, B=cv.split(img)

##creating histogram Equalization of image
histEq_R=cv.equalizeHist(R)
histEq_G=cv.equalizeHist(G)
histEq_B=cv.equalizeHist(B)

histEq1=cv.merge((histEq_R,histEq_G,histEq_B))


##Using CLAHE 
#clahe=cv.createCLAHE()
clahe=cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)) #adjusts the histogram

histEq2_R=clahe.apply(R)
histEq2_G=clahe.apply(G)
histEq2_B=clahe.apply(B)

histEq2=cv.merge((histEq2_R,histEq2_G,histEq2_B))


output=[img,histEq1, histEq2]
titles=['Original Image','Adjusted Histogram','CLAHE']

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



    
