Methods for Image Enhancement

Method1
Using cv2.equalizeHist(img)

Method 2
Contrast Limited Adaptive Histogram Equalization or CLAHE
create a CLAHE object (Arguments are optional)
clahe=cv2.createCLAHE()
clahe=cv2.createCLAHE(clipLimit=2.0, tileGridsize=(8,8))
apply this object to an image
cl1=clahe.apply(img)