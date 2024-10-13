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

    def record_audio(self):
        """Record the audio for given duration """
        print(f"Recording for {self.duration} seconds...")
        try:
            audio_data = sd.rec(int(self.duration * self.sample_rate), samplerate = self.sample_rate, channels= 2)
            sd.wait() # wait until recoding is finished

        except Exception as e:
            print(f"Error recoding audio: {e}")
            return None

    def save_audio(self, audio_data):
        """Save the recorded audio to a wav file """
        try:
            wavio.write(self.filename, audio_data, self.sample_rate, sampwidth=2 )
            print(f"Recording save to {self.filename}")
        except Exception as e:
            print(f"Error saving audio: {e}")



