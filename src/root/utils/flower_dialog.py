import wx

class FlowerDialog(wx.Dialog):
    """
    Dialog window for adding flower parameters.
    """

    def __init__(self, *args, **kw):
        """
        Initializes the FlowerDialog.

        Args:
            *args: Variable length argument list.
            **kw: Arbitrary keyword arguments.
        """
        super(FlowerDialog, self).__init__(*args, **kw, title="Add Flower Parameters")

        self.InitUI()

    def InitUI(self):
        """
        Initializes the user interface of the dialog window.
        """
        pnl = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hboxName = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(pnl, label="Flower Name")
        hboxName.Add(st1, flag=wx.RIGHT, border=8)
        self.flowerName = wx.TextCtrl(pnl)
        hboxName.Add(self.flowerName, proportion=1)
        vbox.Add(hboxName, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # Flower Color
        hboxColor = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(pnl, label="Flower Color")
        hboxColor.Add(st2, flag=wx.RIGHT, border=8)
        self.flower_color = wx.ColourPickerCtrl(pnl)
        hboxColor.Add(self.flower_color, proportion=1)
        vbox.Add(hboxColor, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # Watering Frequency
        hboxFrequency = wx.BoxSizer(wx.HORIZONTAL)
        st3 = wx.StaticText(pnl, label="Watering Frequency (days)")
        hboxFrequency.Add(st3, flag=wx.RIGHT, border=8)
        self.wateringFrequency = wx.Slider(pnl, value=1, minValue=1, maxValue=30, style=wx.SL_HORIZONTAL | wx.SL_LABELS)
        hboxFrequency.Add(self.wateringFrequency, proportion=1)
        vbox.Add(hboxFrequency, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # OK and Cancel Buttons
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
        """
        Event handler for the OK button click event.

        Args:
            event: The event object.
        """
        flowerName = self.flowerName.GetValue()
        flower_color = self.flower_color.GetColour().Get()
        wateringFrequency = self.wateringFrequency.GetValue()
        self.EndModal(wx.ID_OK)

    def OnCancel(self, event):
        """
        Event handler for the Cancel button click event.

        Args:
            event: The event object.
        """
        self.EndModal(wx.ID_CANCEL)

    def get_flower_name(self):
        """
        Returns the name of the flower entered by the user.

        Returns:
            str: The name of the flower.
        """
        return self.flowerName.GetValue()

    def get_flower_color(self):
        """
        Returns the color of the flower selected by the user.

        Returns:
            tuple: RGB values representing the color of the flower.
        """
        return self.flower_color.GetColour().Get()

    def get_watering_freq(self):
        """
        Returns the watering frequency selected by the user.

        Returns:
            int: The watering frequency in days.
        """
        return self.wateringFrequency.GetValue()
