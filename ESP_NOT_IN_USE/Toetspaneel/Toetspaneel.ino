#define x1 1
#define x2 2
#define x3 3
#define x4 4
#define y1 5
#define y2 6
#define y3 7
#define y4 8

int x[] = {x1, x2, x3, x4};
int y[] = {y1, y2, y3, y4};


const char *NAME = "Name";
const char *TOPIC = "Topic"; //HB


String codes[] = { "1234", "3456",  "5434"};
int num_codes = 3;
char *a[10];
int rightcodes = 0;
int numcount = 0;
String tempcode;

String pad[4][4] = {
  {"1", "2", "3", "A"},
  {"4", "5", "6", "B"},
  {"7", "8", "9", "C"},
  {"*", "0", "#", "D"},
};

void setupESP() {
  for (int i = 0; i < 4; i++) {
    pinMode(x[i], OUTPUT);
    pinMode(y[i], INPUT);
  }
}

void loopESP() {

  for (int i = 0; i < 4; i++) {
    digitalWrite(x[i], HIGH);
    for (int j = 0; j < 4; j++) {
      if (digitalRead(y[j])) {
        String num = pad[i][j];
        Serial.println(num);
        tempcode += num;
        numcount++;
        if (numcount == 4) {
          //Check if code is i
          for (int i = 0; i < 4; i++) {
            if (tempcode.equals(codes[i])) {
              rightcodes++;
              //send mqqt
            }
            numcount = 0;
            tempcode = "";
          }
        }
      }
    }
    digitalWrite(x[i], LOW);
  }



}

void callbackESP(char* topic, byte * payload) {

}
