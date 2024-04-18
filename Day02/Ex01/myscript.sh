#!/bin/bash

# Display the pip version
pip_version=$(pip --version)
echo "Using pip version: $pip_version"

# Define the directory to install the library
install_dir="local_lib"

# Remove the existing local_lib directory if it exists
if [ -d "$install_dir" ]; then
    echo "Removing existing $install_dir directory..."
    rm -rf "$install_dir"
fi

# Install the path.py development version from its GitHub repo
echo "Installing path.py from GitHub repo..."
pip install git+https://github.com/jaraco/path.py.git --target="$install_dir" > install.log 2>&1

# Check if installation was successful
if [ $? -eq 0 ]; then
    echo "Installation successful."
    # Execute the Python program
    python program.py
else
    echo "Installation failed. Check install.log for details."
fi

