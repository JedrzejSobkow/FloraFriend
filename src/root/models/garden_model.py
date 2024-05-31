import json

from src.root.utils.constants import GARDENS_DATA_FILENAME

class GardenModel:
    def __init__(self, name, size, plants=None, decorations=None):
        if decorations is None:
            decorations = []
        if plants is None:
            plants = []
        self.name = name
        self.size = size
        self.plants = plants
        self.decorations = decorations

    def add_plant(self, name, type, watering_frequency):
        # Metoda dodająca roślinę do ogrodu
        pass

    def remove_plant(self, plant):
        # Metoda usuwająca roślinę z ogrodu
        pass

    def add_decoration(self, decoration):
        # Metoda dodająca dekorację do ogrodu
        pass

    def remove_decoration(self, decoration):
        # Metoda usuwająca dekorację z ogrodu
        pass

    def to_json_format(self):
        return {
            ""
            "name": self.name,
            "size": self.size,
            "plants": self.plants,
            "decorations": self.decorations
        }

    def __str__(self):
        return f'GARDEN OBJECT: [gardenName: {self.name}; gardenSize: {self.size}]'

    @staticmethod
    def validate_garden_name(gardenName):
        return 3 <= len(gardenName) <= 25

    @staticmethod
    def validate_garden_size(gardenSize):
        width, height = gardenSize
        return 100 > width >= 3 and 100 > height >= 3
