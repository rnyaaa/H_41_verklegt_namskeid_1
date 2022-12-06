class PlayerSummary:
    def __init__(
        self, 
        playerid: str, 
        QPs: int = 0, 
        inshots: int = 0, 
        outshots: int = 0, 
        result501singles = [0, 0], 
        result301 = [0, 0], 
        resultcricket = [0, 0], 
        result501fours = [0, 0]):
        self.playerid = playerid
        self.QPs = QPs
        self.inshots = inshots
        self.outshots = outshots
        self.result501singles = result501singles
        self.result301 = result301
        self.resultcricket = resultcricket
        self.result501fours = result501fours

    def listify(self):
        return [self.playerid, self.QPs, self.inshots, self.outshots, self._501winlose[0], self._501winlose[1], self._301winlose[0], self._301winlose[1], self.cricketwinlose[0], self.cricketwinlose[1], self._5014winlose[0], self._5014winlose[1]]

    def model(self):
        return "playersummary"