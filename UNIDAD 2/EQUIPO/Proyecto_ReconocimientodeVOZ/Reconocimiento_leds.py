import speech_recognition as sr
import serial
import time

color_to_char = {
    'encender': 'A',
    'rojo': 'R',
    'amarillo': 'Y',
    'verde': 'G',
    'azul': 'B',
    'blanco': 'W',
    'apagar': 'Z'
}

#Puerto COM7 del Bluetooth.
#Puerto COM4 ó COM5 de alguno de los arduinos para Arduino IDE
arduino = serial.Serial('COM7', 9600, timeout=1)

def send_command_to_arduino(character):
    arduino.write(character.encode())

def recognize_voice_and_send_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Di un color (Rojo, Amarillo, Verde, Azul, Blanco) o encender/apagar:")
        audio = r.listen(source)

    try:
        recognized_text = r.recognize_google(audio, language='es-ES').lower()
        print("Color detectado:", recognized_text)

        recognized_colors = []
        for color in color_to_char:
            if color in recognized_text:
                recognized_colors.append(color)

        if recognized_colors:
            first_color = recognized_colors[0]
            character = color_to_char[first_color]
            print("Enviando carácter:", character)
            send_command_to_arduino(character)
        else:
            print("No se detectó ningún color válido. Intenta de nuevo!.")
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

    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
    except sr.RequestError:
        print("Error en la solicitud de reconocimiento de voz.")

while True:
    recognize_voice_and_send_command()
    time.sleep(1)