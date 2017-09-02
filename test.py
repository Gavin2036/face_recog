import guess3
import cv2
import numpy as np
img_file = '/Users/apple/Desktop/try/old.jpg'
img = cv2.imread(img_file)
[a,b,c]=np.shape(img)

font = cv2.FONT_HERSHEY_SIMPLEX
result = guess3.guessGender(img_file)

cv2.putText(img,result[0],(int(b*0.1),int(a*0.8)), font, 4,(255,255,255),2,cv2.LINE_AA)
cv2.imshow('test',img)
cv2.waitKey(0)
#print guess3.guessGender(img_file)
