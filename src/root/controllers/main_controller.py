import datetime

from src.root.controllers.menu_controller import MenuController
from src.root.controllers.garden_create_intro_controller import GardenCreateIntroController
from src.root.controllers.garden_controller import GardenController
from src.root.controllers.garden_load_controller import GardenLoadController
from src.root.models.decoration_model import DecorationModel
from src.root.models.flower_model import FlowerModel
from src.root.models.garden_model import GardenModel
from src.root.utils.json_database_controller import read_json
from src.root.utils.constants import GARDENS_DATA_FILENAME, FLOWERS_DATA_FILENAME, DECORATIONS_DATA_FILENAME
from plyer import notification


class MainController:
    """
    Main controller class responsible for managing the application flow.
    """

    def __init__(self, mainFrame):
        """
        Initializes the MainController.

        Args:
            mainFrame: The main frame of the application.
        """
        self.mainFrame = mainFrame
        self.menuController = MenuController(self)
        self.gardenCreateIntroController = GardenCreateIntroController(self)
        self.gardenController = GardenController(self)
        self.gardenLoadController = GardenLoadController(self)
        self.selectedGarden = None
        self.selectedGardenName = None
        self.change_controller("menu")
        self.allGardens = None
        self.allFlowers = None
        self.allDecorations = None
        self.prepare_gardens_flowers_and_decorations_data()
        witheringFlowers = self.get_flowers_to_water()
        self.show_notification_about_flowers_to_water(witheringFlowers)

    def change_controller(self, controllerName):
        """
        Changes the current controller to the specified one.

        Args:
            controller_name (str): The name of the controller to change to.
        """
        if controllerName == "menu":
            self.menuController.take_control()
        elif controllerName == "garden create intro":
            self.gardenCreateIntroController.take_control()
        elif controllerName == "garden":
            self.gardenController.take_control()
        elif controllerName == "garden load":
            self.gardenLoadController.take_control()
        else:
            raise Exception("Unknown controller name returned")
        self.mainFrame.Layout()

    def close_app(self):
        """
        Closes the application.
        """
        self.mainFrame.Close()

    def load_garden(self, gardenName):
        """
        Loads the specified garden.

        Args:
            gardenName (str): The name of the garden to load.
        """
        self.selectedGardenName = gardenName
        for garden in self.allGardens:
            if garden.name == gardenName:
                self.selectedGarden = garden

    def get_loaded_garden_name(self):
        """
        Gets the name of the loaded garden.

        Returns:
            str: The name of the loaded garden.
        """
        return self.selectedGarden.name

    def get_loaded_garden_size(self):
        """
        Gets the size of the loaded garden.

        Returns:
            tuple: The size of the loaded garden.
        """
        return self.selectedGarden.size

    def get_loaded_garden_board(self):
        """
        Gets the board of the loaded garden.

        Returns:
            numpy.ndarray: The board of the loaded garden.
        """
        return self.selectedGarden.board

    def add_garden(self, garden):
        """
        Adds a new garden.

        Args:
            garden (GardenModel): The garden to add.
        """
        self.allGardens.append(garden)

    def add_flower(self, flower):
        """
        Adds a new flower.

        Args:
            flower (FlowerModel): The flower to add.
        """
        self.allFlowers[flower.id] = flower

    def add_decoration(self, decoration):
        """
        Adds a new decoration.

        Args:
            decoration (DecorationModel): The decoration to add.
        """
        self.allDecorations[decoration.id] = decoration

    def create_gardens_boards(self):
        """
        Creates the boards for all gardens.
        """
        for garden in self.allGardens:
            gardenBoardIds = garden.boardIds
            for rowId, row in enumerate(gardenBoardIds):
                for colId, cell in enumerate(row):
                    if cell is not None:
                        if cell in self.allFlowers.keys():
                            garden.board[(rowId, colId)] = self.allFlowers[cell]
                        elif cell in self.allDecorations.keys():
                            garden.board[(rowId, colId)] = self.allDecorations[cell]

    def prepare_gardens_flowers_and_decorations_data(self):
        """
        Prepares the data for gardens, flowers, and decorations.
        """
        self.allGardens = read_json(GARDENS_DATA_FILENAME, GardenModel)
        self.allFlowers = read_json(FLOWERS_DATA_FILENAME, FlowerModel)
        self.allDecorations = read_json(DECORATIONS_DATA_FILENAME, DecorationModel)
        lastFlowerId = max(self.allFlowers.keys()) if len(self.allFlowers.keys()) > 0 else 0
        FlowerModel.idCounter = lastFlowerId
        lastDecorationId = max(self.allDecorations.keys()) if len(self.allDecorations.keys()) > 0 else 0
        DecorationModel.idCounter = lastDecorationId
        self.create_gardens_boards()

    def delete_selected_garden(self):
        """
        Deletes the selected garden.
        """
        for gardenId, garden in enumerate(self.allGardens):
            if garden.name == self.selectedGardenName:
                self.allGardens.pop(gardenId)
                break

    def get_flowers_to_water(self):
        """
        Gets the flowers that need watering.

        Returns:
            dict: A dictionary containing the gardens and their respective flowers to water.
        """
        flowersToWater = {}
        for garden in self.allGardens:
            flowersForFardenX = set()
            for row in garden.board:
                for obj in row:
                    if isinstance(obj, FlowerModel) and obj.nextWatering <= datetime.datetime.now():
                        flowersForFardenX.add(obj)
            flowersToWater[garden.name] = flowersForFardenX
        return flowersToWater

    def show_notification_about_flowers_to_water(self, toWater):
        """
        Shows a notification about flowers that need watering.

        Args:
            toWater (dict): A dictionary containing the gardens and their respective flowers to water.
        """
        for gardenName, flowers in toWater.items():
            for flower in flowers:
                notification.notify(
                    title='PLEASE WATER ME',
                    message=f"In garden {gardenName}, flower named {flower.name} is withering. Water it as soon as possible.",
                    app_name='FloraFriend',
                    timeout=5,  # Display time in seconds
                )
