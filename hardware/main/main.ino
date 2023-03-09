#include "wifi_connection.h"
#include "requests.h"

const String domain = "http://192.168.1.8:5000/";

void setup()
{
  Serial.begin(115200); // open the serial port at 9600 bps:
  Serial.println("Starting Device");
  connectToWiFi();
}

void loop()
{
  String res = get(domain);
  Serial.println(res);
  delay(15000);
}
