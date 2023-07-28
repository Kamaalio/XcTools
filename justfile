set export

init-venv:
    python3 -m venv .venv
    . .venv/bin/activate
    pip install poetry
    poetry install
