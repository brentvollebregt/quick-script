NAME = "SCRIPT3"
DESCRIPTION = "Run script3"
TAGS = ["3"]

def main(parent):
    print ("script3.py")
    parent.dialogCritical("Hello!", "Hope this worked!")
    return True
