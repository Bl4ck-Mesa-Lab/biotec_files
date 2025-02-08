int buzzer = 8; // set the buzzer control digital IO pin

void setup() {
	pinMode(buzzer, OUTPUT); // set pin 8 as output
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
	for (int i = 0; i < 100; i++) {  // make a sound
		digitalWrite(buzzer, HIGH); // send high signal to buzzer
    digitalWrite(LED_BUILTIN, HIGH); 
		delay(1); // delay 1ms
		digitalWrite(buzzer, LOW); // send low signal to buzzer
    digitalWrite(LED_BUILTIN, LOW); 
		delay(1);
	}
	delay(50);
	for (int j = 0; j < 100; j++) { //make another sound
		digitalWrite(buzzer, HIGH);
    digitalWrite(LED_BUILTIN, HIGH);
		delay(1); // delay 2ms
		digitalWrite(buzzer, LOW);
    digitalWrite(LED_BUILTIN, LOW); 
		delay(1);
	}
  	delay(50);
	for (int k = 0; k < 100; k++) { //make another sound
		digitalWrite(buzzer, HIGH);
    digitalWrite(LED_BUILTIN, HIGH);
		delay(1); // delay 2ms
		digitalWrite(buzzer, LOW);
    digitalWrite(LED_BUILTIN, LOW); 
		delay(1);
	}
	delay(3000);
}
