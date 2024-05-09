int mestados[5][4] = {
  {1, 0, 1, 0}, // avanzar
  {0, 0, 0, 0}, // detenerse
  {0, 1, 1, 0}, // izquierda
  {1, 0, 0, 1}  // derecha
};

int velocidades[5][2] = {
  {130, 130}, // avanzar
  {0, 0},     // detenerse
  {130, 130}, // izquierda
  {130, 130}  // derecha
};

int IZQ = 12; // izquierdo = S1
int DER = 13; // derecho = S2

void setup() {
  Serial.begin(9600);

  pinMode(IZQ, INPUT);
  pinMode(DER, INPUT);

  for (int i = 0; i < 4; i++) {
    pinMode(i + 2, OUTPUT);
  }

  for (int i = 0; i < 2; i++) {
    pinMode(i + 5, OUTPUT);
  }
}

void loop() {
  int S1 = digitalRead(IZQ);
  int S2 = digitalRead(DER);

  // Imprimir el estado de los sensores por el puerto serial
  Serial.println("Izquierdo: " + String(S1));
  Serial.println("Derecho: " + String(S2));

  int estado;

  // Determinar el estado del robot basado en los sensores de línea
  if (S1 == 1 && S2 == 1) {
    estado = 0; // avanzar
  } else if (S1 == 1 && S2 == 0) {
    estado = 3; // derecha
  } else if (S1 == 0 && S2 == 1) {
    estado = 2; // izquierda
  } else {
    estado = 1; // detenerse
  }

  // Aplicar el estado al robot
  for (int i = 0; i < 4; i++) {
    digitalWrite(i + 2, mestados[estado][i]);
  }

  for (int i = 0; i < 2; i++) {
    analogWrite(i + 5, velocidades[estado][i]);
  }
}

