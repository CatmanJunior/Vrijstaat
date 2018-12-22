#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <ArduinoOTA.h>
#include <Servo.h>

const char *ssid =  "Vrijstaat";     // change according to your Network - cannot be longer than 32 characters!
const char *pass =  "vrijstaat"; // change according to your Network
const char *mqtt_server = "192.168.178.40";
const char *NAME = "Servo_Piezo1";
const char *TOPIC = "SP1"; //HB

const int SIGNNUM = 3;
const char *SIGNTOPIC = "SIGN"; //HB

WiFiClient espClient;
PubSubClient client(espClient);
Servo servoA;
long lastMsg = 0;
char msg[50];

void setup() {
  //D3 and D4 keep being HIGH despite not being HIGH, DONT USE FOR INPUT
  servoA.attach(14);

  pinMode(12, INPUT); //D6

  Serial.begin(115200);    // Initialize serial communications
  Serial.println(NAME);

  WiFi.begin(ssid, pass);
  ArduinoOTA.setHostname(NAME);
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);

  while ((WiFi.status() != WL_CONNECTED)) {
    delay(500);
    Serial.print(".");
  }
  Serial.println(F("WiFi connected"));
  ArduinoOTA.onStart([]() {
    String type;
    if (ArduinoOTA.getCommand() == U_FLASH) {
      type = "sketch";
    } else { // U_SPIFFS
      type = "filesystem";
    }

    // NOTE: if updating SPIFFS this would be the place to unmount SPIFFS using SPIFFS.end()
    Serial.println("Start updating " + type);
  });
  ArduinoOTA.onEnd([]() {
    Serial.println("\nEnd");
  });
  ArduinoOTA.onProgress([](unsigned int progress, unsigned int total) {
    Serial.printf("Progress: %u%%\r", (progress / (total / 100)));
  });
  ArduinoOTA.onError([](ota_error_t error) {
    Serial.printf("Error[%u]: ", error);
    if (error == OTA_AUTH_ERROR) {
      Serial.println("Auth Failed");
    } else if (error == OTA_BEGIN_ERROR) {
      Serial.println("Begin Failed");
    } else if (error == OTA_CONNECT_ERROR) {
      Serial.println("Connect Failed");
    } else if (error == OTA_RECEIVE_ERROR) {
      Serial.println("Receive Failed");
    } else if (error == OTA_END_ERROR) {
      Serial.println("End Failed");
    }
  });
  ArduinoOTA.begin();
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  ArduinoOTA.handle();
  if (!client.connected()) {
    reconnect();
  }
  
  client.loop();

}

void sendMsg(int ms) {
  snprintf (msg, 75, "#%ld", ms);
  Serial.print("Publish message: ");
  Serial.println(msg);
  client.publish(TOPIC, msg);
}

void Sign(int ms) {
  snprintf (msg, 75, "#%ld", ms);
  Serial.print("Publish message: ");
  Serial.println(msg);
  client.publish(SIGNTOPIC, msg);
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect(NAME)) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish(SIGNTOPIC, NAME);
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

  if ((char)payload[0] == '3') {
    servoA.write(180);
  }
  if ((char)payload[0] == '4') {
    servoA.write(0);
  }
  if ((char)payload[1] == '5') {
    digitalWrite(4, LOW);
  }
  if ((char)payload[1] == '6') {
    digitalWrite(4, HIGH);
  }
  if ((char)payload[1] == '7') {
    digitalWrite(16, LOW);
  }
  if ((char)payload[1] == '8') {
    digitalWrite(16, HIGH);
  }
  if ((char)payload[1] == '9') {
    digitalWrite(14, LOW);
  }
  if ((char)payload[1] == '0') {
    digitalWrite(14, HIGH);
  }


}
