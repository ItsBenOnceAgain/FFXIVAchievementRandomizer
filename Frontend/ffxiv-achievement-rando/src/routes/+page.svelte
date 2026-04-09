<script lang="ts">
    class Achievement {
        id: number = 0;
        name: string = "";
        description: string = "";
        icon_path: string = "";
        category: string = "";
        hide_achievement: boolean = false;
        item_reward: string = "";
        title: Title = new Title();
    }

    class Title {
        feminine_title: string = "";
        masculine_title: string = "";
        is_prefix: boolean = false;
    }

    let achievement = $state(new Achievement());
    let loading = $state(false);
    let errorMessage = $state("");
    let base_icon_url = "https://v2.xivapi.com/api/asset?format=webp&path="

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

<h1 class="final-fantasy-text">Welcome to the FFXIV Achievement Randomizer Tool</h1>
<p>This tool picks a random achievement in FFXIV for you to prioritize.</p>

<button on:click={fetchRandomAchievement} disabled={loading}>
    {#if loading}
        Loading...
    {:else}
        Get Random Achievement
    {/if}
</button>

{#if errorMessage}
    <p class="error">{errorMessage}</p>
{/if}

{#if achievement.id !== 0}
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
{/if}
