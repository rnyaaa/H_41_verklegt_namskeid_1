class PlayerScore:
    def __init__(
        self, 
        playerid: str, 
        id: str,
        tournamentid:str,
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
        self.id = id
        self.playerid = playerid
        self.QPs = QPs
        self.inshots = inshots
        self.outshots = outshots
        self.result501singles = [result501singles_wins, result501singles_losses]
        self.result301 = [result301_wins, result301_losses]
        self.resultcricket = [resultcricket_wins, resultcricket_losses]
        self.result501fours = [result501fours_wins, result501fours_losses]

    def listify(self):
        """Returns the model on a list form."""
        return [self.playerid, self.id, self.tournamentid, self.QPs, self.inshots, self.outshots, self.result501singles[0], self.result501singles[1], self.result301[0], self.result301[1], self.resultcricket[0], self.resultcricket[1], self.result501fours[0], self.result501fours[1]]

    def model(self):
        return "playerscore"