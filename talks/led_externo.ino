int led_externo = 32;

void setup() {
  
  pinMode(led_externo, OUTPUT);
}

void loop() {
  
  digitalWrite(led_externo, HIGH);
  delay(1000);
  digitalWrite(led_externo, LOW);
  delay(1000);
}
