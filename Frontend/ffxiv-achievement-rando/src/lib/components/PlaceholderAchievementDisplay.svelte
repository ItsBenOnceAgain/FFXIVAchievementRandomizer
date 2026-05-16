<script lang="ts">
    import '$lib/styles/placeholderAchievementDisplay.scss';

    import moogle from '$lib/assets/mailMoogleStatic.png';
    import moogleLoading from '$lib/assets/mailMoogle.gif';

    let {is_reroll, is_loading} : {is_reroll: boolean, is_loading: boolean } = $props();
</script>

<section id="placeholder-achievement-body">
    <div id="dialogue-box-wrapper">
        {#if !is_reroll}
        <div id="moogle-static-container">
            <img id="moogle" class="{is_loading ? 'moogle-leaving' : 'moogle-floating'}" src={moogle} alt="mail moogle" />
        </div>
        <div id="dialogue-box" class="{is_loading ? 'fade-out' : ''}">
            <p id="dialogue-text">Hey there! Click the button below and I'll fetch a random achievement for you, kupo!</p>
        </div>
        {/if}
        {#if is_loading}
        <div id="moogle-loading-container" class="fade-in">
            <img id="moogle-loading" class="{is_loading ? 'fade-in' : ''}" src={moogleLoading} alt="mail moogle loading" />
        </div>
        {/if}
    </div>
</section>
