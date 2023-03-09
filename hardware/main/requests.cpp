#include "requests.h"
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

String get(String url) {
  HTTPClient http;
  WiFiClient client;
  http.begin(client, url);
  int httpCode = http.GET();
  String payload = http.getString();
  http.end();
  return payload;
}
