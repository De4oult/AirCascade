import server.server as server
import client.repo   as repo

import click

@click.group()
@click.pass_context
def cli(context):
    context.ensure_object(dict)


@cli.command()
def init() -> None:
    repo.initialize()

@cli.command()
def declarate() -> None:
    repo.declarate()

@cli.command()
@click.argument('files')
def add(files: str) -> None:
    repo.add(files)

@cli.command()
@click.argument('label')
def label(label: str) -> None:
    repo.label(label)

@cli.command()
def send() -> None:
    repo.send()

@cli.command()
def configure() -> None:
    repo.configure()


if __name__ == '__main__':
    cli(obj = {})