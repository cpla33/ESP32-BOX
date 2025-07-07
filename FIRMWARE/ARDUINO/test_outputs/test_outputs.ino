#define LED_OK 2 // RGB-led (green)
#define LED_FAULT 16 // RGB-led (red)
#define LED_CONN 17 // RGB-led (blue)

#define RELAY_1 32 // Relay1
#define RELAY_2 33 // Relay2
#define RELAY_3 27 // Relay3
#define RELAY_4 26 // Relay4

#define INPUT_4 4
#define INPUT_18 18


// the setup function runs once when you press reset or power the board
void setup() {
  Serial.begin(115200); // for debugging
  
  pinMode(LED_OK, OUTPUT);
  pinMode(LED_FAULT, OUTPUT);
  pinMode(LED_CONN, OUTPUT);

  pinMode(RELAY_1, OUTPUT);
  pinMode(RELAY_2, OUTPUT);
  pinMode(RELAY_3, OUTPUT);
  pinMode(RELAY_4, OUTPUT);

  pinMode(INPUT_4, INPUT_PULLUP);
  pinMode(INPUT_18, INPUT_PULLUP);
  
  Serial.println("Setup ready! Start...");
}

// the loop function runs over and over again forever
void loop() {
  
  digitalWrite(RELAY_1, HIGH);
  digitalWrite(RELAY_2, LOW);
  digitalWrite(RELAY_3, LOW);
  digitalWrite(RELAY_4, LOW);
  Serial.println("Relay 1");
  delay(500);

  digitalWrite(RELAY_1, HIGH);
  digitalWrite(RELAY_2, HIGH);
  digitalWrite(RELAY_3, LOW);
  digitalWrite(RELAY_4, LOW);
  Serial.println("Relay 1+2");
  delay(500);

  digitalWrite(RELAY_1, HIGH);
  digitalWrite(RELAY_2, HIGH);
  digitalWrite(RELAY_3, HIGH);
  digitalWrite(RELAY_4, LOW);
  Serial.println("Relay 1+2+3");
  delay(500);

  digitalWrite(RELAY_1, HIGH);
  digitalWrite(RELAY_2, HIGH);
  digitalWrite(RELAY_3, HIGH);
  digitalWrite(RELAY_4, HIGH);
  Serial.println("Relay 4");
  delay(500);

  digitalWrite(RELAY_1, LOW);
  digitalWrite(RELAY_2, LOW);
  digitalWrite(RELAY_3, HIGH);
  digitalWrite(RELAY_4, HIGH);
  Serial.println("Relay 3+4");
  delay(500);
  
}
