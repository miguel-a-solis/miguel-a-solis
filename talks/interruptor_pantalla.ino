int interruptor = 35;
bool apretado = false;

void setup() {
  pinMode(interruptor, INPUT);
  Serial.begin(9600);
}

void loop() {

apretado = digitalRead(interruptor);
if(apretado){
  Serial.println("Interruptor apretado");
}

}
