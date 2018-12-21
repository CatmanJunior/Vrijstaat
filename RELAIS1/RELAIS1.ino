const char *NAME = "LAMPLABTL";
const char *TOPIC = "LAB/RELAIS/TL"; //HB

long lastMsg = 0;
char msg[50];

void setupESP() {
  pinMode(2, OUTPUT);  //D2
}

void loopESP() {

}

void callbackESP(char* topic, byte * payload) {
  if (strcmp(topic, TOPIC) == 0) {
    if ((char)payload[1] == '1') {
      digitalWrite(2,HIGH);
    }
    if ((char)payload[1] == '0') {
      digitalWrite(2,LOW);
    } 
  }
}
