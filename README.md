# Quick Script

## What this is
This script allows you to save mini scripts made for small tasks and turn them into an easily accessed library. The scripts will appear in a scroll window and on selection they will run and the window will then close (can be configured).

## Installation / Setup
 1. Clone or download this git
 2. Install requirements
    - Python 3 (not tested with other versions currently)
    - PYQT5 (pip install pyqt5)
 4. Run quick-script.py / RunQuickScript.vbs (could attach it to a hotkey for easy access)

## Usage
To run this the script quick-script.py needs to be run with Python. A window will appear with your scripts. <br/>
![Main Window](http://i.imgur.com/1PGAOod.png "Main Window")<br/>
![Settings Window](http://i.imgur.com/p5ZHgn2.png "Settings Window")


#### Configuration (settings.json)
This file is located by quick-script.py and keeps a record of settings and script run counts.
```json
{
    "close_on_run": true,
    "run_count": {},
    "stay_on_top": true,
    "window_height": 400
}
```

#### Python script files
To make a script appear in the UI they need to be in the /scripts/ folder. The script needs four main features; name, description, tags and a main method which returns True on success. An example of a script is shown here:
```python
NAME = "Example Script"
DESCRIPTION = "Run example script"
TAGS = ["example", "script"]

def main():
    print ("This is an example script")
    return True
```
The scripts can be named anything as long as they are in /scripts/ with a .py extension. The script does not have to have name, description or tags, they will just be rendered as none.

A parameter can be added to the main() method and as long as their is only one parameter required, the window class will be passed to main() so the method will now have access to the window and can use functions like dialogCritical().

## Scripts included
 - [Remove edge quotes](scripts/remove_edge_quotes.py): Will remove edge quotes from the string in your current clipboard (one or both sides)
 - [Save Clipboard to File](scripts/save_clipboard_to_file.py): Will request where to save the current clipboard contents to. Supports images and text (will save to .bmp/.txt)
 - [Put IP on Clipboard](scripts/ip_to_clipboard.py): Will set your local IP to the clipboard.
 - [Restart Windows Exporer](scripts/restart_window_explorer.py): Restarts windows explorer.
 - [UI to PY from Clipboard](scripts/ui_to_py_from_clipboard.py): Gets the current .ui file in the clipboard and will convert it to py using pyuic5 and stores it where the .ui file is located.
 - [Open Clipboard Directory](scripts/open_clipboard_directory.py): Open the location in the clipboard in windows explorer.
 - [Type Clipboard](scripts/type_clipboard.py): Type clipboard contents at a slow pace.

## RunQuickScript.vbs
This just makes it easier to run the project without a shell. Run RunQuickScript.vbs and the GUI will appear without the annoying shell.
