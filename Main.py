import board
import supervisor

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.handlers.sequences import simple_key_sequence

# ---------------------------
# 1) MATRIX AND PIN SETUP
# ---------------------------

# EDIT THESE to match your wiring
ROW_PINS = (
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
)

COL_PINS = (
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP11,
    board.GP12,
    board.GP13,
    board.GP14,
    board.GP15,
    board.GP16,
    board.GP17,
    board.GP18,
    board.GP19,
    board.GP20,
)

# Change if diodes go from row->col instead of col->row
DIODE_DIRECTION = DiodeOrientation.COL2ROW


class Keycool84Pico(KMKKeyboard):
    def __init__(self):
        super().__init__()

        # Tell KMK about our matrix scanner
        self.matrix = MatrixScanner(
            row_pins=ROW_PINS,
            col_pins=COL_PINS,
            columns_to_anodes=(DIODE_DIRECTION == DiodeOrientation.COL2ROW),
            interval=0.002,  # scan interval (seconds)
            max_events=64,
        )

        # Set USB product/vendor strings (optional, but nice)
        self.debug_enabled = False
        self.product = 'Keycool 84 Pico KMK'
        self.manufacturer = 'Muhammad'
        self.description = 'Keycool 84 with Raspberry Pi Pico running KMK'


keyboard = Keycool84Pico()

# ---------------------------
# 2) LAYOUT HELPER
# ---------------------------

# We’ll define a simple helper "layout" that assumes a
# 6x15 matrix and maps keys row by row.
#
# You MUST map keys in the same order that the PCB matrix is wired.
# For now, we'll assume a fairly typical 84-key ANSI layout and leave
# some positions as KC.NO where no switch exists.

____ = KC.NO  # easier placeholder


# ---------------------------
# 3) LAYERS
# ---------------------------

keyboard.keymap = [

    # Layer 0: Base layer
    [
        # Row 0 (15 columns)
        KC.ESC,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,
        KC.N0,   KC.MINS, KC.EQL,  KC.BSPC, KC.INS,

        # Row 1
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,
        KC.P,    KC.LBRC, KC.RBRC, KC.BSLS, KC.DEL,

        # Row 2
        KC.CAPS, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,
        KC.SCLN, KC.QUOT, KC.ENT,  ____,    ____,

        # Row 3
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,
        KC.SLSH, KC.RSFT, KC.UP,   ____,    ____,

        # Row 4
        KC.LCTL, KC.LGUI, KC.LALT, ____,    KC.SPC,  KC.SPC,  KC.SPC,  ____,    KC.RALT, KC.RGUI,
        KC.APP,  KC.RCTL, KC.LEFT, KC.DOWN, KC.RGHT,

        # Row 5 – if your board uses it (often for nav/extra keys)
        ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,
        ____,    ____,    ____,    ____,    ____,
    ],

    # Layer 1: Fn layer
    [
        # Row 0
        ____,    KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,
        KC.F10,  KC.F11,  KC.F12,  ____,    ____,

        # Row 1
        ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    KC.PSCR, KC.SLCK,
        KC.PAUS, ____,    ____,    ____,    ____,

        # Row 2
        ____,    ____,    ____,    ____,    ____,    ____,    KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT,
        ____,    ____,    ____,    ____,    ____,

        # Row 3
        ____,    ____,    ____,    ____,    ____,    ____,    KC.HOME, KC.PGDN, KC.PGUP, KC.END,
        ____,    ____,    ____,    ____,    ____,

        # Row 4
        ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,
        ____,    ____,    ____,    ____,    ____,

        # Row 5
        ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,    ____,
        ____,    ____,    ____,    ____,    ____,
    ],
]

# Example Fn: Hold right Alt to access Layer 1
# Change the spot of MO(1) to match your actual matrix position
keyboard.keymap[0][COL_PINS.index(COL_PINS[-3]) + 4 * len(COL_PINS)] = KC.MO(1)

# ---------------------------
# 4) MAIN LOOP
# ---------------------------

if __name__ == '__main__':
    supervisor.runtime.autoreload = True
    keyboard.go()
