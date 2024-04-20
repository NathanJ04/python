class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self, status=False, muted=False, volume=MIN_VOLUME, channel=MIN_CHANNEL):
        self.__status = status
        self.__muted = muted
        self.__volume = volume
        self.__channel = channel

    def power(self):
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self):
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self):
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        if self.__status:
            if self.__volume != self.MAX_VOLUME:
                self.__volume += 1
            if self.__muted:
                self.__muted = False

    def volume_down(self):
        if self.__status:
            if self.__volume != self.MIN_VOLUME:
                self.__volume -= 1
            if self.__muted:
                self.__muted = False

    def get_volume(self):
        if self.__muted:
            return self.MIN_VOLUME
        else:
            return self.__volume

    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.get_volume()}'

