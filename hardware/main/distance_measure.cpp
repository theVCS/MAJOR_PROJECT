#include "distance_measure.h"

//define sound velocity in cm/uS
#define SOUND_VELOCITY 0.034

double measureDistance(const int trigPin, const int echoPin) {
  // Clears the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Reads the echoPin, returns the sound wave travel time in microseconds
  double duration = pulseIn(echoPin, HIGH);

  // Calculate the distance in centimeters
  double distanceCm = duration * SOUND_VELOCITY / 2;

  return distanceCm/100;
}