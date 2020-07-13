import cv2,time
video=cv2.VideoCapture(0)
count=0
while True:
    count=count+1 
    check,frame=video.read()
    print(check)
    print(frame)
    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) (if you want black & white then use this line)
    #time.sleep(3)   #It waits to capture the picture
    cv2.imshow("Capturing",frame)
    key=cv2.waitKey(1)   #after 3 sec it takes a picture then wait 2000ms and again click another picture
    if key==ord('z'):   #to break the while loop
        break
print(count)    #it will print how many time the loop iterate
video.release()
cv2.destroyAllWindows()

