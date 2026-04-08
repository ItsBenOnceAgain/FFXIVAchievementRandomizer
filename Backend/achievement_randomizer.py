import json
import achievement_data_structs
import achievement_file_manager

def filter_out_bad_achievements(data, filter_settings: achievement_data_structs.FilterSettings):
    filtered_data = dict(filter(lambda x: achievement_filter(x, filter_settings), data.items()))
    return filtered_data

def achievement_filter(key_value_pair, filter_settings: achievement_data_structs.FilterSettings):
    key, value = key_value_pair
    is_valid = True
    if not filter_settings:
        filter_settings
    if filter_settings.allow_empty_achievements == False and (value.name == "None" or value.name.strip() == ""):
        is_valid = False
    if filter_settings.allow_legacy_achievements == False and value.category == achievement_data_structs.AchievementKind.LEGACY:
        is_valid = False
    if key in filter_settings.blacklisted_achievement_ids:
        is_valid = False
    return is_valid

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

# def main():
#     """Main console loop."""
#     print("=== FFXIV Achievement Lookup ===")
#     print("Loading Achievement Data...")
#     data = achievement_file_manager.read_simple_achievement_data_from_file()
#     data = filter_out_bad_achievements(data)
#     print("Data loaded!")
#     print("Type 'exit' to quit.\n")
    
    
#     if data is None:
#         print("Failed to load achievement data. Exiting.")
#         return
    
#     while True:
#         try:
#             user_input = input("Enter achievement ID: ").strip()
            
#             if user_input.lower() == 'exit':
#                 print("Goodbye!")
#                 break
            
#             if not user_input:
#                 print("Please enter a valid ID.\n")
#                 continue
            
#             display_achievement(user_input, data)
            
#         except KeyboardInterrupt:
#             print("\n\nGoodbye!")
#             break
#         except Exception as e:
#             print(f"Error: {e}\n")

# if __name__ == "__main__":
#     main()
