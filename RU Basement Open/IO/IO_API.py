class IO_API:

    def getAll(type=str):
        filestream = Loader(type)
        file = Decoder(filestream)
        return file
        
    def Loader(filename):
        filestream = open(filename.csv, "r", newline=' ', encoding="UTF-8")
        return filestream

    def Decoder(filestream):
        file = [[]]
        for line in filestream:
            for item in line.split():
                file[line].append(item)
        return file

    def Update(update, type):
        linestr = ""
        for line in update:
            for item in line:
                linestr += items + ","
            linestr += '\n'
        file = open(type, "w")
        file.write(linestr)
        file.close

    def getResults(resultsID):
        resultstream = loader(resultsID=str)
        resultsfile = [[]]
        for line in resultstream:
            for item in line.split():
                resultsfile[line].append(item)
        return resultsfile

    def updateResults(newresults, resultsID):
        linestr = ""
        create_new_results = open(resultsID.csv, "x", newline=' ', encoding=UTF-8)
        create_new_results.close()
        write_new_results = open(resultsID.csv, "w", newline=' ', encoding=UTF-8)
        for line in newresults:
            for items in line:
                linestr += items + ","
            linestr += '\n'
        write_new_results.write(linestr)
        write_new_results.close()