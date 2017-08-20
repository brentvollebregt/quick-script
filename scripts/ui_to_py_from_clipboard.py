NAME = "Convert .ui on Clipboard to .py"
DESCRIPTION = "Converts the .ui file on your cliboard to .py. Will store the .py file in the same location the .ui file is located."
TAGS = ["ui", "clipboard", "py", "convert", "pyuic5", "pyqt5"]

import os

def main(window):
    try:
        import win32clipboard
    except:
        window.dialogCritical("pywin32 needs to be installed to use this\n(pip install pypiwin32)")

    pyuic_path = "C:/Python35/Lib/site-packages/PyQt5/pyuic5.bat"

    win32clipboard.OpenClipboard()
    if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_HDROP):
        current_clipboard = list(win32clipboard.GetClipboardData(win32clipboard.CF_HDROP))
        if len(current_clipboard) == 1:
            if os.path.basename(current_clipboard[0]).endswith(".ui"):
                file_name = os.path.basename(current_clipboard[0])
                folder = os.path.dirname(current_clipboard[0])
                os.system(pyuic_path + " " + current_clipboard[0] + " -x -o " + current_clipboard[0][:-2] + 'py')

    win32clipboard.CloseClipboard()

    return True