import sys

import click

from xctools_kamaalio.list_utils import removed, find_index
from xctools_kamaalio.xctools import XcTools


ACTIONS = ["archive"]


def cli():
    action_index = find_index(sys.argv, lambda arg: arg in ACTIONS)
    if action_index is None:
        raise CLIException("Invalid action provided")

    action = sys.argv[action_index]
    sys.argv = removed(sys.argv, action_index)
    if action == "archive":
        archive()


@click.command(context_settings={"ignore_unknown_options": True})
@click.option(
    "--configuration",
    type=click.Choice(["Debug", "Release"], case_sensitive=False),
    required=True,
)
@click.option("--scheme", required=True)
@click.option("--destination", required=True)
@click.option(
    "--sdk",
    type=click.Choice(["iphoneos", "macosx"], case_sensitive=False),
    required=True,
)
@click.option("--archive-path", required=True)
@click.option("--project")
@click.option("--workspace")
def archive(configuration, scheme, destination, sdk, archive_path, project, workspace):
    xctools = XcTools()
    status = xctools.archive(
        scheme=scheme,
        configuration=configuration,
        destination=destination,
        sdk=sdk,
        archive_path=archive_path,
        project=project,
        workspace=workspace,
    )
    print(status)


class CLIException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
