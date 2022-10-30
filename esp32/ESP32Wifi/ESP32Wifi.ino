#include <WiFi.h>
 
const char* ssid = ""; // CONFIG
const char* password =  ""; // CONFIG
 
const uint16_t port = 8091;
const char * host = "192.168.137.1";

WiFiClient client;

/* 
 *  Connects esp32 to wifi by ssid and password. 
 *  Then connect to pc on same wifi by using a host ip and selected port.
 */
void setup()
{
 
  Serial.begin(115200);
 
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("...");
  }
 
  Serial.print("WiFi connected with IP: ");
  Serial.println(WiFi.localIP());
 
}
 
void loop()
{
    if (!client.connected()) {
      if (!client.connect(host, port)) {
          Serial.println("Connection to host failed"); 
          return;
      }
    }
    Serial.println("Connected to server successful!");
    client.println("Hello!");
    delay(500);
}
