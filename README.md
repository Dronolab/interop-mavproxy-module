# interop-mavproxy-module
Forward mavlink packets through UDP using json format

## Install

1. Put `mavproxy_interop.py` file in your MAVProxy module directory.
2. After MAVProxy is started, you have to load the plugin using `module load interop` command.

## Development

Each modification to the module will require a recompile operation of MAVProxy:

`python setup.py build install --user`

