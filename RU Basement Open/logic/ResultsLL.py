from logic.LL_API import LL_API

class ResultsLL():

    def getResults(resultsID):
        resultstream = LL_API.getResults(resultsID)

    def changeResults():
        """ TODO: Fatta hvernig við tökum results úr gagnagrunni, breytum þeim og vistum nýrri útgáfu"""
        """ Þetta þarf líka að geta uppfært player, team og tournament gildi."""
        raise NotImplementedError

    def updateResults(newresults, resultsID):
        """TODO: Fatta hvernig við fáum inn results í LL og hvernig við geymum ný"""
        """ Hvernig á að uppfæra playerr, team og tournament gagnagrunninn út frá þessu?"""
        LL_API.updateResults(newresults, resultsID)