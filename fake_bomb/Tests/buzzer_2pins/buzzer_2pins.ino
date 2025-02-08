int buzzer = 8; // set the buzzer control digital IO pin

void setup() {
	pinMode(buzzer, OUTPUT); // set pin 8 as output
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
	tone(9, 7000, 100);
  digitalWrite(LED_BUILTIN, HIGH); 
	delay(100); // delay 1ms
	noTone(buzzer);
  digitalWrite(LED_BUILTIN, LOW); 
	delay(100);
	delay(1000);
}
