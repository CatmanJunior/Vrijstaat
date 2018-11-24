/*     Arduino Color Sensing Tutorial

    by Dejan Nedelkovski, www.HowToMechatronics.com

*/
#define FASTLED_FORCE_SOFTWARE_SPI
#include <FastLED.h>
#define B1 4
#define B2 5
#define T1 6
#define T2 7
#define Rotary1 8
#define Rotary2 9

#define NUM_LEDS 16
#define DATA_PIN 2


int counter = 0;
int aState;
int aLastState;

CRGB leds[NUM_LEDS];
int frequency = 0;
void setup() {
  pinMode(B1, INPUT_PULLUP);
  pinMode(B2, INPUT_PULLUP);
  pinMode(T1, INPUT_PULLUP);
  pinMode(T2, INPUT_PULLUP);
  pinMode (Rotary1, INPUT);
  pinMode (Rotary2, INPUT);
  aLastState = digitalRead(outputA);
  FastLED.addLeds<WS2812, DATA_PIN, GRB>(leds, NUM_LEDS);
  Serial.begin(9600);
}
void loop() {
  for (int i = 0; i < 16; i++) {
    leds[i] = CRGB::Black;
  }
  if (digitalRead(B1) == HIGH && digitalRead(B2) == HIGH) {
    for (int i = 0; i < 4; i++) {
      leds[i] = CRGB::Red;
    }
  }
  if (digitalRead(T1) == HIGH && digitalRead(T2) == HIGH) {
    for (int i = 4; i < 8; i++) {
      leds[i] = CRGB::Red;
    }
  }

  //Rotary
  aState = digitalRead(outputA);
  // If the previous and the current state of the outputA are different, that means a Pulse has occured
  if (aState != aLastState) {
    // If the outputB state is different to the outputA state, that means the encoder is rotating clockwise
    if (digitalRead(outputB) != aState) {
      counter ++;
    } else {
      counter --;
    }
    Serial.print("Position: ");
    Serial.println(counter);
  }
  aLastState = aState; // Updates the previous state of the outputA with the current state


  FastLED.show();
  Serial.println("showing");
  delay(50);
}
