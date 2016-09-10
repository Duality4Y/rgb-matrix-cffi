# rpi-matrix-cffi

this project creates c bindings with cffi for python using this library: https://github.com/hzeller/rpi-rgb-led-matrix/,<br>

the goal to be able to use pypy's optimazations, to speed up
python code running on a raspberry pi.

# Installing
make sure your pypy version is 5.0 or higher.
and make sure you have libcffi5 installed.
clone this repo, enter it and then type:
```
    git submodule init
    git submodule update
```
enter the matrix folder and compile:
```
    cd matrix/
    make
```

there is no way to install the code yet. future work wil be done on
making it pip installable.

this code is not tested with any other interpreter besides pypy.
