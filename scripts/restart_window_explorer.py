NAME = "Restart Windows Explorer"
DESCRIPTION = "Restart Windows Explorer"
TAGS = ["Restart", "Explorer", "Windows", "WE"]

import os

def main():
    os.system("taskkill /f /im explorer.exe")
    os.system("start explorer.exe")

    return True