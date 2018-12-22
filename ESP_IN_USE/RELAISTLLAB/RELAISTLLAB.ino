const char *NAME = "LampLabTL";
const char *TOPIC = "LAB/RELAIS/TL";

#define RELAIS 13

void setupESP() {
  pinMode(RELAIS, OUTPUT);  //D7
  digitalWrite(RELAIS,HIGH);
}

void loopESP() {

}

void callbackESP(char* topic, byte * payload) {
  if (strcmp(topic, TOPIC) == 0) {
    if ((char)payload[0] == '1') {
      digitalWrite(RELAIS,HIGH);
    }
    if ((char)payload[0] == '0') {
      digitalWrite(RELAIS,LOW);
    } 
  }
}
