#!/bin/python3
import string
import evdev

eventLocation = f"""/dev/input/event"""
eventList = (0, 1, 2, 3, 4, 5, 6, 7)
for eventInteger in eventList:
    eventPath = f"""{eventLocation}{eventInteger}"""
    deviceString = str(evdev.InputDevice(eventPath))
        # We changed this string in order to allow for other devices than just this one
    if "HID 0581:011c" in deviceString:
        print(f"""Device: {deviceString}""")
        device = evdev.InputDevice(eventPath)
        break

storedPath = r"/home/airxcel1/Scripts/RawEmployeeFile"
Letters = list(string.ascii_uppercase + string.ascii_lowercase)
Specials = list(string.digits) + ["_", "-"]
alphaNumeric = Letters + Specials
evenOdd = 0
finalString = ""

for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        barcodeData = (str(evdev.categorize(event)))
        if "LEFTSHIFT" not in barcodeData:
            if evenOdd % 2 == 1:
                for i in alphaNumeric:
                    keySearch = "KEY_"
                    keyValid = keySearch + i
                    barcodeIndex = barcodeData.find(keySearch)
                    barcodeGet = barcodeData[barcodeIndex:barcodeIndex + 5]
                    barcodeFinal = barcodeGet.replace("KEY_", "")
                        # prints as "KEY_MINUS"
                    keyMinus = keySearch + "MINUS"
                    minusGet = barcodeData[barcodeIndex:barcodeIndex + 9]
                    if minusGet == "KEY_MINUS":
                        finalString = finalString + "-"
                        break
                    elif barcodeGet == keyValid:
                        finalString = finalString + barcodeFinal
                        break
                    barcodeBreak = "KEY_ENTER"
                    barcodeBreakValid = barcodeData[barcodeIndex:barcodeIndex + 9]
                    if barcodeBreak == barcodeBreakValid:
                        storeBarcode = open(storedPath, "w")
                        storeBarcode.write(f"""{finalString}""")
                        storeBarcode.close()
                        finalString = ""
                        break
                if barcodeBreakValid == barcodeBreak:
                    break
                evenOdd += 1
            elif evenOdd % 2 == 0:
                evenOdd += 1
        else:
            pass
