from abc import ABC, abstractmethod
class BaseController(ABC):
    @abstractmethod
    def take_control(self):
        """Take control and handle the application flow."""
        return
