# SPDX-FileCopyrightText: 2018 Mikey Sklar for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`aaronwmorris_mlx90615`
====================================================

CircuitPython module for the MLX90615 IR object temperature sensor.

* Author(s): Mikey Sklar based on code from these projects:
  Limor Fried - https://github.com/adafruit/Adafruit-MLX90614-Library
  Bill Simpson - https://github.com/BillSimpson/ada_mlx90614
  Mike Causer - https://github.com/mcauser/micropython-mlx90614

Implementation Notes
--------------------

**Hardware:**

* Adafruit does not currently offer this sensor

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads
"""

from adafruit_bus_device import i2c_device
from micropython import const

try:
    from busio import I2C
except ImportError:
    pass

# imports

__version__ = "0.0.1"
__repo__ = "https://github.com/aaronwmorris/CircuitPython_mlx90615.git"

# Internal constants:
_MLX90615_I2CADDR = const(0x5B)

# RAM
_MLX90615_TA = const(0x06)
_MLX90615_TO = const(0x07)


class MLX90615:
    """Create an instance of the MLX90615 temperature sensor.

    :param ~busio.I2C i2c_bus: The I2C bus the MLX90615 is connected to.
                               Do not use an I2C bus speed of 400kHz. The sensor only works
                               at the default bus speed of 100kHz.
    :param int address: I2C device address. Defaults to :const:`0x5B`.

    **Quickstart: Importing and using the MLX90615**

        Here is an example of using the :class:`MLX90615` class.
        First you will need to import the libraries to use the sensor

        .. code-block:: python

            import board
            import aaronwmorris_mlx90615

        Once this is done you can define your `board.I2C` object and define your sensor object

        .. code-block:: python

            i2c = board.I2C()
            mlx = aaronwmorris_mlx90615.MLX90615(i2c)

        Now you have access to the :attr:`ambient_temperature` attribute

        .. code-block:: python

            temperature = mlx.ambient_temperature

    """

    def __init__(self, i2c_bus: I2C, address: int = _MLX90615_I2CADDR) -> None:
        self._device = i2c_device.I2CDevice(i2c_bus, address)
        self.buf = bytearray(2)

    @property
    def ambient_temperature(self) -> float:
        """Ambient Temperature in Celsius."""
        return self._read_temp(_MLX90615_TA)

    @property
    def object_temperature(self) -> float:
        """Object Temperature in Celsius."""
        return self._read_temp(_MLX90615_TO)

    def _read_temp(self, register: int) -> float:
        temp = self._read_16(register)
        temp *= 0.02
        temp -= 273.15
        return temp

    def _read_16(self, register: int) -> int:
        # Read and return a 16-bit unsigned big endian value read from the
        # specified 16-bit register address.
        with self._device as i2c:
            self.buf[0] = register
            i2c.write_then_readinto(self.buf, self.buf, out_end=1)
            return self.buf[1] << 8 | self.buf[0]
