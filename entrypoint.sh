#!/bin/sh

set -e

# Print the Python version
python --version

# Print environment variables
echo "Environment Variables:"
env

# Run the Python script
exec python main.py
