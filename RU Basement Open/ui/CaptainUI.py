
from ui.UI import Menu_prompt

class CaptainUI():
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
            user_input = Menu_prompt.menuFooter(True)
            return user_input

    def openResultsMenu():
        None


