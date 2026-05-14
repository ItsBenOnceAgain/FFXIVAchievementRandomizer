from enum import StrEnum
from pydantic import BaseModel

class AchievementKind(StrEnum):
    NONE = "None"
    BATTLE = "Battle"
    PVP = "PvP"
    CHARACTER = "Character"
    ITEMS = "Items"
    CRAFTING_AND_GATHERING = "Crafting & Gathering"
    QUESTS = "Quests"
    EXPLORATION = "Exploration"
    GRAND_COMPANY = "Grand Company"
    LEGACY = "Legacy"
    SEASONAL = "Seasonal"

class Title(BaseModel):
    feminine_title: str = ""
    masculine_title: str = ""
    is_prefix: bool = False

    def __str__(self):
        return_string = self.feminine_title
        if not return_string:
            return_string = "None"
        elif self.feminine_title != self.masculine_title:
            return_string = self.feminine_title + "/" + self.masculine_title
        return return_string

class Achievement(BaseModel):
    id: int = 0
    name: str = "None"
    description: str = "None"
    category: AchievementKind = AchievementKind.NONE
    hide_achievement: bool = False
    points: int = 0
    icon_path: str = "None"
    item_reward: str = "None"
    item_icon_path: str = "None"
    title: Title = Title()

class FilterSettings:
    allow_empty_achievements = False
    allowed_categories = []
    blacklisted_achievement_ids = []

class CategoryFormatException(Exception):
    pass