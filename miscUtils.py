import sys

def printBorder(length = 64):
    print("-" * length)

## Function to convert a value in a range to another range
## Credit: https://stackoverflow.com/questions/929103
def convertRange(OldMin, OldMax, NewMin, NewMax, OldValue):
    OldRange = (OldMax - OldMin)
    if OldRange == 0:
        NewValue = NewMin
    else:
        NewRange = (NewMax - NewMin)  
        NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin
    return NewValue

## Function to remove the last printed line in the console
## Credit: https://stackoverflow.com/a/52590238
def removeLastLine():
    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')

