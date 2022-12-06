class PlayerScore:
    def __init__(
            self,
            gameid,
            playerid,
            QPs,
            inshots,
            outshots,
            _501winlose,
            _301winlose,
            cricketwinlose,
            _5014winlose):
        self.playerid = playerid
        self.gameid = gameid
        self.playerid = playerid
        self.QPs = QPs
        self.inshots = inshots
        self.outshots = outshots
        self._501winlose = _501winlose
        self._301winlose = _301winlose
        self.cricketwinlose = cricketwinlose
        self._5014winlose = _5014winlose

    def listify(self):
        return [self.gameid, self.playerid, self.QPs, self.inshots, self.outshots, self._501winlose, self._301winlose, self.cricketwinlose, self._5014winlose]

    def model(self):
        return "playerscore"
