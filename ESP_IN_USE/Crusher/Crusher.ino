#include <FastLED.h>
#include <ESP32Servo.h>

#define F2 32
#define F1 33
#define SerA 2
#define T1 0
#define T2 4
#define B1 14
#define B2 27
#define Rotary1 35
#define Rotary2 25
#define RotarySw 26
#define KR 16
#define KL 17
#define DATA_PIN 13 //LED

#define NUM_LEDS 16

const char *NAME = "Crusher";
const char *TOPIC = "LAB/CRUSHER/#";

const char *INPUTTOPIC[] = {
  "LAB/CRUSHER/b1",
  "LAB/CRUSHER/b2",
  "LAB/CRUSHER/t1",
  "LAB/CRUSHER/t2",
  "LAB/CRUSHER/rS",
  "LAB/CRUSHER/kl",
  "LAB/CRUSHER/kr",
  "LAB/CRUSHER/f1",
  "LAB/CRUSHER/f2"
};

const char *OUPUTTOPIC[] = {
  "LAB/CRUSHER/LED",
  "LAB/CRUSHER/SERVO",
};

int pins[] = {
  B1, B2, T1, T2, RotarySw, KL, KR
};

int len = 7;

int high[] = {
  HIGH, HIGH, HIGH, HIGH, HIGH, HIGH, HIGH
};

CRGB leds[NUM_LEDS];

Servo servoA;

int valueA = 0;
int valueB = 0;

void setupESP() {
  valueA = analogRead(F1);
  valueB = analogRead(F2);
  servoA.attach(SerA);
  servoA.write(50);
  pinMode(F1, INPUT);
  pinMode(F2, INPUT);

  for (int i = 0; i < len; i++) {
    pinMode(pins[i], INPUT_PULLUP);
  }

  FastLED.addLeds<WS2812, DATA_PIN, GRB>(leds, NUM_LEDS);
  for (int i = 0; i < NUM_LEDS; i++) {
    leds[i] = CRGB::Green;
  }
}

void loopESP() {
  for (int i = 0; i < len; i++) {
    if (digitalRead(pins[i]) != high[i]) {
      high[i] = digitalRead(pins[i]);
      sendInput(INPUTTOPIC[i], !high[i]);
    }
  }
}
//  if (abs(valueA - analogRead(F1)) > 400) {
//    Serial.println(analogRead(F1));
//    valueA = analogRead(F1);
//    sendInput(INPUTTOPIC[len], valueA);
//  }
//  if (abs(valueB -   analogRead(F2)) > 400) {
//    Serial.println(analogRead(F2));
//    valueB = analogRead(F2);
//    sendInput(INPUTTOPIC[len + 1], valueB);
//  }
//}

void callbackESP(char* topic, byte * payload) {
  if ((char)payload[1] == 'A') {
    servoA.write(160);
  } else if ((char)payload[1] == 'B') {
    servoA.write(50);
  }
}
