#include "wifi_connection.h"
#include "requests.h"
#include "distance_measure.h"
#include <ArduinoJson.h>

// urls for server
const String domain = "http://10.10.101.136:5000/";
const String faceReco = domain + "recognisePerson";
const String captionImage = domain + "getImageCaption";
const String getText = domain + "getImageText";

// distance measurement
const int trigPin = D6;
const int echoPin = D5;
const int buzzerPin = D7;

void setup() {
  Serial.begin(115200);  // open the serial port at 9600 bps:
  Serial.println("Starting Device");
  pinMode(trigPin, OUTPUT);  // Sets the trigPin as an Output
  pinMode(echoPin, INPUT);   // Sets the echoPin as an Input
  pinMode(buzzerPin, OUTPUT);   // Sets the buzzer pin as output
  connectToWiFi();
}

void loop() {
  // getting command from talkback
  String res = get("http://api.thingspeak.com/talkbacks/48450/commands/execute.json?api_key=0JE5FBIWBIUINJEI");
  StaticJsonDocument<200> doc;

  DeserializationError error = deserializeJson(doc, res);

  if (error) {
    Serial.print(F("deserializeJson() failed: "));
    Serial.println(error.f_str());
    return;
  }

  String command = doc["command_string"];

  if (command == "L2") {
    //  retrieving text from image
    Serial.println("retrieving text from image");
    String res = get(getText);
    Serial.println(res);
  } else if (command == "L3") {
    // captioning the image
    Serial.println("captioning the image");
    String res = get(captionImage);
    Serial.println(res);
  } else if (command == "L4") {
    // recognize person
    Serial.println("recognizing person");
    String res = get(faceReco);
    Serial.println(res);
  } else if (command == "L5") {
    double dist = measureDistance(trigPin, echoPin);
    Serial.print(dist);
    Serial.println(" meters");
    
    if(dist<1){
      digitalWrite(buzzerPin,HIGH);
      delay(1000);
      digitalWrite(buzzerPin,LOW);
    }
  }

  delay(3000);
}
