import wx
import wx.grid

from src.root.utils.flower_dialog import FlowerDialog
from src.root.utils.decoration_dialog import DecorationDialog
from src.root.utils.info_dialog import InfoDialog

CELL_SIDE_SIZE = 20


class GardenView(wx.Panel):
    """Panel for displaying and interacting with a garden."""

    def __init__(self, parent, on_cell_left_click, on_menu_click, on_back, on_save, add_flower, add_decoration, on_mode_click, on_delete_garden):
        """Initialize the garden view.

        Args:
            parent: The parent window.
            on_cell_left_click (function): Function to call on left click on a cell.
            on_menu_click (function): Function to call on right click to show menu.
            on_back (function): Function to call to go back.
            on_save (function): Function to call to save the garden.
            add_flower (function): Function to call to add a flower.
            add_decoration (function): Function to call to add a decoration.
            on_mode_click (function): Function to call on mode change click.
            on_delete_garden (function): Function to call to delete the garden.
        """
        super().__init__(parent)

        self.on_cell_left_click_controller = on_cell_left_click
        self.on_menu_click_controller = on_menu_click
        self.add_flower_controller = add_flower
        self.add_decoration_controller = add_decoration
        self.on_save_controller = on_save
        self.on_mode_click_controller = on_mode_click
        self.on_delete_garden_controller = on_delete_garden

        self.label = wx.StaticText(self, label=f"GARDEN UNKNOWN")
        font = wx.Font(24, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.label.SetFont(font)

        buttonBack = wx.Button(self, label="Back")
        buttonBack.Bind(wx.EVT_BUTTON, on_back)

        buttonSave = wx.Button(self, label="Save")
        buttonSave.Bind(wx.EVT_BUTTON, on_save)

        buttonDuplicate = wx.Button(self, label="Duplicate")
        buttonDuplicate.Bind(wx.EVT_BUTTON, lambda _: self.on_mode_click_controller("DUPLICATE"))

        buttonDelete = wx.Button(self, label="Delete")
        buttonDelete.Bind(wx.EVT_BUTTON, lambda _: self.on_mode_click_controller("DELETE"))

        buttonShowInfo = wx.Button(self, label="Show info")
        buttonShowInfo.Bind(wx.EVT_BUTTON, lambda _: self.on_mode_click_controller("INFO"))

        buttonWaterGroup = wx.Button(self, label="Water plants")
        buttonWaterGroup.Bind(wx.EVT_BUTTON, lambda _: self.on_mode_click_controller("WATER"))

        buttonDeleteGarden = wx.Button(self, label="Garden delete")
        buttonDeleteGarden.Bind(wx.EVT_BUTTON, lambda _: self.on_delete_garden_controller())

        buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        buttonSizer.Add(buttonBack, 0, wx.ALL | wx.CENTER, 10)
        buttonSizer.Add(buttonSave, 0, wx.ALL | wx.CENTER, 10)
        buttonSizer.Add(buttonDuplicate, 0, wx.ALL | wx.CENTER, 10)
        buttonSizer.Add(buttonDelete, 0, wx.ALL | wx.CENTER, 10)
        buttonSizer.Add(buttonShowInfo, 0, wx.ALL | wx.CENTER, 10)
        buttonSizer.Add(buttonWaterGroup, 0, wx.ALL | wx.CENTER, 10)
        buttonSizer.Add(buttonDeleteGarden, 0, wx.ALL | wx.CENTER, 10)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.label, 0, wx.ALL | wx.CENTER, 10)
        self.sizer.Add(buttonSizer, 0, wx.EXPAND)
        self.SetSizer(self.sizer)
        self.SetSize((1024, 768))

    def load_correct_garden(self, gardenName, gardenSize):
        """Load the correct garden into the view.

        Args:
            gardenName (str): Name of the garden.
            gardenSize (tuple): Size of the garden as (width, height).
        """
        self.label.SetLabelText(f"GARDEN: {gardenName}")

        if hasattr(self, 'grid'):
            self.sizer.Detach(self.grid)
            self.grid.Destroy()

        self.grid = wx.grid.Grid(self)
        self.grid.CreateGrid(gardenSize[0], gardenSize[1])

        self.grid.SetColSizes(wx.grid.GridSizesInfo(CELL_SIDE_SIZE, []))
        self.grid.SetRowSizes(wx.grid.GridSizesInfo(CELL_SIDE_SIZE, []))
        self.grid.HideColLabels()
        self.grid.HideRowLabels()

        self.grid.DisableDragColSize()
        self.grid.DisableDragRowSize()
        self.grid.SetSelectionMode(wx.grid.Grid.GridSelectNone)

        self.grid.EnableEditing(False)

        self.grid.Bind(wx.grid.EVT_GRID_SELECT_CELL, self.on_cell_left_click_controller)
        self.grid.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.show_menu)

        grid_sizer = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer.Add(self.grid, 1, wx.EXPAND | wx.ALL, 10)

        self.sizer.Add(grid_sizer, 1, wx.EXPAND | wx.ALL | wx.CENTER, 10)

        self.grid.SetGridCursor(-1, -1)
        self.Layout()

    def show_menu(self, event):
        """Show the context menu when right-clicked on a cell."""
        row, col = event.GetRow(), event.GetCol()
        self.grid.ClearSelection()
        self.grid.SelectBlock(row, col, row, col)

        menu = wx.Menu()
        mouse_pos = event.GetPosition()
        flower_opt = menu.Append(wx.ID_ANY, "ADD FLOWER")
        decoration_opt = menu.Append(wx.ID_ANY, "ADD DECORATION")

        self.Bind(wx.EVT_MENU, lambda event: self.on_menu_click_controller("FLOWER", (row, col)), flower_opt)
        self.Bind(wx.EVT_MENU, lambda event: self.on_menu_click_controller("DECORATION", (row, col)), decoration_opt)

        self.grid.PopupMenu(menu, mouse_pos)
        menu.Destroy()

    def show_flower_dialog(self, pos):
        """Show the flower dialog."""
        dialog = FlowerDialog(self)
        if dialog.ShowModal() == wx.ID_OK:
            flower_name = dialog.get_flower_name()
            flower_color = dialog.get_flower_color()
            watering_freq = dialog.get_watering_freq()

            self.add_flower_controller(pos, flower_name, flower_color, watering_freq)
        dialog.Destroy()

    def show_decoration_dialog(self, pos):
        """Show the decoration dialog."""
        dialog = DecorationDialog(self)
        if dialog.ShowModal() == wx.ID_OK:
            decoration_name = dialog.get_decoration_name()
            decoration_color = dialog.get_decoration_color()

            self.add_decoration_controller(pos, decoration_name, decoration_color)

        dialog.Destroy()

    def change_cell_color_and_content(self, pos, color, content):
        """Change the color and content of a cell."""
        row, col = pos
        if row < 0 or row >= self.grid.GetNumberRows() or col < 0 or col >= self.grid.GetNumberCols():
            return
        self.grid.SetCellBackgroundColour(row, col, color)
        self.grid.SetCellValue(row, col, content)
        self.Refresh()

    def show_info(self, name, color, wateringFrequency=None, nextWatering=None):
        """Show the info dialog."""
        infoDialog = InfoDialog(self, name, color, wateringFrequency, nextWatering)
        infoDialog.ShowModal()
        infoDialog.Destroy()
