#include "requests.h"
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

const int timeout = 50000;

String get(String url) {
  Serial.println("get request to " + url);
    WiFiClient client;
    HTTPClient http;

    http.setTimeout(timeout);

    if(http.begin(client, url)){
      int httpCode = http.GET();

      if (httpCode > 0) {
        Serial.printf("[HTTP] GET... code: %d\n", httpCode);

        if (httpCode == HTTP_CODE_OK || httpCode == HTTP_CODE_MOVED_PERMANENTLY) {
          String payload = http.getString();
          Serial.println(payload);
          return payload;
        }
      } else {
        Serial.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str());
      }
            http.end();
    }else {
      Serial.printf("[HTTP} Unable to connect\n");
    }
    
  return "{}";
}
