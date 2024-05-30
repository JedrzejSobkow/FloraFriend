from src.root.controllers.menu_controller import MenuController
from src.root.controllers.garden_creation_controller import GardenCreationController
from src.root.controllers.garden_controller import GardenController
from src.root.controllers.garden_load_controller import GardenLoadController
from src.root.controllers.all_plants_controller import AllPlantsController


class MainController:

    def __init__(self, mainFrame):

        self.mainFrame = mainFrame

        self.menuController = MenuController(self)
        self.gardenCreationController = GardenCreationController(self)
        self.gardenController = GardenController(self)
        self.gardenLoadController = GardenLoadController(self)
        # self.allPlantsController = AllPlantsController(self)
        self.selectedGardenName = None
        self.change_controller("menu")

    def change_controller(self, controller_name):

        if controller_name == "menu":
            self.menuController.take_control()
        elif controller_name == "garden creation":
            self.gardenCreationController.take_control()
        elif controller_name == "garden":
            self.gardenController.take_control()
        elif controller_name == "garden load":
            self.gardenLoadController.take_control()
        # elif controller_name == "all plants":
        #     self.allPlantsController.take_control()
        else:
            raise Exception("Unknown controller name returned")


    def close_app(self):
        self.mainFrame.Close()

    def set_loaded_garden_name(self, gardenName):
        self.selectedGardenName = gardenName

    def get_loaded_garden_name(self):
        return self.selectedGardenName
