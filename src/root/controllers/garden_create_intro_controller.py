from src.root.controllers.controller_base import BaseController
from src.root.views.garden_create_intro_view import GardenCreateIntroView
from src.root.models.garden_model import GardenModel

class GardenCreateIntroController(BaseController):
    """
    Controller class for managing the creation of a new garden.

    Attributes:
        view (GardenCreateIntroView): The associated view for garden creation introduction.
        main_controller: The main controller instance.
    """

    def __init__(self, main_controller):
        """
        Initializes the GardenCreateIntroController.

        Args:
            main_controller: The main controller instance.
        """
        self.view = GardenCreateIntroView(main_controller.mainFrame, self.on_next, self.on_back)
        self.view.Hide()
        self.main_controller = main_controller


    def take_control(self):
        """
        Takes control of the garden creation introduction view.
        """
        self.view.Show()


    def on_next(self, garden_name, garden_size, event):
        """
        Handles the next button click event for garden creation.

        Args:
            garden_name (str): The name of the garden.
            garden_size (tuple): The size of the garden.
            event: The event object.
        """
        self.view.unhighlight_every_field()
        validation_ok = self.validate_garden_name(garden_name) * self.validate_garden_width(garden_size[0]) * self.validate_garden_height(garden_size[1])
        if validation_ok:
            garden = GardenModel(garden_name, garden_size)
            self.main_controller.add_garden(garden)
            self.view.Hide()
            self.view.clear_inputs()
            self.main_controller.load_garden(garden_name)
            self.main_controller.change_controller("garden")

        else:
            self.view.Refresh()

    def on_back(self, event):
        """
        Handles the back button click event.

        Args:
            event: The event object.
        """
        self.view.Hide()
        self.view.clear_inputs()
        self.main_controller.change_controller("menu")

    def validate_garden_name(self, garden_name):
        """
        Validates the garden name.

        Args:
            garden_name (str): The name of the garden.

        Returns:
            bool: True if the garden name is valid, False otherwise.
        """
        result = GardenModel.validate_garden_name(garden_name)
        if not result:
            self.view.highlight_incorrect_name()
        return result

    def validate_garden_width(self, garden_width):
        """
        Validates the garden width.

        Args:
            garden_width (int): The width of the garden.

        Returns:
            bool: True if the garden width is valid, False otherwise.
        """
        result = GardenModel.validate_garden_width(garden_width)
        if not result:
            self.view.highlight_incorrect_width()
        return result

    def validate_garden_height(self, garden_height):
        """
        Validates the garden height.

        Args:
            garden_height (int): The height of the garden.

        Returns:
            bool: True if the garden height is valid, False otherwise.
        """
        result = GardenModel.validate_garden_height(garden_height)
        if not result:
            self.view.highlight_incorrect_height()
        return result
