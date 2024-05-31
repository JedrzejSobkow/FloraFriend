from src.root.controllers.controller_base import BaseController
from src.root.views.garden_create_view import GardenCreateView
from src.root.utils.json_database_controller import save_json
from src.root.utils.constants import GARDENS_DATA_FILENAME


class GardenCreateController(BaseController):
    def __init__(self, mainController):
        self.view = GardenCreateView(mainController.mainFrame, self.on_save, self.on_discard, self.on_clear, self.on_back)
        self.view.Hide()
        self.mainController = mainController


    def take_control(self):
        self.view.Show()


    def on_save(self, event):
        self.view.Hide()
        print("SAVED")
        # DO NOT SAVE ALL DATA
        save_json(GARDENS_DATA_FILENAME, self.mainController.all_gardens)
        self.mainController.change_controller("menu")

    def on_discard(self, event):
        self.view.Hide()
        print("NOT SAVED")
        self.mainController.change_controller("menu")

    def on_clear(self, event):
        print("PANEL IS CLEAN")

    def on_back(self, event):
        if input("ARE YOU SURE YOU WANT TO LEAVE WITHOUT SAVING? Y/n").lower() == "y":
            self.on_discard(event)

