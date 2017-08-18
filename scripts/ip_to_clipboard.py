NAME = "Put IP on Clipboard"
DESCRIPTION = "Put local IP on the clipboard"
TAGS = ["IP", "Clipboard"]

import socket

def main():
    try:
        import win32clipboard
    except:
        window.dialogCritical("pywin32 needs to be installed to use this\n(pip install pypiwin32)")

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText(socket.gethostbyname(socket.gethostname()))
    win32clipboard.CloseClipboard()

    return True