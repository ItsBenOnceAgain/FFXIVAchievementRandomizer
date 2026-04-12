<script>
    import { Achievement, Title } from '$lib/models/models';
    import AchievementDisplay from '$lib/components/AchievementDisplay.svelte';
    import AchievementCategoryOption from '$lib/components/AchievementCategoryOption.svelte';
    import '$lib/styles/randomizer.scss';

    let achievement = $state(new Achievement());
    let loading = $state(false);
    let errorMessage = $state("");
    let baseAPIURL = 'http://localhost:5000';
    let baseAPIEndpoint = 'random_achievement';

    // Category option states
    let battleChecked = $state(true);
    let pvpChecked = $state(true);
    let characterChecked = $state(true);
    let itemsChecked = $state(true);
    let craftingChecked = $state(true);
    let questsChecked = $state(true);
    let explorationChecked = $state(true);
    let grandCompanyChecked = $state(true);
    let legacyChecked = $state(false);
    let seasonalChecked = $state(false);

    let selectedCategoryValues = $derived([
        battleChecked ? 2 : null,
        pvpChecked ? 3 : null,
        characterChecked ? 4 : null,
        itemsChecked ? 5 : null,
        craftingChecked ? 6 : null,
        questsChecked ? 7 : null,
        explorationChecked ? 8 : null,
        grandCompanyChecked ? 9 : null,
        legacyChecked ? 10 : null,
        seasonalChecked ? 11 : null,
    ].filter(v => v !== null));

    function generateButtonIsDisabled() {
        return selectedCategoryValues.length == 0 || loading
    }

    async function fetchRandomAchievement() {
        loading = true;
        errorMessage = "";
        let categoryFilter = `allowed_categories=${selectedCategoryValues.join(',')}`;
        let apiEndpoint = `${baseAPIURL}/${baseAPIEndpoint}?${categoryFilter}`;

        try {
            const response = await fetch(apiEndpoint);
            if (!response.ok) {
                throw new Error(`Request failed with status ${response.status}`);
            }

            const data = await response.json();
            achievement = new Achievement();
            achievement.id = data.id;
            achievement.name = data.name;
            achievement.description = data.description;
            achievement.icon_path = data.icon_path;
            achievement.category = data.category._name_;
            achievement.hide_achievement = data.hide_achievement;
            achievement.item_reward = data.item_reward;
            achievement.item_icon_path = data.item_icon_path;
            achievement.points = data.points;
            achievement.title = new Title();
            achievement.title.feminine_title = data.title.feminine_title;
            achievement.title.masculine_title = data.title.masculine_title;
            achievement.title.is_prefix = data.title.is_prefix;

        } catch (error) {
            errorMessage = error instanceof Error ? error.message : String(error);
            achievement = new Achievement();
        } finally {
            loading = false;
        }
    }
</script>

<div id="randomizer-grid">
    <div id="randomizer-options">
        <button id="randomizer-button" onclick={fetchRandomAchievement} disabled={generateButtonIsDisabled()}>
            {#if loading}
                Loading...
            {:else}
                Generate!
            {/if}
        </button>
        <div id="options-header">
            OPTIONS
        </div>
        <div class="option"><AchievementCategoryOption category_name="BATTLE" bind:is_checked={battleChecked}/></div>
        <div class="option"><AchievementCategoryOption category_name="PVP" bind:is_checked={pvpChecked}/></div>
        <div class="option"><AchievementCategoryOption category_name="CHARACTER" bind:is_checked={characterChecked}/></div>
        <div class="option"><AchievementCategoryOption category_name="ITEMS" bind:is_checked={itemsChecked}/></div>
        <div class="option"><AchievementCategoryOption category_name="CRAFTING_AND_GATHERING" bind:is_checked={craftingChecked}/></div>
        <div class="option"><AchievementCategoryOption category_name="QUESTS" bind:is_checked={questsChecked}/></div>
        <div class="option"><AchievementCategoryOption category_name="EXPLORATION" bind:is_checked={explorationChecked}/></div>
        <div class="option"><AchievementCategoryOption category_name="GRAND_COMPANY" bind:is_checked={grandCompanyChecked}/></div>
        <div class="option"><AchievementCategoryOption category_name="LEGACY" bind:is_checked={legacyChecked}/></div>
        <div class="option"><AchievementCategoryOption category_name="SEASONAL" bind:is_checked={seasonalChecked}/></div>
    </div>

    <div id="achievement-display">
        <div id="achievement-display-header">
            Achievement Details
        </div>
        {#if achievement.id !== 0}
            <AchievementDisplay {achievement} />
        {/if}

        {#if errorMessage}
            <p class="error">{errorMessage}</p>
        {/if}
    </div>
</div>

