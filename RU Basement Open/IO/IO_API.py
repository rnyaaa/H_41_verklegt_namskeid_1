import os
import csv
filedict = {
    "players": "models/players.csv",
    "games": "models/teams.csv",
    "teams": "models/teams.csv",
    "tournaments": "models/tournaments.csv"
}

fieldnames = {
    "players": ["id", "name", "birth_year", "phone_nr", "email"]
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
            writer = csv.DictWriter(csvfile, fieldnames=fnames)
            d = {}
            counter = 0
            for field in fnames:
                d[field] = model.listify()[counter]
                counter += 1
            writer.writerow(d)

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
