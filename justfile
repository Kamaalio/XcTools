set export

build:
    . .venv/bin/activate
    echo "y" | pyinstaller main.py

init-venv:
    python3 -m venv .venv
    . .venv/bin/activate
    pip install poetry
    poetry install
