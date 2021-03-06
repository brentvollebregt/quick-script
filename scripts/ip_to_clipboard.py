NAME = "Put IP on Clipboard"
DESCRIPTION = "Put local IP on the clipboard"
TAGS = ["IP", "Clipboard"]

import socket

def main(window):
    try:
        import win32clipboard
    except:
        window.dialogCritical("Cannot import win32clipboard", "pywin32 needs to be installed to use this\n(pip install pypiwin32)")
        return False

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(socket.gethostbyname(socket.gethostname()))
    win32clipboard.CloseClipboard()

    return True