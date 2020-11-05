import pyaudio
import wave
import os
import threading

class WavePlayerLoop(threading.Thread)

    def __init__(self, filepath, loop=true):
        super(WavePlayerLoop, self).__init__()
        self.filepa