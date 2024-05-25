input.onButtonPressed(Button.A, function () {
    for (let index = 0; index <= 7; index++) {
        radio.sendValue(picsA[modes.indexOf(currentMode)][index], index)
    }
    radio.sendString("updateLeds")
    music.play(music.builtinPlayableSoundEffect(soundExpression.hello), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.AB, function () {
    radio.sendString("updateLeds")
    music.play(music.builtinPlayableSoundEffect(soundExpression.twinkle), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.B, function () {
    for (let index = 0; index <= 7; index++) {
        radio.sendValue(picsB[modes.indexOf(currentMode)][index], index)
    }
    radio.sendString("updateLeds")
    music.play(music.builtinPlayableSoundEffect(soundExpression.happy), music.PlaybackMode.UntilDone)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.InBackground)
    currentMode = modes[(modes.indexOf(currentMode) + 1) % modes.length]
    basic.showString("" + (currentMode))
})
function initVariables () {
    modes = [
    "E",
    "S",
    "Z",
    "T"
    ]
    currentMode = modes[0]
    pic = [
    "rrrrrrrr",
    "oooooooo",
    "yyyyyyyy",
    "gggggggg",
    "bbbbbbbb",
    "iiiiiiii",
    "vvvvvvvv",
    "wwwwwwww"
    ]
    picsA = [
    [
    "rrrrrrrr",
    "oooooooo",
    "yyyyyyyy",
    "gggggggg",
    "bbbbbbbb",
    "iiiiiiii",
    "wwwwwwww",
    "wwwwwwww"
    ],
    [
    "oooooooo",
    "rrrrrrrr",
    "yyyyyyyy",
    "gggggggg",
    "bbbbbbbb",
    "iiiiiiii",
    "wwwwwwww",
    "wwwwwwww"
    ],
    [
    "yyyyyyyy",
    "oooooooo",
    "rrrrrrrr",
    "gggggggg",
    "bbbbbbbb",
    "iiiiiiii",
    "wwwwwwww",
    "wwwwwwww"
    ],
    [
    "gggggggg",
    "oooooooo",
    "yyyyyyyy",
    "rrrrrrrr",
    "bbbbbbbb",
    "iiiiiiii",
    "wwwwwwww",
    "wwwwwwww"
    ]
    ]
    picsB = [
    [
    "rrrrrrrr",
    "oooooooo",
    "yyyyyyyy",
    "gggggggg",
    "bbbbbbbb",
    "iiiiiiii",
    "vvvvvvvv",
    "wwwwwwww"
    ],
    [
    "oooooooo",
    "rrrrrrrr",
    "yyyyyyyy",
    "gggggggg",
    "bbbbbbbb",
    "iiiiiiii",
    "vvvvvvvv",
    "wwwwwwww"
    ],
    [
    "yyyyyyyy",
    "oooooooo",
    "rrrrrrrr",
    "gggggggg",
    "bbbbbbbb",
    "iiiiiiii",
    "vvvvvvvv",
    "wwwwwwww"
    ],
    [
    "gggggggg",
    "oooooooo",
    "yyyyyyyy",
    "rrrrrrrr",
    "bbbbbbbb",
    "iiiiiiii",
    "vvvvvvvv",
    "wwwwwwww"
    ]
    ]
}
let pic: string[] = []
let picsB: string[][] = []
let modes: string[] = []
let picsA: string[][] = []
let currentMode = ""
initVariables()
radio.setGroup(1)
basic.showString("" + (currentMode))
radio.sendString("ledMapTx")
music.setVolume(127)
music.setTempo(500)
basic.forever(function () {
	
})
