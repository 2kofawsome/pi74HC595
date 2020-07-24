# pi74HC595

Allows for easy use of the 74HC595 Shift Register with a Raspberry Pi

<p>
	<a href="https://pypi.org/project/pi74HC595/"><img src="https://img.shields.io/pypi/v/pi74HC595" alt="Pypi version" height="18"></a>
	<a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.x-blue.svg" alt="Python version" height="18"></a>
	<a href="https://github.com/2kofawsome/pi74HC595/blob/master/LICENSE"><img src="https://img.shields.io/github/license/2kofawsome/pi74HC595" alt="License" height="18"></a>
	<a href="https://pepy.tech/project/pi74hc595"><img src="https://pepy.tech/badge/pi74hc595" alt="Downloads" height="18"></a>
</p>

## Install
```bash
$ pip install pi74HC595
```


## Initialize pi74HC595 class

You should install the stockfish engine in your operating system globally or specify path to binary file in class constructor

```python
from pi74HC595 import pi74HC595
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
shift_register = pi74HC595()
```

<p align="center"><i>This package uses gpio.BOARD (pin numbering as opposed to GPIO numbering)</i></p>

### There are some default settings:

```python
def __init__(
        DS: int = 11,
        ST: int = 13,
        SH: int = 15,
        daisy_chain: int = 1,
    )
```

### Pin Numbering

Raspberry Pi Pinout     |  74HC595 Pinout
:-------------------------:|:-------------------------:
![Raspberry Pi Pinout](https://raw.githubusercontent.com/2kofawsome/pi74HC595/master/READMEimages/Pi_pinout.jpg)  |  ![74HC595 Pinout](https://raw.githubusercontent.com/2kofawsome/pi74HC595/master/READMEimages/74HC595_pinout.png)

<p align="center"><i>Both Vcc and MR require 5V</i></p>

You will likely need to change the Raspberry Pi pins during initialization. 
```python
shift_register = pi74HC595(7, 37, 22)
```

These can also be set after initialization with...
```python
shift_register.set_ds(7) # Any GPIO pin on Raspberry Pi
shift_register.set_sh(37)
shift_register.set_st(22)
```

### Daisy Chaining

If you are daisy chaining multiple 74HC595s then you can set daisy_chain to your number of 74HC595s during initialization.
```python
shift_register = pi74HC595(7, 37, 22, 2)

shift_register = pi74HC595(daisy_chain = 13)

# etc
```

This can also be done after initialization with...
```python
shift_register.set_daisy_chain(3) # Any positive int
```

## Usage

### Set Values with a List:

Will accept both Integers (1 and 0 only) as well as Boolean values (True and False)
```python
shift_register.set_by_list([0, 1, 0, 1, 1, 1, 0, 0])
shift_register.set_by_list([False, True, False,...])
```

### Set Values with an Integer:

This was created with the intent to send a single 1 or 0 for on or off,
but can also function with a larger int as it converts to binary
```python
shift_register.set_by_int(0)
shift_register.set_by_int(1)

shift_register.set_by_int(12) #1100
shift_register.set_by_int(9999) #1111100111
```

### Set Values with a Boolean:

Can send a single True or False for on or off.
```python
shift_register.set_by_bool(True)
shift_register.set_by_bool(False)
```

### Clear All Current Values:

Sets each value to off (0)
```python
shift_register.clear()
```

### Get All Current Values:

Returns the current values
```python
shift_register.get_values()
```
```text
[0, 0, 0, 0, 0, 0, 0, 0]
```

## Good 74HC595 Tutorials

It took me awhile to finally understand how the 74HC595 worked since I had no prior hardware experience. These are the tutorials I used to understand the shift register.

[Great but with Arduino](https://lastminuteengineers.com/74hc595-shift-register-arduino-tutorial/)

[Good and with Raspberry Pi](https://circuitdigest.com/microcontroller-projects/raspberry-pi-74hc595-shift-register-tutorial)

## Credits
- [Sam Gunter](https://github.com/2kofawsome)

## License
MIT License. Please see [License File](LICENSE) for more information.