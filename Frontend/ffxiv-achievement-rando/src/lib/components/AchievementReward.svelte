<script lang="ts">
    import { Achievement } from '$lib/models/models';
    import '$lib/styles/achievementReward.scss';
    import rewardBackground from '$lib/assets/achievementRewardBackground.png';
    import titleIcon from '$lib/assets/titleIcon.png';
    let {achievement} : { achievement: Achievement } = $props();
</script>

<div id="reward-wrapper">
    {#if achievement.item_reward || achievement.title.masculine_title || achievement.title.feminine_title}
        <img id="reward-background-image" src={rewardBackground} alt={"Reward Background"}/>
        <div id="base-reward-text">
            <p><strong><em>REWARD</em></strong></p>
        </div>
        <div id="reward-icon">
            {#if achievement.item_reward}
                <img src={"https://v2.xivapi.com/api/asset?format=webp&path=" + achievement.item_icon_path} alt={achievement.item_reward}/>
            {:else if achievement.title.masculine_title || achievement.title.feminine_title}
                <img src={titleIcon} alt={"Title Reward Icon"}/>
            {/if}
        </div>
        <div id="reward-details">
            {#if achievement.item_reward}
                <strong>{achievement.item_reward}</strong>
            {:else if achievement.title.masculine_title || achievement.title.feminine_title}
                <strong>{achievement.title.toString()}</strong>
            {/if}
        </div>
    {/if}
</div>