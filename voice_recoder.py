import sounddevice as sd
import wavio
import argparse
import os
import time

class VoiceRecoder:
    def __int__(self, filename = "recoding.wav", duration = 5, sample_rate = 44100, play_after = False):
        """Initialize the voice recoder with default setting """
        self.filename = filename
        self.duration = duration
        self.sample_rate = sample_rate
        self.play_after = play_after





