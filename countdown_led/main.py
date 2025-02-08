# --------------------------------
# @Author: C. Boudehenn, S. A.
# @Date: 24/07/07
# @Description : BIOTEC PROGRAM for recruitment timer.
# Based on Raspberry Pi Pico W + LEDs.
# Save ws2812b.py and main.py on the Pico.
# --------------------------------

# ------------------
# LIBRARIES
# ------------------

from machine import Pin, Timer
import neopixel
import time
import ws2812b
import socket
import network
import gc
import _thread

# ------------------
# CONFIGURATION
# ------------------

# CONF PROD (60 LED & 60min => All True)
LEDx60 = True
TIME60M = True
REALTIMESCALE = True

# False => Click RESET then START
START_LIGHTSUP_LEDS = False

# ------------------
# PROGRAM CODE
# ------------------

def reset_led_vars():

    global led_on
    global led_off
    global led_reset
    global led_success
    global led_failed
    global led_pause

    led_on = 0
    led_off = 0
    led_reset = 0
    led_success = 0
    led_failed = 0
    led_pause = 0


def reset_countdown_save():
    global countdown_save_a
    global countdown_save_b
    global countdown_save_c
    global countdown_save_d
    countdown_save_a = a
    countdown_save_b = b
    countdown_save_c = c
    countdown_save_d = d
    #print(f'{countdown_save_a} {countdown_save_b} {countdown_save_c} {countdown_save_d}')

# ------------------
# WEB INITIALISATION
# ------------------

gc.collect()

ssid = 'BIOTEC-Escape'
password = 'Biotec1234!'
pico_hostname = "RPI-pico-BIOTEC"
if not LEDx60:
    pico_hostname += "-LAB"

reset_led_vars()
is_countdown_paused = False

station = network.WLAN(network.STA_IF)
#led = Pin('LED', Pin.OUT)
led = Pin(7, Pin.OUT)

led.off()
#station.config(hostname=pico_hostname)
network.hostname(pico_hostname)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  led.toggle()
  print('Waiting for connection...')
  time.sleep(1)

print('Connection successful')
print(station.ifconfig())


# ------------------
# LED INITIALISATION
# ------------------

led.on()
led_state = "STANDING BY"

# -----------------------
# NEOPIXEL INITIALISATION
# -----------------------

PIN = 0

if LEDx60:
    NUM_LEDS = 60
else:
    NUM_LEDS = 14

if TIME60M:
    REPEAT = 60
else:
    REPEAT = 3

if REALTIMESCALE:
    BLINK_TIME = 0.497
else:
    BLINK_TIME = 0.1

BRIGHTNESS = 0.01

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

reset_countdown_save()

# ------------------
# FUNCTIONS
# ------------------

def update_ledstate():
    global led_state
    global led_on
    global led_off
    global led_reset
    global led_success
    global led_failed
    global led_pause
    
    if led_on == 6:
        led_state = "STARTED"
    elif led_off == 6:
        led_state = "OFF"
    elif led_reset == 6:
        led_state = "RESET"
    elif led_success == 6:
        led_state = "SUCCESS"
    elif led_failed == 6:
        led_state = "FAILED"
    elif led_pause == 6:
        led_state = "PAUSED"

def web_page():
    
    global led_state
    global is_countdown_paused
    
    if is_countdown_paused:
        button_start = "RESUME"
        button_pause = '<span align="center" class="button" style="font-style:italic">PAUSED</span>'
    else:
        button_start = "START"
        button_pause = '<a href=\"led_pause\"><button class="button button_pause">PAUSE</button></a> '
    
    html = f"""<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
        html {{
            font-family: Arial;
            display: inline-block;
            margin: 0px auto;
            text-align: center;
        }}
        
            .button {{
            background-color: #1FA5F1;
            border: none;
            color: white;
            padding: 16px 60px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }}

        .button_start {{
            background-color: #1FA5F1;
            padding: 16px 50px;
            border-radius: 50px;
        }}

        .button_stop {{
            background-color: #44484A;
            padding: 16px 50px;
            border-radius: 50px;
        }}
        
        .button_success {{
            background-color: #53be5f;
            padding: 16px 40px;
            border-radius: 50px;
        }}
        

        .button_failed {{
            background-color: #F34D22;
            padding: 16px 45px;
            border-radius: 50px;
        }}
        
        .button_reset {{
            background-color: #afaca5; color: black; /* Gray */
            padding: 16px 50px;
            border-radius: 50px;
        }}
        
        .button_pause {{
            background-color: #efc52d; color: black; /* Gray */
            padding: 16px 50px;
            border-radius: 50px;
        }}
        

        
    </style>
</head>

<body>
    <h1> BIOTEC LED PROGRAM </h1>
    <h2>Status Neopixel Operations</h2>
    <p>Current LEDs state: <strong>""" + led_state + """</strong></p>
    
    <br>
    <br>
    
    <div class="start_and_stop">
        
  <a href=\"led_on\"><button class="button button_start" style="font-weight:bold;">{}</button></a>
  <a href=\"led_off\"><button class="button button_stop" style="font-weight:bold;">STOP</button></a>
        
    </div>
    
    
    <br>
    <hr>
    <br>
    
    <div class="success_and_failed">
        
  <a href=\"led_success\"><button class="button button_success" style="font-weight:bold;">SUCCESS</button></a>
  <a href=\"led_failed\"><button class="button button_failed" style="font-weight:bold;">FAILED</button></a>
        
    </div>

    <br>
    <hr>
    <br>
    
<div class="pause_and_reset">
  {}
  <a href=\"led_reset\"><button class="button button_reset">RESET</button></a>
</div>
    
</body>

</html>
""".format(button_start, button_pause)
    
    return html

    
