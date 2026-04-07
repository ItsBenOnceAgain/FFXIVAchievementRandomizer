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

def write_data_to_file_from_server():
    achievement_data = {}
    last_row_fround = 0
    more_rows = True

    while(more_rows):
        achievement_block = get_achievements(last_row_fround)
        if(len(achievement_block['rows']) > 0):
            print("Found achievement block " + str(last_row_fround) + "!")
            for row in achievement_block['rows']:  
                row_id = row["row_id"]
                print("Getting detailed data for achievement " + str(row_id) + "...")
                achievement_data[row_id] = get_detailed_achievement_data(row_id)
                last_row_fround = row_id
        else:
            print("Final block reached, ending!")
            more_rows = False
    
    with open("AchievementData/FFXIV_Achievement_Data.json", "w") as file:
        file.write(json.dumps(achievement_data))
