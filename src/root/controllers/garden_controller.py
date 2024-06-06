from src.root.controllers.controller_base import BaseController
from src.root.views.garden_view import GardenView
from src.root.models.flower_model import FlowerModel
from src.root.models.decoration_model import DecorationModel
from src.root.utils.json_database_controller import save_json
from src.root.utils.constants import GARDENS_DATA_FILENAME
from src.root.utils.constants import FLOWERS_DATA_FILENAME
from src.root.utils.constants import DECORATIONS_DATA_FILENAME
from src.root.utils.constants import EMPTY_CELL_COLOR
import numpy as np

class GardenController(BaseController):
    """
    Controller class for managing garden interactions.

    Attributes:
        view (GardenView): The associated garden view.
        board (numpy.ndarray): Array representing the garden layout.
        selectedCellPos (tuple): Position of the currently selected cell.
        rememberedCellPos (tuple): Position of the remembered selected cell.
        mode (str): The current mode of operation.
        mainController: The main controller instance.
    """

    def __init__(self, mainController):
        """
        Initializes the GardenController.

        Args:
            mainController: The main controller instance.
        """
        self.view = GardenView(mainController.mainFrame, self.on_cell_left_click, self.on_menu_click, self.on_back,
                               self.on_save, self.add_flower, self.add_decoration, self.on_mode_click, self.on_delete_garden)
        self.board = np.zeros((0, 0))
        self.selectedCellPos = None
        self.rememberedCellPos = None
        self.mode = None
        self.view.Hide()
        self.mainController = mainController

    def take_control(self):
        """
        Takes control of the garden view.
        """
        self.board = self.mainController.get_loaded_garden_board()
        self.view.Show()
        self.view.load_correct_garden(self.mainController.get_loaded_garden_name(),
                                      self.mainController.get_loaded_garden_size())
        for row_id, row in enumerate(self.board):
            for col_id, cell in enumerate(row):
                if cell is not None:
                    content = "D"
                    if isinstance(cell, FlowerModel):
                        content = "F"
                    self.view.change_cell_color_and_content((row_id, col_id), cell.color, content)

    def on_back(self, event):
        """
        Handles back button click event.

        Args:
            event: The event object.
        """
        self.view.Hide()
        self.mainController.change_controller("garden load")
        self.mainController.prepare_gardens_flowers_and_decorations_data()

    def on_save(self, event):
        """
        Handles save button click event.

        Args:
            event: The event object.
        """
        self.view.Hide()
        self.save_data()
        self.mainController.change_controller("menu")

    def on_cell_left_click(self, event):
        """
        Handles cell left click event.

        Args:
            event: The event object.
        """
        self.selectedCellPos = (event.GetRow(), event.GetCol())
        if self.mode == "DUPLICATE":
            cell_source = self.board[(self.rememberedCellPos)]
            self.board[self.selectedCellPos] = cell_source
            self.view.change_cell_color_and_content(self.selectedCellPos, cell_source.color, 'F' if isinstance(cell_source, FlowerModel) else "D")
        elif self.mode == "DELETE":
            self.board[self.selectedCellPos] = None
            self.view.change_cell_color_and_content(self.selectedCellPos, EMPTY_CELL_COLOR, "")
        elif self.mode == "WATER":
            self.try_to_water_an_object(self.selectedCellPos)

    def try_to_water_an_object(self, objPos):
        """
        Tries to water an object in the garden.

        Args:
            objPos (tuple): Position of the object.
        """
        selectedCell = self.board[objPos]
        if selectedCell is not None and isinstance(selectedCell, FlowerModel):
            selectedCell.water_the_plant()

    def on_menu_click(self, optionName, pos):
        """
        Handles menu item click event.

        Args:
            optionName (str): The name of the selected option.
            pos (tuple): Position of the clicked cell.
        """
        if optionName == "FLOWER":
            self.view.show_flower_dialog(pos)
        elif optionName == "DECORATION":
            self.view.show_decoration_dialog(pos)

    def add_flower(self, pos, flowerName, flowerColor, wateringFreq):
        """
        Adds a new flower to the garden.

        Args:
            pos (tuple): Position to add the flower.
            flowerName (str): Name of the flower.
            flowerColor (str): Color of the flower.
            wateringFreq (int): Frequency of watering.
        """
        flower = FlowerModel(flowerName, flowerColor, wateringFreq)
        self.board[pos] = flower
        self.mainController.add_flower(flower)
        self.view.change_cell_color_and_content(pos, flowerColor, "F")

    def add_decoration(self, pos, decorationName, decorationColor):
        """
        Adds a new decoration to the garden.

        Args:
            pos (tuple): Position to add the decoration.
            decorationName (str): Name of the decoration.
            decorationColor (str): Color of the decoration.
        """
        decoration = DecorationModel(decorationName, decorationColor)
        self.board[pos] = decoration
        self.mainController.add_decoration(decoration)
        self.view.change_cell_color_and_content(pos, decorationColor, "D")

    def on_mode_click(self, modeName):
        """
        Handles mode click event.

        Args:
            modeName (str): The name of the selected mode.
        """

        if self.mode == modeName:
            self.rememberedCellPos = None
            self.mode = None
        elif modeName == "DUPLICATE" and self.selectedCellPos is not None and self.board[self.selectedCellPos] is not None or modeName == "DELETE":
            self.rememberedCellPos = self.selectedCellPos
            self.mode = modeName
        elif modeName == "DUPLICATE":
            self.mode = None
        elif modeName == "INFO":
            self.mode = None
            if self.selectedCellPos is not None and self.board[self.selectedCellPos] is not None:
                obj = self.board[self.selectedCellPos]
                self.selectedCellPos = None
                if isinstance(obj, FlowerModel):
                    self.view.show_info(obj.name, obj.color, obj.wateringFrequency, obj.nextWatering)
                else:
                    self.view.show_info(obj.name, obj.color)
        elif modeName == "WATER":
            self.mode = modeName
            if self.selectedCellPos is not None:
                self.try_to_water_an_object(self.selectedCellPos)

    def on_delete_garden(self):
        """
        Handles delete garden event.
        """
        self.mainController.delete_selected_garden()
        self.save_data()
        self.mainController.prepare_gardens_flowers_and_decorations_data()
        self.view.Hide()
        self.mainController.change_controller("menu")

    def save_data(self):
        """
        Saves garden data to JSON files.
        """
        save_json(GARDENS_DATA_FILENAME, self.mainController.allGardens)
        save_json(FLOWERS_DATA_FILENAME, self.mainController.allFlowers.values())
        save_json(DECORATIONS_DATA_FILENAME, self.mainController.allDecorations.values())
