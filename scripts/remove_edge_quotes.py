NAME = "Remove edge quotes"
DESCRIPTION = "Removed both double and single quotes from the beginning and the end of your current clipboard"
TAGS = ["Quotes", "Clipboard"]

def main(window):
    try:
        import win32clipboard
    except:
        window.dialogCritical("pywin32 needs to be installed to use this\n(pip install pypiwin32)")

    if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_TEXT):
        win32clipboard.OpenClipboard()
        clipboard = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()

        if clipboard.startswith("'") or clipboard.startswith('"'):
            clipboard = clipboard[1:]
        if clipboard.endswith("'") or clipboard.endswith('"'):
            clipboard = clipboard[:-1]

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(clipboard)
        win32clipboard.CloseClipboard()

    return True
