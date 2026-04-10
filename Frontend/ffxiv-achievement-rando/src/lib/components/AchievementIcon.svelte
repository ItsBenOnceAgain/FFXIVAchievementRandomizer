<script lang="ts">
    import '../styles/achievementIcon.scss';
    import iconWrapper from '../assets/achievementIconWrapper.png';
    let base_icon_url = "https://v2.xivapi.com/api/asset?format=webp&path="
    let {icon_path, achievement_name} : { icon_path: string, achievement_name: string } = $props();
</script>

<div class="icon-wrapper">
    <img class="overlay base-icon" src={base_icon_url +icon_path} alt={achievement_name}/>
    <img class="overlay" src={iconWrapper} alt="icon wrapper" width="90" height="90"/>
</div>