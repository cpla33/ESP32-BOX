### Uploading the CircuitPython firmware in Linux:

1. Download [latest firmware](https://circuitpython.org/board/espressif_esp32_devkitc_v4_wroom_32e/) file from official CircuitPython web-site.

2. Install [esptool](https://github.com/espressif/esptool) as below:

```bash
python3 -m pip install --upgrade esptool
```

3. Plug-in USB-C cable and check for device connection:

```bash
ls /dev/ttyACM0
```

4. Erase flash as below:

```bash
esptool.py --chip esp32 --port /dev/ttyACM0 erase_flash
```

5. Write the CircuitPython firmware:

```bash
esptool.py --chip esp32 --port /dev/ttyACM0 \
           --baud 460800 \
           --after hard_reset \
           write_flash -z 0x0 adafruit-circuitpython-espressif_esp32_devkitc_v4_wroom_32e-en_US-9.2.8.bin
           
```

More options could be found [here](https://learn.adafruit.com/circuitpython-with-esp32-quick-start/command-line-esptool).

------

### Code examples:

Code examples could be found in [EXAMPLES](EXAMPLES/) directory.



------
[Back](../../readme.md)