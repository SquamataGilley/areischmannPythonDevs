#!/bin/python3

import evdev
device = evdev.InputDevice('/dev/input/event0')
print(device)
    ### This path is just a simple ubuntu path that can be changed to any location on a linux derivative computer. Our file is named Data.txt
storedPath = r"/home/YOURPC/PATH/TO/FOLDER/Data.txt"

for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
            ### changed the print call to a variable to make this information easier to access when needed further down the road
        barcodeData = (evdev.categorize(event))
            ### this line just turns the variable "barcodeData" into a writable string that adds a new line afterwards
        barcodeWriteable = f"""{barcodeData}\n"""
            ### the barcode information is still printed out to the terminal but it is now named barcodeData to be recognized easier than its previous name
        print(barcodeData)
            ### this line here creates and opens a file in the path above, or will open it if it exists already.
            ### the "a" just means that we are appending data to the file rather than "w" which wipes the data on the file and writes from there
        storeBarcode = open(storedPath, "a")
            ### this actually adds the barcode data to the file
        storeBarcode.write(str(barcodeWriteable))
            ### this line just closes and saves the file so that it can be accessed by another program or person
            ### IT IS IMPERATIVE THAT THIS COMPLETES OR THE INFORMATION WILL NOT BE SAVED
        storeBarcode.close()
            ### just a confirmation message that everything completed successfully
        print("Your information was successfully saved to its file")

