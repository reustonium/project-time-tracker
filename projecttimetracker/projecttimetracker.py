# -*- coding: utf-8 -*-
import click


@click.command()
@click.version_option()
def cli():
    click.echo('hiya')
