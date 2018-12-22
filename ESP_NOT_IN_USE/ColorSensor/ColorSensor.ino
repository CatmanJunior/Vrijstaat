/*     Arduino Color Sensing Tutorial

    by Dejan Nedelkovski, www.HowToMechatronics.com

*/
const char *NAME = "ColorSensor";
const char *TOPIC = "CS"; //HB

#include <FastLED.h>
#define S0 4
#define S1 16
#define S2 5
#define S3 0
#define sensorOut 13
#define L1 14

#define NUM_LEDS 3
#define DATA_PIN 12
CRGB leds[NUM_LEDS];
int frequency = 0;


int red;
int blue;
int green;
void setupESP() {
  pinMode(S0, OUTPUT);
  pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT);
  pinMode(S3, OUTPUT);
  pinMode(sensorOut, INPUT);
  //  Right now its working strangly, put led on 3v
  pinMode(L1, OUTPUT);
  digitalWrite(L1, HIGH);

  //
  //  // Setting frequency-scaling to 20%
  digitalWrite(S0, HIGH);
  digitalWrite(S1, LOW);

  FastLED.addLeds<WS2812, DATA_PIN, GRB>(leds, NUM_LEDS);
  Serial.begin(9600);
}

void loopESP() {
  // Setting red filtered photodiodes to be read
  digitalWrite(S2, LOW);
  digitalWrite(S3, LOW);
  // Reading the output frequency
  red = pulseIn(sensorOut, LOW);
  // Printing the value on the serial monitor
  Serial.print("R= ");//printing name
  Serial.print(red);//printing RED color frequency
  Serial.print("  ");
  delay(100);
  // Setting Green filtered photodiodes to be read
  digitalWrite(S2, HIGH);
  digitalWrite(S3, HIGH);
  // Reading the output frequency
  green = pulseIn(sensorOut, LOW);
  // Printing the value on the serial monitor
  Serial.print("G= ");//printing name
  Serial.print(green);//printing RED color frequency
  Serial.print("  ");
  delay(100);
  // Setting Blue filtered photodiodes to be read
  digitalWrite(S2, LOW);
  digitalWrite(S3, HIGH);
  // Reading the output frequency
  blue = pulseIn(sensorOut, LOW);
  // Printing the value on the serial monitor
  Serial.print("B= ");//printing name
  Serial.print(blue);//printing RED color frequency
  Serial.println("  ");
  delay(100);

  leds[0] = CRGB::Red;
  FastLED.show();
  Serial.println("showing");
  
  // Now turn the LED off, then pause
  leds[0] = CRGB::Black;
  FastLED.show();
  sendColor(red, green, blue);
}


void callbackESP(char* topic, byte * payload){
  
}
