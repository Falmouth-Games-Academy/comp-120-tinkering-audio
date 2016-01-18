    def PlaySound(self):
        sound = SoundLoader.load(r'.\Sounds\Melody.wav')
        if sound:
            print("Sound is %.3f seconds long" % sound.length)
            sound.play()