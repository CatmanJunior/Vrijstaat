const char *NAME = "Controller1";
const char *TOPIC = "UTIL/CONTROLLER1";

void setupESP() {
  pinMode(5, INPUT);  //D1
}

void loopESP() {

  if (digitalRead(5) == HIGH) {

    client.publish("IntroVideo", "LA");

  }

}

void callbackESP(char* topic, byte * payload) {

}
