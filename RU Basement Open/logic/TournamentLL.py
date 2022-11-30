# from LL_API import LL_API

# verðum að hætta að importa LL_API inn í hina LL klasana, annars fáum við circular import
# Megum bara importa hinum LL klösunum inn í LL_API en ekki öfugt!

class TournamentLL():

    def addTournament():
        tournaments = LL_API.getTournament()
        raise NotImplementedError