#from ui.UI import Main_Menu, OrganizerUI
from models.player import Player
from ui.UI import CaptainUI
from ui.Main_menu_ui import Main_Menu_UI
from logic.LL_API import LL_API

test = LL_API()
# print(test.getPlayers())
test.createPlayer(Player("7", "hallo", "2000", "123", "b@t.is"))
