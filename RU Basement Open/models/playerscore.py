class PlayerScore:
    def __init__(
        self, 
        gameid: str,
        playerid: str, 
        QPs: int = 0, 
        inshots: int = 0, 
        outshots: int = 0, 
        result501singles = [0, 0], 
        result301 = [0, 0], 
        resultcricket = [0, 0], 
        result501fours = [0, 0]):
        self.playerid = playerid
        self.gameid = gameid
        self.QPs = QPs
        self.inshots = inshots
        self.outshots = outshots
        self.result501 = result501singles
        self.result301 = result301
        self.resultcricket = resultcricket
        self.result5014 = result501fours

    def listify(self):
        #return [self.gameid, self.playerid, self.QPs, self.inshots, self.outshots, self._501winlose[0], self._501winlose[1], self._301winlose[0], self._301winlose[1], self.cricketwinlose[0], self.cricketwinlose[1], self._5014winlose[0], self._5014winlose[1]]
        return [self.gameid, self.playerid, self.QPs, self.inshots, self.outshots, self._501winlose, self._301winlose, self.cricketwinlose, self._5014winlose]

    def model(self):
        return "playerscore"