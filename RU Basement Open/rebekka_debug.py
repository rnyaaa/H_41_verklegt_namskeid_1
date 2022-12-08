from ui.Main_menu_ui import Main_Menu_UI
from logic.LL_API import LL_API
from IO.IO_API import IO_API

ioapi = IO_API()
llapi = LL_API(ioapi)
menu = Main_Menu_UI(llapi)
menu.header()
menu.displayMainMenu()