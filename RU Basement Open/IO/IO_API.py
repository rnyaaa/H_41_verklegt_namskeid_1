import csv
import os
from typing import Any

from models.game import Game
from models.player import Player
from models.playerscore import PlayerScore
from models.results import Results
from models.team import Team
from models.teamscore import TeamScore
from models.tournament import Tournament


class IO_API:

    def __init__(self):
        """ a filename dict keyed by class objects """
        self.filedict = {
            Player: "models/players.csv",
            Game: "models/games.csv",
            Team: "models/teams.csv",
            Tournament: "models/tournaments.csv",
            PlayerScore: "models/playerscore.csv",
            TeamScore: "models/teamscore.csv",
            Results: "models/results.csv"
        }
        """ a fieldname dict keyed by class objects """
        self.fieldnames = {
            Player: ["id", "name", "mobile", "home_phone", "email", "address", "team_id", "is_captain"],
            Team: ["id", "team_name", "address", "association_name", "phone_nr", "total_games_won", "total_rounds_won", "player1", "player2", "player3", "player4"],
            Tournament: ["id", "name", "organizer_name", "organizer_phone", "start_date", "end_date"],
            PlayerScore: ["gameid", "playerid", "QPs", "inshots", "outshots", "win501_1",
                          "lose501_1", "win301", "lose301", "wincricket", "losecricket", "win501_4", "lose501_4"],
<<<<<<< HEAD
            TeamScore: ["team_id", "tournament_id", "game_id", "games_won", "rounds_won"],
=======
            TeamScore: [],
>>>>>>> 8eb8f16d053b6847806609e75461db9998303892
            Game: ["gameid", "tournament_id", "home_team",
                   "away_team", "self.date", "self.results"]
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
            next(reader) # skip first row
            for row in reader:
                row_return = []
                for item in row:
                    try:
                        item = int(item)
                    except ValueError:
                        item = item 
                    row_return.append(item)
                model_return.append(row_return)
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

    def update(self, updated_model):
        tournaments = self.return_model(updated_model.__class__)
        for i in range(len(tournaments)):
            if updated_model.id == tournaments[i].id:
                tournaments[i] = updated_model
        with open(self.filedict[updated_model.__class__], mode="w", encoding="utf-8", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.fieldnames[updated_model.__class__])
            for tournament in tournaments:
                writer.writerow(tournament.listify())
