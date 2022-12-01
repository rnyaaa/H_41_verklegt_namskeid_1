class Game:
    def __INIT__(self, gameid, date, results):
        self.gameid = gameid
        self.date = date
        self.results = results

    def listify(self):
        return [self.gameid, self.date, self.results]

    def model(self):
        return "games"