int S1 = 12;
int S2 = 13;

void setup() {
  Serial.begin(9600);
  pinMode(S1, INPUT);
  pinMode(S2, INPUT);
}

void loop() {
  int DER = digitalRead(S2);
  int IZQ = digitalRead(S1);

  //1 = negro
  //0 = otro

  // Imprimir el mensaje por el puerto serial
  Serial.println("Derecho: " + String(DER));
  Serial.println("Izquierdo: " + String(IZQ));
  delay(500);
}

