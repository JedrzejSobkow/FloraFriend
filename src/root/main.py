# DO ZMIANY:
# wprowadzenia wersji pythona wymaganej do uruchomienia aplikacji w git.
# wprowadzenie versji bibliotek do zaintalowania w requirements.txt

# TODO
# 31.05 - podstawowe okno tworzenia ogrodu
# 31.05 - działająca baza danych

import wx
from controllers.main_controller import MainController


def create_app_window():
    app = wx.App()

    frame = wx.Frame(None, title="Flora Friend", size=(1024, 768))

    frame.Centre()
    frame.Show()
    MainController(frame)

    app.MainLoop()



# Wywołanie funkcji tworzącej okienko aplikacji

if __name__ == "__main__":
    create_app_window()
