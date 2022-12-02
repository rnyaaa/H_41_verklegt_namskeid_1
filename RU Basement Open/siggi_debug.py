from ui.Main_menu_ui import Main_Menu_UI
from logic.LL_API import LL_API
from models.player import Player

test = LL_API()
print(test.getPlayers())
test.createPlayer(Player("7", "hallo", "2000", "123", "b@t.is"))
