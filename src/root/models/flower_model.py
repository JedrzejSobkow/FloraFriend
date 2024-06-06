import datetime
import json

from src.root.models.model_base import ModelBase


class FlowerModel(ModelBase):
    idCounter = 0

    def __init__(self, name, color, wateringFrequency, id=None, nextWatering=None):
        """
        Initializes a FlowerModel instance.

        Args:
            name (str): The name of the flower.
            color (str): The color of the flower.
            wateringFrequency (int): The frequency of watering in days.
            id (int, optional): The ID of the flower. If not provided, it will be generated automatically.
            nextWatering (str or datetime.datetime, optional): The next watering time of the flower. If not provided,
                it will be set automatically.
        """
        if id is None:
            id = self.get_last_saved_flower_id() + 1
            FlowerModel.idCounter += 1
        self.id = id
        self.name = name
        self.color = color
        self.wateringFrequency = wateringFrequency
        if not nextWatering:
            self.set_automatically_next_watering()
        else:
            if isinstance(nextWatering, str):
                self.nextWatering = datetime.datetime.strptime(nextWatering, "%Y-%m-%d %H:%M:%S.%f")
            elif isinstance(nextWatering, datetime.datetime):
                self.nextWatering = nextWatering
            else:
                raise ValueError("Invalid format for nextWatering.")

    @classmethod
    def get_last_saved_flower_id(cls):
        """
        Gets the last saved flower ID.

        Returns:
            int: The last saved flower ID.
        """
        if cls.idCounter > 0:
            return cls.idCounter
        return 0

    def water_the_plant(self):
        """Waters the flower and updates the next watering time."""
        self.set_automatically_next_watering()

    def __str__(self):
        """
        Returns a string representation of the flower.

        Returns:
            str: String representation of the flower.
        """
        return f"Flower ID: {self.id}, Name: {self.name}, Color: {self.color}, Watering Frequency: {self.wateringFrequency} days, Next Watering: {self.nextWatering}"

    def to_json_format(self):
        """
        Converts the flower object to JSON format.

        Returns:
            dict: Dictionary representing the flower object in JSON format.
        """
        return {
            "id": self.id,
            "name": self.name,
            "color": self.color,
            "wateringFrequency": self.wateringFrequency,
            "nextWatering": self.nextWatering.strftime('%Y-%m-%d %H:%M:%S.%f')
        }

    def set_automatically_next_watering(self):
        """Sets the next watering time of the flower automatically."""
        self.nextWatering = datetime.datetime.now() + datetime.timedelta(days=self.wateringFrequency)
