import wx

class GardenLoadView(wx.Panel):

    def __init__(self, parent, on_load, on_back):
        super().__init__(parent)

        self.on_load_controller = on_load
        self.gardensButtons = []
        label = wx.StaticText(self, label="LOAD GARDEN", pos=(20, 20))

        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        label.SetFont(font)
        label.SetForegroundColour(wx.Colour(255, 0, 0))

        self.buttonBack = wx.Button(self, label="back to menu", pos=(20, 100))
        self.buttonBack.Bind(wx.EVT_BUTTON, on_back)

        self.SetSize((1024, 768))


    def add_buttons_for_gardens(self, gardensNames):
        for id, garden in enumerate(gardensNames):
            button = wx.Button(self, label=garden, pos=(20, 60 + 40*id))
            button.Bind(wx.EVT_BUTTON, lambda event, gdn=garden: self.on_load_controller(gdn, event))
            self.gardensButtons.append(button)

    def update_view(self):
        self.buttonBack.SetPosition((20, 60 + 40 * len(self.gardensButtons)))

    def remove_gardens_from_view(self):
        self.gardensButtons = []
