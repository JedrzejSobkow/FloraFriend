from src.root.controllers.controller_base import BaseController
from src.root.views.garden_load_view import GardenLoadView

class GardenLoadController(BaseController):
    """
    Controller class for managing the loading of gardens.

    Attributes:
        view (GardenLoadView): The associated view for garden loading.
        main_controller: The main controller instance.
    """

    def __init__(self, main_controller):
        """
        Initializes the GardenLoadController.

        Args:
            main_controller: The main controller instance.
        """
        self.view = GardenLoadView(main_controller.mainFrame, self.on_load, self.on_back)
        self.view.Hide()
        self.main_controller = main_controller

    def take_control(self):
        """
        Takes control of the garden loading view.
        """
        self.view.Show()
        self.remove_garden_buttons()
        self.view.add_buttons_for_gardens([garden.name for garden in self.main_controller.allGardens])

    def on_load(self, garden_name, event):
        """
        Handles the event of loading a garden.

        Args:
            garden_name (str): The name of the garden.
            event: The event object.
        """
        self.view.Hide()
        self.view.remove_all_buttons_for_garden()
        self.main_controller.load_garden(garden_name)
        self.main_controller.change_controller("garden")
        self.remove_garden_buttons()

    def on_back(self, event):
        """
        Handles the back button click event.

        Args:
            event: The event object.
        """
        self.view.Hide()
        self.view.remove_all_buttons_for_garden()
        self.main_controller.change_controller("menu")

    def remove_garden_buttons(self):
        """
        Removes all garden buttons from the view.
        """
        self.view.remove_all_buttons_for_garden()
