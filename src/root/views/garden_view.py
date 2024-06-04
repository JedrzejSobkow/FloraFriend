import wx
import wx.grid

from src.root.utils.flower_dialog import FlowerDialog

CELL_SIDE_SIZE = 20

class GardenView(wx.Panel):

    def __init__(self, parent, on_cell_left_click, on_right_menu_click, on_back):
        super().__init__(parent)

        self.on_cell_left_click_controller = on_cell_left_click
        self.on_right_menu_click_controller = on_right_menu_click

        self.selected_range_of_cells = []

        self.label = wx.StaticText(self, label=f"GARDEN ___EMPTY___")
        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.label.SetFont(font)
        self.label.SetForegroundColour(wx.Colour(255, 0, 0))

        buttonBack = wx.Button(self, label="back")
        buttonBack.Bind(wx.EVT_BUTTON, on_back)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.label, 0, wx.ALL | wx.CENTER, 10)
        self.sizer.Add(buttonBack, 0, wx.ALL | wx.CENTER, 10)

        self.SetSizer(self.sizer)
        self.SetSize((1024, 768))

    def load_correct_garden(self, gardenName, gardenSize):
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

        self.grid.Bind(wx.grid.EVT_GRID_SELECT_CELL, self.on_cell_left_click_controller)
        self.grid.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.show_right_click_menu)
        self.grid.Bind(wx.grid.EVT_GRID_CMD_RANGE_SELECTING, self.save_selection)

        self.sizer.Add(self.grid, 1, wx.EXPAND | wx.ALL, 10)

        self.grid.SetGridCursor(0, 0)

        self.Layout()

    #   TODO repair grid, so that errors will not occcur after 2nd garden loading
    #   TODO repair right and left popup menu
    #   TODO repair wx.ID_ANY, so that indices can be used easily


    def save_selection(self, event):
        self.selected_range_of_cells = list(self.grid.GetSelectedBlocks())
        print("dragging")

    def show_right_click_menu(self, event):
        # row, col = event.GetRow(), event.GetCol()
        #
        # selected_cells = self.grid.GetSelectedCells()
        # print(self.selected_range_of_cells)
        #
        #
        # clicked_inside_selection = any((row, col) in selected_cells for row, col in selected_cells)
        #
        # if not clicked_inside_selection:
        print(self.selected_range_of_cells)
        row, col = event.GetRow(), event.GetCol()

        x_start, y_start, x_end, y_end = self.grid.GetSelectedCells().Get
        print(self.selected_range_of_cells)


        if not (x_start <= row <= x_end and y_start <= col <= y_end):
            self.grid.ClearSelection()
        # print(self.grid.GetSelectedCells())

        # Tworzenie menu kontekstowego
        menu = wx.Menu()
        mouse_pos = event.GetPosition()
        flover_opt = menu.Append(wx.ID_ANY, "ADD FLOWER")
        decoration_opt = menu.Append(wx.ID_ANY, "ADD DECORATION")
        remove_opt = menu.Append(wx.ID_ANY, "REMOVE")

        self.Bind(wx.EVT_MENU, lambda _: self.on_right_menu_click_controller("FLOWER"), flover_opt)
        self.Bind(wx.EVT_MENU, lambda _: self.on_right_menu_click_controller("DECORATION"), decoration_opt)
        self.Bind(wx.EVT_MENU, lambda _: self.on_right_menu_click_controller("REMOVE"), remove_opt)

        # Wyświetlanie menu kontekstowego w miejscu kliknięcia
        self.grid.PopupMenu(menu, mouse_pos)
        menu.Destroy()




    def show_flower_dialog(self):
        dialog = FlowerDialog(self)
        if dialog.ShowModal() == wx.ID_OK:
            flower_name = dialog.get_flower_name()  # Pobierz nazwę kwiatka z okienka dialogowego
            image_path = dialog.get_image_path()  # Pobierz ścieżkę obrazu z okienka dialogowego

            # Tutaj umieść kod, który wczytuje obraz z podanej ścieżki i umieszcza go w komórce siatki

            # Przykładowy kod umieszczający nazwę kwiatka w komórce
            selected_cells = self.grid.GetSelectedCells()
            for row, col in selected_cells:
                self.grid.SetCellValue(row, col, flower_name)
        dialog.Destroy()


