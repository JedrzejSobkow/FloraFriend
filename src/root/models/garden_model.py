import json
import numpy as np

from src.root.models.model_base import ModelBase
from src.root.utils.constants import GARDENS_DATA_FILENAME, MIN_AND_MAX_GARDEN_NAME_LENGTH, MIN_BOARD_SIZE, MAX_BOARD_SIZE
from src.root.models.flower_model import FlowerModel
from src.root.models.decoration_model import DecorationModel

class GardenModel(ModelBase):

    def __init__(self, name, size, boardIds=None):
        """
        Initializes a GardenModel instance.

        Args:
            name (str): The name of the garden.
            size (tuple): The size of the garden board (width, height).
            boardIds (list, optional): List of IDs representing objects on the board. Defaults to None.
        """
        self.name = name
        self.size = size
        self.board = np.empty(size, dtype=object)
        self.boardIds = boardIds

    def add_plant(self, position, name, color, wateringFrequency):
        """
        Adds a plant to the garden.

        Args:
            position (tuple): The position (row, column) where the plant will be added.
            name (str): The name of the plant.
            color (str): The color of the plant.
            wateringFrequency (int): The watering frequency of the plant in days.
        """
        flower = FlowerModel(name, color, wateringFrequency)
        self.board[position] = flower


    def add_decoration(self, position, name, color):
        """
        Adds a decoration to the garden.

        Args:
            position (tuple): The position (row, column) where the decoration will be added.
            name (str): The name of the decoration.
            color (str): The color of the decoration.
        """
        decoration = DecorationModel(name, color)
        self.board[position] = decoration


    def to_json_format(self):
        """
        Converts the garden object to JSON format.

        Returns:
            dict: Dictionary representing the garden object in JSON format.
        """
        boardIds = [[obj.id if obj else None for obj in row] for row in self.board]
        return {
            "name": self.name,
            "size": self.size,
            "boardIds": boardIds
        }

    def __str__(self):
        """
        Returns a string representation of the garden object.

        Returns:
            str: String representation of the garden object.
        """
        return f'GARDEN OBJECT: [gardenName: {self.name}; gardenSize: {self.size}]'

    @staticmethod
    def validate_garden_name(gardenName):
        """
        Validates the length of the garden name.

        Args:
            gardenName (str): The name of the garden to validate.

        Returns:
            bool: True if the garden name length is within the acceptable range, False otherwise.
        """
        return MIN_AND_MAX_GARDEN_NAME_LENGTH[0] <= len(gardenName) <= MIN_AND_MAX_GARDEN_NAME_LENGTH[1]

    @staticmethod
    def validate_garden_width(gardenWidth):
        """
        Validates the width of the garden board.

        Args:
            gardenWidth (int): The width of the garden board to validate.

        Returns:
            bool: True if the width is within the acceptable range, False otherwise.
        """
        return MIN_BOARD_SIZE[0] <= gardenWidth <= MAX_BOARD_SIZE[0]

    @staticmethod
    def validate_garden_height(gardenWidth):
        """
        Validates the height of the garden board.

        Args:
            gardenWidth (int): The height of the garden board to validate.

        Returns:
            bool: True if the height is within the acceptable range, False otherwise.
        """
        return MIN_BOARD_SIZE[1] <= gardenWidth <= MAX_BOARD_SIZE[1]
