# pi74HC595

Allows for easy use of the 74HC595 Shift Register with a Raspberry Pi

<p>
    <a href="https://pypi.org/project/pi74HC595/"><img src="https://img.shields.io/pypi/v/pi74HC595" alt="Pypi version" height="18"></a>
    <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.x-blue.svg" alt="Python version" height="18"></a>
    <a href="https://github.com/2kofawsome/pi74HC595/blob/master/LICENSE"><img src="https://img.shields.io/github/license/2kofawsome/pi74HC595" alt="License" height="18"></a>
</p>

## Install
```bash
$ pip install stockfish
```

## Usage

### Initialize pi74HC595 class

You should install the stockfish engine in your operating system globally or specify path to binary file in class constructor

```python
import pi74HC595

shift_register = pi74HC595()
```

There are some default settings:
```python
def __init__(
        self,
        DS: int = 11,
        ST: int = 13,
        SH: int = 15,
        daisy_chain: int = 1,
        remember: bool = True,
    )
```

##### Pin Numbering

You will likely need to change the Raspberry Pi pins during initialization. This package uses gpio.BOARD (pin numbering as opposed to GPIO numbering):
```python
shift_register = pi74HC595(7, 37, 22)
```

These can also be set after initialization with 
```python
shift_register.set_ds(7)
shift_register.set_sh(37)
shift_register.set_st(22)
```

##### Daisy Chaining

If you are daisy chaining multiple 74HC595s then you will can set daisy_chain during initialization.
```python
shift_register = pi74HC595(7, 37, 22, daisy_chain = 2)

shift_register = pi74HC595(daisy_chain = 13)

# etc
```

This can also be done after initialization with 
```python
shift_register.set_daisy_chain(3) # Any positive int
```


##### Remembering Previous State

The default behaviour of a 74HC595 is that if a single new value is passed and the storage register is clocked, 
the old valuesa are "forgotten"

ie if current state is "10101010" and "1" is sent, the new state is "10000000"
I built this package to fix this for my purposes, so if "1" is sent it will update to "11010101"

You can remove this functionality and keep the 74HC595 from "remembering" the past state during initialization.
```python
shift_register = pi74HC595(7, 37, 22, daisy_chain = 2, remember = False)

shift_register = pi74HC595(remember = False)

# etc
```

This can also be done after initialization with 
```python
shift_register.set_remember(False) # True or False
```


### Set Values with a List:

Will accept both Integers (1 and 0 only) as well as Boolean values (True and False)
```python
shift_register.set_by_list([0, 1, 0, 1, 1, 1, 0, 0])
shift_register.set_by_list([False, True, False,...])
```

### Set Values with an Integer:

This was created with the intent to send a single 1 or 0 for on or off,
but can also function with a larger int by converting to binary
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

Sets each value that is remembered to off (0)
```python
shift_register.clear()
```

### Get All Current Values:

Returns the current values, only when remember is set True
```python
shift_register.get_values()
```
```text
[0, 0, 0, 0, 0, 0, 0, 0]
```


## Testing
```bash
$ python setup.py test
```

## Credits
- [Ilya Zhelyabuzhsky](https://github.com/2kofawsome)

## License
MIT License. Please see [License File](LICENSE) for more information.