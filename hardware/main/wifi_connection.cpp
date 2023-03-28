#include "wifi_connection.h"
#include <ESP8266WiFi.h>

const char *ssid = "PRINCEMISHRA 4240";
const char *password = "0123456789";

void connectToWiFi() {
  Serial.print("Connecting to WiFi.........");
  WiFi.begin(ssid, password);
  int retries = 0;

  while ((WiFi.status() != WL_CONNECTED) && (retries < 15)) {
    retries++;
    delay(500);
    Serial.print(".");
  }

  if (WiFi.status() == WL_CONNECTED) {
    Serial.println("WiFi connected!");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
  }else {
    Serial.println("WiFi connection FAILED");
  }
}