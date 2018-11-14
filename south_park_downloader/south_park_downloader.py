# !/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
South Park Downloader.

A module to scrape videos from southpark.de or southpark.cc.com
"""

from __future__ import unicode_literals
import os
import json
import glob
import logging
import shutil
import youtube_dl

logger = logging.getLogger(__file__)


def download_all_episodes(language, basepath):
    """Download all episodes from all seasons."""
    database_path = os.path.join(os.path.dirname(__file__), 'seasons.json')
    with open(database_path) as f:
        db = json.load(f)
    for season_dict in db["seasons"]:
        season = int(season_dict["season"])
        for episode in range(1, int(season_dict["episodes"]) + 1):
            download_episode(season, episode, language, basepath)


def download_episode(season, episode, language, basepath):
    """Download an episode from a season."""
    ep_string = "s{:02}e{:02}".format(season, episode)
    logger.info("Downloading {} in {}".format(ep_string, language))
    if language == 'german':
        url = "http://www.southpark.de/alle-episoden/{}"
    elif language == 'english':
        url = "https://southpark.cc.com/full-episodes/{}"
    else:
        logger.warn("Unsupported language: {}".format(language))
    season_dir = "Season {}".format(season)
    season_path = os.path.join(basepath, "South Park", season_dir)
    if not os.path.exists(season_path):
        os.makedirs(season_path)

    # Download the raw episode
    ydl_opts = {'outtmpl': 'raw/%(title)s.%(ext)s'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url.format(ep_string)])
        except AttributeError as err:
            logger.error("Episode unavailable.")

    # Merge its acts
    part_list = glob.glob('raw/*.mp4')
    episode_title = part_list[0].split(" - ")[1]
    input_file_name = 'files.txt'
    with open(input_file_name, 'a') as f:
        for part in sorted(part_list):
            f.write("file '" + part + '\'\n')
    cmd = "ffmpeg -f concat -safe 0 -i {} -c copy \"{}/South Park - S{:02}E{:02} - {}.mp4\"".format(input_file_name, season_path, season, episode, episode_title)
    os.system(cmd)

    # Clean up
    if os.path.exists(input_file_name):
        os.remove(input_file_name)
    if os.path.exists("raw") and os.path.isdir("raw"):
        shutil.rmtree("raw")
