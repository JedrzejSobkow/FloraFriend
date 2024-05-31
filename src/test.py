from wx import Frame, grid, App

class MyGrid(Frame):
    def __init__(self, parent, title):
        super(MyGrid, self).__init__(parent, title=title, size=(300, 200))

        self.grid = grid.Grid(self)
        self.grid.CreateGrid(3, 3)

        # Dodanie zdarzenia kliknięcia w komórkę siatki
        self.grid.Bind(grid.EVT_GRID_CELL_LEFT_CLICK, self.on_cell_click)

        self.Centre()
        self.Show()

    def on_cell_click(self, event):
        row = event.GetRow()
        col = event.GetCol()
        value = self.grid.GetCellValue(row, col)
        print(f"Clicked cell ({row}, {col}): {value}")

if __name__ == '__main__':
    app = App()
    frame = MyGrid(None, "Interactive Grid")
    app.MainLoop()
