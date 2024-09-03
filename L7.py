import cv2
import numpy as np
import time
print(cv2.__version__)
v=cv2.VideoCapture("video.mp4")
count=0
bg=0
for i in range(60):
    r,bg=v.read()
    if r==False:
        continue
mirror=np.flip(bg,axis=1)
while(v.isOpened()):
    r,bg1=v.read()
    if not v:
        break
    count+=1
    m2=np.flip(bg1,axis=1)
    hsv=cv2.cvtColor(m2,cv2.COLOR_BGR2HSV)
    lowerred=np.array([100,40,40])
    upperred=np.array([100,255,255])
    mask1=cv2.inRange(hsv,lowerred,upperred)
    lowerred1=np.array([155,40,40])
    upperred1=np.array([180,255,255])
    mask2=cv2.inRange(hsv,lowerred1,upperred1) 
    mask=mask1+mask2
    #refining the image
    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
    mask=cv2.dilate(mask,np.ones((3,3),np.uint8),iterations=1)
    mask3=cv2.bitwise_not(mask)
    result1=cv2.bitwise_and(bg,mirror,mask=mask)
    result2=cv2.bitwise_and(bg1,m2,mask=mask3)
    finaloutput=cv2.addWeighted(result1,1,result2,1,0)
    cv2.imshow("Invisible Man",finaloutput)
    k=cv2.waitKey(1)
    if k==27:
        break

cv2.destroyAllWindows()