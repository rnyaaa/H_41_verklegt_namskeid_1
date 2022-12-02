class Results:
    def __init__(self, game_id, results_id, players, QPs_awarded, inshots_awarded, outshots_awarded, winningscore, losingscore, winning501s, losing501s, winning301, losing301, winningcricket, losingcricket, winning501f, losing501f):
        self.game_id = game_id
        self.results_id = results_id
        self.players = players
        self.QPs_awarded = QPs_awarded
        self.inshots_awarded = inshots_awarded
        self.outshots_awarded = outshots_awarded
        self.winningscore = winningscore
        self.losingscore = losingscore
        self.winning501s = winning501s
        self.losing501s = losing501s
        self.winning301 = winning301
        self.losing301 = losing301
        self.winningcricket = winningcricket
        self.losingcricket = losingcricket
        self.winning501f = winning501f
        self.losing501f = losing501f

    def listify(self):
        return [self.game_id, self.results_id, self.QPs_awarded, self.inshots_awarded, self.outshots_awarded, self.winningscore, self.losingscore, self.winning501s, self.losing501s, self.winning301, self.losing301, self.winningcricket, self.losingcricket, self.winning501f, self.losing501f]

    def model(self):
        return "Results"