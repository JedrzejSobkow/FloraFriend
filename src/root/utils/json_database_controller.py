import json
from src.root.models.garden_model import GardenModel

def append_to_json(filePath, obj):
    with open(filePath, "r") as file:
        data = json.load(file)

    data.append(obj.to_json_format())

    with open(filePath, "w") as file:
        json.dump(data, file, indent=4)


def read_json(filePath, objects_class):
    try:
        with open(filePath, "r") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        data = []

    objects_list = []

    if objects_class == "GardenModel":
        for obj_as_dict in data:
            objects_list.append(GardenModel(**obj_as_dict))

    return objects_list

def save_json(filePath, objects):

    with open(filePath, "w") as file:
        json.dump([obj.to_json_format() for obj in objects], file, indent=4)
