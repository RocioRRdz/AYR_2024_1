//int sensor = 13; es uno
int sensor = 12;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(sensor, INPUT);
}

//1 = negro
//0 = otro

void loop() {
  // put your main code here, to run repeatedly:
  int v = digitalRead(sensor);
  Serial.println(v);
  delay(100);
}
