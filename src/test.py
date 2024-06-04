import wx
import wx.lib.filebrowsebutton as filebrowse

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MyFrame, self).__init__(*args, **kwargs)

        self.Bind(wx.EVT_RIGHT_DOWN, self.show_right_click_menu)

    def show_right_click_menu(self, event):
        # Tworzenie menu kontekstowego
        menu = wx.Menu()
        mouse_pos = event.GetPosition()

        flover_opt = menu.Append(wx.ID_ANY, "ADD FLOWER")
        decoration_opt = menu.Append(wx.ID_ANY, "ADD DECORATION")
        remove_opt = menu.Append(wx.ID_ANY, "REMOVE")

        self.Bind(wx.EVT_MENU, lambda _: self.on_right_menu_click_controller("FLOWER"), flover_opt)
        self.Bind(wx.EVT_MENU, lambda _: self.on_right_menu_click_controller("DECORATION"), decoration_opt)
        self.Bind(wx.EVT_MENU, lambda _: self.on_right_menu_click_controller("REMOVE"), remove_opt)

        # Wyświetlanie menu kontekstowego w miejscu kliknięcia
        self.PopupMenu(menu, mouse_pos)
        menu.Destroy()

    def on_right_menu_click_controller(self, optionName):
        print(f"{optionName} CLICKED")
        if optionName == "FLOWER":
            self.show_flower_dialog()

    def show_flower_dialog(self):
        dialog = FlowerDialog(self)
        dialog.ShowModal()
        dialog.Destroy()

class FlowerDialog(wx.Dialog):
    def __init__(self, *args, **kw):
        super(FlowerDialog, self).__init__(*args, **kw, title="Add Flower Parameters")

        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        # Nazwa kwiata
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(pnl, label="Flower Name")
        hbox1.Add(st1, flag=wx.RIGHT, border=8)
        self.flower_name = wx.TextCtrl(pnl)
        hbox1.Add(self.flower_name, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # Ścieżka do zdjęcia kwiata
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(pnl, label="Flower Image")
        hbox2.Add(st2, flag=wx.RIGHT, border=8)
        wildcard = "Image files (*.png;*.jpg;*.jpeg;*.bmp)|*.png;*.jpg;*.jpeg;*.bmp"
        self.flower_image = filebrowse.FileBrowseButton(pnl, fileMask=wildcard)
        hbox2.Add(self.flower_image, proportion=1)
        vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # Częstotliwość podlewania
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        st3 = wx.StaticText(pnl, label="Watering Frequency (days)")
        hbox3.Add(st3, flag=wx.RIGHT, border=8)
        self.watering_frequency = wx.Slider(pnl, value=1, minValue=1, maxValue=30, style=wx.SL_HORIZONTAL | wx.SL_LABELS)
        hbox3.Add(self.watering_frequency, proportion=1)
        vbox.Add(hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # Przyciski OK i Cancel
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        btn_ok = wx.Button(pnl, label='Ok')
        btn_cancel = wx.Button(pnl, label='Cancel')
        hbox4.Add(btn_ok)
        hbox4.Add(btn_cancel, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(hbox4, flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=10)

        pnl.SetSizer(vbox)

        btn_ok.Bind(wx.EVT_BUTTON, self.OnOk)
        btn_cancel.Bind(wx.EVT_BUTTON, self.OnCancel)

    def OnOk(self, event):
        flower_name = self.flower_name.GetValue()
        flower_image = self.flower_image.GetValue()
        watering_frequency = self.watering_frequency.GetValue()
        print(f"Flower Name: {flower_name}, Flower Image: {flower_image}, Watering Frequency: {watering_frequency} days")
        self.EndModal(wx.ID_OK)

    def OnCancel(self, event):
        self.EndModal(wx.ID_CANCEL)

app = wx.App(False)
frame = MyFrame(None, title="Menu Example")
frame.Show()
app.MainLoop()
    
