import wx

class GardenLoadView(wx.Panel):
    """Panel for loading gardens."""

    def __init__(self, parent, on_load, on_back):
        """Initialize the view.

        Args:
            parent: The parent window.
            on_load (function): Function to call when loading a garden.
            on_back (function): Function to call when moving back.
        """
        super().__init__(parent)

        self.SetSize(parent.GetSize())

        self.on_load_controller = on_load
        self.gardensButtons = []

        # Label for garden loading
        label = wx.StaticText(self, label="LOAD GARDEN")
        self.font = wx.Font(24, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        label.SetFont(self.font)
        label.SetPosition((self.GetSize().width / 2 - label.GetSize()[0] / 2, 50))

        # Back button
        self.buttonBack = wx.Button(self, label="Go Back")
        self.buttonBack.SetFont(self.font)
        self.buttonBack.SetSize(200, 100)
        self.buttonBack.SetPosition((self.GetSize().width / 2 - self.buttonBack.GetSize()[0] / 2, 25 + self.buttonBack.GetSize()[1]))
        self.buttonBack.Bind(wx.EVT_BUTTON, on_back)

    def add_buttons_for_gardens(self, gardensNames):
        """Add buttons for loading gardens.

        Args:
            gardensNames (list): List of garden names.
        """
        startingY = self.buttonBack.GetPosition()[1] + self.buttonBack.GetSize()[1]

        for id, garden in enumerate(gardensNames):
            x, y, width, height = self.get_position_and_size_for_garden_button(id, 0, startingY, self.GetSize()[0], self.GetSize()[1], 50, 25)
            button = wx.Button(self, label=garden)
            button.SetPosition((x, y))
            button.SetSize((width, height))
            button.SetFont(self.font)
            button.Bind(wx.EVT_BUTTON, lambda event, gdn=garden: self.on_load_controller(gdn, event))
            self.gardensButtons.append(button)

    def remove_all_buttons_for_garden(self):
        """Remove all buttons for gardens."""
        for button in self.gardensButtons:
            button.Destroy()
        self.gardensButtons = []

    def get_position_and_size_for_garden_button(self, gardenButtonNumber, xStart, yStart, xEnd, yEnd, xSpacing, ySpacing):
        """Calculate position and size for a garden button.

        Args:
            gardenButtonNumber (int): Index of the garden button.
            xStart (int): Starting x-coordinate.
            yStart (int): Starting y-coordinate.
            xEnd (int): Ending x-coordinate.
            yEnd (int): Ending y-coordinate.
            xSpacing (int): Spacing between buttons along x-axis.
            ySpacing (int): Spacing between buttons along y-axis.

        Returns:
            tuple: Position and size of the button (x, y, width, height).
        """
        col = gardenButtonNumber % 2
        row = gardenButtonNumber // 2
        width = ((xEnd - xStart) - 4 * xSpacing) / 2
        height = ((yEnd - yStart) - 6 * ySpacing) / 4
        x = xStart + xSpacing
        if col == 1:
            x = xEnd - xSpacing - width
        y = yStart + ySpacing * (1 + row) + height * row

        return (x, y, width, height)
