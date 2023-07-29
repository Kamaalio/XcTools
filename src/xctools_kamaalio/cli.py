import click

from xctools_kamaalio.xctools import XcTools


@click.command(context_settings={"ignore_unknown_options": True})
@click.option("--action", type=click.Choice(["archive"], case_sensitive=False))
def cli(action):
    xctools = XcTools()
    if action == "archive":
        xctools.archive(
            scheme="UnixTime (iOS)",
            configuration="Release",
            destination="platform=iOS",
            sdk="iphoneos",
            archive_path="EpochStamp.xcarchive",
            project="UnixTime.xcodeproj",
        )
        return
