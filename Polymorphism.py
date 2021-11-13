
#Audio formats: .mp3, .wav, .flac
class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")
        self.filename = filename

class MP3File(AudioFile):
    ext = "mp3"

    def play(self):
        print("Mp3 processing complete")
        print(f"playing {self.filename} as mp3")

class WAVFile(AudioFile):
    ext = "wav"

    def play(self):
        print("wav processing complete")
        print(f"playing {self.filename} as wav")

class FlacFile(AudioFile):
    ext = "flac"

    def play(self):
        print("flac processing complete")
        print(f"playing {self.filename} as flac")

if __name__ == "__main__":
    myflac = FlacFile("jamrock.flac")
    myflac.play()