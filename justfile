set export

default:
  just --list

build-and-upload: build upload

run:
    . .venv/bin/activate
    python3 -c "from src.xctools_kamaalio.cli import cli; cli()" --action archive

build:
    rm -rf dist
    . .venv/bin/activate
    python3 -m build

upload:
    . .venv/bin/activate
    twine upload dist/*

install-self:
    . .venv/bin/activate
    pip install -e .

init-venv:
    python3 -m venv .venv
    . .venv/bin/activate
    pip install -r requirements.txt
