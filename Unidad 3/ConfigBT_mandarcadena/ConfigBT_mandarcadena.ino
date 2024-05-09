#include <SoftwareSerial.h>
SoftwareSerial BT1(10,11); // RX, TX recordar que se cruzan

void setup(){
  Serial.begin(9600);
  Serial.println("Listo: ");
  BT1.begin(9600);
}

void loop(){
  if (BT1.available()){
    Serial.write(BT1.read());
  }
       
  if (Serial.available()){
    BT1.write(Serial.read());
  }
}
