import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
import board
import digitalio

btn1_pin = board.GP1
btn2_pin = board.GP4
btn3_pin = board.GP21
btn4_pin = board.GP2
btn5_pin = board.GP5
btn6_pin = board.GP20
btn7_pin = board.GP3
btn8_pin = board.GP6
btn9_pin = board.GP19
btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN
btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN
btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN
btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN
btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN
btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN
btn7 = digitalio.DigitalInOut(btn7_pin)
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.DOWN
btn8 = digitalio.DigitalInOut(btn8_pin)
btn8.direction = digitalio.Direction.INPUT
btn8.pull = digitalio.Pull.DOWN
btn9 = digitalio.DigitalInOut(btn9_pin)
btn9.direction = digitalio.Direction.INPUT
btn9.pull = digitalio.Pull.DOWN
keyboard = Keyboard(usb_hid.devices)

while True:
    if btn1.value:
        keyboard.send(Keycode.ONE)
        time.sleep(0.1)
    if btn2.value:
        keyboard.send(Keycode.TWO)
        time.sleep(0.1)
    if btn3.value:
        keyboard.send(Keycode.THREE)
        time.sleep(0.1)
    if btn4.value:
        keyboard.send(Keycode.CONTROL, Keycode.MINUS)
        time.sleep(0.1)
    if btn5.value:
        keyboard.send(Keycode.CONTROL, Keycode.EQUALS)
        time.sleep(0.1)
    if btn6.value:
        keyboard.send(Keycode.SHIFT, Keycode.COMMA)
        keyboard.send(Keycode.SHIFT, Keycode.ONE)
        keyboard.send(Keycode.SHIFT, Keycode.D)
        keyboard.send(Keycode.SHIFT, Keycode.O)
        keyboard.send(Keycode.SHIFT, Keycode.C)
        keyboard.send(Keycode.SHIFT, Keycode.T)
        keyboard.send(Keycode.SHIFT, Keycode.Y)
        keyboard.send(Keycode.SHIFT, Keycode.P)
        keyboard.send(Keycode.SHIFT, Keycode.E)
        keyboard.send(Keycode.SPACE, Keycode.H, Keycode.T, Keycode.M, Keycode.L)
        keyboard.send(Keycode.SHIFT, Keycode.PERIOD)
        keyboard.send(Keycode.ENTER)
        keyboard.send(Keycode.SHIFT, Keycode.COMMA)
        keyboard.send(Keycode.H, Keycode.T, Keycode.M, Keycode.L)
        keyboard.send(Keycode.SHIFT, Keycode.PERIOD)
        keyboard.send(Keycode.ENTER)
        keyboard.send(Keycode.SHIFT, Keycode.COMMA)
        keyboard.send(Keycode.H, Keycode.E, Keycode.A, Keycode.D)
        keyboard.send(Keycode.SHIFT, Keycode.PERIOD) #<head> tag
        keyboard.send(Keycode.ENTER)
        keyboard.send(Keycode.SHIFT, Keycode.COMMA)#<meta> tag start
        keyboard.send(Keycode.M, Keycode.E, Keycode.T, Keycode.A, Keycode.SPACE)
        keyboard.send(Keycode.C, Keycode.H, Keycode.A, Keycode.R, Keycode.S)
        keyboard.send(Keycode.E, Keycode.T, Keycode.EQUALS)
        keyboard.send(Keycode.SHIFT, Keycode.QUOTE)
        keyboard.send(Keycode.U, Keycode.T, Keycode.F, Keycode.MINUS, Keycode.EIGHT)
        keyboard.send(Keycode.SHIFT, Keycode.QUOTE)
        keyboard.send(Keycode.SHIFT, Keycode.PERIOD) #<meta> tag end
        keyboard.send(Keycode.ENTER)
        keyboard.send(Keycode.SHIFT, Keycode.COMMA)
        keyboard.send(Keycode.M, Keycode.E, Keycode.T, Keycode.A)
        keyboard.send(Keycode.SPACE, Keycode.N, Keycode.A, Keycode.M, Keycode.E)
        keyboard.send(Keycode.EQUALS)
        keyboard.send(Keycode.SHIFT, Keycode.QUOTE)
        keyboard.send(Keycode.V, Keycode.I, Keycode.E, Keycode.W)
        keyboard.send(Keycode.P, Keycode.O, Keycode.R, Keycode.T)
        keyboard.send(Keycode.SHIFT, Keycode.QUOTE)
        keyboard.send(Keycode.SPACE)
        keyboard.send(Keycode.C, Keycode.O, Keycode.N, Keycode.T, Keycode.E)
        keyboard.send(Keycode.N, Keycode.T, Keycode.EQUALS)
        keyboard.send(Keycode.SHIFT, Keycode.QUOTE)
        keyboard.send(Keycode.W, Keycode.I, Keycode.D, Keycode.T, Keycode.H)
        keyboard.send(Keycode.EQUALS)
        keyboard.send(Keycode.D, Keycode.E, Keycode.V, Keycode.I, Keycode.C)
        keyboard.send(Keycode.E, Keycode.MINUS)
        keyboard.send(Keycode.W, Keycode.I, Keycode.D, Keycode.T, Keycode.H)
        keyboard.send(Keycode.SHIFT, Keycode.QUOTE)
        keyboard.send(Keycode.SHIFT, Keycode.PERIOD)
        keyboard.send(Keycode.ENTER)
        keyboard.send(Keycode.SHIFT, Keycode.COMMA)#<title>
        keyboard.send(Keycode.T, Keycode.I)
        keyboard.send(Keycode.T, Keycode.L, Keycode.E)
        keyboard.send(Keycode.SHIFT, Keycode.PERIOD)
        keyboard.send(Keycode.SHIFT, Keycode.COMMA)
        keyboard.send(Keycode.FORWARD_SLASH, Keycode.T, Keycode.I)
        keyboard.send(Keycode.T, Keycode.L, Keycode.E)
        keyboard.send(Keycode.SHIFT, Keycode.PERIOD) #</title> tag
        keyboard.send(Keycode.ENTER)
        keyboard.send(Keycode.SHIFT, Keycode.COMMA)
        keyboard.send(Keycode.FORWARD_SLASH)
        keyboard.send(Keycode.H, Keycode.E, Keycode.A, Keycode.D)
        keyboard.send(Keycode.SHIFT, Keycode.PERIOD) #</head> tag
        keyboard.send(Keycode.ENTER)
        keyboard.send(Keycode.ENTER)
        keyboard.send(Keycode.SHIFT, Keycode.COMMA)
        keyboard.send(Keycode.B, Keycode.O, Keycode.D, Keycode.Y)
        keyboard.send(Keycode.SHIFT, Keycode.PERIOD)
        keyboard.send(Keycode.ENTER)
        keyboard.send(Keycode.ENTER, Keycode.BACKSPACE)
        keyboard.send(Keycode.SHIFT, Keycode.COMMA)
        keyboard.send(Keycode.FORWARD_SLASH, Keycode.B, Keycode.O, Keycode.D, Keycode.Y)
        keyboard.send(Keycode.SHIFT, Keycode.PERIOD)
        keyboard.send(Keycode.ENTER, Keycode.BACKSPACE, Keycode.BACKSPACE)
        keyboard.send(Keycode.SHIFT, Keycode.COMMA)
        keyboard.send(Keycode.FORWARD_SLASH, Keycode.H, Keycode.T, Keycode.M, Keycode.L)
        keyboard.send(Keycode.SHIFT, Keycode.PERIOD)
        time.sleep(0.1)
    if btn7.value: #copy button
        keyboard.send(Keycode.CONTROL, Keycode.C)
        time.sleep(0.1)
    if btn8.value: #paste button
        keyboard.send(Keycode.CONTROL, Keycode.V)
        time.sleep(0.1)
    if btn9.value: #email address button
        keyboard.send(Keycode.L)
        keyboard.send(Keycode.U)
        keyboard.send(Keycode.C)
        keyboard.send(Keycode.A)
        keyboard.send(Keycode.S)
        keyboard.send(Keycode.O)
        keyboard.send(Keycode.T)
        keyboard.send(Keycode.A)
        keyboard.send(Keycode.N)
        keyboard.send(Keycode.E)
        keyboard.send(Keycode.Z)
        keyboard.send(Keycode.ZERO)
        keyboard.send(Keycode.SHIFT, Keycode.TWO)
        keyboard.send(Keycode.G)
        keyboard.send(Keycode.M)
        keyboard.send(Keycode.A)
        keyboard.send(Keycode.I)
        keyboard.send(Keycode.L)
        keyboard.send(Keycode.PERIOD)
        keyboard.send(Keycode.C)
        keyboard.send(Keycode.O)
        keyboard.send(Keycode.M)
        time.sleep(0.1)
    time.sleep(0.1)
