#from keras.preprocessing.image import load_img, img_to_array  #deprecated en tf 2.9 #alternative 0
#from tensorflow.keras.utils import load_img  #alternative 1
from keras.utils import load_img, img_to_array #alternative 2

largo, alto = 500, 600
#file = './FIT V.jpg'
#file = './gato.jpeg'
#file = './Imagen1.png'
file = './RocioEstela.jpg'
#file = './RocioEstela(2).png'

img = load_img(file, target_size = (largo, alto)
             ,color_mode = "grayscale"
             )

print(img.size)
print(img.mode)

#opcion 1
img.show()

#opcion 2
#import matplotlib.pyplot as plt
#plt.imshow(img, cmap="gray")
#plt.imshow(img)
#plt.xticks([])
#plt.yticks([])
#plt.show()


imagen_en_array = img_to_array(img)  #filas, columnas, canales de colores
print(imagen_en_array.shape)

#print(imagen_en_array)

for i in imagen_en_array:
    print(i)
