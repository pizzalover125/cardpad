import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.scanners.ioexpander import PCF857X, PCF857XScanner
from kmk.modules.macros import Macros, Press, Release, Tap
from kmk.keys import KC

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

direct_gpio_pins = [
    board.GP26, board.GP27, board.GP28,
    board.GP29, board.GP1, board.GP2,
    board.GP0,  board.GP3, board.GP4,
]

direct_scanner = KeysScanner(
    pins=direct_gpio_pins,
    value_when_pressed=False,
    pull=True
)

ioexpander = PCF857X(i2c=board.I2C(), address=0x38)
pcf_scanner = PCF857XScanner(
    ioexpander=ioexpander,
    pins=[0, 1, 2, 3, 4, 5, 6],
    value_when_pressed=False,
)

keyboard.matrix = [direct_scanner, pcf_scanner]

keyboard.keymap = [
    [
        KC.A, KC.B, KC.C, KC.D, KC.E, KC.F, KC.G, KC.H, KC.I, KC.J, KC.K, KC.L, KC.M, KC.N, KC.O, KC.MACRO("https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
    ]
]

if __name__ == '__main__':
    keyboard.go()
