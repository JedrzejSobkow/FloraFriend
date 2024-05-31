import wx
from src.root.utils.numeric_text_box import NumericTextBox

class GardenCreateIntroView(wx.Panel):

    def __init__(self, parent, on_next, on_back):
        super().__init__(parent)

        self.on_next_controller = on_next
        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        label = wx.StaticText(self, label="GARDEN CREATION INTRO", pos=(20, 20))

        label.SetFont(font)
        label.SetForegroundColour(wx.Colour(255, 0, 0))

        nameLabel = wx.StaticText(self, label="Enter name for the garden", pos=(20, 60))
        nameLabel.SetFont(font)
        nameLabel.SetForegroundColour(wx.Colour(255, 0, 0))

        self.enterNameBox = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER, pos=(20, 100))
        self.enterNameBox.SetMaxLength(25)

        enterWidthAndHeightLabel = wx.StaticText(self, label="Enter width and height of your garden", pos=(20, 140))
        enterWidthAndHeightLabel.SetFont(font)
        enterWidthAndHeightLabel.SetForegroundColour(wx.Colour(255, 0, 0))

        self.widthBox = NumericTextBox(self, pos=(20, 180), size=(25, 25))
        self.widthBox.SetMaxLength(2)

        slashLabel = wx.StaticText(self, label="\\", pos=(50, 180))
        slashLabel.SetFont(font)
        slashLabel.SetForegroundColour(wx.Colour(255, 0, 0))

        self.heightBox = NumericTextBox(self, pos=(65, 180), size=(25, 25))
        self.heightBox.SetMaxLength(2)

        buttonNext = wx.Button(self, label="next", pos=(20, 220))
        buttonNext.Bind(wx.EVT_BUTTON, self.get_data_from_boxes)

        buttonBack = wx.Button(self, label="back", pos=(20, 260))
        buttonBack.Bind(wx.EVT_BUTTON, on_back)

        self.SetSize((1024, 768))


    def get_data_from_boxes(self, event):
        width = int(self.widthBox.GetValue()) if self.widthBox.GetValue() != '' else 0
        height = int(self.heightBox.GetValue()) if self.heightBox.GetValue() != '' else 0
        self.on_next_controller(gardenName=self.enterNameBox.GetValue(),
                                gardenSize=(width, height), event=event)


