from src.root.controllers.menu_controller import MenuController
from src.root.controllers.garden_create_intro_controller import GardenCreateIntroController
from src.root.controllers.garden_create_controller import GardenCreateController
from src.root.controllers.garden_controller import GardenController
from src.root.controllers.garden_load_controller import GardenLoadController
from src.root.controllers.all_plants_controller import AllPlantsController
from src.root.utils.json_database_controller import read_json
from src.root.utils.constants import GARDENS_DATA_FILENAME


class MainController:

    def __init__(self, mainFrame):

        self.mainFrame = mainFrame

        self.menuController = MenuController(self)
        self.gardenCreateIntroController = GardenCreateIntroController(self)
        self.gardenCreateController = GardenCreateController(self)
        self.gardenController = GardenController(self)
        self.gardenLoadController = GardenLoadController(self)
        # self.allPlantsController = AllPlantsController(self)
        self.selectedGarden = None
        self.change_controller("menu")
        self.all_gardens = read_json(GARDENS_DATA_FILENAME, "GardenModel")

    def change_controller(self, controller_name):

        if controller_name == "menu":
            self.menuController.take_control()
        elif controller_name == "garden create intro":
            self.gardenCreateIntroController.take_control()
        elif controller_name == "garden create":
            self.gardenCreateController.take_control()
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

    def load_garden(self, gardenName):
        self.selectedGardenName = gardenName
        for garden in self.all_gardens:
            if garden.name == gardenName:
                self.selectedGarden = garden
        #TODO


    def get_loaded_garden_name(self):
        return self.selectedGarden.name

    def get_loaded_garden_size(self):
        return self.selectedGarden.size

    def add_garden(self, garden):
        self.all_gardens.append(garden)
