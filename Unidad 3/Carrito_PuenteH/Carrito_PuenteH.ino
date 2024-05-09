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
  {100,150},
  {0,0},
  {150,150},
  {150,150}
  };
String nEstados[5] = {
  "Avanzar", 
  "Retroceder", 
  "Detenerse", 
  "Izquierda", 
  "Derecha"};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(100);
  for (int i=0; i<4; i++){
    pinMode(inputs[i], OUTPUT); 
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0){
    int estado = Serial.readString().toInt();
    Serial.println(nEstados[estado]);

  for (int i=0;i<4;i++){
    digitalWrite(inputs[i],mestados[estado][i]);
    Serial.println(String(inputs[i])+" estado: "+String(mestados[estado][i]));
  }

  for (int i=0; i<2; i++){
    analogWrite(enables[i],velocidades[estado][i]);
    Serial.println(String(enables[i])+" estado :"+String(velocidades[estado][i]));
  }
  }
delay(100);
}