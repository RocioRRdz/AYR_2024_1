import serial

# Create a serial object
ser = serial.Serial('COM7', 9600)  # replace 'COM3' with the port number of your HC05 module

while True:
    # Send a string to the Arduino Serial monitor
    a = input("valor:")
    ser.write(a.encode())

# Close the serial connection
ser.close()
