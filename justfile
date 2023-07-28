set export

build:
    rm -rf dist
    . .venv/bin/activate
    python3 -m build

upload:
    . .venv/bin/activate
    twine upload dist/*

init-venv:
    python3 -m venv .venv
    . .venv/bin/activate
    pip install -r requirements.txt
