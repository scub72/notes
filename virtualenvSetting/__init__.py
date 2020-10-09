import os
from sys import platform

def createVirtualEnv():
    """
    1. Creating virtual environment
              python3 -m venv ./venv                   "./venv" -> path to virtual environment catalogue
    2. Activating virtual environment:
              source ./venv/bin/activate
    3. Installing "pipenv" for dependencies control and automatic libraries installation
        (pipenv creates catalogues Pipfile i Pipfile.lock)
              pip3 install pipenv
    4. Next packages we install with:
              pipenv install <package_name>
    """

    if platform == "linux" or platform == "linux2":
        """ Setting linux virtual environment"""
        try:
            os.system('python3 -m venv ./venv')
            print('=> venv catalogue created')

            os.system('source ./venv/bin/activate')
            print('=> virtual environment activated')

            os.system('pip3 install pipenv')
            print('=> pipenv installed')

            print('\n\tNow you should install files with "pipenv install <package_name>"'
                  '\n\tThe virtual environment is set.\n')
        finally:
            print('Probably you should install python3-venv.')

    elif platform == "darwin":
        """ Setting OSX virtual environment"""
        pass # here should be osx command

    elif platform == "win32":
        """ Setting Windows virtual environment"""
        pass  # here should be osx command

    else:
        print("OS cannot be recognized")
