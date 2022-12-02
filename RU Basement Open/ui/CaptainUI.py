from logic.LL_API import LL_API
from ui.UI import Menu_functions

class CaptainUI():

    def __init__(self, llapi: LL_API):
        self.llapi = llapi

    def displayCaptainUI():
        while True:
            print(78*"_")
            print("                      ___     \n"
                  "                    /\ _ /\   \n"
                  "    >>>----        / /\ /\ \  \n"
                  ">>>----           |---(*)---| \n"
                  "                   \ \/_\/ /  \n"
                  "        >>>----     \/___\/   \n"
                  "\n")
            print(
                "Velkominn, Fyrirliði.\n"
                "\n\n"
                "➢  Valmynd:\n"
                "\n"
                "1.  Skrá úrslit viðureignar")
            user_input = Menu_functions.menuFooter(True)
            return user_input

    def openResultsMenu():
        None
