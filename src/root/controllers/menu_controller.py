from src.root.controllers.controller_base import BaseController
from src.root.views.menu_view import MenuView

class MenuController(BaseController):
    """
    Controller class responsible for managing the menu view and its interactions.

    Attributes:
        view (MenuView): The menu view instance.
        main_controller: The main controller instance.
    """

    def __init__(self, mainController):
        """
        Initializes the MenuController.

        Args:
            mainController: The main controller instance.
        """
        self.view = MenuView(mainController.mainFrame, self.on_create_garden, self.on_load_garden, self.on_close)
        self.view.Hide()
        self.mainController = mainController

    def take_control(self):
        """Takes control of the menu view."""
        self.view.Show()

    def on_create_garden(self, event):
        """
        Handles the event when the "Create Garden" button is clicked.

        Args:
            event: The event object.
        """
        self.view.Hide()
        self.mainController.change_controller("garden create intro")

    def on_load_garden(self, event):
        """
        Handles the event when the "Load Garden" button is clicked.

        Args:
            event: The event object.
        """
        self.view.Hide()
        self.mainController.change_controller("garden load")

    def on_close(self, event):
        """
        Handles the event when the "Close" button is clicked.

        Args:
            event: The event object.
        """
        self.view.Hide()
        self.mainController.close_app()
