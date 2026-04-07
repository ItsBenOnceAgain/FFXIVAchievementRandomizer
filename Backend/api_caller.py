import requests
import json
import achievement_data_structs

base_achievement_url = "https://v2.xivapi.com/api/sheet/Achievement"

def get_achievements(after = 0):
    full_url = base_achievement_url + "?after=" + str(after) + "&limit=100"

    response = requests.get(full_url)

    return response.json()

def get_detailed_achievement_data(achievementId):
    full_url = base_achievement_url + "/" + str(achievementId)

    response = requests.get(full_url)

    return response.json()
