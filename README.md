
PyArduinoProxy now is py-arduino
================================

I've renamed the project to **py-arduino**, please check it out at:

[https://github.com/hgdeoro/py-arduino](https://github.com/hgdeoro/py-arduino "https://github.com/hgdeoro/py-arduino")

I didn't like the 'proxy' word in its name, and made big changes, including:

- refactored `low level` code to the new `py_arduino` package
- refactores `web application stuff` to `py_arduino_web` package
- add multiprocess support + background tasks, aka: concurrent access (thanks to uWSGI + PyRO)
- labeling of pins and restricted acces from web (administrable using Django)
- cleaned up old code (like old examples) and an updated README
