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
    
    with open("FFXIV_Achievement_Data.json", "w") as file:
        file.write(json.dumps(achievement_data))

def get_achievement_kind_from_string(category_string):
    kind = achievement_data_structs.AchievementKind.NONE
    match(category_string):
        case "Battle":
            kind = achievement_data_structs.AchievementKind.BATTLE
        case "PvP":
            kind = achievement_data_structs.AchievementKind.PVP
        case "Character":
            kind = achievement_data_structs.AchievementKind.CHARACTER
        case "Items":
            kind = achievement_data_structs.AchievementKind.ITEMS
        case "Crafting & Gathering" | "Gathering":
            kind = achievement_data_structs.AchievementKind.CRAFTING_AND_GATHERING
        case "Quests":
            kind = achievement_data_structs.AchievementKind.QUESTS
        case "Exploration":
            kind = achievement_data_structs.AchievementKind.EXPLORATION
        case "Grand Company":
            kind = achievement_data_structs.AchievementKind.GRAND_COMPANY
        case "Legacy":
            kind = achievement_data_structs.AchievementKind.LEGACY
    
    return kind

def read_achievement_data_from_file():
    file = open("FFXIV_Achievement_Data.json", "r")
    achievement_data = json.loads(file.read())
    achievement_list = []
    for achievement_id in achievement_data:
        entry_data = achievement_data[achievement_id]["fields"]

        achievement = achievement_data_structs.Achievement()
        achievement.id = achievement_id
        achievement.name = str(entry_data["Name"])
        achievement.description = str(entry_data["Description"])
        achievement.icon_path = str(entry_data["Icon"]["path_hr1"])
        achievement.category = get_achievement_kind_from_string(str(entry_data["AchievementCategory"]["fields"]["AchievementKind"]["fields"]["Name"]))
        achievement.hide_achievement = bool(entry_data["AchievementHideCondition"]["fields"]["HideAchievement"])
        achievement.item_reward = str(entry_data["Item"]["fields"]["Name"])
        
        title = achievement_data_structs.Title()
        title.feminine_title = str(entry_data["Title"]["fields"]["Feminine"])
        title.masculine_title = str(entry_data["Title"]["fields"]["Masculine"])
        title.is_prefix = bool(entry_data["Title"]["fields"]["IsPrefix"])

        achievement.title = title

        achievement_list.append(achievement)
    
    return achievement_list
