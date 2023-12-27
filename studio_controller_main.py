'''
Pimoroni custom UF2 File for PICO W v 1.19
https://github.com/pimoroni/pimoroni-pico/releases/tag/v1.19.10
pimoroni-pico-v1.19.10-micropython.uf2

Key Code Table - Button number on left - Code on right
0 = 1 - top row
1 = 2 - top row
2 = 4 - top row
3 = 8 - top row
4 = 16
5 = 32
6 = 64
7 = 128
8 = 256
9 = 512
A = 1024
B = 2048
C = 4096
D = 8192
E = 16384
F = 32768
'''

import picokeypad as keypad
import _thread
import network
from time import sleep
from secrets import ssid, password, token
from pages import draw_page_0, draw_page_1
from HA_handlers import key_do



#initialize keyboard
keypad.init()
keypad.set_brightness(1.0)
keypad.update()

#global variables
#total numebr of keys
NUM_PADS = keypad.get_num_pads()
#Keys in top row to use with len() as a variable to use in ranges for manipulating the top row?
top_row = [1, 2, 4, 8]
#Rest of the keys
bottom_keys = [16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]
#variable handling the latest button state
last_button_states = 0
#flag is used to terminate concurrent processes at startup
flag = True
#Global variable for page
current_page = 0

#Startup functions
#Function to conenc tot he WLAN
def connect():
    sleep(5)
    global flag
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    flag = False
    return

#Start the spinning wheel evvect at the beginning - resets to "dim" white at the end
def light_show():
    global flag
    sequence = [0, 1, 2, 3, 7, 11, 15, 14, 13, 12, 8, 4]
    while flag == True:
        for i in range(0,len(sequence)):
            keypad.illuminate(sequence[i],255,0,0)
            keypad.update()
            keypad.illuminate(sequence[i-1],110,0,0)
            keypad.update()
            keypad.illuminate(sequence[i-2],20,0,0)
            keypad.update()
            sleep(0.1)
            keypad.illuminate(sequence[i],5,5,5)
            keypad.illuminate(sequence[i-1],5,5,5)
            keypad.illuminate(sequence[i-2],5,5,5)
            keypad.update()
    return

#Function to handle top row paging
def page(page_n):
    global current_page
    current_page = page_n
    for i in range(0,4):
        if i == page_n:
            keypad.illuminate(i,255,0,0)
            keypad.update()
        else:
            keypad.illuminate(i,25,25,0)
            keypad.update()
    draw_page(page_n)
    return

#Function to refresh page upon page change
def draw_page(page_n):
    if page_n == 0:
        draw_page_0()
    if page_n == 1:
        draw_page_1()
    if page_n == 2:
        for i in range(4, 16):
            keypad.illuminate(i, 128, 128, 0)
            keypad.update()
    if page_n == 3:
        for i in range(4, 16):
            keypad.illuminate(i, 0, 0, 255)
            keypad.update()

#================start=================

#Initially set buttons to dim white
for i in range(0,NUM_PADS):
    keypad.illuminate(i,5,5,5)
    keypad.update()
#light show starts on separate CPU thread
_thread.start_new_thread(light_show, ())

#start connection
connect()

#Once connected display page 0
if flag == False:
    sleep(2)
    page(0)
    
while True:
    button_states = keypad.get_button_states()
    if last_button_states != button_states:
        last_button_states = button_states
        if button_states in top_row:
            page(top_row.index(button_states))
            button_states = 0
        elif button_states in bottom_keys:
            key_do(button_states, current_page, token)


