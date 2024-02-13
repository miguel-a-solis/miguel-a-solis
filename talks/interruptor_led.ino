int interruptor = 35;
int led_externo = 32;
bool apretado = false;

void setup() {
  pinMode(led_externo, OUTPUT);
  pinMode(interruptor, INPUT);

}

void loop() {

apretado = digitalRead(interruptor);
if(apretado){
  digitalWrite(led_externo, HIGH);
}else{
  digitalWrite(led_externo, LOW);
}

}
