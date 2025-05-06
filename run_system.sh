#!/bin/bash

# Activate the virtual environment
source .venv/bin/activate

# Run launch.py in the background using nohup
nohup python3 launch.py &