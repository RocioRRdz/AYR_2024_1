#include <SoftwareSerial.h>
SoftwareSerial BT1(10,11); // RX, TX recordar que se cruzan

int inputs[4] = {2, 4, 7, 8};
int enables[2] = {5,6};
int mestados[5][4]={
  {1,0,1,0},
  {0,1,0,1}, //no se usa
  {0,0,0,0},
  {0,1,1,0},
  {1,0,0,1}
  }; //avanzar, retroceder, detenerse, izquierda, derecha
int velocidades[5][2]={
  {150,150},   //0
  {150,150}, // 1 no se usa
  {0,0},   //2
  {90,90}, //3
  {90,90}  //4
  };

int IZQ = 12; //izquierdo = S1
int DER = 13; //derecho = S2
int S1;
int S2;
int estadoNuevo;
int estadoActual = -1;

void setup() {
  Serial.begin(9600);
  BT1.begin(9600);
  BT1.setTimeout(10);

  for (int i=0; i<4; i++){
    pinMode(inputs[i], OUTPUT); 
  }

  pinMode(IZQ, INPUT);
  pinMode(DER, INPUT);
}

void loop() {
  S1 = digitalRead(IZQ);
  S2 = digitalRead(DER);
  int estadoNuevo = -1;
  
  //1 = negro
  //0 = otro
  // Imprimir el mensaje por el puerto serial
  Serial.println("IZQUIERDO: "+ String(S1));
  Serial.println("DERECHA: "+ String(S2));
  
  if (S1 == 1 && S2 == 1) {
    estadoNuevo = 0; // Avanzar
  }
  if (S1 == 1 && S2 == 0) {
    estadoNuevo = 3; // Izquierda
  }
  if (S1 == 0 && S2 == 1) {
    estadoNuevo = 4; // Derecha
  } 
  if (S1 == 0 && S2 == 0) {
    estadoNuevo = 2; // Detenerse
  }

  // Solo establecer el estado si ha cambiado
  if (estadoNuevo != estadoActual) {
    nuevo(estadoNuevo);
    estadoActual = estadoNuevo;
  }
}

void nuevo(int estado){
  for(int i = 0; i<4; i++){
    digitalWrite(inputs[i], mestados[estado][i]);
    Serial.println(String(inputs[i])+" estado :"+String(mestados[estado][i]));
  }

  for(int i = 0; i<2; i++){
    analogWrite(enables[i], velocidades[estado][i]);
    Serial.println(String(enables[i])+" estado: "+ String(velocidades[estado][i]));
  }
}
