from datetime import datetime, timedelta
from crontab import CronTab
from tvmaze.api import Api

"""
A scheduler to schedule the download of the next south park episode.
"""

api = Api()
cron = CronTab(user=True)


episodes = api.show.episodes(112)

for episode in episodes:
    airdate = datetime.fromisoformat(episode.airdate)
    now = datetime.now()
    if airdate > now:
        # only schedule next episode
        job = cron.new(command='/usr/local/bin/south_park_downloader --season {} --episode {}'.format(episode.season, episode.number), comment="Scheduled download of episode {}".format(episode.name))
        job.setall(airdate)
        cron.write()
        break
