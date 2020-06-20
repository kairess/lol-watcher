from riotwatcher import LolWatcher
from datetime import datetime, timedelta
import time

lol_watcher = LolWatcher('RGAPI-d74ed218-6659-457b-933f-0e25b4c0b346')

my_region = 'kr'

me = lol_watcher.summoner.by_name(my_region, '파 월')

spectator = None

while True:
    print('[*] Checking...', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    try:
        spectator = lol_watcher.spectator.by_summoner(my_region, me['id'])

        start_time = datetime.fromtimestamp(spectator['gameStartTime'] / 1000)

        if datetime.now() - start_time < timedelta(minutes=5):
            print('[!] My son is playing LoL!', start_time.strftime('%Y-%m-%d %H:%M:%S'))
    except:
        pass

    time.sleep(5)