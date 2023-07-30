import sys


from xctools_kamaalio.list_utils import removed, find_index
from xctools_kamaalio.actions.upload import upload
from xctools_kamaalio.actions.archive import archive
from xctools_kamaalio.actions.bump_version import bump_version
from xctools_kamaalio.actions.export_archive import export_archive


ACTIONS = ["archive", "upload", "bump-version", "export-archive"]


def cli():
    action_index = find_index(sys.argv, lambda arg: arg in ACTIONS)
    if action_index is None:
        raise CLIException("Invalid action provided")

    action = sys.argv[action_index]
    sys.argv = removed(sys.argv, action_index)

    if action == "archive":
        archive()
    if action == "upload":
        upload()
    if action == "bump-version":
        bump_version()
    if action == "export-archive":
        export_archive()


class CLIException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
