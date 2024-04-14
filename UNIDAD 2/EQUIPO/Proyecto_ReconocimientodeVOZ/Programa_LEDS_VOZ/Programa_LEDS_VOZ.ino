#include <SoftwareSerial.h>
SoftwareSerial BT1(10, 11); // RX, TX (recuerda que se cruzan)

const int redLed = 2;
const int yellowLed = 3;
const int greenLed = 4;
const int blueLed = 6;
const int whiteLed = 7;

void setup() {
  Serial.begin(9600);
  BT1.begin(9600);   
  
  pinMode(redLed, OUTPUT);
  pinMode(yellowLed, OUTPUT);
  pinMode(greenLed, OUTPUT);
  pinMode(blueLed, OUTPUT);
  pinMode(whiteLed, OUTPUT);
}

void loop() {
  if (BT1.available() > 0) {
    char receivedChar = BT1.read(); 
    Serial.println(receivedChar);  
    
    digitalWrite(redLed, LOW);
    digitalWrite(yellowLed, LOW);
    digitalWrite(greenLed, LOW);
    digitalWrite(blueLed, LOW);
    digitalWrite(whiteLed, LOW);
    
    switch (receivedChar) {
      case 'R':
        digitalWrite(redLed, HIGH);
        Serial.println("Rojo encendido");
        break;
      case 'Y':
        digitalWrite(yellowLed, HIGH);
        Serial.println("Amarillo encendido");
        break;
      case 'G':
        digitalWrite(greenLed, HIGH);
        Serial.println("Verde encendido");
        break;
      case 'B':
        digitalWrite(blueLed, HIGH);
        Serial.println("Azul encendido");
        break;
      case 'W':
        digitalWrite(whiteLed, HIGH);
        Serial.println("Blanco encendido");
        break;
      case 'A':
        digitalWrite(redLed, HIGH);
        digitalWrite(yellowLed, HIGH);
        digitalWrite(greenLed, HIGH);
        digitalWrite(blueLed, HIGH);
        digitalWrite(whiteLed, HIGH);
        Serial.println("Todos los LEDs Encendidos");
        break;
      case 'Z':
        digitalWrite(redLed, LOW);
        digitalWrite(yellowLed, LOW);
        digitalWrite(greenLed, LOW);
        digitalWrite(blueLed, LOW);
        digitalWrite(whiteLed, LOW);
        Serial.println("Todos los LEDs Apagados");
        break;
      default:
        break;
    }
  }
  
  if (Serial.available() > 0) {
    char commandChar = Serial.read();
    BT1.write(commandChar);       
  }
}


