import subprocess
from typing import Literal, overload


Configuration = Literal["Debug", "Release"]
SDK = Literal["macosx", "iphoneos"]


class XcTools:
    def __init__(self) -> None:
        pass

    @overload
    def archive(
        self,
        scheme: str,
        configuration: Configuration,
        destination: str,
        sdk: SDK,
        archive_path: str,
        project: str,
    ):
        ...

    @overload
    def archive(
        self,
        scheme: str,
        configuration: Configuration,
        destination: str,
        sdk: SDK,
        archive_path: str,
        workspace: str,
    ):
        ...

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

        print(command)
        # subprocess.Popen


class XcToolsException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
