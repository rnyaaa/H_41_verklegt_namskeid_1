import os
import csv

from models.game import Game
from models.player import Player
from models.playerscore import PlayerScore
from models.tournament import Tournament
from models.team import Team

class IO_API:

    def __init__(self):
        self.filedict = {
            Player: "models/players.csv",
            Game: "models/games.csv",
            Team: "models/teams.csv",
            Tournament: "models/tournaments.csv",
            PlayerScore: "models/playerscore.csv"
        }
        self.fieldnames = {
            Player: ["id", "name", "birth_year", "phone_nr", "email"],
            Team: ["id", "team_name", "address", "association_name", "phone_nr", "total_games_won", "total_rounds_won", "player1", "player2", "player3", "player4"],
            Tournament: [""],
            PlayerScore: ["gameid", "playerid", "QPs", "inshots", "outshots", "win501_1", "lose501_1", "win301", "los301", "wincricket", "losecricket", "win501_4,lose501_4"]
        }

    def getAll(self, type=str):
        print("---------------------------------", os.getcwd())
        filestream = self.Loader(type)
        file = self.Decoder(filestream)
        filestream.close()
        return file

    def Loader(self, model, mode="r"):
        filestream = open(self.filedict[model], mode, newline='', encoding="UTF-8")
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

    def return_model(self, model_type):
        model_return = []
        with self.Loader(model_type) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                model_return.append([item for item in row])
        """ Dark magic pls do not touch """
        model_return = list(map(lambda x: model_type(*x), model_return))


    def create_model(self, model):
        with self.Loader(model.__class__, mode="w") as csvfile:
            fnames = self.fieldnames[model.__class__]
            writer = csv.writer(csvfile)
            print(model.listify())
            writer.writerow(model.listify())

    def getResults(self, resultsID):
        resultstream = IO_API.Loader(resultsID=str)
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
