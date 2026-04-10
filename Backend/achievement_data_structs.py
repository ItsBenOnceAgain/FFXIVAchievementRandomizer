from enum import Enum

class AchievementKind(Enum):
    NONE = 1
    BATTLE = 2
    PVP = 3
    CHARACTER = 4
    ITEMS = 5
    CRAFTING_AND_GATHERING = 6
    QUESTS = 7
    EXPLORATION = 8
    GRAND_COMPANY = 9
    LEGACY = 10
    SEASONAL = 11

class Title:
    feminine_title = ""
    masculine_title = ""
    is_prefix = False

    def __str__(self):
        return_string = self.feminine_title
        if not return_string:
            return_string = "None"
        elif self.feminine_title != self.masculine_title:
            return_string = self.feminine_title + "/" + self.masculine_title
        return return_string

class Achievement:
    id = 0
    name = "None"
    description = "None"
    category = AchievementKind.NONE
    hide_achievement = False
    points = 0
    icon_path = "None"
    item_reward = "None"
    item_icon_path = "None"
    title = Title()

class FilterSettings:
    allow_legacy_achievements = False
    allow_empty_achievements = False
    allow_seasonal_achievements = False
    blacklisted_achievement_ids = []