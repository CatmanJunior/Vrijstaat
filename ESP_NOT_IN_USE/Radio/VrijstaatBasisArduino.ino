
void setup() {
  setupESP();

  Serial.begin(9600);    // Initialize serial communications
  Serial.println(NAME);

}

void loop() {
  
  loopESP();
}
