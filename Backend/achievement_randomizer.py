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
        filter_settings = achievement_data_structs.FilterSettings()
    if filter_settings.allow_empty_achievements == False and (value.name == "None" or value.name.strip() == ""):
        is_valid = False
    if value.category.value not in filter_settings.allowed_categories:
        is_valid = False
    if key in filter_settings.blacklisted_achievement_ids:
        is_valid = False
    return is_valid

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
    update_achievement_data()

def update_achievement_data():
    data = achievement_file_manager.read_achievement_data_from_file()
    achievement_file_manager.write_simple_achievement_data_to_file(data)

if __name__ == "__main__":
    main()
