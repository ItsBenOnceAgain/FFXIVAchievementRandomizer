<script lang="ts">
    import '$lib/styles/placeholderAchievementDisplay.scss';

    import moogle from '$lib/assets/mailMoogleStatic.png';

</script>

<section id="placeholder-achievement-body">
    <div id="dialogue-box-wrapper">
        <div id="moogle-static-container">
            <img id="moogle-static" src={moogle} alt="mail moogle" />
        </div>
        <div id="dialogue-box">
            <p id="dialogue-text">Hey there! Click the button below and I'll fetch a random achievement for you, kupo!</p>
        </div>
    </div>
</section>
