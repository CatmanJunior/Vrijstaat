#include <ESP8266WiFi.h>
#include <PubSubClient.h>

const char *ssid =  "Ziggo78F5D45";     // change according to your Network - cannot be longer than 32 characters!
const char *pass =  "Sx7phx8fnkeP"; // change according to your Network
const char *mqtt_server = "192.168.178.40";
const char *NAME = "HolletjesButton";
const char *TOPIC = "HB"; //HB

bool A;
bool B;
bool C;
bool D;
bool E;
WiFiClient espClient;
PubSubClient client(espClient);

long lastMsg = 0;
char msg[50];

void setup() {
  //D3 and D4 keep being HIGH despite not being HIGH, DONT USE FOR INPUT
  pinMode(5, INPUT);  //D1
  pinMode(4, INPUT);  //D2
  pinMode(16, INPUT); //D0
  pinMode(14, INPUT); //D5
  pinMode(12, INPUT); //D6

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


  void sendMsg(int ms) {
    snprintf (msg, 75, "#%ld", ms);
    Serial.print("Publish message: ");
    Serial.println(msg);
    client.publish(TOPIC, msg);
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

  void callback(char* topic, byte * payload, unsigned int length) {
    Serial.print("Message arrived [");
    Serial.print(topic);
    Serial.print("] ");
    Serial.println((char*)payload);
  }
