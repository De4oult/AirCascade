import server.server as server
import client.repo   as repo

import click

@click.group()
@click.pass_context
def cli(context):
    context.ensure_object(dict)

@cli.command()
def configure() -> None:
    repo.configure()

@cli.command()
def run() -> None:
    server.run()



if __name__ == '__main__':
    cli(obj = {})