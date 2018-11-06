#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <Servo.h>

const char *ssid =  "Ziggo78F5D45";     // change according to your Network - cannot be longer than 32 characters!
const char *pass =  "Sx7phx8fnkeP"; // change according to your Network
const char *mqtt_server = "192.168.178.40";
const char *NAME = "HolletjesServo";
const char *TOPIC = "HB"; //HB

WiFiClient espClient;
PubSubClient client(espClient);


Servo servoA;  // create servo object to control a servo
Servo servoB;
Servo servoC;
Servo servoD;

Servo servoE;

int servoAState = 1;

long lastMsg = 0;
char msg[50];

void setup() {
  //D3 and D4 keep being HIGH despite not being HIGH, DONT USE FOR INPUT
  servoA.attach(5);  // attaches the servo on GIO2 to the servo object
  servoB.attach(4);
  servoC.attach(14);
  servoD.attach(16);
  servoE.attach(12);

  Serial.begin(115200);    // Initialize serial communications
  Serial.println(NAME);

  WiFi.begin(ssid, pass);

  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);

  while ((WiFi.status() != WL_CONNECTED)) {
    delay(500);
    Serial.print(".");
  }
  Serial.println(F("WiFi connected"));

}

void loop() {
  if (!client.connected()) {
    reconnect();
  }

  client.loop();
  delay(50);
}





void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect(NAME)) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("outTopic", "hello world");
      // ... and resubscribe
      client.subscribe(TOPIC);
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  Serial.println((char*)payload);
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
//  if ((char)payload[1] == '2') {
//    servoA.write(180);
//  }
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
