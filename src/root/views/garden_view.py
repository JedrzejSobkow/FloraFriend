import wx

class GardenView(wx.Panel):

    def __init__(self, parent, on_back):
        super().__init__(parent)

        self.label = wx.StaticText(self, label=f"GARDEN ___EMPTY___", pos=(20, 20))

        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.label.SetFont(font)
        self.label.SetForegroundColour(wx.Colour(255, 0, 0))

        button_back = wx.Button(self, label="back", pos=(20, 180))
        button_back.Bind(wx.EVT_BUTTON, on_back)

        self.SetSize((1024, 768))

    def load_correct_garden(self, gardenName):
        self.label.SetLabel(gardenName)






