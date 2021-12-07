from SomeEnv import SomeEnv

class Checker:
    def __init__(self, env: SomeEnv):
        self.env = env
        self.wasPlayed = False

    def wavWasPlayed(self):
        self.wasPlayed = True

    def resetWav(self):
        self.wasPlayed = False

    def reminder(self, file):
        if self.env.getTime().hour >= 17:
            self.env.playWavFile(file)
            self.wavWasPlayed()
        else:
            self.resetWav()