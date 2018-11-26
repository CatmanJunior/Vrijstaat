#include <FastLED.h>
#include "Timer.h"

#define T1 4
#define T2 5
#define B1 6
#define B2 7
#define Rotary1 8
#define Rotary2 9
#define RotarySw 10

#define NUM_LEDS 16
#define DATA_PIN 2


const char *NAME = "Crusher";
const char *TOPIC = "CRUSH"; //HB

int counter = 0;
int aState;
int aLastState;

Timer t;

int SideA = 0;
int SideB = 0;
int SideC = 0;
int SideD = 0;

int But1 = 0;
int But2 = 0;

CRGB leds[NUM_LEDS];
int frequency = 0;

void setupESP() {
  pinMode(B1, INPUT_PULLUP);
  pinMode(B2, INPUT_PULLUP);
  pinMode(T1, INPUT_PULLUP);
  pinMode(T2, INPUT_PULLUP);
  pinMode (RotarySw, INPUT_PULLUP);

  pinMode (Rotary1, INPUT);
  pinMode (Rotary2, INPUT);

  t.every(200, checkA, 0);
  aLastState = digitalRead(Rotary1);
  FastLED.addLeds<WS2812, DATA_PIN, GRB>(leds, NUM_LEDS);
  for (int i = 0; i < NUM_LEDS; i++) {
    leds[i] = CRGB::Green;
  }
}



void SideAFunc() {
  //1,1,2,2+1,2+1 = YBRG
  switch (SideA) {
    case 0:
      if (digitalRead(B1) == LOW) {
        SideA = 1;
        leds[0] = CRGB::Red;
      }
      break;
    case 1:
      if (digitalRead(B1) == HIGH) {
        SideA = 2;
      }
      break;
    case 2:
      if (digitalRead(B1) == LOW) {
        SideA = 3;
        leds[1] = CRGB::Red;

      }
      if (digitalRead(B2) == LOW) {
        SideA = 0;
        for (int i = 0; i < 4; i++) {
          leds[i] = CRGB::Black;
        }
      }
      break;
    case 3:
      if (digitalRead(B1) == HIGH) {
        SideA = 4;
      }
      break;
    case 4:
      if (digitalRead(B2) == LOW) {
        SideA = 5;
        leds[2] = CRGB::Red;
      }
      if (digitalRead(B1) == LOW) {
        SideA = 0;
        for (int i = 0; i < 4; i++) {
          leds[i] = CRGB::Black;
        }
      }
      break;
    case 5:
      if (digitalRead(B2) == LOW && digitalRead(B1) == LOW) {
        SideA = 6;
      }
      if (digitalRead(B2) == HIGH) {
        SideA = 0;
        for (int i = 0; i < 4; i++) {
          leds[i] = CRGB::Black;
        }
      }
      break;
    case 6:
      if (digitalRead(B2) == LOW && digitalRead(B1) == HIGH) {
        SideA = 7;
      }
      if (digitalRead(B2) == HIGH) {
        SideA = 0;
        for (int i = 0; i < 4; i++) {
          leds[i] = CRGB::Black;
        }
      }
      break;
    case 7:
      if (digitalRead(B2) == LOW && digitalRead(B1) == LOW) {
        SideA = 8;
      }
      if (digitalRead(B2) == HIGH) {
        SideA = 0;
        for (int i = 0; i < 4; i++) {
          leds[i] = CRGB::Black;
        }
      }
      break;
    case 8:
      leds[0] = CRGB::Yellow;
      leds[1] = CRGB::Blue;
      leds[2] = CRGB::Red;
      leds[3] = CRGB::Green;
      if (digitalRead(B1) == LOW && digitalRead(B2) == HIGH) {
        SideA = 0;
        for (int i = 0; i < 4; i++) {
          leds[i] = CRGB::Black;
        }
      }
      break;
  }
}

