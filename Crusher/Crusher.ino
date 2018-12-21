#include <FastLED.h>
#include <ESP32Servo.h>

#define F1 A4
#define F2 A5
#define SerA 2
#define T1 0
#define T2 4
#define B1 33
#define B2 32
#define Rotary1 35
#define Rotary2 25
#define RotarySw 26
#define KR 16
#define KL 17

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
      sendMsg((String(i+1) + String(high[i])).toInt());
      
    }
  }
}

void callbackESP(char* topic, byte * payload) {

}

int DecodeR(byte* rgb) {
  String newR;
  for (int i = 0; i < 3; i++) {
    newR += (char)rgb[i];
  }
  return newR.toInt();
}

int DecodeG(byte* rgb) {
  String newG;
  for (int i = 0; i < 3; i++) {
    newG += (char)rgb[i];
  }
  return newG.toInt();
}

int DecodeB(byte* rgb) {
  String newB;
  for (int i = 0; i < 3; i++) {
    newB += (char)rgb[i];
  }
  return newB.toInt();
}
