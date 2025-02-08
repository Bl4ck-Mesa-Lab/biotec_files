
// Note: I recommend connecting SCL and SDA from the LCD to Analog 4 & 5 on the Uno.
// You can also use the SCL and SDA ports (near the USB).
// In general: 16 chars, 2 or 4 lines of text:	0x27
// 20 chars, 4 lines of text: 	0x3F
// But remember that most of these i2c adapters are addressable

#include <LiquidCrystal_I2C.h>
#include <Wire.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
	
lcd.init();
lcd.backlight();
	
}

void loop() { // do nothing here 

lcd.clear();
lcd.setCursor(0,0); // positionne le curseur à la colonne 1 et à la ligne 2  
lcd.print("Hello World!");
delay(1000);

}