void SideBFunc() {

  switch (SideB) {
    case 0:
      if (digitalRead(T1) == LOW) {
        SideB = 1;
        leds[8] = CRGB::Red;
      }
      break;
    case 1:
      if (digitalRead(T1) == HIGH) {
        SideB = 2;
      }
      break;
    case 2:
      if (digitalRead(T1) == LOW) {
        SideB = 3;
        leds[9] = CRGB::Red;

      }
      if (digitalRead(T2) == LOW) {
        SideB = 0;
        for (int i = 8; i < 12; i++) {
          leds[i] = CRGB::Black;
        }
      }
      break;
    case 3:
      if (digitalRead(T1) == HIGH) {
        SideB = 4;
      }
      break;
    case 4:
      if (digitalRead(T2) == LOW) {
        SideB = 5;
        leds[10] = CRGB::Red;
      }
      if (digitalRead(T1) == LOW) {
        SideB = 0;
        for (int i = 8; i < 12; i++) {
          leds[i] = CRGB::Black;
        }
      }
      break;
    case 5:
      if (digitalRead(T2) == LOW && digitalRead(T1) == LOW) {
        SideB = 6;
      }
      if (digitalRead(T2) == HIGH) {
        SideB = 0;
        for (int i = 8; i < 12; i++) {
          leds[i] = CRGB::Black;
        }
      }
      break;
    case 6:
      if (digitalRead(T2) == LOW && digitalRead(T1) == HIGH) {
        SideB = 7;
      }
      if (digitalRead(T2) == HIGH) {
        SideB = 0;
        for (int i = 8; i < 12; i++) {
          leds[i] = CRGB::Black;
        }
      }
      break;
    case 7:
      if (digitalRead(T2) == LOW && digitalRead(T1) == LOW) {
        SideB = 8;
      }
      if (digitalRead(T2) == HIGH) {
        SideB = 0;
        for (int i = 8; i < 12; i++) {
          leds[i] = CRGB::Black;
        }
      }
      break;
    case 8:
      leds[8] = CRGB::Yellow;
      leds[9] = CRGB::Blue;
      leds[10] = CRGB::Red;
      leds[11] = CRGB::Green;
      if (digitalRead(T1) == LOW && digitalRead(T2) == HIGH) {
        SideB = 0;
        for (int i = 4; i < 8; i++) {
          leds[i] = CRGB::Black;
        }
      }
      break;
  }
}


void SideCFunc() {
  //Rotary
  aState = digitalRead(Rotary1);
  // If the previous and the current state of the outputA are different, that means a Pulse has occured
  if (aState != aLastState) {
    // If the outputB state is different to the outputA state, that means the encoder is rotating clockwise
    if (digitalRead(Rotary2) != aState) {
      counter ++;
    } else {
      counter --;
    }
    Serial.print("Position: ");
    Serial.println(counter);
    Serial.println(digitalRead(RotarySw));
  }
  aLastState = aState; // Updates the previous state of the outputA with the current state

  if (SideC != 6) {
    if (counter > 30) {
      counter = 0;
    } else if (counter > 15) {
      leds[7] = CRGB::Blue;
    } else if (counter > 5) {
      leds[7] = CRGB::Green;
    } else if (counter > 0) {
      leds[7] = CRGB::HotPink;
    } else if (counter > -5) {
      leds[7] = CRGB::BlueViolet;
    } else if (counter > -15) {
      leds[7] = CRGB::DarkOrange;
    } else if (counter > -30) {
      leds[7] = CRGB::Yellow;
    } else if (counter < -30) {
      counter = 0;
    }
  }


  switch (SideC) {
    case 0:
      if (counter > 15) {
        SideC = 1;
        leds[4] = CRGB::Red;
      }
      break;
    case 1:
      if (counter < 0) {
        SideC = 2;
      }
      break;
    case 2:
      if (digitalRead(RotarySw) == LOW) {
        SideC = 3;
        leds[5] = CRGB::Red;
      }
      break;
    case 3:
      if (counter < -15) {
        SideC = 4;
      }
      break;
    case 4:
      if (counter > 0) {
        SideC = 5;
        leds[6] = CRGB::Red;
      }
      if (digitalRead(RotarySw) == LOW) {
        counter = 0;
        SideC = 0;
        for (int i = 4; i < 8; i++) {
          leds[i] = CRGB::Black;
        }
      }
      break;
    case 5:
      if (counter < -15) {
        SideC = 6;
      }
      if (counter > 15) {
        counter = 0;
        SideC = 0;
        for (int i = 4; i < 8; i++) {
          leds[i] = CRGB::Black;
        }
      }
      break;

    case 6:
      leds[4] = CRGB::Yellow;
      leds[5] = CRGB::Blue;
      leds[6] = CRGB::Red;
      leds[7] = CRGB::Green;
      if (digitalRead(RotarySw) == LOW) {
        SideC = 0;
        for (int i = 4; i < 8; i++) {
          leds[i] = CRGB::Black;
        }
      }
      break;
  }
}


void loopESP() {
  SideAFunc();
  SideBFunc();
  SideCFunc();
  t.update();
  //  if (digitalRead(T1) == HIGH && digitalRead(T2) == HIGH) {
  //    for (int i = 4; i < 8; i++) {
  //      leds[i] = CRGB::Red;
  //    }
  //
  //  }


  FastLED.show();


}

void callbackESP(char* topic, byte * payload) {

}

void checkA(void* context) {


  Serial.print("SideA: ");
  Serial.println(SideA);
  Serial.print("SideB: ");
  Serial.println(SideC);
}
