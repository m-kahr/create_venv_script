"""
Script create virtual environment and install required packages from requirements.txt

To manually create a virtual environment and install the required packages, follow these steps:
1. Open a terminal
>> python -m venv C:\path\to\new\virtual\environment

2. Activate the virtual environment
on windows:
>> C:\path\to\new\virtual\environment\Scripts\activate
on linux/mac:
>> source /path/to/new/virtual/environment/bin/activate

3. Install the required packages
>> pip install -r requirements.txt
or 
>> pip install package1 package2 package3 ...

4. Deactivate the virtual environment
>> deactivate
"""

from venv import create
import os
import platform
from subprocess import run

# set path and name of virtual environment
venv_name = ".venv"
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
venv_dir = os.path.join(script_dir, venv_name)

# create virtual environment if it does not exists
# NOTE: The virtual environment is created with the same Python version as the current interpreter
# NOTE: a requirments.txt file is used to install the required packages
if not os.path.isfile(os.path.join(venv_dir, "pyvenv.cfg")):
    print("Creating virtual environment: ", venv_dir)
    create(venv_dir, with_pip=True)

    # install packages from requirements.txt (if it exists)
    if not os.path.isfile("requirements.txt"):
        print("No requirements.txt file found")
    else:
        pip_executable = ""
        if platform.system() == "Windows":              # Windows operating systems
            pip_executable = os.path.join(venv_dir, "Scripts\\pip.exe")

        if platform.system() in ["Linux", "Darwin"]:    # Linux and MacOS operating systems
            pip_executable = os.path.join(venv_dir, "bin/pip")

        run([pip_executable, "install", "-r", os.path.join(script_dir, "requirements.txt")], cwd=venv_dir)

    

# print the command to activate the virtual environment (in shell)
activate_command = ""
if platform.system() == "Windows":
    activate_command = "source " + os.path.join(venv_dir, "Scripts", "activate")
if platform.system() in ["Linux", "Darwin"]:
    activate_command = "source " + os.path.join(venv_dir, "bin", "activate")
print(f"Activate the virtual environment with: {activate_command}")



"""
import os
import sys
import venv
from subprocess import run

# Define the directory for the virtual environment
venv_dir = os.path.join(os.getcwd(), '.venv')

# Create the virtual environment
if not os.path.isfile(os.path.join(os.getcwd(), venv_dir, "bin", "python")):
    venv.create(venv_dir, with_pip=True)
    run(["bin/pip", "install", "-r", os.path.abspath("requirements.txt")], cwd=dir)
    print(f"Virtual environment created at {venv_dir}")

# Activate the virtual environment
"""
