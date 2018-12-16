#include <FastLED.h>
#include <ESP32Servo.h>

#define F1 A4
#define F2 A5
#define SerA 2
#define T1 1
#define T2 2
#define B1 0
#define B2 6
#define Rotary1 35
#define Rotary2 25
#define RotarySw 26
#define KR 5
#define KL 4

int pins[] = {
  B1,B2, T1, T2, RotarySw, KL, KR
};

int len = 7;

int high[] = {
  LOW, LOW, LOW, LOW, LOW, LOW, LOW
};

#define NUM_LEDS 16
#define DATA_PIN 32

const char *NAME = "Crusher";
const char *TOPIC = "CRUSH"; //HB

CRGB leds[NUM_LEDS];

Servo servoA;

void setupESP() {
  
  servoA.attach(SerA);
  servoA.write(160);
  
  for (int i = 0; i < len; i++) {
    pinMode(pins[i], INPUT_PULLUP);
  }

  FastLED.addLeds<WS2812, DATA_PIN, GRB>(leds, NUM_LEDS);
  for (int i = 0; i < NUM_LEDS; i++) {
    leds[i] = CRGB::Green;
  }
}

void loopESP() {
  if (high[0] == HIGH){
    servoA.write(0);
  } else{
    servoA.write(160);
  }
  for (int i = 0; i < len; i++) {
    if (digitalRead(pins[i]) != high[i]) {
      high[i] = digitalRead(pins[i]);
      Serial.println(String(i) + String(high[i]).toInt());
      sendMsg((String(i) + String(high[i])).toInt());
    }
  }
}

void callbackESP(char* topic, byte * payload) {

}
