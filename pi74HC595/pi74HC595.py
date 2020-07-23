import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)


class pi74HC595:
    def __init__(
        self,
        DS: int = 11,
        ST: int = 13,
        SH: int = 15,
        daisy_chain: int = 1,
        remember: bool = True,
    ):

        self.data = DS  # DS
        self.parallel = ST  # ST_CP
        self.serial = SH  # SH_CP
        self.daisy_chain = daisy_chain  # Number of 74HC595s
        self.current = [0, 0, 0, 0, 0, 0, 0, 0] * self.daisy_chain
        self.remember = (
            remember  # If past state is saved, default is to remember (True)
        )
        self._setup_board()
        self.clear()

    def _setup_board(self):
        gpio.setup(self.data, gpio.OUT)
        gpio.output(self.data, gpio.LOW)
        gpio.setup(self.parallel, gpio.OUT)
        gpio.output(self.parallel, gpio.LOW)
        gpio.setup(self.serial, gpio.OUT)
        gpio.output(self.serial, gpio.LOW)

    def _output(self):  # ST_CP
        gpio.output(self.parallel, gpio.HIGH)
        gpio.output(self.parallel, gpio.LOW)

    def _tick(self):  # SH_CP
        gpio.output(self.serial, gpio.HIGH)
        gpio.output(self.serial, gpio.LOW)

    def _set_values(self, values):
        if self.remember == True:
            for bit in reversed(values):
                self.current.append(bit)
                del self.current[0]
        else:
            self.current = values + [0] * (self.daisy_chain * 8 - len(values))

        for bit in self.current:
            if bit == 1:
                gpio.output(self.data, gpio.HIGH)
            elif bit == 0:
                gpio.output(self.data, gpio.LOW)
            self._tick()
        self._output()

    def set_ds(self, pin):
        """
        Sets the pin for the serial data input (DS)

        Returns: None

        """
        self.data = DS

    def set_sh(self, pin):
        """
        Sets the pin for the shift register clock pin (SH_CP)

        Returns: None

        """
        self.parallel = DS

    def set_st(self, pin):
        """
        Sets the pin for the storage register clock pin (ST_CP)

        Returns: None

        """
        self.serial = ST

    def set_daisy_chain(self, num: int):
        """
        Sets the the number of 74HC595s used in Daisy Chain

        Returns: None

        """
        self.daisy_chain = num

    def set_remember(self, save: bool):
        """
        Sets if the past state will be remembered when new values are given
            (shift instead of replace)

        Returns: None

        """
        self.data = save

    def set_by_list(self, values):
        """
        Sends values in list to the internal function

        args: [0, 1, 0,...]
            or
            [False, True, False,...]

        Returns: None

        """
        for i in range(len(values)):
            if values[i] == True:
                values[i] = 1
            elif values[i] == False:
                values[i] = 0
        self._set_values(values)

    def set_by_int(self, value):
        """
        Sends the int value to the internal function
            (int to binary)

        args: 1 --> 1
            0 --> 0
            12 --> 1100
            999 -- > 1111100111
            etc...

        Returns: None

        """
        self._set_values(list(bin(value)[2:]))

    def set_by_bool(self, value):
        """
        Sends the boolean value to the internal function

        args: True
            or
            False

        Returns: None

        """
        if value == True:
            self._set_values([1])
        elif value == False:
            self._set_values([0])

    def get_values(self):
        """
        Returns the values of the current 74HC595(s)

        args: None

        Returns: List of current state
            [0, 1, 0,...]

        """
        return self.current

    def clear(self):
        """
        Sets the 74HC595 back to all off

        Returns: None

        """
        self._set_values([0, 0, 0, 0, 0, 0, 0, 0] * self.daisy_chain)
