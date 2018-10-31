# -*- coding: utf-8 -*-

"""Console script for south_park_downloader."""
import sys
import click
from south_park_downloader.south_park_downloader import download_episode, download_all_episodes


@click.command()
@click.option('--season', default='all', help='Season')
@click.option('--episode', default='all', help='Episode')
@click.option('--language', default='english', help='english|german')
def main(season, episode, language):
    """Console script for south_park_downloader."""
    click.echo("Downloading episode {} of season {}".format(episode, season))
    if season == 'all' and episode == 'all':
        download_all_episodes(language)
    else:
        download_episode(int(season), int(episode), language)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
