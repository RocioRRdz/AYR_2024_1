def letra():
    while True:
        letra_O = input("Ingresa el Orígen (A-J): ").upper()
        letra_D = input("Ingresa el Destino (A-J): ").upper()
        if letra_O in 'ABCDEFGHIJ' and letra_D in 'ABCDEFGHIJ':
            return letra_O, letra_D
        else:
            print("La letra ingresada de orígen/destino no es válida.")


letra_origen, letra_destino = letra()
print("Orígen: ",letra_origen, "        ", "Destino: ",letra_destino)