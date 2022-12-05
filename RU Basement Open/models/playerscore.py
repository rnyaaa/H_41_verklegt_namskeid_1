class PlayerScore:
    def __init__(self, gameid=int, playerid="", QPs="", Inshots="", Outshots="", _501winlose=tuple, _301winlose=tuple, cricketwinlose=tuple, _5014winlose=tuple):
        self.gameid = gameid
        self.playerid = playerid
        self.QPs = QPs
        self.inshots = Inshots
        self.outshots = Outshots
        self._501winlose = _5014winlose
        self._301winlose = _301winlose
        self.cricketwinlose = cricketwinlose
        self._5014winlose = _5014winlose

    def listify(self):
        return [self.gameid, self.playerid, self.QPs, self.inshots, self.outshots, self._501winlose[0], self._501winlose[1], self._301winlose[0], self._301winlose[1], self.cricketwinlose[0], self.cricketwinlose[1], self._5014winlose[0], self._5014winlose[1]]

    def model(self):
        return "playerscore"