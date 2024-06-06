import wx

class DecorationDialog(wx.Dialog):
    """
    Dialog window for adding decoration parameters.
    """

    def __init__(self, *args, **kw):
        """
        Initializes the DecorationDialog.

        Args:
            *args: Variable length argument list.
            **kw: Arbitrary keyword arguments.
        """
        super(DecorationDialog, self).__init__(*args, **kw, title="Add Decoration Parameters")

        self.InitUI()

    def InitUI(self):
        """
        Initializes the user interface of the dialog window.
        """
        pnl = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hboxName = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(pnl, label="Decoration Name")
        hboxName.Add(st1, flag=wx.RIGHT, border=8)
        self.decorationName = wx.TextCtrl(pnl)
        hboxName.Add(self.decorationName, proportion=1)
        vbox.Add(hboxName, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # Decoration Color
        hboxColor = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(pnl, label="Decoration Color")
        hboxColor.Add(st2, flag=wx.RIGHT, border=8)
        self.decorationColor = wx.ColourPickerCtrl(pnl)
        hboxColor.Add(self.decorationColor, proportion=1)
        vbox.Add(hboxColor, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        # OK and Cancel Buttons
        hboxButtons = wx.BoxSizer(wx.HORIZONTAL)
        btnOk = wx.Button(pnl, label='Ok')
        btnCancel = wx.Button(pnl, label='Cancel')
        hboxButtons.Add(btnOk)
        hboxButtons.Add(btnCancel, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(hboxButtons, flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=10)

        pnl.SetSizer(vbox)

        btnOk.Bind(wx.EVT_BUTTON, self.OnOk)
        btnCancel.Bind(wx.EVT_BUTTON, self.OnCancel)

    def OnOk(self, event):
        """
        Event handler for the OK button click event.

        Args:
            event: The event object.
        """
        decoration_name = self.decorationName.GetValue()
        decoration_color = self.decorationColor.GetColour().Get()
        self.EndModal(wx.ID_OK)

    def OnCancel(self, event):
        """
        Event handler for the Cancel button click event.

        Args:
            event: The event object.
        """
        self.EndModal(wx.ID_CANCEL)

    def get_decoration_name(self):
        """
        Returns the name of the decoration entered by the user.

        Returns:
            str: The name of the decoration.
        """
        return self.decorationName.GetValue()

    def get_decoration_color(self):
        """
        Returns the color of the decoration selected by the user.

        Returns:
            tuple: RGB values representing the color of the decoration.
        """
        return self.decorationColor.GetColour().Get()
