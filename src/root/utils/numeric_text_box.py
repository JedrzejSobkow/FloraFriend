from wx import TextCtrl, ID_ANY, DefaultPosition, DefaultSize, DefaultValidator, TextCtrlNameStr, WXK_SPACE, WXK_DELETE, EVT_CHAR, EVT_TEXT_PASTE

class NumericTextBox(TextCtrl):
    """
    A custom text box control that only allows numeric input.

    Attributes:
        parent: The parent window.
        allowPasting (bool): Whether pasting text is allowed or not.
        id: The window identifier.
        value (str): The initial text value.
        pos: The initial position.
        size: The initial size.
        style: The window style.
        validator: The window validator.
        name: The window name.
    """
    def __init__(self, parent, allowPasting=False, id=ID_ANY, value="",
                 pos=DefaultPosition, size=DefaultSize,
                 style=0, validator=DefaultValidator,
                 name=TextCtrlNameStr):
        """
        Initializes the NumericTextBox.

        Args:
            parent: The parent window.
            allowPasting (bool): Whether pasting text is allowed or not.
            id: The window identifier.
            value (str): The initial text value.
            pos: The initial position.
            size: The initial size.
            style: The window style.
            validator: The window validator.
            name: The window name.
        """
        super(NumericTextBox, self).__init__(parent, id, value,
                                              pos, size, style,
                                              validator, name)
        self.Bind(EVT_CHAR, self.OnChar)
        if not allowPasting:
            self.Bind(EVT_TEXT_PASTE, lambda event: None)

    def OnChar(self, event):
        """
        Event handler for character input.

        Args:
            event: The event object.
        """
        # Allow control keys, backspace, delete, etc.
        if event.GetUnicodeKey() < WXK_SPACE or event.GetUnicodeKey() == WXK_DELETE:
            event.Skip()
            return
        # Allow digits
        if chr(event.GetUnicodeKey()).isdigit():
            event.Skip()
            return
        # Block everything else
        return
