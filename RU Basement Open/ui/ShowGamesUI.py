from ui.UI import Menu_prompt


class ShowGamesUI():

    def showGamesPage():
        """Displays game overview menu."""
        while True:
            print(78*"_")
            print()
            print(
                "➢  Valmynd:\n"
                "\n"
                "1.	Listi yfir komandi viðureignir\n"
                "2.	Listi yfir yfirstaðnar viðureignir\n")

            user_input = Menu_prompt.menuFooter(False)
            return user_input

    def showTournamentDates():
        raise NotImplementedError

    def showGamesFinished():
        raise NotImplementedError

    def showUpcomingGames():
        raise NotImplementedError
