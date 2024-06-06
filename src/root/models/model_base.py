from abc import ABC, abstractmethod
class ModelBase(ABC):

    @abstractmethod
    def to_json_format(self):
        """
        Converts the garden object to JSON format.

        Returns:
            dict: Dictionary representing the garden object in JSON format.
        """
        pass
