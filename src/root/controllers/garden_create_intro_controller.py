from src.root.controllers.controller_base import BaseController
from src.root.views.garden_create_intro_view import GardenCreateIntroView
from src.root.models.garden_model import GardenModel


class GardenCreateIntroController(BaseController):
    def __init__(self, mainController):
        self.view = GardenCreateIntroView(mainController.mainFrame, self.on_next, self.on_back)
        self.view.Hide()
        self.mainController = mainController


    def take_control(self):
        self.view.Show()


    def on_next(self, gardenName, gardenSize, event):
        if GardenModel.validate_garden_name(gardenName) and GardenModel.validate_garden_size(gardenSize):
            garden = GardenModel(gardenName, gardenSize)
            self.mainController.add_garden(garden)
            print(f"Garden '{garden}' created")
            self.view.Hide()
            self.mainController.load_garden(gardenName)
            self.mainController.change_controller("garden create")

        else:
            print("INVALID DATA")
        pass
    #     TODO
    #     CHECK IF NAME ENTERED AND IF NAME CAN BE USED (NAME NOT FOUND IN DATABASE)
    #     CHECK IF BOARD SIZE ENTERED AND IF IS CORRECT

    def on_back(self, event):
        if input("ARE YOU SURE YOU WANT TO LEAVE WITHOUT SAVING? Y/n").lower() == "y":
            self.mainController.change_controller("menu")
#         TODO
#         MAKE SURE USER DOESN'T WANT TO CONTINUE

