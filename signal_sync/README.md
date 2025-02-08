# Signal synchronizer

## Hardware
- ESP32 (LOLIN D32)
- Signal generator XR2206
- Oscilloscope
- Resistors (100 KOhms & 47 KOhms)
- Capacitor (whatever capacity)
- OLED SSD1306
- Blue LED: frequency validation
- Yellow LED: amplitude validation

## Tension divider
Limits voltage on ESP32 analog pins to 2.96V.
Note: ADC saturates at 3.1V (sensor = 4095).

## Capacitor
Suppresses DC component of generated signal for oscilloscope visualization.

## Signal reception
GPIO34 => Signal (from tension divider)

## OLED SSD1306
- GPIO 22 => SCL
- GPIO 21 => SDA
- 3V3 => Vin
- GND => GND

## LED
- GPIO26 => Blue
- GPIO27 => Yellow

