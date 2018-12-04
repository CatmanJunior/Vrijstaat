#include <FastLED.h>
#include <Servo.h>

#include <BlynkSimpleEsp8266.h>
#define BLYNK_PRINT Serial

//  Led's
#define LED_DATA1 5  // D1
#define LED_DATA2 0 // D3
#define NUM_LEDS 18
#define COLOR_ORDER GRB
#define LED_TYPE    WS2811
#define FRAMES_PER_SECOND  120

CRGB leds[(NUM_LEDS - 1)];
CRGB leds2[NUM_LEDS];

//  Blynk authentication key
const char auth[] = "930fab0e15964e8690aa1671b4e11d33";

const char *NAME = "MedKast";
const char *TOPIC = "Med"; //HB

//  Servo's
Servo servoA;  // create servo object to control a servo
Servo servoB;
Servo servoC;
Servo servoD;
Servo servoE;
Servo servoF;

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
bool doorState[6] ;

// Blynk msg's
BLYNK_WRITE(V0)
{
  doorState[0]  = param.asInt();
  Serial.print("Door 0 is: ");
  Serial.println(doorState[0]);
}

BLYNK_READ(V0)
{
  Blynk.virtualWrite(V0, doorState[0]);
}

BLYNK_WRITE(V1)
{
  doorState[1]  = param.asInt();
  Serial.print("Door 1 is: ");
  Serial.println(doorState[1]);
}

BLYNK_READ(V1)
{
  Blynk.virtualWrite(V1, doorState[1]);
}


BLYNK_WRITE(V2)
{
  doorState[2]  = param.asInt();
  Serial.print("Door 2 is: ");
  Serial.println(doorState[2]);
}

BLYNK_READ(V2)
{
  Blynk.virtualWrite(V2, doorState[2]);
}


BLYNK_WRITE(V3)
{
  doorState[3]  = param.asInt();
  Serial.print("Door 3 is: ");
  Serial.println(doorState[3]);
}

BLYNK_READ(V3)
{
  Blynk.virtualWrite(V3, doorState[3]);
}

BLYNK_WRITE(V4)
{
  doorState[4]  = param.asInt();
  Serial.print("Door 4 is: ");
  Serial.println(doorState[4]);
}

BLYNK_READ(V4)
{
  Blynk.virtualWrite(V4, doorState[4]);
}


BLYNK_WRITE(V5)
{
  doorState[5]  = param.asInt();
  Serial.print("Door 5 is: ");
  Serial.println(doorState[5]);
}

BLYNK_READ(V5)
{
  Blynk.virtualWrite(V5, doorState[5]);
}

void setupESP() {
  FastLED.addLeds<WS2812B, LED_DATA1, GRB>(leds, NUM_LEDS);
  FastLED.addLeds<WS2812B, LED_DATA2, GRB>(leds2, NUM_LEDS);
  FastLED.setBrightness( brightness );
  FastLED.delay(1000 / FRAMES_PER_SECOND);
  FastLED.setBrightness( brightness );

  for (int i = 0; i < 6; i++)
  {
    doorState[i] = false;
  }

  servoA.attach(4);   // d2
  servoB.attach(14);  // d5
  servoC.attach(12);  // d6
  servoD.attach(13);  // d7
  servoE.attach(15);  // d8
  servoF.attach(2);   // d4


  for (int i = 0; i < NUM_LEDS - 1; ++i)
  {
    leds[i] = colorOff;
  }
  for (int i = 0; i < NUM_LEDS; ++i)
  {
    leds2[i] = colorOff;
  }
  FastLED.show();
  servoA.write(0);
  servoB.write(0);
  servoC.write(0);
  servoD.write(0);
  servoE.write(0);
  servoF.write(0);

  Blynk.begin(auth, ssid, pass);
}

void loopESP() {
  for (int i = 0; i < 3; ++i)
  {
    for (int j = 0; j < 5; ++j)
    {
      // make sets of 6 leds per door
      int num = (6 * i) + j;

      //  check the state of the door
      if (doorState[i] == true)
      {
        // if open, set 6 leds to correctRGB
        leds[num] = colorOn;
      }
      else
      {
        //if closed keep state
        leds[num] = colorOff;
      }
    }
  }
  for (int i = 3; i < 6; ++i)
  {
    for (int j = 0; j < 6; ++j)
    {
      // make sets of 6 leds per door
      int num = (6 * i) + j;

      //  check the state of the door
      if (doorState[i] == true)
      {
        // if open, set 6 leds to correctRGB
        leds2[num] = colorOn;
      }
      else
      {
        //if closed keep state
        leds2[num] = colorOff;
      }
    }
  }
  FastLED.show();
  Blynk.run();
}

void callbackESP(char* topic, byte * payload) {
  if ((char)payload[1] == '1') {
    if ((char)payload[2] == 'A') {
      servoA.write(180);
      doorState[0] = false;
    }
    if ((char)payload[2] == 'B') {
      servoA.write(90);
      doorState[0] = true;
    }
  }

  if ((char)payload[1] == '2') {
    if ((char)payload[2] == 'A') {
      servoB.write(180);
      doorState[1] = false;
    }
    if ((char)payload[2] == 'B') {
      servoB.write(90);
      doorState[1] = true;
    }
  }
  if ((char)payload[1] == '3') {
    if ((char)payload[2] == 'A') {
      servoC.write(180);
      doorState[2] = false;
    }
    if ((char)payload[2] == 'B') {
      servoC.write(90);
      doorState[2] = true;
    }
  }
  if ((char)payload[1] == '4') {
    if ((char)payload[2] == 'A') {
      servoD.write(180);
      doorState[3] = false;
    }
    if ((char)payload[2] == 'B') {
      servoD.write(90);
      doorState[3] = true;
    }
  }
  if ((char)payload[1] == '5') {
    if ((char)payload[2] == 'A') {
      servoE.write(180);
      doorState[4] = false;
    }
    if ((char)payload[2] == 'B') {
      servoE.write(90);
      doorState[4] = true;
    }
  }
  if ((char)payload[1] == '6') {
    if ((char)payload[2] == 'A') {
      servoF.write(180);
      doorState[5] = false;
    }
    if ((char)payload[2] == 'B') {
      servoF.write(90);
      doorState[5] = true;
    }
  }
}
