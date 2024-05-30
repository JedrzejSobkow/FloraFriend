import wx

class GardenCreateView(wx.Panel):

    def __init__(self, parent, on_save, on_discard, on_clear, on_back):
        super().__init__(parent)

        label = wx.StaticText(self, label="GARDEN CREATION", pos=(20, 20))

        # Ustawianie czcionki i koloru tekstu
        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        label.SetFont(font)
        label.SetForegroundColour(wx.Colour(255, 0, 0))

        button_save = wx.Button(self, label="save garden", pos=(20, 60))
        button_save.Bind(wx.EVT_BUTTON, on_save)

        button_discard = wx.Button(self, label="discard garden", pos=(20, 100))
        button_discard.Bind(wx.EVT_BUTTON, on_discard)

        button_clear = wx.Button(self, label="clear garden", pos=(20, 140))
        button_clear.Bind(wx.EVT_BUTTON, on_clear)

        button_back = wx.Button(self, label="back to menu", pos=(20, 180))
        button_back.Bind(wx.EVT_BUTTON, on_back)

        self.SetSize((1024, 768))





