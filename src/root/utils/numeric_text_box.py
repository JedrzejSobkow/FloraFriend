from wx import TextCtrl, ID_ANY, DefaultPosition, DefaultSize, DefaultValidator, TextCtrlNameStr, WXK_SPACE, WXK_DELETE, EVT_CHAR, EVT_TEXT_PASTE

class NumericTextBox(TextCtrl):
    def __init__(self, parent, allowPasting=False, id=ID_ANY, value="",
                 pos=DefaultPosition, size=DefaultSize,
                 style=0, validator=DefaultValidator,
                 name=TextCtrlNameStr):
        super(NumericTextBox, self).__init__(parent, id, value,
                                              pos, size, style,
                                              validator, name)
        self.Bind(EVT_CHAR, self.OnChar)
        if not allowPasting:
            self.Bind(EVT_TEXT_PASTE, lambda event: None)

    def OnChar(self, event):
        # print(len(self.GetValue()))
        key_code = event.GetKeyCode()
        # Allow control keys, backspace, delete, etc.
        if key_code < WXK_SPACE or key_code == WXK_DELETE or key_code > 255:
            event.Skip()
            return
        # Allow digits
        if chr(key_code).isdigit():
            event.Skip()
            return
        # Block everything else
        return
