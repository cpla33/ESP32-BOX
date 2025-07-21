# The states of the relays changed in the loop
# only if the INPUT_4 input (button) is shorted to GND.
# If the INPUT_18 input is shorted to GND, we signal "FAULT" (red LED) and
# the relays remain in the safe position (de-energized).
# In the normal state, the green "OK" is lit, and when the cycle is active, the blue "CONN" additionally
# blinks.

import time
import board
import digitalio

# GPIO map
#LED_OK     = board.IO2     # green channel of RGB-led
LED_FAULT  = board.IO16    # red
LED_CONN   = board.IO17    # blue

RELAY_1    = board.IO32
RELAY_2    = board.IO33
RELAY_3    = board.IO27
RELAY_4    = board.IO26

INPUT_4    = board.IO4     # start cycle (will be pulled-up)
INPUT_18   = board.IO18    # fault signal (will be pulled-up)

# INITS
def make_output(pin, value=False):
    p = digitalio.DigitalInOut(pin)
    p.direction = digitalio.Direction.OUTPUT
    p.value = value
    return p

def make_input(pin):
    p = digitalio.DigitalInOut(pin)
    p.direction = digitalio.Direction.INPUT
    p.pull = digitalio.Pull.UP          # HIGH by default, tight to the GND pin to get LOW state
    return p

led_fault = make_output(LED_FAULT, False)
led_conn  = make_output(LED_CONN, False)

relay1 = make_output(RELAY_1)
relay2 = make_output(RELAY_2)
relay3 = make_output(RELAY_3)
relay4 = make_output(RELAY_4)

inp4  = make_input(INPUT_4)
inp18 = make_input(INPUT_18)

print("Setup ready! Start...")

# FUNCTIONS
def set_relays(a, b, c, d):
    relay1.value = a
    relay2.value = b
    relay3.value = c
    relay4.value = d

def fault_state():
    # Turn ON red led and reset relay states
    set_relays(False, False, False, False)
    # led_ok.value    = False
    led_conn.value  = False
    led_fault.value = True

def run_sequence():
    led_fault.value = False
    # led_ok.value    = True
    steps = [
        (True,  False, False, False, "Relay 1"),
        (True,  True,  False, False, "Relay 1+2"),
        (True,  True,  True,  False, "Relay 1+2+3"),
        (True,  True,  True,  True,  "Relay 4"),
        (False, False, True,  True,  "Relay 3+4"),
    ]
    for st in steps:
        set_relays(*st[:4])
        print(st[4])
        # Blue led flashing while the Cycle in progress
        led_conn.value = not led_conn.value
        time.sleep(0.5)
    led_conn.value = False

# MAIN CYCLE
while True:
    if not inp18.value:           # "fault" signal processing
        fault_state()

    elif not inp4.value:          # "start" signal processing
        run_sequence()

    else:
        # ordinary waiting mode
        led_fault.value = False
        led_conn.value  = False
        # led_ok.value    = True
        set_relays(False, False, False, False)

    time.sleep(0.1)
