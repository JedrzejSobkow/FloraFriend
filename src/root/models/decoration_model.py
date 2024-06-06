from src.root.models.model_base import ModelBase


class DecorationModel(ModelBase):
    idCounter = 0

    def __init__(self, name, color, id=None):
        """
        Initializes a DecorationModel instance.

        Args:
            name (str): The name of the decoration.
            color (str): The color of the decoration.
            id (int, optional): The ID of the decoration. If not provided, it will be generated automatically.
        """
        if id is None:
            id = self.get_last_saved_decoration_id() - 1
            DecorationModel.idCounter -= 1
        self.id = id
        self.name = name
        self.color = color

    @classmethod
    def get_last_saved_decoration_id(cls):
        """
        Gets the last saved decoration ID.

        Returns:
            int: The last saved decoration ID.
        """
        if cls.idCounter > 0:
            return cls.idCounter
        return 0

    def __str__(self):
        """
        Returns a string representation of the decoration.

        Returns:
            str: String representation of the decoration.
        """
        return f"Decoration ID: {self.id}, Name: {self.name}, Color: {self.color}"

    def to_json_format(self):
        """
        Converts the decoration object to JSON format.

        Returns:
            dict: Dictionary representing the decoration object in JSON format.
        """
        return {
            "id": self.id,
            "name": self.name,
            "color": self.color,
        }
