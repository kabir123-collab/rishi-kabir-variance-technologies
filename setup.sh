#!/bin/bash

# Install virtualenv if it's not installed
sudo apt install python3-venv

# Create a virtual environment named .venv
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install the required dependencies from requirements.txt
pip install -r requirements.txt

# Print done message
echo "Done Setup"
