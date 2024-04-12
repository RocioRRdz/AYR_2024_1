from keras.utils import load_img, img_to_array

largo, alto = 400, 400
#file = './FIT V.jpg'
#file = './gato.jpeg'
#file = './Imagen1.png'
file = './RocioEstela.jpg'
#file = './RocioEstela(2).png'

img = load_img(file, target_size = (largo, alto)
             ,color_mode = "grayscale"
             )

imagen_en_array = img_to_array(img)  #filas, columnas, canales de colores
print(imagen_en_array.shape)

#archivo_imagen = open("./gato_en_arreglo.csv", "w")
archivo_imagen = open("./RocioEstela_en_arreglo.csv", "w")
for i in imagen_en_array:
    for pixel in i:
        archivo_imagen.write(str(int(pixel[0])) + ",")
    archivo_imagen.write("\n")
archivo_imagen.flush()
archivo_imagen.close()

