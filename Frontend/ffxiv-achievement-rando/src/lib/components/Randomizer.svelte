<script>
    import { Achievement, Title } from '$lib/models/models';
    import AchievementDisplay from '$lib/components/AchievementDisplay.svelte';
    import '$lib/styles/randomizer.scss';

    let achievement = $state(new Achievement());
    let loading = $state(false);
    let errorMessage = $state("");
    let allow_legacy = $state(false);
    let allow_seasonal = $state(false);

    async function fetchRandomAchievement() {
        loading = true;
        errorMessage = "";
        try {
            const response = await fetch('http://localhost:5000/random_achievement');
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
        <button id="randomizer-button" onclick={fetchRandomAchievement} disabled={loading}>
            {#if loading}
                Loading...
            {:else}
                Generate!
            {/if}
        </button>
        <div id="options-header">
            OPTIONS
        </div>
        <div class="option"><input type="checkbox" bind:checked={allow_legacy} />Allow Legacy Achievements</div>
        <div class="option"><input type="checkbox" bind:checked={allow_seasonal} />Allow Seasonal Achievements</div>
    </div>

    {#if errorMessage}
        <p class="error">{errorMessage}</p>
    {/if}

    {#if achievement.id !== 0}
        <div id="achievement-display">
            <div id="achievement-display-header">
                Achievement Details
            </div>
            <AchievementDisplay {achievement} />
        </div>
    {/if}
</div>

