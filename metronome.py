from pydub import AudioSegment
from pydub.playback import play
from threading import Timer
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-bpm', action='store', type=int, default=60, 
                        help='the number of beats per minute the metronome should play, default is 60')
my_parser.add_argument('-beats', action='store',type=int, default=1, 
                        help='the number of beats per measure, default is 1 or no measure separator')

args = my_parser.parse_args()

#global variables
count = 1
beats = args.beats
bpm = args.bpm
freq = 60.0/bpm

tickup = AudioSegment.from_wav('tickup.wav')
tick = AudioSegment.from_wav('tick.wav')

def playClick():
    global count
    global beats

    if (count > beats):
        count = 1
    
    print('Count = ', count)
    if (count == 1):
        # playsound('tickup.wav')
        play(tickup)
    else:
        # playsound('tick.wav')
        play(tick)
    count += 1
    
print("%d BPM" % bpm)
print("%d beats per measure" % beats)
print('Press \'Enter\' to stop')    

# rt = RepeatedTimer(freq, playClick)
def playit():
    t = Timer(freq, playit)
    t.daemon = True
    t.start()
    playClick()

playit()
s = input()

