'''
main.py
- Reads input from switches and rotary encoders wired directly to GPIO pins on raspberry pi pico.
- Handles input and sends data to computer as both a MIDI device or keyboard device.
- Handles mode control for different apps and updates LED binary display accordingly.
'''

# Imports
import board
import digitalio
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.midi import MidiKeys
from kmk.modules.encoder import EncoderHandler
from kmk.scanners.keypad import KeysScanner
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.layers import Layers


## CUSTOM LAYERS CLASS + LEDs ##
# Inherit from Layers and override 
class ModeLayers(Layers):
  def __init__(self):
    super().__init__()
    # Setup 3-bit LED binary display as digital output. 
    # In reverse order to allow for indexing through from
    # array item 0, which is LED 2
    self.led_pins = [
        digitalio.DigitalInOut(board.GPO22),
        digitalio.DigitalInOut(board.GPO21),
        digitalio.DigitalInOut(board.GPO20),
    ]
    for pin in self.led_pins:
      pin.direction = digitalio.Direction.OUTPUT
      pin.value = False

  def update_leds(self, layer_index):
    # Convert layer integer (0, 1, etc.) directly into 3-bit binary for your 3 LEDs
    for i, pin in enumerate(self.led_pins):
        pin.value = bool((layer_index >> i) & 1)
    

  def activate_layer(self, keyboard, layer, idx=None):
    # Activate a keymapping layer
    super().activate_layer(keyboard, layer, idx)
    # Layer now on, so update LEDs and mode
    self.update_leds(layer)
    current_mode_index = possible_modes.index(current_mode)
    current_mode = possible_modes[current_mode_index + 1]

  def deactivate_layer(self, keyboard, layer):
    super().deactivate_layer(keyboard, layer)
    # Runs when a layer is popped/deactivated, fallback to current top layer
    if keyboard.active_layers:
      self.update_leds(keyboard.active_layers[0])


## KEYBOARD SETUP ##
# Define keyboard with pin reads for each MX switch
class MacroPad (KMKKeyboard):
    def __init__ (self):
        self.matrix = KeysScanner (
            pins = [
                board.GP0,
                board.GP1,
                board.GP2,
                board.GP3,
                board.GP4,
                board.GP5,
                board.GP6,
                board.GP7,
                board.GP8,
                board.GP9
            ], 
            pull=True,
            value_when_pressed=False,
        )

# Instantiate keyboard
keyboard = MacroPad() # Instead of the usual keyboard = KMKKeyboard()


## MODES ##
try:
    with open ('mode.txt', 'r') as f:
        current_mode = f.read()
    if current_mode == '':
        current_mode = "ableton"
except:
   current_mode = "ableton"

possible_modes = ["ableton", "fcpx"]


## HANDLERS ##
# Instantiate handlers
midi_module = MidiKeys()
layers_module = ModeLayers()
encoder_handler = EncoderHandler()
mousekey_handler = MouseKeys()
# Add handlers
keyboard.modules.append(midi_module)
keyboard.modules.append(encoder_handler)
keyboard.modules.append(mousekey_handler)
keyboard.modules.append(layers_module)
#keyboard.modules.append(layers, holdtap) # I don't know if I need this, but the encoder tutorial added these two as well.


## ROTARY ENCODER SETUP ##
# See https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/encoder.md if not working. e.g. if it's I2C.
# Define pin reads for encoders

encoder_handler.divisor = 1 # Change if number of gradiations doesn't feel good
encoder_handler.pins = (
    # Encoder 1 (zoom)
    (board.GPO19, board.GPO26, None), # Format: pin_a, pin_b, pin_switch
    # Encoder 2 (scroll)
    (board.GPO27, board.GPO28, None),
)


## SWITCH HANDLER ##
keyboard.keymap = [
    # Layer 0: Ableton
    [
        KC.LGUI(KC.Z), # 1: cmd + z
        KC.MIDI_CC(21, 127),
        KC.MIDI_CC(22, 127),
        KC.MIDI_CC(23, 127), # 4: Record
        KC.MIDI_CC(24, 127),
        KC.MIDI_CC(25, 127),
        KC.MIDI_CC(26, 127),
        KC.MIDI_CC(27, 127),
        KC.SPACE,
        KC.TO(1) # 10: Cycle Mode
    ],
    # Layer 1: Final Cut Pro X
        [
            KC.LGUI(KC.Z), # 1: cmd + z
            KC.N, # 2: Snapping
            KC.B, # 3: Blade
            KC.A, # 4: Arrow
            KC.LALT(KC.LBRACKET), # 5: Trim start to playhead
            KC.LALT(KC.RBRACKET), # 6: Trim end to playhead
            KC.R,
            KC.T,
            KC.SPACE, # 9: Play/Pause
            KC.TO(0) # 10: Cycle Mode (change as I add more)
        ]
]



## ROTARY ENCODER HANDLER ##
encoder_handler.map = [
      (
          KC.LGUI(KC.MINUS),
          KC.LGUI(KC.EQUAL),
          KC.NO,
      ),  # Encoder 1: Zoom In/Out, No push
      (
          KC.LSHIFT(KC.MWUP),
          KC.LSHIFT(KC.MWDOWN),
          KC.NO,
      ),  # Encoder 2: Horizontal Scroll, No push
  ]