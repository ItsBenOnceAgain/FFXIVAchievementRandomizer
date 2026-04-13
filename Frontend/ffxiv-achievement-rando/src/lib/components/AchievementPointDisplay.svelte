<script lang="ts">
    import '$lib/styles/achievementPointDisplay.scss';
    let {achievementPoints} : { achievementPoints: number } = $props();

    function getProperAchievementClass(points: number) : string {
        let returnClass = "";

        switch(points){
            case 0:
                returnClass = "pointCounterZero";
                break;
            case 5:
                returnClass = "pointCounterOne";
                break;
            case 10:
                returnClass = "pointCounterTwo";
                break;
            default:
                returnClass = "pointCounterThree";
                break;
        }

        return returnClass;
    }

</script>

<div id="achievementPointCounter" class={getProperAchievementClass(achievementPoints)}>
    <div id="pointHolder">
        {achievementPoints}
    </div>
</div>