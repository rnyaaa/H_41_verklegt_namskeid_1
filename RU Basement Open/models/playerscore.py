class PlayerScore:
    def __init__(
        self, 
        tournamentid:str,
        gameid: str,
        playerid: str, 
        QPs: int = 0, 
        inshots: int = 0, 
        outshots: int = 0, 
        result501singles_wins = 0, 
        result501singles_losses = 0,
        result301_wins = 0, 
        result301_losses = 0, 
        resultcricket_wins = 0,
        resultcricket_losses = 0, 
        result501fours_wins = 0,
        result501fours_losses = 0
    ):
        self.tournamentid = tournamentid
        self.gameid = gameid
        self.playerid = playerid
        self.QPs = QPs
        self.inshots = inshots
        self.outshots = outshots
        self.result501singles = [result501singles_wins, result501singles_losses]
        self.result301 = [result301_wins, result301_losses]
        self.resultcricket = [resultcricket_wins, resultcricket_losses]
        self.result501fours = [result501fours_wins, result501fours_losses]

    def listify(self):
        #return [self.gameid, self.playerid, self.QPs, self.inshots, self.outshots, self._501winlose[0], self._501winlose[1], self._301winlose[0], self._301winlose[1], self.cricketwinlose[0], self.cricketwinlose[1], self._5014winlose[0], self._5014winlose[1]]
        return [self.tournamentid, self.gameid, self.playerid, self.QPs, self.inshots, self.outshots, self.result501singles, self.result301, self.resultcricket, self.result501fours]

    def model(self):
        return "playerscore"