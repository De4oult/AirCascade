import server.server as server
import client.repo   as repo

import click

@click.group()
@click.pass_context
def cli(context):
    context.ensure_object(dict)


@cli.command()
def declarate() -> None:
    repo.declarate()

@cli.command()
def init() -> None:
    repo.initialize()

@cli.command()
@click.argument('label')
def label(label: str) -> None:
    repo.label(label)

@cli.command()
def deliver() -> None:
    repo.deliver()

@cli.command()
@click.argument('label')
def fast(label: str) -> None:
    repo.fast_delivery(label)

@cli.command()
def drop() -> None:
    repo.drop()

@cli.command()
def configure() -> None:
    repo.configure()


if __name__ == '__main__':
    cli(obj = {})