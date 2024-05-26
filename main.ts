input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    radio.sendString("ledMapTx")
    basic.pause(200)
    for (let index = 0; index < 8; index++) {
        while (!ACK) {
            lastSentName = picsA[_py.py_array_index(modes, currentMode)][index]
            lastSentValue = index
            radio.sendValue(lastSentName, lastSentValue)
            basic.pause(100)
        }
        ACK = false
    }
    while (!ACK) {
        lastSentString = "updateLeds"
        radio.sendString(lastSentString)
        basic.pause(100)
    }
    ACK = false
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    radio.sendValue("bright", 30)
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    
    if (receivedString == lastSentString) {
        ACK = true
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    radio.sendString("ledMapTx")
    basic.pause(200)
    for (let index2 = 0; index2 < 8; index2++) {
        while (!ACK) {
            lastSentName = picsB[_py.py_array_index(modes, currentMode)][index2]
            lastSentValue = index2
            radio.sendValue(lastSentName, lastSentValue)
            basic.pause(100)
        }
        ACK = false
    }
    while (!ACK) {
        lastSentString = "updateLeds"
        radio.sendString(lastSentString)
        basic.pause(100)
    }
    ACK = false
})
radio.onReceivedValue(function on_received_value(name: string, value: number) {
    
    if (name == lastSentName && value == lastSentValue) {
        ACK = true
    }
    
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    
    currentMode = modes[(_py.py_array_index(modes, currentMode) + 1) % modes.length]
    basic.showString("" + currentMode)
})
function initVariables() {
    
    lastSentValue = 0
    lastSentName = ""
    lastSentString = ""
    ACK = false
    messageRx = false
    modes = ["E", "S", "Z", "T"]
    currentMode = modes[3]
    pic = ["rrrrrrrr", "oooooooo", "yyyyyyyy", "gggggggg", "bbbbbbbb", "iiiiiiii", "vvvvvvvv", "wwwwwwww"]
    picsA = [["pppppppp", "piiiiiip", "pibbbbip", "pibggbip", "pibggbip", "pibbbbip", "piiiiiip", "pppppppp"], ["pppppppp", "vvvvvvvv", "pppppppp", "vvvvvvvv", "pppppppp", "vvvvvvvv", "pppppppp", "vvvvvvvv"], ["bbbbbbbb", "bbbbbbbb", "bbbbbbbb", "bbbbbbbb", "bbbbbbbb", "bbbbbbbb", "bbbbbbbb", "bbbbbbbb"], ["00oooo00", "0o0000o0", "o0g00g0o", "o000000o", "o0g00g0o", "o00gg00o", "0o0000o0", "00oooo00"]]
    picsB = [["roygbvpw", "roygbvpw", "roygbvpw", "roygbvpw", "roygbvpw", "roygbvpw", "roygbvpw", "roygbvpw"], ["rrrrrrrr", "oooooooo", "yyyyyyyy", "gggggggg", "bbbbbbbb", "iiiiiiii", "vvvvvvvv", "wwwwwwww"], ["yyyyyyyy", "oooooooo", "rrrrrrrr", "gggggggg", "bbbbbbbb", "iiiiiiii", "vvvvvvvv", "wwwwwwww"], ["00ooo000", "0o000o00", "o0g0g0o0", "o00000o0", "o0g0g0o0", "0o0g0o00", "00ooo000", "00000000"]]
}

let pic : string[] = []
let messageRx = false
let picsB : string[][] = []
let lastSentString = ""
let lastSentValue = 0
let picsA : string[][] = []
let lastSentName = ""
let ACK = false
let currentMode = ""
let modes : string[] = []
initVariables()
radio.setGroup(1)
radio.sendString("ledMapTx")
radio.sendString("updateLeds")
basic.showString("" + currentMode)
music.setVolume(50)
music.setTempo(500)
basic.forever(function on_forever() {
    
})
