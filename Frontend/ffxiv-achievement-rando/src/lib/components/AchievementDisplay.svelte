<script lang="ts">
    import { Achievement } from '$lib/models/models';
    import { getCleanCategoryName } from '$lib/scripts/commonScripts';
    import AchievementIcon from '$lib/components/AchievementIcon.svelte';
    import AchievementReward from '$lib/components/AchievementReward.svelte';
    import '$lib/styles/achievementDisplay.scss';
    let {achievement} : { achievement: Achievement } = $props();

</script>

<section id="achievement-body">
    <div id="achievement-icon">
        <AchievementIcon icon_path={achievement.icon_path} achievement_name={achievement.name} />
    </div>
    <h2 id="achievement-name">{achievement.name}</h2>
    <h3 id="achievement-description">▶ {achievement.description}</h3>
    <div id="achievement-details">
        <div id="category">
            <strong>{getCleanCategoryName(achievement.category)}</strong>
        </div>
        <div id="reward">
            {#if achievement.item_reward || achievement.title.masculine_title || achievement.title.feminine_title}
                <AchievementReward achievement={achievement} />
            {/if}
        </div>
    </div>
</section>
