# simple voice recoder using python
import sounddevice as sd
import wavio
import argparse
import os
import time

class VoiceRecoder:
    def __init__(self, filename = "recoding.wav", duration = 5, sample_rate = 44100, play_after = False):
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

def main():
    """Main function for parse command-line arguments and start the voice recording """
    parser = argparse.ArgumentParser(description="Simple Python Voice Recorder")
    parser.add_argument("-f", "--file", file_type=str, default = "recording.wav", help="Output file name (default: recording.wav)")
    parser.add_argument("-d", "--duration", type=int, default=5, help="Duration of recording in seconds (default: 5")
    parser.add_argument("-r", "--rate", type=int, default=44100, help="Sample rate (default: 44100 Hz )")
    parser.add_argument("-p","--play", action="store_true", help="play the audio after recording (optional) ")

    args = parser.parse_args()

    # check the file name has correct extension
    if not args.file.endwith(".wav"):
        print("Error: The file output must be a .wav file")
        return

    # check if output file exists and confirm overwrite
    if os.path.exists(args.file):
        confirm = input(f"File '{args.file}' already exists. Overwrite ? (y/n): ")
        if confirm.lower() != 'y':
            print("Recording Canceled ")
            return

    # initialize the voice recoder with user argument
    recoder = VoiceRecoder(filename=args.file, duration = args.duration, sample_rate = args.sample_rate, play_after = args.play_after )

    # Start recording
    recoder.start_recording()

if __name__ == "__main__":
    main()
