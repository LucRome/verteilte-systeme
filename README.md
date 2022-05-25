# Geburtstags-Namens-Datenbank

# Setup
- Go to `src` folder and run:
    ```
    python -m venv .venv
    ```
- After creating the virtual environment enter it:
    - Windows: `.venv\Scripts\activate.bat`
    - Unix: `source .venv/bin/activate`
- Install the dependencies:
    - `pip install -r requirements.txt`

# Running the App
- Requirements: Visual-Studio-Code (mit Python-Plugin)

- Open this Folder in VSCode
- Most times the VSCode Tasks can be used
    - Before being able to use them:
        - `F1` -> `Python: Select interpreter` -> Select the interpreter from the virtual Environment

- Database migration:
    - VSCode Task: 
        1. `F1` -> `Tasks: Run Task` -> `Run Makemigrations`
        2. `F1` -> `Tasks: Run Task` -> `Run Migrate`
    - Commandline:
        ```
        cd ./src
        py ./manage.py makemigrations birthday_db
        py ./manage.py migrate
        ```
- Add Test-Persons (optional)
    - VSCode Tasks:
        1. `F1` -> `Tasks: Run Task` -> `Run Add Persons`
- Run Server:
    - VSCode Tasks:
        1. `F1` -> `Tasks: Run Task` -> `Run Server`
- Open Website:
    - [Link](http://127.0.0.1:8000/)
