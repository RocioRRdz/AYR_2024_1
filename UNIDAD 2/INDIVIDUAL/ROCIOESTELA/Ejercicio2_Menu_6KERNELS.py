from keras.utils import load_img, img_to_array, array_to_img, save_img #alternative 2

def convolution(img_a_convolucionar, kernel):
    img_convolucionada = []  # nueva imagen
    for filas in range(1, alto - 1):  # ignora los pixeles de la primera y ultima fila
        new_fila = []
        for columnas in range(1, largo - 1):  # ignora los pixeles de la primera y ultima columna
            pixelConvulucionado = 0
            for f_kernel in range(len(kernel)):  # 0 1 2
                for c_kernel in range(len(kernel)):  # 0 1 2
                    pixelConvulucionado += (kernel[f_kernel][c_kernel]
                                            * img_a_convolucinar[filas + (f_kernel - 1)][columnas + (c_kernel - 1)])

            if op == "1":
                pass
            elif op == "2":
                pass
            elif op == "3":
                pass
            elif op == "4":
                pass
            elif op == "5":
                pixelConvulucionado = pixelConvulucionado * (1 / 9)
            elif op == "6":
                pixelConvulucionado = pixelConvulucionado * (1 / 16)

            new_fila.append(pixelConvulucionado)
        img_convolucionada.append(new_fila)

    return array_to_img(img_convolucionada)

largo, alto = 500,500
#file = 'C:/Users/Usuario/PycharmProjects/AYR_2024_1/Unidad 2/Intro_Convolutional/RocioEstela(2).png'
file = 'C:/Users/Usuario/PycharmProjects/AYR_2024_1/Unidad 2/Intro_Convolutional/RocioEstela.jpg'

img_original = load_img(file, target_size = (largo, alto)
             ,color_mode = "grayscale")

img_a_convolucinar = img_to_array(img_original)  #filas, columnas, canales de colores
print(img_a_convolucinar.shape)

#Operación: Identify
kernel_Identify = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

#Operación: Ridge
kernel_Ridge = [
    [0, -1, 0],
    [-1, 4, -1],
    [0, -1, 0]
]

#Operación: Ridge V2
kernel_Ridge_v2 = [
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
]

#Operación: SHARPEN
kernel_Sharpen = [
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
]

#Operación: Box blur
kernel_Box_Blur = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

#Operación: Gaussian blur 3x3
kernel_Gaussian_Blur_3x3 = [
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
]

while True:
    print('\n***************************************************')
    print('Menú de operaciones de imágenes procesadas: ')
    print('1. Identify')
    print('2. Ridge V1')
    print('3. Ridge v2')
    print('4. Sharpen')
    print('5. Box Blur')
    print('6. Gaussian Blur 3x3')
    print('7. Salir')
    op = input('Selecciona la operación a realizar: ')

    import matplotlib.pyplot as plt
    plt.figure(figsize=(15, 5))

    if op == "1":
        plt.suptitle('Identify')
        img = convolution(img_a_convolucinar, kernel_Identify)
        #img.show()
        plt.subplot(1, 2, 1)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(img_original, cmap='gray')

        plt.subplot(1, 2, 2)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(img, cmap='gray')

        plt.show()
        #save_img('imagen_convolucionada.jpg', img_convolucionada)

    elif op == "2":
        plt.suptitle('Ridge Versión.1')
        img = convolution(img_a_convolucinar, kernel_Ridge)
        #img.show()
        plt.subplot(1, 2, 1)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(img_original, cmap='gray')

        plt.subplot(1, 2, 2)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(img, cmap='gray')

        plt.show()
        #save_img('imagen_convolucionada.jpg', img_convolucionada)

    elif op == "3":
        plt.suptitle('Ridge Versión.2')
        img = convolution(img_a_convolucinar, kernel_Ridge_v2)
        #img.show()
        plt.subplot(1, 2, 1)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(img_original, cmap='gray')

        plt.subplot(1, 2, 2)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(img, cmap='gray')

        plt.show()
        #save_img('imagen_convolucionada.jpg', img_convolucionada)

    elif op == "4":
        plt.suptitle('Sharpen')
        img = convolution(img_a_convolucinar, kernel_Sharpen)
        #img.show()
        plt.subplot(1, 2, 1)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(img_original, cmap='gray')

        plt.subplot(1, 2, 2)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(img, cmap='gray')

        plt.show()
        #save_img('imagen_convolucionada.jpg', img_convolucionada)

    elif op == "5":
        plt.suptitle('Box Blur')
        img = convolution(img_a_convolucinar, kernel_Box_Blur)
        #img.show()
        plt.subplot(1, 2, 1)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(img_original, cmap='gray')

        plt.subplot(1, 2, 2)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(img, cmap='gray')

        plt.show()
        # save_img('imagen_convolucionada.jpg', img_convolucionada)

    elif op == "6":
        plt.suptitle('Gaussian Blur 3x3')
        img = convolution(img_a_convolucinar, kernel_Gaussian_Blur_3x3)
        #img.show()
        plt.subplot(1, 2, 1)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(img_original, cmap='gray')

        plt.subplot(1, 2, 2)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(img, cmap='gray')

        plt.show()
        # save_img('imagen_convolucionada.jpg', img_convolucionada)

    elif op == "7":
        print('Salir')
        break
    else:
        print('No se reconoce lo ingresado')