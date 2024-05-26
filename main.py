def on_button_pressed_a():
    global lastSentName, lastSentValue, ACK, lastSentString
    radio.send_string("ledMapTx")
    basic.pause(200)
    for index in range(8):
        while not (ACK):
            lastSentName = picsA[modes.index(currentMode)][index]
            lastSentValue = index
            radio.send_value(lastSentName, lastSentValue)
            basic.pause(100)
        ACK = False
    while not (ACK):
        lastSentString = "updateLeds"
        radio.send_string(lastSentString)
        basic.pause(100)
    ACK = False
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    radio.send_value("bright", 30)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    global ACK
    if receivedString == lastSentString:
        ACK = True
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global lastSentName, lastSentValue, ACK, lastSentString
    radio.send_string("ledMapTx")
    basic.pause(200)
    for index2 in range(8):
        while not (ACK):
            lastSentName = picsB[modes.index(currentMode)][index2]
            lastSentValue = index2
            radio.send_value(lastSentName, lastSentValue)
            basic.pause(100)
        ACK = False
    while not (ACK):
        lastSentString = "updateLeds"
        radio.send_string(lastSentString)
        basic.pause(100)
    ACK = False
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_value(name, value):
    global ACK
    if name == lastSentName and value == lastSentValue:
        ACK = True
radio.on_received_value(on_received_value)

def on_logo_pressed():
    global currentMode
    currentMode = modes[(modes.index(currentMode) + 1) % len(modes)]
    basic.show_string("" + (currentMode))
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def initVariables():
    global lastSentValue, lastSentName, lastSentString, ACK, messageRx, modes, currentMode, pic, picsA, picsB
    lastSentValue = 0
    lastSentName = ""
    lastSentString = ""
    ACK = False
    messageRx = False
    modes = ["E", "S", "Z", "T"]
    currentMode = modes[3]
    pic = ["rrrrrrrr",
        "oooooooo",
        "yyyyyyyy",
        "gggggggg",
        "bbbbbbbb",
        "iiiiiiii",
        "vvvvvvvv",
        "wwwwwwww"]
    picsA = [["pppppppp",
            "piiiiiip",
            "pibbbbip",
            "pibggbip",
            "pibggbip",
            "pibbbbip",
            "piiiiiip",
            "pppppppp"],
        ["pppppppp",
            "vvvvvvvv",
            "pppppppp",
            "vvvvvvvv",
            "pppppppp",
            "vvvvvvvv",
            "pppppppp",
            "vvvvvvvv"],
        ["bbbbbbbb",
            "bbbbbbbb",
            "bbbbbbbb",
            "bbbbbbbb",
            "bbbbbbbb",
            "bbbbbbbb",
            "bbbbbbbb",
            "bbbbbbbb"],
        ["00oooo00",
            "0o0000o0",
            "o0g00g0o",
            "o000000o",
            "o0g00g0o",
            "o00gg00o",
            "0o0000o0",
            "00oooo00"]]
    picsB = [["roygbvpw",
            "roygbvpw",
            "roygbvpw",
            "roygbvpw",
            "roygbvpw",
            "roygbvpw",
            "roygbvpw",
            "roygbvpw"],
        ["rrrrrrrr",
            "oooooooo",
            "yyyyyyyy",
            "gggggggg",
            "bbbbbbbb",
            "iiiiiiii",
            "vvvvvvvv",
            "wwwwwwww"],
        ["yyyyyyyy",
            "oooooooo",
            "rrrrrrrr",
            "gggggggg",
            "bbbbbbbb",
            "iiiiiiii",
            "vvvvvvvv",
            "wwwwwwww"],
        ["00ooo000",
            "0o000o00",
            "o0g0g0o0",
            "o00000o0",
            "o0g0g0o0",
            "0o0g0o00",
            "00ooo000",
            "00000000"]]
pic: List[str] = []
messageRx = False
picsB: List[List[str]] = []
lastSentString = ""
lastSentValue = 0
picsA: List[List[str]] = []
lastSentName = ""
ACK = False
currentMode = ""
modes: List[str] = []
initVariables()
radio.set_group(1)
radio.send_string("ledMapTx")
radio.send_string("updateLeds")
basic.show_string("" + (currentMode))
music.set_volume(50)
music.set_tempo(500)

def on_forever():
    pass
basic.forever(on_forever)
