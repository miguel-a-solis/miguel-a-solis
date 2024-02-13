#include <WiFi.h>
#include <WiFiClient.h>
#include <WiFiAP.h>

#define LED 32  
#define SENSOR 35

const char ssid[] = "mi_nodo_medidor";
const char password[] = "miclave123";

WiFiServer server(80);

void setup() {
  pinMode(LED, OUTPUT);
  pinMode(SENSOR, INPUT);
  Serial.begin(9600);
  WiFi.softAP(ssid, password);
  IPAddress IP = WiFi.softAPIP();
  Serial.print("Conectate a la red ");
  Serial.print(ssid);
  Serial.print(" y luego en el navegador web ingresa: ");
  Serial.println(IP);
  server.begin();

}

void loop() {
  WiFiClient client = server.available();

  if (client) {                          
    Serial.println("nuevo cliente conectado");       
    String currentLine = "";               
    while (client.connected()) {           
      if (client.available()) {            
        char c = client.read();            
        Serial.write(c);                   
        if (c == '\n') {                   
          if (currentLine.length() == 0) {
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type:text/html");
            client.println();

            client.print("Click <a href=\"/H\">aca</a> para prender LED.<br>");
            client.print("Click <a href=\"/L\">aca</a> para apagar LED.<br>");
            client.println();
            client.print("El interruptor esta ");
            if(digitalRead(SENSOR)){
              client.println("apretado");
            }else{
              client.println("sin apretar");
            }
            break;
          } else {   
            currentLine = "";
          }
        } else if (c != '\r') { 
          currentLine += c;     
        }

        if (currentLine.endsWith("GET /H")) {
          digitalWrite(LED, HIGH); 
        }
        if (currentLine.endsWith("GET /L")) {
          digitalWrite(LED, LOW);
        }

      }
    }

    client.stop();
    Serial.println("cliente desconectado");
  }
}
