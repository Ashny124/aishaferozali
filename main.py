def on_button_pressed_a():
    basic.show_number(14)
    basic.show_string("Hello!")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    led.plot(4, 2)
    led.plot(3, 3)
    led.plot(2, 4)
    led.plot(1, 3)
    led.plot(0, 2)
    led.plot(0, 1)
    led.plot(1, 0)
    led.plot(2, 1)
    led.plot(3, 0)
    led.plot(4, 1)
    basic.show_string("  I LOVE YOU!       SIKE!!!!!")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_string("STOP IT!")
    basic.show_icon(IconNames.ANGRY)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_sound_loud():
     pass
input.on_sound(DetectedSound.LOUD, on_sound_loud)