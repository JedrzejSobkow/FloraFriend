import wx.lib.filebrowsebutton as filebrowse
import wx

class FlowerDialog(wx.Dialog):
    def __init__(self, *args, **kw):
        super(FlowerDialog, self).__init__(*args, **kw, title="Add Flower Parameters")

        self.InitUI()

    def InitUI(self):
        pnl = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox_name = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(pnl, label="Flower Name")
        hbox_name.Add(st1, flag=wx.RIGHT, border=8)
        self.flower_name = wx.TextCtrl(pnl)
        hbox_name.Add(self.flower_name, proportion=1)
        vbox.Add(hbox_name, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # Ścieżka do zdjęcia kwiata
        hbox_path = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(pnl, label="Flower Image")
        hbox_path.Add(st2, flag=wx.RIGHT, border=8)
        wildcard = "Image files (*.png;*.jpg;*.jpeg;*.bmp)|*.png;*.jpg;*.jpeg;*.bmp"
        self.flower_image = filebrowse.FileBrowseButton(pnl, fileMask=wildcard)
        hbox_path.Add(self.flower_image, proportion=1)
        vbox.Add(hbox_path, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # Częstotliwość podlewania
        hbox_frequency = wx.BoxSizer(wx.HORIZONTAL)
        st3 = wx.StaticText(pnl, label="Watering Frequency (days)")
        hbox_frequency.Add(st3, flag=wx.RIGHT, border=8)
        self.watering_frequency = wx.Slider(pnl, value=1, minValue=1, maxValue=30, style=wx.SL_HORIZONTAL | wx.SL_LABELS)
        hbox_frequency.Add(self.watering_frequency, proportion=1)
        vbox.Add(hbox_frequency, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # Przyciski OK i Cancel
        hbox_buttons = wx.BoxSizer(wx.HORIZONTAL)
        btn_ok = wx.Button(pnl, label='Ok')
        btn_cancel = wx.Button(pnl, label='Cancel')
        hbox_buttons.Add(btn_ok)
        hbox_buttons.Add(btn_cancel, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(hbox_buttons, flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=10)

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
