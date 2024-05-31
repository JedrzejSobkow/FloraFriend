import wx
import wx.grid

class GardenView(wx.Panel):

    def __init__(self, parent, on_cell_left_click, on_cell_right_click, on_left_menu_click, on_right_menu_click, on_back):
        super().__init__(parent)

        # self.label = wx.StaticText(self, label=f"GARDEN ___EMPTY___", pos=(20, 20))
        # self.on_cell_left_click_controller = on_cell_left_click
        # self.on_cell_right_click_controller = on_cell_right_click
        # self.on_left_menu_click_controller = on_left_menu_click
        # self.on_right_menu_click_controller = on_right_menu_click
        #
        # font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        # self.label.SetFont(font)
        # self.label.SetForegroundColour(wx.Colour(255, 0, 0))
        #
        # buttonBack = wx.Button(self, label="back", pos=(20, 180))
        # buttonBack.Bind(wx.EVT_BUTTON, on_back)
        #
        # self.SetSize((1024, 768))

        self.on_cell_left_click_controller = on_cell_left_click
        self.on_cell_right_click_controller = on_cell_right_click
        self.on_left_menu_click_controller = on_left_menu_click
        self.on_right_menu_click_controller = on_right_menu_click

        self.label = wx.StaticText(self, label=f"GARDEN ___EMPTY___")
        font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)
        self.label.SetFont(font)
        self.label.SetForegroundColour(wx.Colour(255, 0, 0))

        buttonBack = wx.Button(self, label="back")
        buttonBack.Bind(wx.EVT_BUTTON, on_back)

        # Tworzenie sizerów
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.label, 0, wx.ALL | wx.CENTER, 10)
        self.sizer.Add(buttonBack, 0, wx.ALL | wx.CENTER, 10)

        self.SetSizer(self.sizer)
        self.SetSize((1024, 768))

    def load_correct_garden(self, gardenName, gardenSize):
        # self.label.SetLabel(gardenName)
        #
        # self.grid = wx.grid.Grid(self)
        # self.grid.SetPosition((20, 60))
        # self.grid.CreateGrid(3, 3)
        #
        # # Dodanie zdarzenia kliknięcia w komórkę siatki
        # self.grid.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.on_cell_left_click_controller)
        # self.grid.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.on_cell_right_click_controller)
        #
        # self.Layout()

        self.label.SetLabel(gardenName)

        # Usuń starą siatkę, jeśli istnieje
        if hasattr(self, 'grid'):
            self.sizer.Remove(self.grid)
            self.grid.Destroy()

        # Tworzenie nowej siatki
        self.grid = wx.grid.Grid(self)
        self.grid.CreateGrid(gardenSize[0], gardenSize[1])

        # Dodanie zdarzenia kliknięcia w komórkę siatki
        self.grid.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.on_cell_left_click_controller)
        self.grid.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.on_cell_right_click_controller)

        # Dodanie siatki do sizer'a
        self.sizer.Add(self.grid, 1, wx.EXPAND | wx.ALL, 10)

        # Przeorganizowanie układu
        self.Layout()
    #   TODO repair grid, so that errors will not occcur after 2nd garden loading
    #   TODO repair right and left popup menu
    #   TODO repair wx.ID_ANY, so that indices can be used easily



    def show_right_click_menu(self, mouse_pos):
        # Tworzenie menu kontekstowego
        menu = wx.Menu()
        item1 = menu.Append(wx.ID_ANY, "Opcja 1")
        item2 = menu.Append(wx.ID_ANY, "Opcja 2")
        item3 = menu.Append(wx.ID_ANY, "Opcja 3")
        self.Bind(wx.EVT_MENU, self.on_right_menu_click_controller, item1)
        self.Bind(wx.EVT_MENU, self.on_right_menu_click_controller, item2)
        self.Bind(wx.EVT_MENU, self.on_right_menu_click_controller, item3)

        # Wyświetlanie menu kontekstowego w miejscu kliknięcia
        self.PopupMenu(menu, mouse_pos)
        menu.Destroy()

    def show_left_click_menu(self, mouse_pos):
        menu = wx.Menu()
        item1 = menu.Append(wx.ID_ANY, "LEWA Opcja 1")
        item2 = menu.Append(wx.ID_ANY, "LEWA Opcja 2")
        item3 = menu.Append(wx.ID_ANY, "LEWAOpcja 3")
        self.Bind(wx.EVT_MENU, self.on_left_menu_click_controller, item1)
        self.Bind(wx.EVT_MENU, self.on_left_menu_click_controller, item2)
        self.Bind(wx.EVT_MENU, self.on_left_menu_click_controller, item3)

        # Wyświetlanie menu kontekstowego w miejscu kliknięcia
        self.PopupMenu(menu, mouse_pos)
        menu.Destroy()
