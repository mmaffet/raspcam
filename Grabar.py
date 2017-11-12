import numpy as np
import cv2
import time
fecha=time.strftime("%d.%m.%Y")
tiempo=time.strftime("%H-%M-%S")
cap = cv2.VideoCapture('http://camarapat-01.ddns.net:8081/')
nombre_archivo=str(fecha+" at "+tiempo)
print (nombre_archivo)
# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('fecha/'+nombre_archivo+'.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()