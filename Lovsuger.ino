

  const int buttonLedPin = 22; // pin for led on button
  const int buttonPin = 21;    // Pin for button
  const int relayPin = 34;    // Pin for relay

  bool relayState = false;
  bool buttonState = true;

void setup() {
  // Start the relay pin as an output:
  pinMode(relayPin, OUTPUT);
  // Start the button pin as an input:
  pinMode(buttonPin, INPUT);
  // Start the button led pin as an output:
  pinMode(buttonLedPin, OUTPUT);

  Serial.begin(9600);

}

void loop() {
  // If button is pressed toggle relay state
  buttonState = digitalRead(buttonPin);
  
  if (buttonState==LOW) {
    relayState =! relayState;
    digitalWrite(relayPin, relayState);
    digitalWrite(buttonLedPin, relayState);
//    Serial.println(relayState);
    delay(500);
  }



}
