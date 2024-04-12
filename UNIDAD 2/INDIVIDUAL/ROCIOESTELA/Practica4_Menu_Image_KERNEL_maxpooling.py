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

def maxpooling(img, stride):
    img_max_pooling = []
    for filas in range(1, alto - 1 - stride, stride):
        new_fila = []
        for columnas in range(1, largo - 1 - stride, stride):
            max_pixel = -1
            for f_kernel in range(stride):
                for c_kernel in range(stride):
                    pixel = img[filas + f_kernel][columnas + c_kernel][0]
                    if pixel > max_pixel:
                        max_pixel = pixel
            new_fila.append([max_pixel])  # se agrega como lista para agregarlo como canal 1 (escala de grises)
        img_max_pooling.append(new_fila)

    return array_to_img(img_max_pooling)

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

stride = 4 # 2 x 2
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
        kernel_nombre = 'Identify'
        kernel = kernel_Identify

    elif op == "2":
        kernel_nombre = 'Ridge Versión.1'
        kernel_nombre = kernel_Ridge

    elif op == "3":
        kernel_nombre = 'Ridge Versión.2'
        kernel = kernel_Ridge_v2

    elif op == "4":
        kernel_nombre = 'Sharpen'
        kernel = kernel_Sharpen

    elif op == "5":
        kernel_nombre = 'Box Blur'
        kernel = kernel_Box_Blur

    elif op == "6":
        kernel_nombre = 'Gaussian Blur 3x3'
        kernel = kernel_Gaussian_Blur_3x3

    elif op == "7":
        print('Salir')
        break
    else:
        print('No se reconoce lo ingresado')

    while True:
        print('****************************************************')
        print('Aplicar Maxpooling: ')
        print('a. Si')
        print('b. No')
        print('c. Salir')
        op_mp = input('Selecciona la operación a realizar: ')

        img = convolution(img_a_convolucinar, kernel)
        plt.suptitle(f'{kernel_nombre} {"con" if op_mp.lower() == "a" else "sin"} Maxpooling')

        if op_mp.lower() == 'a':
            img_array = img_to_array(img)
            img_max_pooling = maxpooling(img_array, stride)
            #img.show()
            plt.subplot(1, 3, 1)
            plt.xticks([])
            plt.yticks([])
            plt.imshow(img_original, cmap='gray')

            plt.subplot(1, 3, 2)
            plt.xticks([])
            plt.yticks([])
            plt.imshow(img, cmap='gray')

            plt.subplot(1, 3, 3)
            plt.xticks([])
            plt.yticks([])
            plt.imshow(img_max_pooling, cmap='gray')

            plt.show()

        elif op_mp.lower() == 'b':
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

        elif op_mp.lower() == 'c':
            print('Salir del segundo menú')
            break

        else:
            print('No es posible realizar el Maxpooling.')