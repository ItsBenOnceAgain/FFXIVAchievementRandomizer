<script lang="ts">
    import Randomizer from "$lib/components/Randomizer.svelte";
    import AchievementHeader from "$lib/components/AchievementHeader.svelte";
    import '$lib/styles/mainPage.scss';

</script>
<div id="main-page-scaler">
    <div id="main-page-wrapper">
        <div id="main-page-header-wrapper">
            <div id="main-page-header">
                <AchievementHeader />
            </div>
        </div>
        <div id="main-page-content-wrapper">
            <div id="main-page-content">
                <Randomizer />
            </div>
        </div>
    </div>
</div>

