int led_interno = 2;

void setup() {
  
  pinMode(led_interno, OUTPUT);
}

void loop() {
  
  digitalWrite(led_interno, HIGH);
  delay(1000);
  digitalWrite(led_interno, LOW);
  delay(1000);
}
