import click


@click.command(context_settings={"ignore_unknown_options": True})
@click.option("--archive-path", required=True)
@click.option("--export-options", required=True)
def export_archive(archive_path, export_options):
    print(archive_path, export_options)
