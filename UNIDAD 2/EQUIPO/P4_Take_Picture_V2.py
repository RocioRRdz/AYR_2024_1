#opencv-python
#FOR EN LUGAR DE WHILE
#WAITKEY POR SLEEP
#PRACTICA 2
#100 FOTOS

import cv2  ##opencv
import time

cam = cv2.VideoCapture(0) ##videocamara ---
contFotos = 0
for i in range(100):
    result, image = cam.read()
    if result:
        cv2.imshow("Camara_Principal", image)
        time.sleep(5) ## Espera 5 segundos
        #print(res , "  ", ord("q"))
        if cv2 == ord("q"):
            cam.release()
            cv2.destroyWindow("Camara_Principal")
            break
        elif cv2 == ord(" "): ##space
            cv2.imwrite("foto_"+ str(contFotos) +".png", image)
            contFotos+=1
    else:
        print("No image detected. Please! try again")
        break

