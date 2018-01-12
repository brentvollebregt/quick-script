NAME = "Type Clipboard"
DESCRIPTION = "Type clipboard at a slow pace"
TAGS = ["clipboard", "type"]

import time
initial_delay = 3
delay = 0.09

def main(window):
    try:
        from pynput.keyboard import Controller
    except:
        window.dialogCritical("Cannot import pynput.keyboard", "pynput needs to be installed to use this\n(pip install pynput)")
        return False
    try:
        import win32clipboard
    except:
        window.dialogCritical("Cannot import win32clipboard", "pywin32 needs to be installed to use this\n(pip install pypiwin32)")
        return False
    if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_TEXT):
        win32clipboard.OpenClipboard()
        clipboard = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()

        keyboard = Controller()
        time.sleep(initial_delay) # GUI is now focused, need to put cursor before text is typed
        for character in clipboard:
            keyboard.type(character)
            time.sleep(delay)

    return True