def ResetColor(color, instant: bool=False):
    for i in range(NUM_LEDS):
        if i <= (NUM_LEDS-1):
            neoClock[i] = color
            if not instant:
                neoClock.write()
                time.sleep(0.05)
            #neoClock[i] = color
            #if not instant:
                #neoClock.write()
        else:
            neoClock[i] = color
            if not instant:
                neoClock.write()
    if instant:
        neoClock.write()


def InitialBlink(color,min_range,max_range):
    #print(f'InitialBlink {min_range} {max_range}')
#    for i in range(min_range,max_range):
#        if i <= (NUM_LEDS-1):
#            neoClock[i] = color
#            neoClock.write() 
#            time.sleep(0.05)
#            if i+1 <= (NUM_LEDS-1):
#                neoClock[i+1] = color
#                neoClock.write()
#        else:
#            neoClock[i] = color
#            neoClock.write() 
#            time.sleep(0.1)
    for i in range(min_range,max_range):
        if i < NUM_LEDS:
            neoClock[i] = color
            neoClock.write()
            time.sleep(0.03)
            if i+1 == NUM_LEDS-1:
                neoClock[i+1] = color
                neoClock.write()


def InitialBlinkAll():
    InitialBlink(green,a,b)
    InitialBlink(yellow,b,c)
    InitialBlink(orange,c,d)
    InitialBlink(red,d,e)


def InitialBlinkUpToSavedCountdown():
    global countdown_save_a
    global countdown_save_b
    global countdown_save_c
    global countdown_save_d
    
    if countdown_save_a < b:
        InitialBlink(green, countdown_save_a, countdown_save_b)
    if countdown_save_b < c:
        InitialBlink(yellow, countdown_save_b, countdown_save_c)
    if countdown_save_c < d:
        InitialBlink(orange, countdown_save_c, countdown_save_d)
    if countdown_save_d < e:
        InitialBlink(red, countdown_save_d, e)


def lineClock(color,led_id):
    
    global led_on
    
    i = 0
    while i < REPEAT and led_on == 6 and not is_interrupted():
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
        if is_interrupted():
            return
        if i <= (NUM_LEDS-1):
            neoClock[i] = black
            neoClock.write()
            time.sleep(0.025)
            neoClock[i] = color
            neoClock.write()
        else:
            neoClock[i] =  color
            neoClock.write()


