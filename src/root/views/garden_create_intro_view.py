import wx
from src.root.utils.numeric_text_box import NumericTextBox
from src.root.utils.constants import MAX_BOARD_SIZE
from src.root.utils.constants import MIN_BOARD_SIZE
from src.root.utils.constants import MIN_AND_MAX_GARDEN_NAME_LENGTH

class GardenCreateIntroView(wx.Panel):
    """Panel for creating a garden.

    Attributes:
        on_next_controller (function): Function to call when moving to the next step.
        enterNameBox (wx.TextCtrl): Text control for entering the garden name.
        widthBox (NumericTextBox): Text box for entering the width of the garden.
        heightBox (NumericTextBox): Text box for entering the height of the garden.
    """

    def __init__(self, parent, on_next, on_back):
        """Initialize the view.

        Args:
            parent: The parent window.
            on_next (function): Function to call when moving to the next step.
            on_back (function): Function to call when moving to the previous step.
        """
        super().__init__(parent)

        spacing = 25

        self.SetSize(parent.GetSize())

        self.on_next_controller = on_next

        font = wx.Font(24, wx.DEFAULT, wx.NORMAL, wx.BOLD)

        # Label for garden creation
        label = wx.StaticText(self, label="GARDEN CREATION")
        label.SetFont(font)
        label.SetPosition((self.GetSize().width / 2 - label.GetSize()[0] / 2, 50))

        labelHeight = label.GetSize()[1]

        # Label for garden name
        nameLabel = wx.StaticText(self, label="Enter name for the garden")
        nameLabel.SetFont(font)
        nameLabel.SetPosition((self.GetSize().width / 2 - nameLabel.GetSize()[0] / 2, 50 + labelHeight + spacing))

        # Text control for entering garden name
        self.enterNameBox = wx.TextCtrl(self, style=wx.TE_PROCESS_ENTER)
        self.enterNameBox.SetMaxLength(MIN_AND_MAX_GARDEN_NAME_LENGTH[1])
        self.enterNameBox.SetFont(font)
        self.enterNameBox.SetSize(nameLabel.GetSize())
        self.enterNameBox.SetPosition((self.GetSize().width / 2 - self.enterNameBox.GetSize()[0] / 2, 50 + labelHeight * 2 + 2 * spacing))

        # Label for entering garden width and height
        enterWidthAndHeightLabel = wx.StaticText(self, label=f"Enter width and height of your garden(min={max(MIN_BOARD_SIZE)}; max={min(MAX_BOARD_SIZE)})")
        enterWidthAndHeightLabel.SetFont(font)
        enterWidthAndHeightLabel.SetPosition((self.GetSize().width / 2 - enterWidthAndHeightLabel.GetSize()[0] / 2, 50 + labelHeight * 3 + 3 * spacing))

        # Text box for entering garden width
        self.widthBox = NumericTextBox(self, size=(25, 25))
        self.widthBox.SetMaxLength(2)
        self.widthBox.SetFont(font)

        # Slash label
        slashLabel = wx.StaticText(self, label="\\")
        slashLabel.SetFont(font)

        # Text box for entering garden height
        self.heightBox = NumericTextBox(self, size=(25, 25))
        self.heightBox.SetMaxLength(2)
        self.heightBox.SetFont(font)

        self.widthBox.SetSize((enterWidthAndHeightLabel.GetSize()[0]/4, slashLabel.GetSize()[1]))
        self.heightBox.SetSize((enterWidthAndHeightLabel.GetSize()[0]/4, slashLabel.GetSize()[1]))

        slashLabel.SetPosition((self.GetSize().width / 2 - slashLabel.GetSize()[0]/2, 50 + labelHeight * 4 + 4 * spacing))
        self.widthBox.SetPosition((self.GetSize().width / 2 - self.widthBox.GetSize()[0] - slashLabel.GetSize()[0], 50 + labelHeight * 4 + 4 * spacing))
        self.heightBox.SetPosition((self.GetSize().width / 2 + slashLabel.GetSize()[0], 50 + labelHeight * 4 + 4 * spacing))

        # Next button
        buttonNext = wx.Button(self, label="next")
        buttonNext.Bind(wx.EVT_BUTTON, self.get_data_from_boxes)
        buttonNext.SetSize((300, labelHeight * 2))
        buttonNext.SetPosition((self.GetSize().width / 2 - buttonNext.GetSize()[0] / 2, 50 + labelHeight * 6 + 6 * spacing))
        buttonNext.SetFont(font)

        # Back button
        buttonBack = wx.Button(self, label="back")
        buttonBack.Bind(wx.EVT_BUTTON, on_back)
        buttonBack.SetSize((300, labelHeight*2))
        buttonBack.SetPosition((self.GetSize().width / 2 - buttonBack.GetSize()[0] / 2, 50 + labelHeight * 8 + 8 * spacing))
        buttonBack.SetFont(font)

        self.SetSize((1024, 768))


    def get_data_from_boxes(self, event):
        """Get data entered by user."""
        width = int(self.widthBox.GetValue()) if self.widthBox.GetValue() != '' else 0
        height = int(self.heightBox.GetValue()) if self.heightBox.GetValue() != '' else 0
        self.on_next_controller(garden_name=self.enterNameBox.GetValue(),
                                garden_size=(width, height), event=event)


    def highlight_incorrect_name(self):
        """Highlight incorrect garden name."""
        self.enterNameBox.SetBackgroundColour(wx.RED)

    def highlight_incorrect_width(self):
        """Highlight incorrect garden width."""
        self.widthBox.SetBackgroundColour(wx.RED)

    def highlight_incorrect_height(self):
        """Highlight incorrect garden height."""
        self.heightBox.SetBackgroundColour(wx.RED)

    def unhighlight_every_field(self):
        """Remove highlighting from all fields."""
        self.enterNameBox.SetBackgroundColour(wx.NullColour)
        self.widthBox.SetBackgroundColour(wx.NullColour)
        self.heightBox.SetBackgroundColour(wx.NullColour)
