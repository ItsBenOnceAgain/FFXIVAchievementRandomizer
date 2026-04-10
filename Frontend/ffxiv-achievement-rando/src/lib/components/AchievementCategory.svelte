<script lang="ts">
    import '$lib/styles/achievementCategory.scss';
    import categoryBackground from '$lib/assets/achievementCategoryBackground.png';
    let {category_name} : { category_name: string } = $props();

    function getCleanCategoryName(rawCategory: string): string {
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
</script>

<div class="category-wrapper">
    <img class="category-background-image" src={categoryBackground} alt={"Category Background"}/>
    <h2 class="category-name">{getCleanCategoryName(category_name)}</h2>
</div>