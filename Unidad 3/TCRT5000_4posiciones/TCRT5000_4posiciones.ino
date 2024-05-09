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
  {130,130},
  {130,130},
  {0,0},
  {130,130},
  {130,130}
  };

int IZQ = 12; //izquierdo = S1
int DER = 13; //derecho = S2

void setup() {
  Serial.begin(9600);
  pinMode(IZQ, INPUT);
  pinMode(DER, INPUT);

  for (int i=0; i<4; i++){
    pinMode(inputs[i], OUTPUT); 
  }
}

void loop() {
  int S2 = digitalRead(DER);
  int S1 = digitalRead(IZQ);
  int estado;
  
  //1 = negro
  //0 = otro
  // Imprimir el mensaje por el puerto serial
  Serial.println("Izquierdo: " + String(S1));
  Serial.println("Derecho: " + String(S2));
  
  if (S1 == 1 && S2 == 1) {
    estado = 0; // Avanzar
  } else if (S1 == 1 && S2 == 0) {
    estado = 3; // Derecha
  } else if (S1 == 0 && S2 == 1) {
    estado = 4; // Izquierda
  } else {
    estado = 2; // Detenerse
  }

  for(int i = 0; i<4; i++){
    digitalWrite(inputs[i], mestados[estado][i]);
    Serial.println(String(inputs[i])+" estado :"+String(mestados[estado][i]));
  }

  for(int i = 0; i<2; i++){
    analogWrite(enables[i], velocidades[estado][i]);
    Serial.println(String(enables[i])+" estado: "+ String(velocidades[estado][i]));
  }
  delay(500);
}
