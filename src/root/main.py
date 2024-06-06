
import wx
from controllers.main_controller import MainController


def create_app_window():
    app = wx.App()

    frame = wx.Frame(None, title="Flora Friend", size=(1024, 768), style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER))

    frame.Centre()
    MainController(frame)
    frame.Center()
    frame.Show()

    app.MainLoop()




if __name__ == "__main__":
    create_app_window()
