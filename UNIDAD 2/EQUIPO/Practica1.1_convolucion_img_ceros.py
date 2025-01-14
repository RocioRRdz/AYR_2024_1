from keras.utils import load_img, img_to_array, array_to_img, save_img #alternative 2

largo, alto = 500,500
#file = './FIT V.jpg'
file = './gato.jpeg'

img_original = load_img(file, target_size = (largo, alto)
             ,color_mode = "grayscale"
             )

img_a_convolucinar = img_to_array(img_original)  #filas, columnas, canales de colores

print(img_a_convolucinar.shape)

"""
kernel = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]
"""
#BLUR
kernel = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]
"""
#SHARPEN
kernel = [
    [0, -1, 0],
    [-1, 4, -1],
    [0, -1, 0]
]
"""


img_convolucionada = [] #nueva imagen

for filas in range(alto+2): #pixeles de la primera y ultima fila
    new_fila = []
    for columnas in range(largo+2): #pixeles de la primera y ultima columna

        pixelConvulucionado = 0
        if 0 < filas < alto + 1 and 0 < columnas < largo + 1: #original
            for f_kernel in range(len(kernel)):  # 0 1 2
                for c_kernel in range(len(kernel)):  # 0 1 2
                    pixelConvulucionado += (kernel[f_kernel][c_kernel]
                                            * img_a_convolucinar[filas - 1][columnas - 1])
            pixelConvulucionado = pixelConvulucionado * (1 / 9)
        new_fila.append(pixelConvulucionado)

        # Imprimir valores de los píxeles
        print("Fila:", filas, "Columna:", columnas, "Valor:", pixelConvulucionado)

    img_convolucionada.append(new_fila)

img = array_to_img(img_convolucionada)
print(img.size)

##plot - 2 imagenes
import matplotlib.pyplot as plt
plt.figure(figsize=(15,5))

plt.subplot(1,2,1)
plt.xticks([])
plt.yticks([])
plt.imshow(img_original, cmap='gray')

plt.subplot(1,2,2)
plt.xticks([])
plt.yticks([])
plt.imshow(img, cmap='gray')

plt.show()
