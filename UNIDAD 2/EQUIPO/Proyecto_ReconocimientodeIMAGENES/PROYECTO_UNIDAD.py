import cv2  ##opencv
import os

def tomar_foto():
    cam = cv2.VideoCapture(0)  ##videocamara ---

    while True:
        result, image = cam.read()
        if result:
            cv2.imshow("Cámara_Principal", image)
            res = cv2.waitKey(1)  ## 1  = .. no detenga la ejecucion
            if res == ord("q"):
                #opcion1
                #cam.release() #recursos sistema
                #cv2.destroyWindow("Camara_Principal")
                #break
                print("Saliendo de la Cámara")
                break
            elif res == ord(" "):  ##space
                #cv2.imwrite("foto.png", image)
                #print("Fotografía Aceptada")
                #cam.release() #recursos sistema
                #cv2.destroyAllWindows()
                ##cv2.destroyWindow("Camara_Principal")
                nombre = "foto.png"
                if os.path.exists(nombre):
                    op2 = input("Ya existe una foto. ¿Tomar una nueva? (s/n):")
                    if op2.lower() == 's':
                        cv2.imwrite(nombre, image)
                        print("Fotografía Aceptada.")
                    else:
                        print("No se tomó una nueva foto.")
                        break
                else:
                    cv2.imwrite(nombre, image)
                    print("Fotografía Aceptada")
                break
        else:
            print("No image detected. Please! try again")
    cv2.destroyAllWindows()


import numpy as np
from keras.utils import load_img, img_to_array #alternative 2
from keras.models import load_model

alto, largo = 300, 300
modelo = '../Intro_ConvolutionalNeuronalNetwork/modelo/modelo.h5'
pesos = '../Intro_ConvolutionalNeuronalNetwork/modelo/pesos.h5'

cnn = load_model(modelo)
cnn.load_weights(pesos)
def probar_red_neuronal(from_location, files):
    for file in files:
        composed_location = os.path.join(from_location, file)
        prediction_resultado = predict(composed_location)
        print('Folder Name: ', file, ' Prediction: ', prediction_resultado, " Resultado: ", prediction_resultado)

def predict(file):
    imagen_a_predecir = load_img(file, target_size = (alto, largo))
    imagen_a_predecir = img_to_array(imagen_a_predecir)
    imagen_a_predecir = np.expand_dims(imagen_a_predecir, axis=0) #agrega una dimension adicional
    arreglo = cnn.predict(imagen_a_predecir) ## [[1,0,0,0,0,0]]
    resultado = arreglo[0]
    respuesta = np.argmax(resultado) #indice del valor mas alto

    match respuesta:
        case 0:
            return 'C1-Clase1'
        case 1:
            return 'C2-Clase2'
        case 2:
            return 'C3-Clase3'
        case _:
            return '----'


from matplotlib import pyplot as plt
def visualizar_foto(from_location, files):
    for file in files:
        composed_location = os.path.join(from_location, file)
        prediction_resultado = predict(composed_location)

        imagen = cv2.imread(composed_location)
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        plt.imshow(imagen)
        plt.title(f'Predicción: {prediction_resultado}')
        plt.show()

def get_folders_name_from(from_location):
    list_dir = os.listdir(from_location)
    # folders = [archivo for archivo in listDir if os.path.splitext(archivo)[1] == ""]
    # the above is equals to ....
    folders = []
    for file in list_dir:
        temp = os.path.splitext(file)
        if temp[1] == "":
            folders.append(temp[0])
    folders.sort()
    return folders

def prediccion_imagen():
    base_location = 'C:/Users/Usuario/PycharmProjects/AYR_2024_1/Unidad 2/Intro_ConvolutionalNeuronalNetwork/F3-Prueba/'
    folders = get_folders_name_from(base_location)

    for folder in folders:
        files = [archivo for archivo in os.listdir(os.path.join(base_location + folder)) if
                 archivo.endswith(".png") or archivo.endswith(".png") or archivo.endswith(".png")]

        for file in files:
            composed_location = os.path.join(base_location, folder, file)
            prediction = predict(composed_location)

            if prediction == 'C1-Clase1':
                imagen = cv2.imread(composed_location)
                imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
                plt.imshow(imagen)
                plt.title(f'Predicción: {prediction}')
                plt.show()
                return

            elif prediction == 'C2-Clase2':
                imagen = cv2.imread(composed_location)
                imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
                plt.imshow(imagen)
                plt.title(f'Predicción: {prediction}')
                plt.show()
                return

            elif prediction == 'C3-Clase3':
                imagen = cv2.imread(composed_location)
                imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
                plt.imshow(imagen)
                plt.title(f'Predicción: {prediction}')
                plt.show()
                return

            else:
                print('Predicción de la ClaseX no reconocida.')
                return

