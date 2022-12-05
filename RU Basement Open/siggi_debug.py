from ui.Main_menu_ui import Main_Menu_UI
from ui.UI import Menu_functions
from logic.LL_API import LL_API
from IO.IO_API import IO_API

dags = Menu_functions.getDate("Sláðu inn dags. (dd.mm.yy): ")
print(dags)
