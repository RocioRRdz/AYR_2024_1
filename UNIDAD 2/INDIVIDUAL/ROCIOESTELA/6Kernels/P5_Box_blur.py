from keras.utils import load_img, img_to_array, array_to_img, save_img #alternative 2

largo, alto = 500,500
#file = 'C:/Users/Usuario/PycharmProjects/AYR_2024_1/Unidad 2/Intro_Convolutional/RocioEstela(2).png'
file = 'C:/Users/Usuario/PycharmProjects/AYR_2024_1/Unidad 2/Intro_Convolutional/RocioEstela.jpg'

img_original = load_img(file, target_size = (largo, alto)
             ,color_mode = "grayscale"
             )

img_a_convolucinar = img_to_array(img_original)  #filas, columnas, canales de colores
print(img_a_convolucinar.shape)

#Operación: Box blur
kernel = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

img_convolucionada = [] #nueva imagen

for filas in range(1,alto-1): #ignora los pixeles de la primera y ultima fila
    new_fila = []
    for columnas in range(1, largo-1): #ignora los pixeles de la primera y ultima columna

        pixelConvulucionado = 0
        for f_kernel in range(len(kernel)): # 0 1 2
            for c_kernel in range(len(kernel)): # 0 1 2
                pixelConvulucionado += (kernel[f_kernel][c_kernel]
                                        * img_a_convolucinar[filas + (f_kernel-1)][columnas+(c_kernel-1)])

        pixelConvulucionado = pixelConvulucionado * (1/9)
        new_fila.append(pixelConvulucionado)

    img_convolucionada.append(new_fila)

img = array_to_img(img_convolucionada)
print(img.size)


#img.show()

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


#save_img('imagen_convolucionada.jpg', img_convolucionada)