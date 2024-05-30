import wx

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Panel Switcher", size=(400, 300))

        self.panel1 = Panel1(self)
        self.panel2 = Panel2(self)

        self.panel2.Hide()  # Ukryj panel2 na początku
        self.current_panel = self.panel1

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panel1, 1, wx.EXPAND)
        self.sizer.Add(self.panel2, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

        self.Centre()
        self.Show()

    def switch_panels(self):
        if self.current_panel == self.panel1:
            self.panel1.Hide()
            self.panel2.Show()
            self.current_panel = self.panel2
        else:
            self.panel2.Hide()
            self.panel1.Show()
            self.current_panel = self.panel1
        self.Layout()

class Panel1(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(self, label="This is Panel 1")
        button = wx.Button(self, label="Switch to Panel 2")
        button.Bind(wx.EVT_BUTTON, self.on_switch)

        sizer.Add(label, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(button, 0, wx.ALL | wx.CENTER, 5)
        self.SetSizer(sizer)

    def on_switch(self, event):
        self.GetParent().switch_panels()

class Panel2(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(self, label="This is Panel 2")
        button = wx.Button(self, label="Switch to Panel 1")
        button.Bind(wx.EVT_BUTTON, self.on_switch)

        sizer.Add(label, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(button, 0, wx.ALL | wx.CENTER, 5)
        self.SetSizer(sizer)

    def on_switch(self, event):
        self.GetParent().switch_panels()

if __name__ == "__main__":
    app = wx.App()
    frame = MainFrame()
    app.MainLoop()
