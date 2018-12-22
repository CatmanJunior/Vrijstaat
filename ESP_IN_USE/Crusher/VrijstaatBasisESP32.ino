#include <WiFi.h>
#include <PubSubClient.h>
#include <ArduinoOTA.h>
const char *ssid =  "Vrijstaat";     // change according to your Network - cannot be longer than 32 characters!
const char *pass =  "vrijstaat"; // change according to your Network
const char *mqtt_server = "192.168.178.40";

const int SIGNNUM = 0;
const char *SIGNTOPIC = "SIGN";

long lastMsg = 0;


WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  setupESP();

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
  loopESP();
}

void sendMsg(int ms) {
  char msg[50];
  snprintf (msg, 75, "%ld", ms);
  Serial.print("Publish message: ");
  Serial.println(msg);
  client.publish(TOPIC, msg);

}

void Sign(int ms) {
  char msg[50];
  snprintf (msg, 75, "#%ld", ms);
  Serial.print("Publish message: ");
  Serial.println(msg);
  client.publish(SIGNTOPIC, msg);
}


void sendInput(const char *t, int ms) {
  char msg[50];
  snprintf (msg, 75, "%ld", ms);
  Serial.print("Publish message: ");
  Serial.println(msg);
  client.publish(t, msg);
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
      client.subscribe("SIGN");
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
  if (strcmp(topic, "SIGN") == 0) {
    if ((char)payload[1] == '1') {
      ESP.restart();
    }
    if ((char)payload[1] == '0') {
      client.publish(SIGNTOPIC, NAME);
    }
  }
  else
  {
    callbackESP(topic, payload);
  }
}
