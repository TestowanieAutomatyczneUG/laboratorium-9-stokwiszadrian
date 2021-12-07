from datetime import datetime

class SomeEnv:
    mock_method = None

    def getTime(self):
        return datetime.now()

    def playWavFile(self, file):
        pass
