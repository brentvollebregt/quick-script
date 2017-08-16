# Quick Script
***Currently in Development*** <br/>

## What this is
This script allows you to save mini scripts made for small tasks and turn them into an easily accessed library. The scripts will appear in a scroll window and on selection they will run and the window will then close (can be configured).

## Installation / Setup
 1. Clone or download this git
 2. Install requirements
    - Python 3 (not tested with other versions currently)
    - PYQT5 (pip install pyqt5)
 3. Configure settings.json to how you like
 4. Run quick-script.py (could attach it to a hotkey for easy access)

## Usage
To run this the script quick-script.py needs to be run with Python. A window will appear with your scripts. <br/>
*Image of GUI (Add in later)* <br/>


#### Configuration (settings.json)
This file is located by quick-script.py and keeps a record of settings and script run counts.
```json
{
    "close_on_run": true
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
The scripts can be named anything as long as they are in /scripts/ with a .py extension.

## Notes
