#include <FastLED.h>
#include <Servo.h>


//  Led's
#define LED_DATA1 5  // D1
#define LED_DATA2 0 // D3
#define NUM_LEDS 18
#define COLOR_ORDER GRB
#define LED_TYPE    WS2811
#define FRAMES_PER_SECOND  120
#define NUM_STRIPS 2
CRGB leds[NUM_STRIPS][NUM_LEDS];

const char *NAME = "MedKast";
const char *TOPIC = "LAB/MEDKAST";

//  Servo's
Servo servo[6];  // create servo object to control a servo
int pins[6] = { 13, 15, 4, 12, 14, 2  };

//  ColorPallette
int r = 51;
int g = 152;
int b = 255;
CRGB colorOff = CRGB(r, g, b);

int cr = 250;
int cg = 152;
int cb = 5;
CRGB colorOn = CRGB(cr, cg, cb);
const int brightness = 128;

//  Door booleans
bool doorState[6];
bool masterSwitch = false;

void setupESP() {
  FastLED.addLeds<WS2812B, LED_DATA1, GRB>(leds[0], NUM_LEDS);
  FastLED.addLeds<WS2812B, LED_DATA2, GRB>(leds[1], NUM_LEDS);
  FastLED.delay(1000 / FRAMES_PER_SECOND);
  FastLED.setBrightness( brightness );

  for (int i = 0; i < 6; i++)
  {
    doorState[i] = false;
  }

  for (int i = 0; i < 6; i++)
  {
    doorState[i] = false;
    servo[i].attach(pins[i]);
    servo[i].write(90);
  }

  for (int i = 0; i < NUM_LEDS; ++i)
  {
    leds[0][i] = colorOff;
    leds[1][i] = colorOff;
  }

  FastLED.show();
}

void loopESP() {

  for (int i = 0; i < 6; ++i)
  {
    for (int j = 0; j < 6; ++j)
    {
      // make sets of 6 leds per door
      int num = (6 * i) + j;

      //  check the state of the door
      if ( i < 3 )
      {
        if (doorState[i] == true)
        {
          // if open, set 6 leds to correctRGB
          leds[1][num] = colorOn;
          servo[i].write(90);
        }
        else
        {
          //if closed keep state
          leds[1][num] = colorOff;
          servo[i].write(0);
        }
      }
      else
      {
        num -= 18;
        if (doorState[i] == true)
        {
          leds[0][num] = colorOn;
          servo[i].write(90);
        }
        else
        {
          leds[0][num] = colorOff;
          servo[i].write(0);
        }
      }
    }
  }

  FastLED.show();
}

void callbackESP(char* topic, byte * payload) {
  if ((char)payload[1] == '1') {
    if ((char)payload[2] == 'A') {

      doorState[0] = false;
    }
    if ((char)payload[2] == 'B') {

      doorState[0] = true;
    }
  }

  if ((char)payload[1] == '2') {
    if ((char)payload[2] == 'A') {

      doorState[1] = false;
    }
    if ((char)payload[2] == 'B') {

      doorState[1] = true;
    }
  }
  if ((char)payload[1] == '3') {
    if ((char)payload[2] == 'A') {

      doorState[2] = false;
    }
    if ((char)payload[2] == 'B') {

      doorState[2] = true;
    }
  }
  if ((char)payload[1] == '4') {
    if ((char)payload[2] == 'A') {

      doorState[3] = false;
    }
    if ((char)payload[2] == 'B') {

      doorState[3] = true;
    }
  }
  if ((char)payload[1] == '5') {
    if ((char)payload[2] == 'A') {

      doorState[4] = false;
    }
    if ((char)payload[2] == 'B') {
      doorState[4] = true;
    }
  }
  if ((char)payload[1] == '6') {
    if ((char)payload[2] == 'A') {

      doorState[5] = false;
    }
    if ((char)payload[2] == 'B') {

      doorState[5] = true;
    }
  }
  if ((char)payload[1] == '7') {
    if ((char)payload[2] == 'A') {
      masterSwitch = true;
    }
    if ((char)payload[2] == 'B') {
      masterSwitch = false;
    }
  }

}
