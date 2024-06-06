import json
import numpy as np

from src.root.models.decoration_model import DecorationModel
from src.root.models.flower_model import FlowerModel
from src.root.models.garden_model import GardenModel


def read_json(filePath, objects_class):
    """
    Reads JSON data from a file and converts it into corresponding objects.

    Args:
        filePath (str): The path to the JSON file.
        objects_class (class): The class of the objects to be created.

    Returns:
        list or dict: A list of objects or a dictionary of objects, depending on the class.
    """
    try:
        with open(filePath, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

        with open(filePath, "w") as file:
            json.dump(data, file)
    except json.JSONDecodeError:
        data = []

    if objects_class == GardenModel:
        for gardenAsDict in data:
            gardenAsDict['boardIds'] = np.array(gardenAsDict['boardIds'])
        return [GardenModel(**gardenAsDict) for gardenAsDict in data]
    elif objects_class == FlowerModel:
        flowersDict = {}
        for flowerAsDict in data:
            flowersDict[flowerAsDict['id']] = FlowerModel(**flowerAsDict)
        return flowersDict
    elif objects_class == DecorationModel:
        decorationsDict = {}
        for decorationAsDict in data:
            decorationsDict[decorationAsDict['id']] = DecorationModel(**decorationAsDict)
        return decorationsDict


def save_json(filePath, objects):
    """
    Saves objects into a JSON file.

    Args:
        filePath (str): The path to the JSON file.
        objects: The objects to be saved.
    """
    with open(filePath, "w") as file:
        json.dump([obj.to_json_format() for obj in objects], file, indent=4)
