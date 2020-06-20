from riotwatcher import LolWatcher, ApiError
import os

lol_watcher = LolWatcher(os.getenv('API_KEY'))

my_region = 'kr'

me = lol_watcher.summoner.by_name(my_region, 'DWG ShowMaker')
print(me)

# all objects are returned (by default) as a dict
# lets see if i got diamond yet (i probably didnt)
my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
print(my_ranked_stats)

my_matches = lol_watcher.match.matchlist_by_account(my_region, me['accountId'])
# print(my_matches)

# fetch last match detail
last_match = my_matches['matches'][0]
match_detail = lol_watcher.match.by_id(my_region, last_match['gameId'])
print(match_detail)

# First we get the latest version of the game from data dragon
# versions = lol_watcher.data_dragon.versions_for_region(my_region)
# champions_version = versions['n']['champion']

# Lets get some champions
# current_champ_list = lol_watcher.data_dragon.champions(champions_version)
# print(current_champ_list)

