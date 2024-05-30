import wx

class GardenLoadView(wx.Panel):

    def __init__(self, parent, on_load, on_back):
        super().__init__(parent)

        label = wx.StaticText(self, label="LOAD GARDEN", pos=(20, 20))

        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        label.SetFont(font)
        label.SetForegroundColour(wx.Colour(255, 0, 0))

        gardens = ["mojOgrod123", "WMOIMOGRODECKU", "TEST"]

        for id, garden in enumerate(gardens):
            button = wx.Button(self, label=garden, pos=(20, 60 + 40*id))
            button.Bind(wx.EVT_BUTTON, lambda event, garden=garden: on_load(garden, event))

        button_back = wx.Button(self, label="back to menu", pos=(20, 180))
        button_back.Bind(wx.EVT_BUTTON, on_back)

        self.SetSize((1024, 768))





