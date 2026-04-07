import json
import achievement_data_structs

def read_achievement_data_from_file():
    file = open("Backend\\AchievementData\\FFXIV_Achievement_Data.json", "r")
    achievement_data = json.loads(file.read())
    achievement_list = {}
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

        achievement_list[achievement_id] = achievement
    
    return achievement_list

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

def display_achievement(achievement_id, data):
    """Display achievement data for the given ID."""
    if achievement_id in data:
        achievement = data[achievement_id]
        print(f"\n--- Achievement ID: {achievement_id} ---")
        print(f"Name: {achievement.name}")
        print(f"Description: {achievement.description}")
        print(f"Category: {achievement.category.name}")
        print(f"Hidden: {'Yes' if achievement.hide_achievement else 'No'}")
        print(f"Item Reward: {achievement.item_reward}")
        print(f"Title: {achievement.title}")
        print()
    else:
        print(f"\nAchievement ID '{achievement_id}' not found.\n")

def get_achievement_object_from_id(achievement_id, data):
    """Return an achievement object for the given ID."""
    if achievement_id in data:
        achievement_data = data[achievement_id]
        fields = achievement_data.get('fields', {})
        
        achievement = {
            'id': achievement_id,
            'name': fields.get('Name', 'N/A'),
            'description': fields.get('Description', 'N/A'),
            'icon': fields.get('Icon', 'N/A'),
            'category': fields.get('AchievementKind', 'N/A')
        }
        return achievement
    else:
        print(f"Achievement ID '{achievement_id}' not found.")
        return None

def main():
    """Main console loop."""
    print("=== FFXIV Achievement Lookup ===")
    print("Type 'exit' to quit.\n")
    
    data = read_achievement_data_from_file()
    if data is None:
        return
    
    while True:
        try:
            user_input = input("Enter achievement ID: ").strip()
            
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            
            if not user_input:
                print("Please enter a valid ID.\n")
                continue
            
            display_achievement(user_input, data)
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()
