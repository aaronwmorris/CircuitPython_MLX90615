Introduction
============

CircuitPython module for the Melexis MLX90615 Contact-less Infrared Temperature sensor.  See
examples/mlx90615_simpletest.py for a demo of the usage.

This repository is copied from Adafruit's MLX90614 repo with the addresses and registers
updated for the MLX90615.  https://github.com/adafruit/Adafruit_CircuitPython_MLX90614

References to the MLX90614 are still scattered through this repository.


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
====================

.. code-block:: shell

    pip3 install "git+https://github.com/aaronwmorris/CircuitPython_MLX90615.git"

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install "git+https://github.com/aaronwmorris/CircuitPython_MLX90615.git"

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install "git+https://github.com/aaronwmorris/CircuitPython_MLX90615.git"

Usage Example
=============

See examples/mlx90615_simpletest.py for a demo of the usage.

Documentation
=============

API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/mlx90614/en/latest/>`_.

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/adafruit_CircuitPython_MLX90614/blob/main/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
