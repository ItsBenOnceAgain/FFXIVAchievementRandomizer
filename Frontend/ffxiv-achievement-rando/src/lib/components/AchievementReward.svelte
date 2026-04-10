<script lang="ts">
import { Achievement } from '$lib/models/models';
    import '$lib/styles/achievementReward.scss';
    import rewardBackground from '$lib/assets/achievementRewardBackground.png';
    import itemIcon from '$lib/assets/itemIcon.png';
    import titleIcon from '$lib/assets/titleIcon.png';
    let {achievement} : { achievement: Achievement } = $props();
</script>

<div class="reward-wrapper">
    <img class="reward-background-image" src={rewardBackground} alt={"Reward Background"}/>
    <div id="base-reward-text">
        <p><strong><em>REWARD</em></strong></p>
    </div>
    <div class="reward-icon">
        {#if achievement.item_reward}
            <img src={itemIcon} alt={"Item Reward Icon"}/>
        {:else if achievement.title.masculine_title || achievement.title.feminine_title}
            <img src={titleIcon} alt={"Title Reward Icon"}/>
        {/if}
    </div>
    <div class="reward-details">
        {#if achievement.item_reward}
            <h4>{achievement.item_reward}</h4>
        {:else if achievement.title.masculine_title || achievement.title.feminine_title}
            <h4>{achievement.title.toString()}</h4>
        {/if}
    </div>
</div>