import wx

class MenuView(wx.Panel):
    """Panel for the main menu."""

    def __init__(self, parent, on_create_garden, on_load_garden, on_close):
        """Initialize the main menu panel.

        Args:
            parent: The parent window.
            on_create_garden (function): Function to call for creating a garden.
            on_load_garden (function): Function to call for loading a garden.
            on_close (function): Function to call to close the application.
        """
        super().__init__(parent)

        self.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.SetSize(parent.GetSize())

        # Main menu title
        title = wx.StaticText(self, label="MAIN MENU")
        font = wx.Font(24, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        title.SetFont(font)
        title.SetPosition((self.GetSize().width / 2 - title.GetSize()[0] / 2, 50))

        # Menu buttons
        button_size = (400, 100)
        spacing = 50
        button_pos_y = title.GetPosition()[1] + title.GetSize()[1] + spacing

        # Positions of buttons
        positions = [
            (self.GetSize().width / 2 - button_size[0] / 2, button_pos_y + button_size[1]*i + spacing * i)
            for i in range(3)
        ]

        button_labels = ["Create Garden", "Load Garden", "Close App"]
        button_handlers = [on_create_garden, on_load_garden, on_close]

        for position, label, handler in zip(positions, button_labels, button_handlers):
            button = wx.Button(self, label=label, size=button_size)
            button.Bind(wx.EVT_BUTTON, handler)
            button.SetPosition(position)
            button.SetFont(font)
