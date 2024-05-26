def on_button_pressed_a():
    for index in range(8):
        radio.send_value(picsA[modes.index(currentMode)][index], index)
        basic.pause(100)
    radio.send_string("updateLeds")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    radio.send_value("bright", 30)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    for index2 in range(8):
        radio.send_value(picsB[modes.index(currentMode)][index2], index2)
        basic.pause(100)
    radio.send_string("updateLeds")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    global currentMode
    currentMode = modes[(modes.index(currentMode) + 1) % len(modes)]
    basic.show_string("" + (currentMode))
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def initVariables():
    global modes, currentMode, pic, picsA, picsB
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
        [   "pppppppp",
            "vvvvvvvv",
            "pppppppp",
            "vvvvvvvv",
            "pppppppp",
            "vvvvvvvv",
            "pppppppp",
            "vvvvvvvv"],
        [   "bbbbbbbb",
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
        [   "rrrrrrrr",
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
            "o0w0w0o0",
            "o00000o0",
            "o0g0g0o0",
            "0o0g0o00",
            "00ooo000",
            "00000000"]]
pic: List[str] = []
picsB: List[List[str]] = []
picsA: List[List[str]] = []
modes: List[str] = []
currentMode = ""
initVariables()
radio.set_group(1)
radio.send_string("updateLeds")
basic.show_string("" + (currentMode))
radio.send_string("ledMapTx")
music.set_volume(50)
music.set_tempo(500)

def on_forever():
    pass
basic.forever(on_forever)
