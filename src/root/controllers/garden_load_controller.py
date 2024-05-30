from src.root.controllers.controller_base import BaseController
from src.root.views.garden_load_view import GardenLoadView

class GardenLoadController(BaseController):
    def __init__(self, mainController):
        self.view = GardenLoadView(mainController.mainFrame, self.on_load, self.on_back)
        self.view.Hide()
        self.mainController = mainController

    def take_control(self):
        self.view.Show()


    def on_load(self, garden_name, event):
        self.view.Hide()
        print(f"GARDEN: {garden_name} LOADED")
        self.mainController.set_loaded_garden_name(garden_name)
        self.mainController.change_controller("garden")


    def on_back(self, event):
        self.view.Hide()
        self.mainController.change_controller("menu")
