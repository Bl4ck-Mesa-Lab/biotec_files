from machine import Pin
import neopixel
import time
import ws2812b

PIN = 0
NUM_LEDS = 14
BLINK_TIME = 0.1
BRIGHTNESS = 0.01
REPEAT = 3

neoClock = neopixel.NeoPixel(Pin(PIN), NUM_LEDS)
strip = ws2812b.ws2812b(NUM_LEDS, 0, PIN)

blue = 23,242,192
green = 0, 125, 0
yellow = 125, 75, 0
orange = 237,50,0
red = 125, 0, 0
black = 0,0,0
white = 125,125,125


a = (NUM_LEDS-NUM_LEDS)
b = int((NUM_LEDS/4))
c = int((NUM_LEDS/2))
d = int((NUM_LEDS/1.33)+1)
e = (NUM_LEDS-1)

    
def ResetColor():
    for i in range(NUM_LEDS):
        if i <= (NUM_LEDS-1):
            neoClock[i] = black
            neoClock.write()
            time.sleep(0.05)
            neoClock[i] = black
            neoClock.write()
        else:
            neoClock[i] = black
            neoClock.write()
            
        
def InitialBlink(color,min_range,max_range):
    for i in range(min_range,max_range):
        if i <= (NUM_LEDS-1):
            neoClock[i] = color
            neoClock.write() 
            time.sleep(0.05)
            neoClock[i+1] = color
            neoClock.write()   
        else:
            neoClock[i] = color
            neoClock.write() 
            time.sleep(0.1)

def lineClock(color,led_id):
    i = 0
    while i < REPEAT:
        neoClock[led_id] = black
        #neoClock[led_id-1] = black
        neoClock.write()
        time.sleep(BLINK_TIME)
        neoClock[led_id] = color
        neoClock.write()
        time.sleep(BLINK_TIME)
        neoClock[led_id] = black
        neoClock.write()
        i = i + 1
            
            
def FinalBlink(color):
    for i in range(NUM_LEDS):
        if i <= (NUM_LEDS-1):
            neoClock[i] = black
            neoClock.write()
            time.sleep(0.025)
            neoClock[i] = color
            neoClock.write()
        else:
            neoClock[i] =  color
            neoClock.write()         


print("-----------------------")
print("green  between: "+str(a)+" and "+str(b))
print("yellow between: "+str(b)+" and "+str(c))
print("orange between: "+str(c)+" and "+str(d))
print("red    between: "+str(d)+" and "+str(e))
print("-----------------------")
print("")
       
ResetColor()
time.sleep(3)
InitialBlink(green,a,b)
InitialBlink(yellow,b,c)
InitialBlink(orange,c,d)
InitialBlink(red,d,e)


time.sleep(5)
for j in range(a,b):
    lineClock(green,j)
for k in range(b,c):
    lineClock(yellow,k)
for l in range(c,d):
    lineClock(orange,l)    
for m in range(d,e):
    lineClock(red,m)
lineClock(red,NUM_LEDS-1)

while True:
    FinalBlink(red)
    FinalBlink(black)
      
    


