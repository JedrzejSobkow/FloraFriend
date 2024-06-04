from src.root.controllers.controller_base import BaseController
from src.root.views.garden_view import GardenView

class GardenController(BaseController):
    def __init__(self, mainController):
        self.view = GardenView(mainController.mainFrame, self.on_cell_left_click, self.on_right_menu_click, self.on_back)
        self.view.Hide()
        self.mainController = mainController

    def take_control(self):
        self.view.Show()
        self.view.load_correct_garden(self.mainController.get_loaded_garden_name(), self.mainController.get_loaded_garden_size())


    def on_back(self, event):
        self.view.Hide()
        self.mainController.change_controller("garden load")

    def on_cell_left_click(self, event):
        print((event.GetRow(), event.GetCol()))



    def on_right_menu_click(self, optionName):
        print(f"{optionName} CLICKED")
        if optionName == "FLOWER":
            self.view.show_flower_dialog()
