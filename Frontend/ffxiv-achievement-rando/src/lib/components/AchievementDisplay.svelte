<script lang="ts">
    import { Achievement } from '$lib/models/models';

    let base_icon_url = "https://v2.xivapi.com/api/asset?format=webp&path="
    let {achievement} : { achievement: Achievement } = $props();

</script>

<section>
    <h2>Random Achievement</h2>
    <img src={base_icon_url +achievement.icon_path} alt={achievement.name} width="64" height="64" />
    <p><strong>Name:</strong> {achievement.name}</p>
    <p><strong>Description:</strong> {achievement.description}</p>
    <p><strong>Category:</strong> {achievement.category}</p>
    {#if achievement.item_reward}
        <p><strong>Item Reward:</strong> {achievement.item_reward}</p>
    {/if}

    {#if achievement.title.feminine_title || achievement.title.masculine_title}
        <p><strong>Title Reward:</strong> 
            {#if achievement.title.feminine_title === achievement.title.masculine_title}
                {achievement.title.feminine_title}
            {:else}
                {achievement.title.feminine_title} / {achievement.title.masculine_title}
            {/if}
        </p>
    {/if}
</section>