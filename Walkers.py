import cv2 
bodyclassifier = cv2.CascadeClassifier("haarcascade_fullbody.xml")
video=cv2.VideoCapture("walking.avi")
while True:
    ret,image=video.read()
    greyscale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    bodies=bodyclassifier.detectMultiScale(greyscale,1.2,3)
    for (x,y,w,h) in bodies:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),6)
        cv2.imshow("people waklking",image)
    if cv2.waitKey(1)==32:
        break
video.release()
cv2.destroyAllWindows() 