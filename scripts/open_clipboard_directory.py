NAME = "Open Clipboard Directory"
DESCRIPTION = "Opens the directory on the clipboard in windows explorer"
TAGS = ["directory", "clipboard", "explorer", "open"]

import os

def main(window):
    try:
        import win32clipboard
    except:
        window.dialogCritical("Cannot import win32clipboard", "pywin32 needs to be installed to use this\n(pip install pypiwin32)")
        return False

    if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_TEXT):
        win32clipboard.OpenClipboard()
        clipboard = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()

        if os.path.exists(clipboard):
            os.system('%windir%\explorer.exe "' + clipboard + '"')
            return True

    return False
