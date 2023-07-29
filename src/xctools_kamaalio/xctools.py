import subprocess
from typing import Literal


Configuration = Literal["Debug", "Release"]
SDK = Literal["macosx", "iphoneos"]


class XcTools:
    def __init__(self) -> None:
        pass

    def archive(
        self,
        scheme: str,
        configuration: Configuration,
        destination: str,
        sdk: SDK,
        archive_path: str,
        **kwargs,
    ):
        command = [
            "zsh",
            "-c",
            f'xcodebuild archive -scheme "{scheme}" -configuration {configuration}'
            + f'-destination "{destination}" -sdk {sdk} -archivePath "{archive_path}"',
        ]

        if project := kwargs.get("project"):
            command[-1] += f' -project "{project}"'
        elif workspace := kwargs.get("workspace"):
            command[-1] += f' -workspace "{workspace}"'
        else:
            raise XcToolsException("No workspace or project provided")

        status = subprocess.Popen(command).wait()
        if status != 0:
            raise XcToolsException(f"Failed command with status='{status}'")


class XcToolsException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
