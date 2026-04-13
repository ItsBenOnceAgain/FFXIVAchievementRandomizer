export function getCleanCategoryName(rawCategory: string): string {
    let cleanCategory = "None";
    switch(rawCategory) {
        case "BATTLE":
            cleanCategory = "Battle";
            break;
        case "PVP":
            cleanCategory = "PvP";
            break;
        case "CHARACTER":
            cleanCategory = "Character";
            break;
        case "ITEMS":
            cleanCategory = "Items";
            break;
        case "CRAFTING_AND_GATHERING":
            cleanCategory = "Crafting & Gathering";
            break;
        case "QUESTS":
            cleanCategory = "Quests";
            break;
        case "EXPLORATION":
            cleanCategory = "Exploration";
            break;
        case "GRAND_COMPANY":
            cleanCategory = "Grand Company";
            break;
        case "LEGACY":
            cleanCategory = "Legacy";
            break;
        case "SEASONAL":
            cleanCategory = "Seasonal";
            break;
        default:
            cleanCategory = "None";
    }
    return cleanCategory;
}