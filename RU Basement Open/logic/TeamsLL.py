from IO.IO_API import IO_API
from models.team import Team
from models.teamscore import TeamScore

class TeamsLL:

    def __init__(self, ioapi: IO_API):
        self.ioapi = ioapi

    def getAllTeams(self) -> list[Team]:
        """ returns a list of all Team instances """
        return self.ioapi.return_model(Team)

    def getTeamScore(self) -> list[TeamScore]:
        """ returns a list of all TeamScore instances """
        return self.ioapi.return_model(TeamScore)

    def getTeamScoreSummariesByTournament(self, tournamentid) -> list[TeamScore]:
        """ returns a list of all TeamScores in a tournament summarized by teamid """
        teamscores = [score for score in self.getTeamScore() if score.tournament_id == tournamentid]
        teamscores_by_team = {}
        for item in teamscores:
            if item.team_id in teamscores_by_team:
                teamscores_by_team[item.team_id].append(item)
            else:
                teamscores_by_team[item.team_id] = [item]
        team_summaries = []
        for team_id in teamscores_by_team:
            team_summary = TeamScore(team_id)
            for score in teamscores_by_team[team_id]:
                team_summary.games_won += score.games_won
                team_summary.rounds_won += score.rounds_won
            team_summaries.append(team_summary)
        return team_summaries

    def getTeamNameFromId(self, team_id) -> str:
        """ returns a team name from a team_id """
        teams = self.getAllTeams()
        for team in teams:
            if team.id == team_id:
                return team.name


    def addTeam(self, team: Team):
        """ adds a team """
        return self.ioapi.create_model(team)