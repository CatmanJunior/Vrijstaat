#include <Servo.h>
const char *NAME = "HolletjesServo";
const char *TOPIC = "HB"; //HB
//const char *SIGNTOPIC = "SIGN/HolletjesServo";
const char *SIGNTOPIC = "SIGN" + "/HolletjesServo";

Servo servoA;  // create servo object to control a servo
Servo servoB;
Servo servoC;
Servo servoD;
Servo servoE;

int servoAState = 1;

void setupESP() {
  servoA.attach(5);  // attaches the servo on GIO2 to the servo object
  servoB.attach(4);
  servoC.attach(14);
  servoD.attach(16);
  servoE.attach(12);

}

void loopESP() {
}


void callbackESP(char* topic, byte * payload) {
  if (strcmp(topic, TOPIC) == 0) {
    if ((char)payload[1] == '1') {
      servoAState++;
      if (servoAState == 1) {
        servoA.write(160);
      }
      if (servoAState == 2) {
        servoA.write(40);
      }
      if (servoAState == 3) {
        servoA.write(100);
        servoAState = 0;
      }
    }
    if ((char)payload[1] == '3') {
      servoB.write(0);
    }
    if ((char)payload[1] == '4') {
      servoB.write(155);
    }
    if ((char)payload[1] == '5') {
      servoE.write(120);
    }
    if ((char)payload[1] == '6') {
      servoE.write(180);
    }
    if ((char)payload[1] == '7') {
      servoD.write(0);
    }
    if ((char)payload[1] == '8') {
      servoD.write(80);
    }
    if ((char)payload[1] == '9') {
      servoC.write(50);
    }
    if ((char)payload[1] == '0') {
      servoC.write(110);
    }

  }
}
