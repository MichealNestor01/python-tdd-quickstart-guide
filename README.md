# Quickstart guide for TDD and Python 

I have made this to help people quickly get going with python TDD (I made this after seeing people struggle to get started at community events). 

## Installation of required programs

- VSCODE: An amazing and simple IDE, [Download here](https://code.visualstudio.com/download) and install.

- Python: [Download here](https://www.python.org/downloads/)
**IMPORTANT: On windows,when installing python ensure you tick the box that sais "add to PATH" if you do not the rest won't work. If you previously forgot to do this, the easiest fix is to uninstall python and reinstall.**

- Git Bash: Version controll software that will allow you to download this code, [Download here](https://git-scm.com/download/win)

## Setup 

1. Open file explorer and create a folder where you want to store your python programs
2. Open this folder
3. Right click anywhere in this folder and click start git bash (wording might differ slightly) 
4. Copy this code into the terminal that opens and type this: 
    ```
    git clone https://github.com/MichealNestor01/python-tdd-quickstart-guide.git
    ```
5. This should copy all of the code in this repository to a new folder called python-tdd-quickstart-guide. (You can rename this)
6. Open the python-tdd-quickstart-guide folder.
7. Right click here and click open in vscode, if this option isnt available, open vscode normally, click file, open folder, then open the python-tdd-quickstart-guide folder. 
8. Now in vscode, click terminal at the top, and click new terminal. A terminal should now show at the bottom
9. In the terminal type:
    ```
    python -m venv .env
    ```
    this will create a "virtual environment" called ".env", this directory will store all the python libraries you use. You can give this any name you want but .env or .venv is most common.
10. Now you need to activate the environment:
    - Windows:
        ```
        .env/Scripts/activate
        ```
    - Linux:
        ```
        source env/bin/activate
        ```
    You need to activate this environment every time you reopen your project (Though this may happen automatically).
11. If you need to install libraries you can now do:
    ```
    pip install <library here>
    ```
    Try to install the numpy library to test this. Then run pip list to check it is installed:
    ```
    pip list
    ```
