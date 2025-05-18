set export

default:
  just --list

build-and-upload: build upload

build:
    #!/bin/bash

    rm -rf dist
    . .venv/bin/activate
    just install-self
    python3 -m build

upload: build
    #!/bin/bash

    . .venv/bin/activate
    twine upload dist/* --verbose

test: install-self
    #!/bin/bash

    . .venv/bin/activate
    pytest

install-self:
    #!/bin/bash

    . .venv/bin/activate
    pip install -e .

init-venv:
    #!/bin/bash

    python3 -m venv .venv
    . .venv/bin/activate
    just install-deps

install-deps:
    #!/bin/bash

    . .venv/bin/activate
    pip install -r requirements.txt

check-if-tag-exists:
    #!/bin/bash

    . scripts/utils.bash

    new_release_tag=$(extract_tag_from_release_branch)

    version_pattern="^[0-9]+\.[0-9]+\.[0-9]+$"
    if [[ ! $new_release_tag =~ $version_pattern ]]
    then
        echo "Invalid version as a release"
        exit 41
    fi

    git fetch
    tags=$(git tag)
    for tag in $tags
    do
        if [ $tag = $new_release_tag ]
        then
            echo "Tag already exists"
            exit 69
        fi
    done
