# -*- coding: utf-8 -*-

"""Console script for south_park_downloader."""
import sys
import click
from pathlib import Path
from south_park_downloader.south_park_downloader import download_episode, download_all_episodes


@click.command()
@click.option('--season', default='all', help='Season')
@click.option('--episode', default='all', help='Episode')
@click.option('--language', default='english', help='english|german')
@click.option('--basepath', default='~', help='Basepath under which the South Park directory structure will be created')
def main(season, episode, language, basepath):
    """Console script for south_park_downloader."""
    if basepath == "~":
        basepath = str(Path.home())
    click.echo("Downloading episode {} of season {}".format(episode, season))
    if season == 'all' and episode == 'all':
        download_all_episodes(language, basepath)
    else:
        download_episode(int(season), int(episode), language, basepath)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
