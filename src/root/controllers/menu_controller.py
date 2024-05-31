from src.root.controllers.controller_base import BaseController
from src.root.views.menu_view import MenuView

class MenuController(BaseController):

    def __init__(self, mainController):
        self.view = MenuView(mainController.mainFrame, self.on_create_garden, self.on_load_garden, self.on_close)
        self.view.Hide()
        self.mainController = mainController


    def take_control(self):
        self.view.Show()


    def on_create_garden(self, event):
        self.view.Hide()
        self.mainController.change_controller("garden create intro")

    def on_load_garden(self, event):
        self.view.Hide()
        self.mainController.change_controller("garden load")

    def on_close(self, event):
        self.view.Hide()
        self.mainController.close_app()
