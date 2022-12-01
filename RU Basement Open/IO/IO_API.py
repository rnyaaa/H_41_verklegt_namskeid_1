
import os
import csv
filedict = {
    "players": "models/players.csv",
    "games": "models/teams.csv",
    "teams": "models/teams.csv",
    "tournaments": "models/tournaments.csv",
    "playerscore": "models/playerscore.csv"
}

fieldnames = {
    "players": ["id", "name", "birth_year", "phone_nr", "email"],
    "teams": ["id", "team_name", "address", "association_name", "phone_nr", "total_games_won", "total_rounds_won",["player1", "player2", "player3", "player4"]],
    "tournaments": [""],
    "playerscore":[["gameid", "playerid"], "QPs", "inshots", "outshots", ("win501_1", "lose501_1"), ("win301", "los301"), ("wincricket", "losecricket"), ("win501_4,lose501_4")]
}


class IO_API:

    def getAll(self, type=str):
        print("---------------------------------", os.getcwd())
        filestream = self.Loader(type)
        file = self.Decoder(filestream)
        filestream.close()
        return file

    def Loader(self, model):
        filestream = open(filedict[model], "r", newline='', encoding="UTF-8")
        return filestream

    def Decoder(self, filestream):
        first = True
        players = []
        reader = csv.reader(filestream)
        for row in reader:
            if first == True:
                first = False
                continue
            players.append(row)
        return players

    def create_model(self, model):
        file_name = filedict[model.model()]
        print(file_name)
        with open(file=file_name, mode="a", encoding="utf-8", newline="") as csvfile:
            fnames = fieldnames[model.model()]
            writer = csv.writer(csvfile)
            writer.writerow(model.listify())

    def Update(self, update, type):
        linestr = ""
        for line in update:
            for item in line:
                linestr += item + ","
            linestr += '\n'
        file = open(type, "w")
        file.write(linestr)
        file.close

    def getResults(self, resultsID):
        resultstream = self.Loader(resultsID=str)
        resultsfile = [[]]
        for line in resultstream:
            for item in line.split():
                resultsfile[line].append(item)
        return resultsfile

    def updateResults(self, newresults, resultsID):
        linestr = ""
        create_new_results = open(
            resultsID.csv, "x", newline=' ', encoding="UTF-8")
        create_new_results.close()
        write_new_results = open(
            resultsID.csv, "w", newline=' ', encoding="UTF-8")
        for line in newresults:
            for items in line:
                linestr += items + ","
            linestr += '\n'
        write_new_results.write(linestr)
        write_new_results.close()