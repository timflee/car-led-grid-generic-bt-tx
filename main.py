def on_button_pressed_a():
    for index in range(8):
        radio.send_value(picsA[modes.index(currentMode)][index], index)
    radio.send_string("updateLeds")
    music.play(music.builtin_playable_sound_effect(soundExpression.hello),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    radio.send_string("updateLeds")
    music.play(music.builtin_playable_sound_effect(soundExpression.yawn),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    for index2 in range(8):
        radio.send_value(picsB[modes.index(currentMode)][index2], index2)
    radio.send_string("updateLeds")
    music.play(music.builtin_playable_sound_effect(soundExpression.slide),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    global currentMode
    music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.IN_BACKGROUND)
    currentMode = modes[(modes.index(currentMode) + 1) % len(modes)]
    basic.show_string("" + (currentMode))
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def initVariables():
    global modes, currentMode, pic, picsA, picsB
    modes = ["E", "S", "Z", "T"]
    currentMode = modes[0]
    pic = ["rrrrrrrr",
        "oooooooo",
        "yyyyyyyy",
        "gggggggg",
        "bbbbbbbb",
        "iiiiiiii",
        "vvvvvvvv",
        "wwwwwwww"]
    picsA = [["rrrrrrrr",
            "oooooooo",
            "yyyyyyyy",
            "gggggggg",
            "bbbbbbbb",
            "iiiiiiii",
            "wwwwwwww",
            "wwwwwwww"],
        ["oooooooo",
            "rrrrrrrr",
            "yyyyyyyy",
            "gggggggg",
            "bbbbbbbb",
            "iiiiiiii",
            "wwwwwwww",
            "wwwwwwww"],
        ["yyyyyyyy",
            "oooooooo",
            "rrrrrrrr",
            "gggggggg",
            "bbbbbbbb",
            "iiiiiiii",
            "wwwwwwww",
            "wwwwwwww"],
        ["gggggggg",
            "oooooooo",
            "yyyyyyyy",
            "rrrrrrrr",
            "bbbbbbbb",
            "iiiiiiii",
            "wwwwwwww",
            "wwwwwwww"]]
    picsB = [["rrrrrrrr",
            "oooooooo",
            "yyyyyyyy",
            "gggggggg",
            "bbbbbbbb",
            "iiiiiiii",
            "vvvvvvvv",
            "wwwwwwww"],
        ["oooooooo",
            "rrrrrrrr",
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
        ["gggggggg",
            "oooooooo",
            "yyyyyyyy",
            "rrrrrrrr",
            "bbbbbbbb",
            "iiiiiiii",
            "vvvvvvvv",
            "wwwwwwww"]]
pic: List[str] = []
picsB: List[List[str]] = []
modes: List[str] = []
picsA: List[List[str]] = []
currentMode = ""
initVariables()
radio.set_group(1)
basic.show_string("" + (currentMode))
radio.send_string("ledMapTx")
music.set_volume(50)
music.set_tempo(500)

def on_forever():
    pass
basic.forever(on_forever)
