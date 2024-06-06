import datetime
import wx

class InfoDialog(wx.Dialog):
    """
    Dialog window for displaying information about a flower or decoration.
    """

    def __init__(self, parent, name, color, wateringFrequency, nextWatering):
        """
        Initializes the InfoDialog.

        Args:
            parent: The parent window.
            name (str): The name of the flower or decoration.
            color: The color of the flower or decoration.
            wateringFrequency: The watering frequency of the flower.
            nextWatering: The date of the next watering.
        """
        super().__init__(parent, title="Information")

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        nameLabel = wx.StaticText(panel, label=f"Name: {name}")
        colorLabel = wx.StaticText(panel, label=f"Color: {color}")
        vbox.Add(nameLabel, 0, wx.ALL, 10)
        vbox.Add(colorLabel, 0, wx.ALL, 10)

        # Check if it's a flower or decoration
        if (not wateringFrequency) and (not nextWatering):
            self.SetTitle("Decoration Information")
        else:
            wateringLabel = wx.StaticText(panel, label=f"Watering Frequency: {wateringFrequency} days")
            nextWateringLabel = wx.StaticText(panel, label=f"Next Watering: {nextWatering}")
            # Highlight next watering date if it's overdue
            if nextWatering <= datetime.datetime.now():
                nextWateringLabel.SetBackgroundColour(wx.RED)
            self.SetTitle("Flower Information")
            vbox.Add(wateringLabel, 0, wx.ALL, 10)
            vbox.Add(nextWateringLabel, 0, wx.ALL, 10)

        panel.SetSizer(vbox)

        self.Centre()
