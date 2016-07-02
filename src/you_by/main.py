# -*- coding:utf-8 -*-

import click
from bypy import ByPy

@click.group()
@click.option("-d", "--debug", count=True, help="set debugging level (-dd to increase debugging level, -ddd to enable HTPP traffic debugging as well (very talkative)) [default: %(default)s]")
@click.option("-v", "--verbose", count=True, help="set verbosity level [default: %(default)s]")
@click.pass_context
def cli(ctx, debug, verbose):
    ctx.obj = ByPy(debug=debug, verbose=verbose)


@cli.command()
@click.argument('localdir', default='')
@click.argument('remotedir', default='')
@click.argument('deleteremote', default='')
@click.pass_context
def syncup(ctx, localdir, remotedir, deleteremote):
    pcs = ctx.obj
    pcs.syncup(localdir, remotedir, deleteremote)


if __name__ == '__main__':
    cli(obj={})
