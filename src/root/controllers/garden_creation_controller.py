from src.root.controllers.controller_base import BaseController
from src.root.views.garden_create_view import GardenCreateView


class GardenCreationController(BaseController):
    def __init__(self, mainController):
        self.view = GardenCreateView(mainController.mainFrame, self.on_save, self.on_discard, self.on_clear, self.on_back)
        self.view.Hide()
        self.mainController = mainController


    def take_control(self):
        self.view.Show()


    def on_save(self, event):
        self.view.Hide()
        print("SAVED")
        self.mainController.change_controller("menu")

    def on_discard(self, event):
        self.view.Hide()
        print("NOT SAVED")
        self.mainController.change_controller("menu")

    def on_clear(self, event):
        print("PANEL IS CLEAN")

    def on_back(self, event):
        if input("ARE YOU SURE YOU WANT TO LEAVE WITHOUT SAVING? Y/n").lower() == "y":
            self.on_discard(event)



# from src.root.controllers.controller_base import BaseController
# from src.root.views.menu_view import MenuView
#
# class MenuController(BaseController):
#
#     def __init__(self, mainController):
#         self.view = MenuView(mainController.mainFrame, self.on_create_garden, self.on_load_garden, self.on_close)
#         self.mainController = mainController
#
#
#     def take_control(self):
#         self.view.Show()
#
#
#     def on_create_garden(self, event):
#         self.view.Hide()
#         self.mainController.change_controller("garden creation")
#
#     def on_load_garden(self):
#         self.view.Hide()
#         self.mainController.change_controller("garden creation")
#
#     def on_close(self):
#         self.view.Hide()
#         self.mainController.change_controller("garden creation")