def dibujo():
    print(
        '⠀⠀⠀⠀⠀⡀⠀⠀⠀⠨⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
        '⠀⠀⠀⠀⠀⠽⠅⠀⠀⠀⠀⠀⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
        '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠚⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
        '⠀⠀⠀⠀⠠⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣤⠶⠛⠉⠉⠉⠛⠲⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣶⣾⣯⣭⡉⠉⠉⠉⢓⡢⠀⠀⠀⠀⠀\n'
        '⠀⠀⠀⠀⠠⠾⠯⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⠟⠛⠉⠁⠀⠈⠙⠻⣟⡒⠈⠉⠉⠀⠀⠀⠀\n'
        '⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡤⠶⠖⠒⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣆⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣦⠶⢄⠀⠀⠀⠀⠀⠀\n'
        '⠀⠀⠀⠀⠀⣠⡴⠛⠁⠀⠀⠀⠀⠀⠀⠰⣄⠀⠀⠀⠀⠀⠀⠀⠀⡠⢠⣦⣧⣶⣹⣆⠀⠀⠀⠀⠀⢰⣿⣿⠃⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⠳⡄⠀⠀⠀⠀\n'
        '⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠀⠀⠀⠀⠀⠀⣰⢣⣿⡿⣻⣿⣧⣿⠀⠀⠀⠀⣠⣿⡿⠃⠀⠀⠀⣳⡀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠘⡆⠀⠀⠀\n'
        '⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃⣿⣿⣷⣿⣿⣿⢸⣧⣀⡤⠊⠁⠀⠀⠀⡴⠛⠿⠍⠙⠲⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⣀⠀⠀\n'
        '⠀⢀⣀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡏⢸⣿⣿⣿⣿⣿⡿⣼⠏⠁⠀⠀⠀⠀⠀⠸⡿⠦⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠬⠛⡆\n'
        '⢰⣡⣤⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⣼⣿⣿⣿⣿⣿⢣⡟⠀⠀⠛⠛⠛⠛⠛⠛⠛⠂⠀⠀⠀⠀⢸⡇⠀⠀⠀⢰⡿⣄⠀⠀⠀⢀⣠⡇\n'
        '⠘⢿⣿⠟⠙⠳⣤⣀⣀⡀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣼⡔⣿⣿⣿⡿⣛⣵⣿⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠾⣄⣀⣀⣠⡼⠁⠈⠳⢤⣤⡤⠾⠁\n'
        '⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠻⢮⣭⠵⠞⠉⠉⠉⠉⠙⠛⠛⠉⠛⠋⠉⠛⠛⠛⠛⠋⠉⠁⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
    )

def menu():
    while True:
        print('\n***************************************************')
        print('Menú de operaciones: ')
        print('1. Fotografía')
        print('2. Predecir')
        print('3. Visualizar fotografía')
        print('4. Predicción de imagen')
        print('5. Sorpresa')
        print('6. Salir')
        op = input('Selecciona la operación a realizar: ')

        from_location = 'C:/Users/Usuario/PycharmProjects/AYR_2024_1/Unidad 2/Proyecto/'
        files = ['foto.png']
        if op == "1":
            tomar_foto()
        elif op == "2":
            probar_red_neuronal(from_location, files)
        elif op == "3":
            visualizar_foto(from_location, files)
        elif op == "4":
            prediccion_imagen()
        elif op == '5':
            dibujo()
        elif op == "6":
            print("Salir")
            break
        else:
            print('No se reconoce la opción ingresada.')

if __name__ == "__main__":
    menu()

    #Quitar fondo y acercar