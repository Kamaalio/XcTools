from pathlib import Path
from dataclasses import dataclass


class VersionBumber:
    def __init__(self) -> None:
        pass

    @classmethod
    def bump(cls, build_number: int | None, version_number: str | None):
        project_configuration_file = cls.__get_project_configuration_file()
        if not project_configuration_file:
            raise VersionBumberException("No project path found")

        has_changes = cls.__edit_numbers(
            build_number=build_number,
            version_number=version_number,
            project_configuration_file=project_configuration_file,
        )
        if has_changes:
            print("Applied changes to xcode project")
        else:
            print("No changes where needed")

    @classmethod
    def __edit_numbers(
        cls,
        build_number: int | None,
        version_number: str | None,
        project_configuration_file: Path,
    ):
        if build_number is None and version_number is None:
            return False

        project_configuration_file_lines = (
            project_configuration_file.read_text().splitlines()
        )
        has_changes = False
        for line_number, line in enumerate(project_configuration_file_lines):
            line = XcodeProjectConfigurationLine(line=line)
            if not line.is_build_number and not line.is_version_number:
                continue

            if build_number is not None and line.is_build_number:
                line.update_build_number(new_build_number=build_number)
                project_configuration_file_lines[line_number] = line.line
                has_changes = True
            elif version_number is not None and line.is_version_number:
                line.update_version_number(new_version_number=version_number)
                project_configuration_file_lines[line_number] = line.line
                has_changes = True

        if not has_changes:
            return False

        if len(project_configuration_file_lines[-1]) != 0:
            project_configuration_file_lines.append("")

        project_configuration_file.write_text(
            "\n".join(project_configuration_file_lines)
        )
        return True

    @staticmethod
    def __get_project_configuration_file():
        for path in Path.cwd().glob("**/*"):
            if path.name == "project.pbxproj":
                return path


@dataclass
class XcodeProjectConfigurationLine:
    XCODE_BUILD_NUMBER_KEY = "CURRENT_PROJECT_VERSION"
    XCODE_VERSION_NUMBER_KEY = "MARKETING_VERSION"

    line: str

    @property
    def amount_of_tabs(self):
        return self.line.count("\t")

    @property
    def is_build_number(self):
        return self.XCODE_BUILD_NUMBER_KEY in self.line

    @property
    def is_version_number(self):
        return self.XCODE_VERSION_NUMBER_KEY in self.line

    def update_build_number(self, new_build_number: int):
        assert self.is_build_number
        self.__update_line(key=self.XCODE_BUILD_NUMBER_KEY, value=new_build_number)

    def update_version_number(self, new_version_number: int):
        assert self.is_version_number
        self.__update_line(key=self.XCODE_VERSION_NUMBER_KEY, value=new_version_number)

    def __update_line(self, key: str, value: int):
        tabs = "\t" * self.amount_of_tabs
        self.line = f"{tabs}{key} = {value};"


class VersionBumberException(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
