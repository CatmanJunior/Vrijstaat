const char *NAME = "PoepScanner";
const char *TOPIC = "poep"; //HB

#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN         5           //  d1
#define SS_PIN          15          //  d8
#define GRN_LED         4           //  d2
#define YEL_LED         0           //  d3
#define RED_LED         2           //  d4
#define BUZZ            16          //  d0

int num = 0;

MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance.

MFRC522::MIFARE_Key key;

String correct[] = { "04 DC 06 E2 90 5B 84",
                     "04 B5 06 E2 90 5B 84",
                     "04 E1 06 E2 90 5B 84",
                     "04 E5 07 E2 90 5B 84",
                     "04 D2 06 E2 90 5B 84",
                     "04 C7 04 E2 90 5B 84",
                     "04 CB 05 E2 90 5B 84",
                     "04 D7 06 E2 90 5B 84",
                     "04 C2 04 E2 90 5B 84",
                     "04 BD 04 E2 90 5B 84",
                     "04 B9 05 E2 90 5B 84",
                     "04 EA 07 E2 90 5B 84"
                   };

bool tSolved[4], kSolved[3], hSolved[5];
String readID = "";
unsigned long curr, start;
int count = 0;

void setupESP() {
  SPI.begin();        // Init SPI bus
  mfrc522.PCD_Init(); // Init MFRC522 card

  for (byte i = 0; i < 6; i++) {
    key.keyByte[i] = 0xFF;
  }

  dump_byte_array(key.keyByte, MFRC522::MF_KEY_SIZE);

  //init buzzer
  pinMode(BUZZ, OUTPUT);
  noTone(BUZZ);


  //init leds
  pinMode(RED_LED, OUTPUT);
  pinMode(YEL_LED, OUTPUT);
  pinMode(GRN_LED, OUTPUT);
  digitalWrite(RED_LED, LOW);
  digitalWrite(YEL_LED, LOW);
  digitalWrite(GRN_LED, LOW);

  //Set all bools to false
  for (int x = 0; x < 5; x++) {
    hSolved[x] = false;
  }

  for (int i = 0; i < 4; ++i) {
    tSolved[i] = false;

  }
  for (int j = 0; j < 3; j++) {
    kSolved[j] = false;
  }
}

void loopESP() {
  curr = millis();
  if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) {
    Serial.print("UID tag :");
    String readID = "";
    String currID = "";
    byte letter;
    for (byte i = 0; i < mfrc522.uid.size; i++)
    {
      Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
      Serial.print(mfrc522.uid.uidByte[i], HEX);
      currID.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
      currID.concat(String(mfrc522.uid.uidByte[i], HEX));
    }

    Serial.println();
    Serial.print("Message : ");
    currID.toUpperCase();

    if (currID.substring(1) != readID.substring(1))
    {
      readID = currID;

      for (int x = 0; x < 12; ++x) {
        if (readID.substring(1) == correct[x]) {
          if (x < 4) {
            num = 1;                      //  groen
          } else if (x >= 4 && x < 8) {
            num = 2;                      //  geel
          } else if (x >= 8) {
            num = 0;                      //  rood
          }
          // num = round(random(0, 2));
          blink_led(num);
          count++;
          //Send data to broker
          if (count == 12) {
            count = 0;
          }
          sendMsg(count);
        }
      }
    }
    //  Master Key
    if (readID.substring(1) == "C9 CE 7F 00")
    {
      digitalWrite(GRN_LED, HIGH);
      digitalWrite(YEL_LED, HIGH);
      digitalWrite(RED_LED, HIGH);
      tone(BUZZ, 800);
      delay(500);
      digitalWrite(GRN_LED, LOW);
      digitalWrite(YEL_LED, LOW);
      digitalWrite(RED_LED, LOW);
      noTone(BUZZ);
      delay(500);
      tone(BUZZ, 300);
      digitalWrite(GRN_LED, HIGH);
      digitalWrite(YEL_LED, HIGH);
      digitalWrite(RED_LED, HIGH);
      delay(1000);
      digitalWrite(GRN_LED, LOW);
      digitalWrite(YEL_LED, LOW);
      digitalWrite(RED_LED, LOW);
      noTone(BUZZ);
      count = 0;
      delay(1000);

    }
  }
}

void callbackESP(char* topic, byte * payload) {

}



void blink_led(int _c) {

  tone(BUZZ, 1000);
  delay(100);
  tone(BUZZ, 1200);
  delay(100);
  tone(BUZZ, 800);
  delay(200);
  noTone(BUZZ);

  if (_c == 0) {

    digitalWrite (GRN_LED, HIGH);
    delay(500);
    digitalWrite (GRN_LED, LOW);
    delay(500);
    digitalWrite (GRN_LED, HIGH);
    delay(3000);
    digitalWrite (GRN_LED, LOW);
  }

  if (_c == 1)
  {

    digitalWrite (YEL_LED, HIGH);
    delay(500);
    digitalWrite (YEL_LED, LOW);
    delay(500);
    digitalWrite (YEL_LED, HIGH);
    delay(3000);
    digitalWrite (YEL_LED, LOW);

  }
  if (_c == 2)
  {

    digitalWrite (RED_LED, HIGH);
    delay(500);
    digitalWrite (RED_LED, LOW);
    delay(500);
    digitalWrite (RED_LED, HIGH);
    delay(3000);
    digitalWrite (RED_LED, LOW);
  }


}

void dump_byte_array(byte *buffer, byte bufferSize) {
  for (byte i = 0; i < bufferSize; i++) {
    Serial.print(buffer[i] < 0x10 ? " 0" : " ");
    Serial.print(buffer[i], HEX);
  }
}
