NAME = "Save Clipboard to File"
DESCRIPTION = "Will request the user where to store the current text or image contents of the clipboard"
TAGS = ["Clipboard", "Save", "Image"]

def main(window):
    try:
        import win32clipboard
    except:
        window.dialogCritical("pywin32 needs to be installed to use this\n(pip install pypiwin32)")
    try:
        from PIL import ImageGrab
    except:
        window.dialogCritical("PIL needs to be installed to use this\n(pip install Pillow)")
    from PyQt5.QtWidgets import QFileDialog

    if win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_TEXT):
        win32clipboard.OpenClipboard()
        clipboard = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        fileName, _ = QFileDialog.getSaveFileName(window, "QFileDialog.getSaveFileName()", None, "Text Files (*.txt)")
        if fileName == '':
            return True
        f = open(fileName, 'w')
        f.write(clipboard)
        f.close()

    elif win32clipboard.IsClipboardFormatAvailable(win32clipboard.CF_BITMAP):
        im = ImageGrab.grabclipboard()
        fileName, _ = QFileDialog.getSaveFileName(window, "QFileDialog.getSaveFileName()", None, "Text Files (*.bmp)")
        if fileName == '':
            return True
        im.save(fileName, 'BMP')

    return True
