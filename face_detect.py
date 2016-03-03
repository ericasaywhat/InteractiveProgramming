""" Experiment with face detection and image filtering using OpenCV """

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('/home/arianaolson/haarcascade_frontalface_alt.xml')
kernel = np.ones((21,21), 'uint8')
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))
    a = int(cap.get(3))
    for (x,y,w,h) in faces:
    	frame[y:y+h, x:x+w, :] = cv2.dilate(frame[y:y+h, x:x+w, :], kernel)
    	# cv2.rectangle(frame, (0,0), int((cap.get(3)/2), int(cap.get(4))), (0,255,255))
    	if x <= a/2 - x:
    		cv2.rectangle(frame, (x,y),(x+w, y+h), (0,0,255))
    		print 'right',
    		break
		elif x >= a/2 - x:
			cv2.rectangle(frame, (x,y),(x+w, y+h), (0,0,255))
			print 'left',
			break
    	# cv2.circle(frame, (x+w/2, y+h/2), w/4, (0, 200, 250), 150)	#make the face circle
    	# cv2.circle(frame, (x+w/3, y+h/3), 15, (255, 0, 0), 20)	#the eye circles
    	# cv2.circle(frame, (x+w/3, y+h/3), 5, (0, 0, 0), 20)
    	# cv2.circle(frame, (x+w/3, y+h/3), 20, (255,255,255), 30)
    	# cv2.circle(frame, (x+w/3, y+h/3), 15, (255, 0, 0), 20)
    	# cv2.circle(frame, (x+w/3, y+h/3), 5, (0, 0, 0), 20)
    	# cv2.circle(frame, (x+2*w/3, y+h/3), 20, (255,255,255), 30)
    	# cv2.circle(frame, (x+2*w/3, y+h/3), 15, (255, 0, 0), 20)
    	# cv2.circle(frame, (x+2*w/3, y+h/3), 5, (0, 0, 0), 20)
    	# cv2.ellipse(frame, (x+w/2, y+3*h/5),(x/5, y/5), 0, 180, 0, (0,0,255), 30)	#make the mouth
    	# cv2.ellipse(frame, (x+w/2, y+3*h/5),(x/5, y/5), 0, 180, 0, (255,255,255), 10)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()