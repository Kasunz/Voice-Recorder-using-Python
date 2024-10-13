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

    def playing_audio(self, audio_data):
        """Play the recorded audio"""
        try:
            print("playing back the recording... ")
            sd.play(audio_data, self.sample_rate)
            sd.wait()
        except Exception as e:
            print(f"Error playing audio: {e}")

    def start_recording(self):
        """Start the recording process"""
        audio_data = self.record_audio()
        if audio_data is not None:
            self.save_audio(audio_data)
            if self.play_after:
                self.playing_audio(audio_data)


