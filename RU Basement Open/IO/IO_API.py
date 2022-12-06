import os
import csv
from typing import Any
from models.game import Game
from models.player import Player
from models.playerscore import PlayerScore
from models.tournament import Tournament
from models.team import Team
from models.results import Results


class IO_API:

    def __init__(self):
        """ a filename dict keyed by class objects """
        self.filedict = {
            Player: "models/players.csv",
            Game: "RU Basement Open/models/games.csv",  # "models/games.csv",
            Team: "models/teams.csv",
            Tournament: "RU Basement Open/models/tournaments.csv",
            PlayerScore: "models/playerscore.csv",
            Results: "models/results.csv"
        }
        """ a fieldname dict keyed by class objects """
        self.fieldnames = {
            Player: ["id", "name", "phone_1", "phone_2", "email", "address"],
            Team: ["id", "team_name", "address", "association_name", "phone_nr", "total_games_won", "total_rounds_won", "player1", "player2", "player3", "player4"],
            Tournament: ["id", "name", "organizer_name", "organizer_phone", "start_date", "end_date", "tournament_type", "rounds"],
            PlayerScore: ["gameid", "playerid", "QPs", "inshots", "outshots", "win501_1",
                          "lose501_1", "win301", "los301", "wincricket", "losecricket", "win501_4,lose501_4"]
        }

    def Loader(self, model, mode="r"):
        """ loads csv files by filename and points the filestream elsewhere """
        filestream = open(self.filedict[model],
                          mode, newline='', encoding="UTF-8")
        return filestream

    def return_model(self, model_type) -> list[Any]:
        """ returns a full list of instances of any type from the records """
        model_return = []
        with self.Loader(model_type) as csvfile:
            reader = csv.reader(csvfile)
            counter = 0
            for row in reader:
                if counter > 0:
                    model_return.append([item for item in row])
                counter += 1
        # Dark magic pls do not touch
        model_return = list(map(lambda x: model_type(*x), model_return))
        return model_return

    def create_model(self, model):
        """ appends a new instance of any type to the records """
        """ Note: WE STILL NEED SOMETHING TO EDIT THE RECORDS :SSSS """
        with self.Loader(model.__class__, mode="a") as csvfile:
            fnames = self.fieldnames[model.__class__]
            writer = csv.writer(csvfile)
            writer.writerow(model.listify())

    def overwrite_model(self, list, key):
        """ overwrites the list with an edited list (for editing a model or removing entries)"""
        with self.loader(list[0].__class__, mode="w") as csvfile:
            overwriter = csv.reader(csvfile)
            for model in list:
                overwriter.writerow(model.listify())