def handle_led():

    global led_state
    global led_on
    global led_off
    global led_reset
    global led_success
    global led_failed
    global led_pause
    global is_countdown_paused
    global countdown_save_a
    global countdown_save_b
    global countdown_save_c
    global countdown_save_d

    #print("DEBUG - Handle LED - Begin")

    while True:

        time.sleep(0.1)
        #print("DEBUG - Handle LED - While True loop")
    
        if led_on == 6 and not is_interrupted():
            if START_LIGHTSUP_LEDS:
                InitialBlinkUpToSavedCountdown()
            if not is_interrupted():
                #print('LED ON -> GPIO25')
                #print(f'START - countdown saved {countdown_save_a} {countdown_save_b} {countdown_save_c} {countdown_save_d}')
                for j in range(countdown_save_a, b):
                    lineClock(green,j)
                    countdown_save_a = j
                    if is_interrupted():
                        break
                if not is_interrupted():
                    for k in range(countdown_save_b, c):
                        lineClock(yellow,k)
                        countdown_save_b = k
                        if is_interrupted():
                            countdown_save_a = b+1

                            break
                if not is_interrupted():
                    for l in range(countdown_save_c, d):
                        lineClock(orange,l)
                        countdown_save_c = l
                        if is_interrupted():
                            countdown_save_a = b+1
                            countdown_save_b = c+1
                            break
                if not is_interrupted():
                    for m in range(countdown_save_d, e):
                        lineClock(red,m)
                        countdown_save_d = m
                        if is_interrupted():
                            countdown_save_a = b+1
                            countdown_save_b = c+1
                            countdown_save_c = d+1
                            break
                if not is_interrupted():
                    lineClock(red,NUM_LEDS-1)
                    if is_interrupted():
                        countdown_save_a = b+1
                        countdown_save_b = c+1
                        countdown_save_c = d+1
                        countdown_save_d = e+1
            if not is_interrupted():
                led_failed = 6
            #print(f'START - countdown saved {countdown_save_a} {countdown_save_b} {countdown_save_c} {countdown_save_d}')

        if led_off == 6:
            #print('LED OFF -> GPIO25')
            ResetColor(black, True)
            led.off()
            reset_led_vars()
            reset_countdown_save()
        
        if led_reset == 6:
            #print('LED RESET -> GPIO25')
            led.off()
            reset_countdown_save()
            ResetColor(black, True)
            #time.sleep(0.5)
            InitialBlinkAll()
            reset_led_vars()
        
        if led_success == 6:
            #print('LED SUCCESS -> GPIO25')
            while led_success == 6 and not is_interrupted():
                FinalBlink(green)
                FinalBlink(black)
            #reset_led_vars()
            reset_countdown_save()
        
        if led_failed == 6:
            #print('LED FAILED -> GPIO25')
            while led_failed == 6 and not is_interrupted():
                ResetColor(red, True)
                time.sleep(0.7)
                ResetColor(black, True)
                time.sleep(0.7)
            #reset_led_vars()
            reset_countdown_save()

        if led_pause == 6:
            #print('LED PAUSE -> GPIO25')
            led.off()
            reset_led_vars()
            #is_countdown_paused = True # done in webpage management (to be used to generate web response)


def is_interrupted():
    global led_on
    global led_off
    global led_reset
    global led_success
    global led_failed
    global led_pause

    if led_off == 6 or led_reset == 6 or led_pause == 6:
        return True
    
    return False


def handle_webserver():

    global led_state
    global led_on
    global led_off
    global led_reset
    global led_success
    global led_failed
    global led_pause
    global is_countdown_paused

    while True:
        try:
            conn, addr = pico_socket.accept()
            conn.settimeout(3.0)
            print('Received HTTP GET connection request from %s' % str(addr))
            request = conn.recv(1024)
            conn.settimeout(None)
            request = str(request)
            #print('GET Request Content = %s' % request)
            
            led_on = request.find('/led_on')
            led_off = request.find('/led_off')
            led_reset = request.find('/led_reset')
            led_success = request.find('/led_success')
            led_failed = request.find('/led_failed')
            led_pause = request.find('/led_pause')
            
            # Button PAUSE (START becomes RESUME)
            if led_pause == 6:
                #print(f"toggling is_countdown_paused: {is_countdown_paused}")
                is_countdown_paused = not is_countdown_paused
            
            # Any button when already paused (RESUME => becomes START)
            if is_countdown_paused and (led_on == 6 or led_off == 6 or led_reset == 6 or led_success == 6 or led_failed == 6):
                #print(f"toggling is_countdown_paused: {is_countdown_paused}")
                is_countdown_paused = not is_countdown_paused
            
            update_ledstate()
            
            response = web_page()
            conn.send('HTTP/1.1 200 OK\n')
            conn.send('Content-Type: text/html\n')
            conn.send('Connection: close\n\n')
            conn.sendall(response)
            conn.close()
            
        except OSError as e:
            conn.close()
            print('Connection closed')


# ------------------
# USAGE
# ------------------

pico_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pico_socket.bind(('', 80))
pico_socket.listen(5)

print("-----------------------")
print("green  between: "+str(a)+" and "+str(b))
print("yellow between: "+str(b)+" and "+str(c))
print("orange between: "+str(c)+" and "+str(d))
print("red    between: "+str(d)+" and "+str(e))
print("-----------------------")
print("")

ResetColor(black, True)
time.sleep(3)
InitialBlinkAll()

second_thread = _thread.start_new_thread(handle_led, ())

handle_webserver()
