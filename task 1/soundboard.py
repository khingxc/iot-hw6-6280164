from pyfirmata import Arduino, util
import simpleaudio as sa
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

tom = board.get_pin('d:8:i')
powerpuff = board.get_pin('d:9:i')
looney = board.get_pin('d:10:i')
bean = board.get_pin('d:11:i')
song_tom = 'sounds/TomandJerry.wav'
song_powerpuff = 'sounds/PowerPuffGirls.wav'
song_looney = 'sounds/LooneyTunes.wav'
song_bean = 'sounds/MrBean.wav'
pins = [tom, powerpuff, looney, bean]
songs = [song_tom, song_powerpuff, song_looney, song_bean]

time.sleep(1)
for i in range(4):
    button = pins[i]
    button.enable_reporting()
time.sleep(1)

while (1):
    for i in range(4):
        current_button = pins[i].read()
        print(str(pins[i]) + ": " + str(current_button))
        if (str(current_button) == 'False'):
            chosen_sound = songs[i]
            song = sa.WaveObject.from_wave_file(chosen_sound)
            play_obj = song.play()
            play_obj.wait_done()