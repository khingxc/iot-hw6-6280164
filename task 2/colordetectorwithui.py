from pyfirmata import Arduino, util
import PySimpleGUI as sg    
import time

try:
    board = Arduino('/dev/cu.usbserial-110')
    iterator = util.Iterator(board)
    iterator.start()
    print("Successfully Connected to Arduino Board")
except:
    print("ERROR: Could Not Connect to Arduino Board")
    board = None
    exit()

r = board.get_pin('d:9:p')
g = board.get_pin('d:10:p')
b = board.get_pin('d:11:p')
red_val = 0
green_val = 0
blue_val = 0
lcr = board.get_pin('a:0:i')
lcr.enable_reporting()

pins = [r,g,b]
keys = ['redV', 'greenV', 'blueV', 'predV']
names = ['red', 'green', 'blue']
titles =  ['R', 'G', 'B', ]
vals = [red_val, green_val, blue_val]
pred = "-"

def rgb_light():
    for i in range(3):
        pins[i].write(1)
        vals[i] = lcr.read()
        window[keys[i]].update(f'{titles[i]}: {vals[i]}')
        time.sleep(1)
        pins[i].write(0)
    pred = names[vals.index(max(vals))]
    window[keys[3]].update(f'Resulting Color: {pred}')

layout = [[sg.Button('Detect Color')],  
            [sg.Text('Raw Value')],
            [sg.Text(f'R: {red_val}', key='redV')],
            [sg.Text(f'G: {green_val}', key='greenV')],
            [sg.Text(f'B: {blue_val}', key='blueV')],
            [sg.Text(f'Resulting Color: {pred}', key='predV')]]

window = sg.Window('Color Detector', layout)     

while True:
    event = window.read()                   
    if event == sg.WIN_CLOSED: 
        break
    else:
        rgb_light()

window.close()  