<script lang="ts">
    import { Achievement } from '$lib/models/models';
    import AchievementIcon from '$lib/components/AchievementIcon.svelte';
    import AchievementCategory from '$lib/components/AchievementCategory.svelte';
    import AchievementReward from '$lib/components/AchievementReward.svelte';
    import '$lib/styles/achievementDisplay.scss';
    let {achievement} : { achievement: Achievement } = $props();

</script>

<section class="achievement-body">
    <div class="achievement-icon">
        <AchievementIcon icon_path={achievement.icon_path} achievement_name={achievement.name} />
    </div>
    <h2 class="achievement-name">{achievement.name}</h2>
    <h3 class="achievement-description">▶ {achievement.description}</h3>
    <div class="reward">
        {#if achievement.item_reward || achievement.title.masculine_title || achievement.title.feminine_title}
            <AchievementReward achievement={achievement} />
        {/if}
    </div>
    <div class="category">
        <AchievementCategory category_name={achievement.category} />
    </div>
    
</section>
