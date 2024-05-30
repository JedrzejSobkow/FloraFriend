import wx

class MenuView(wx.Panel):

    def __init__(self, parent, on_create_garden, on_load_garden, on_close):
        super().__init__(parent)

        label = wx.StaticText(self, label="MENU VIEW", pos=(20, 20))

        # Ustawianie czcionki i koloru tekstu
        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        label.SetFont(font)
        label.SetForegroundColour(wx.Colour(255, 0, 0))

        button_create_garden = wx.Button(self, label="garden creation", pos=(20, 60))
        button_create_garden.Bind(wx.EVT_BUTTON, on_create_garden)

        button_load_garden = wx.Button(self, label="load garden", pos=(20, 100))
        button_load_garden.Bind(wx.EVT_BUTTON, on_load_garden)

        button_close = wx.Button(self, label="close app", pos=(20, 140))
        button_close.Bind(wx.EVT_BUTTON, on_close)

        self.SetSize((1024, 768))





