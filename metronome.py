from playsound import playsound
from threading import Timer
import argparse

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-bpm', action='store', type=int, default=60, help='the number of beats per minute the metronome should play, default is 60')
my_parser.add_argument('-beats', action='store',type=int, default=1, help='the number of beats per measure, default is 1 or no measure separator')

args = my_parser.parse_args()

#global variables
count = 1
beats = args.beats
bpm = args.bpm
freq = 60.0/bpm

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

def playClick():
    global count
    global beats

    if (count > beats):
        count = 1
    
    if (count == 1):
        playsound('tickup.wav')
    else:
        playsound('tick.wav')
    count += 1
    
print("%d BPM" % bpm)
print("%d beats per measure" % beats)
print('Press \'Enter\' to stop')    

rt = RepeatedTimer(freq, playClick)

s = input()
rt.stop()
