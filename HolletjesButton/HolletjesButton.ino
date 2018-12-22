const char *NAME = "HolletjesButton";
const char *TOPIC = "LAB/HOL/BUTTONS";

bool A;
bool B;
bool C;
bool D;
bool E;

long lastMsg = 0;
char msg[50];

void setupESP() {
  pinMode(5, INPUT);  //D1
  pinMode(4, INPUT);  //D2
  pinMode(16, INPUT); //D0
  pinMode(14, INPUT); //D5
  pinMode(12, INPUT); //D6
}

void loopESP() {

  if (digitalRead(5) == HIGH) {
    if (A == false) {
      Serial.println("button 1");
      sendMsg(1);
      delay(500);
      A = true;
    }
  } else {
    if (A == true) {
      sendMsg(2);
      delay(500);
      A = false;
    }
  }

  if (digitalRead(4) == HIGH) {
    Serial.println("button 2");
    if (B == false) {
      sendMsg(3);
      delay(500);
      B = true;
    }
  } else {
    if (B == true) {
      sendMsg(4);
      delay(500);
      B = false;
    }
  }

  if (digitalRead(16) == HIGH) {
    Serial.println("button 3");
    if (C == false) {
      sendMsg(5);
      delay(500);
      C = true;
    }
  } else {
    if (C == true) {
      sendMsg(6);
      delay(500);
      C = false;
    }
  }
  if (digitalRead(14) == HIGH) {
    Serial.println("button 4");
    if (D == false) {
      sendMsg(7);
      delay(500);
      D = true;
    }
  } else {
    if (D == true) {
      sendMsg(8);
      delay(500);
      D = false;
    }
  }

  if (digitalRead(12) == HIGH) {
    Serial.println("button 5");
    if (E == false) {
      sendMsg(9);
      delay(500);
      E = true;
    }
  } else {
    if (E == true) {
      sendMsg(0);
      delay(500);
      E = false;
    }
  }
}

void callbackESP(char* topic, byte * payload){
  
}
