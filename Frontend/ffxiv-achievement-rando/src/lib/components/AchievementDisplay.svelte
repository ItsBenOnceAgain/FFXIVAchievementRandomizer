<script lang="ts">
    import { Achievement } from '$lib/models/models';
    import { getCleanCategoryName } from '$lib/scripts/commonScripts';
    import AchievementIcon from '$lib/components/AchievementIcon.svelte';
    import AchievementReward from '$lib/components/AchievementReward.svelte';
    import AchievementPointDisplay from '$lib/components/AchievementPointDisplay.svelte';
    import '$lib/styles/achievementDisplay.scss';
    let {achievement} : { achievement: Achievement } = $props();

</script>

<section id="achievement-body">
    <div id="achievement-icon">
        <AchievementIcon icon_path={achievement.icon_path} achievement_name={achievement.name} />
    </div>
    <h2 id="achievement-name">{achievement.name}</h2>
    <h4 id="achievement-description">▶ {achievement.description}</h4>
    <div id="achievement-points">
        <AchievementPointDisplay achievementPoints={achievement.points} />
    </div>
    <div id="achievement-details">
        <div id="category">
            <strong>{getCleanCategoryName(achievement.category)}</strong>
        </div>
        <div id="reward">
            <AchievementReward achievement={achievement} />
        </div>
    </div>
</section>
