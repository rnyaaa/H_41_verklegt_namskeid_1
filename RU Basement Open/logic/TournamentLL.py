from IO.IO_API import IO_API

class TournamentLL():
    
    def __init__(self, ioapi: IO_API):
        self.ioapi = ioapi

    def addTournament(self):
        tournaments = self.ioapi.getTournament()

    def getTournamentScore(self):
        teams = self.ioapi.getTeams()
        """ gets all teams in tournament and sorts by games won and rounds won """
        # NOTE: Implement the sorting so that it sorts by both, as it is it only sorts by games won
        tournamentranklist = []
        for team in teams:
            tournamentranklist.append([line[0], line[4], line[5]])
            # team_name, games won, rounds won
        tournamentranklist.sort()
        return tournamentranklist

    def getTournamentDates(self):
        """ sækir tournament skrá, fer í línu 2 með dagsetningum og liðum sem spila þann dag og setur í lista """
        tournamentdatelist = []
        tournaments = self.ioapi.getTournament()
        """ google svartagaldur, pls finna betri leið til að taka hvert 3 gildi og setja í list """
        tournamentdatelist = zip(*[iter(tournaments[1])]*3)
        return tournamentdatelist
   


    
        
        
        raise NotImplementedError
