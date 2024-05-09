import speech_recognition as sr
import serial
import time

arduino = serial.Serial('COM7', 9600, timeout=1)

estado_to_char = {
    'avanzar': 'W',
    'retroceder': 'S',
    'detenerse': 'X',
    'izquierda': 'A',
    'derecha': 'D'
}

def send_command_to_arduino(character):
    arduino.write(character.encode())

def recognize_voice_and_send_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Comandos ↑ ↓ 0 → ← :")
        audio = r.listen(source)

    try:
        recognized_text = r.recognize_google(audio, language='es-ES').lower()
        print("Detectado:", recognized_text)

        recognized_com = []
        for comando in estado_to_char:
            if comando in recognized_text:
                recognized_com.append(comando)

        if recognized_com:
            first_com = recognized_com[0]
            character = estado_to_char[first_com]
            print("Enviando comando a Arduino:", character)
            send_command_to_arduino(character)
        else:
            print("No se detectó ningún comando válido. Intenta de nuevo.")

    except sr.UnknownValueError:
        print("No se pudo entender el audio.")
    except sr.RequestError:
        print("Error en la solicitud de reconocimiento de voz.")

while True:
    recognize_voice_and_send_command()
    time.sleep(1)
