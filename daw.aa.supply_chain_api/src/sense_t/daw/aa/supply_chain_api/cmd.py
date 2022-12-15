import pathlib
import click
from .config import load_config, config


@click.group()
@click.option('--config',
              '-c',
              '_config',
              envvar='DAW_CONFIG',
              type=pathlib.Path,
              default='config.yml')
def cli(_config=None):
    load_config(_config)


@cli.command()
@click.option('--days', '-d', type=int, default=30)
def jwt(days):
    from .auth import generateToken
    click.echo(f'JWT: {generateToken(days)}')


@cli.command()
def start():
    import uvicorn
    from .api import app
    uvicorn.run(app, **config.get('api', {}))