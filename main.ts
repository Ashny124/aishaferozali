input.onPinPressed(TouchPin.P0, function () {
    radio.sendString(Ashny)
})
radio.onReceivedString(function (receivedString) {
    basic.showLeds(`
        . . . . #
        . . . # .
        # . # . .
        . # . . .
        . . . . .
        `)
})
let Ashny = ""
Ashny = "Ashny"
radio.setGroup(124)
