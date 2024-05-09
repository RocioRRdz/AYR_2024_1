#include <SoftwareSerial.h>
SoftwareSerial BT1(10,11); // RX, TX recordar que se cruzan

int inputs[4] = {2, 4, 7, 8};
int enables[2] = {5,6};
int mestados[5][4]={
  {1,0,1,0},
  {0,1,0,1},
  {0,0,0,0},
  {0,1,1,0},
  {1,0,0,1}
  }; //avanzar, reversa, detenerse, izquierda, derecha
int velocidades[5][2]={
  {150,150},
  {150,150},
  {0,0},
  {130,130},
  {130,130}
  };

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  //Serial.println("Enter AT commands:");
  BT1.begin(9600);
  BT1.setTimeout(10);
  for(int i = 0; i<4; i++){
    pinMode(inputs[i], OUTPUT);
  }
}

//65=A - IZQUIERDA, 68=D - DERECHA, 87=S - ABAJO/REVERSA, 83=W - ARRIBA/AVANZAR, 88=X - DETENERSE.

void loop(){
  // put your main code here, to run repeatedly:
  if(BT1.available()>0){
    byte numero = (byte)BT1.read();
    Serial.println(numero);

    if(numero == 83){
      int estado = 0;
      for(int i = 0; i<4; i++){
        digitalWrite(inputs[i], mestados[estado][i]);
        Serial.println(String(inputs[i])+" estado :"+String(mestados[estado][i]));
      }

      for(int i = 0; i<2; i++){
        analogWrite(enables[i], velocidades[estado][i]);
        Serial.println(String(enables[i])+" estado: "+ String(velocidades[estado][i]));
      }
    }

    if(numero == 87){
      int estado = 1;
      for(int i = 0; i<4; i++){
        digitalWrite(inputs[i], mestados[estado][i]);
        Serial.println(String(inputs[i])+" estado :"+String(mestados[estado][i]));
      }

      for(int i = 0; i<2; i++){
        analogWrite(enables[i], velocidades[estado][i]);
        Serial.println(String(enables[i])+" estado: "+ String(velocidades[estado][i]));
      }
    }

    if(numero == 88){
      int estado = 2;
      for(int i = 0; i<4; i++){
        digitalWrite(inputs[i], mestados[estado][i]);
        Serial.println(String(inputs[i])+" estado :"+String(mestados[estado][i]));
      }

      for(int i = 0; i<2; i++){
        analogWrite(enables[i], velocidades[estado][i]);
        Serial.println(String(enables[i])+" estado: "+ String(velocidades[estado][i]));
      }
    }

    if(numero == 65){
      int estado = 3;
      for(int i = 0; i<4; i++){
        digitalWrite(inputs[i], mestados[estado][i]);
        Serial.println(String(inputs[i])+" estado :"+String(mestados[estado][i]));
      }

      for(int i = 0; i<2; i++){
        analogWrite(enables[i], velocidades[estado][i]);
        Serial.println(String(enables[i])+" estado: "+ String(velocidades[estado][i]));
      }
    }

    if(numero == 68){
      int estado = 4;
      for(int i = 0; i<4; i++){
        digitalWrite(inputs[i], mestados[estado][i]);
        Serial.println(String(inputs[i])+" estado :"+String(mestados[estado][i]));
      }

      for(int i = 0; i<2; i++){
        analogWrite(enables[i], velocidades[estado][i]);
        Serial.println(String(enables[i])+" estado: "+ String(velocidades[estado][i]));
      }
    }
  }
}
