<script lang="ts">
    import '$lib/styles/achievementCategoryOption.scss';
    import { getCleanCategoryName } from '$lib/scripts/commonScripts';
    import categoryBackground from '$lib/assets/achievementCategoryBackground.png';

    let {category_name} : { category_name: string } = $props();
</script>

<div class="category-wrapper">
    <img class="category-background-image" src={categoryBackground} alt={"Category Background"}/>
    <h2 class="category-name">{getCleanCategoryName(category_name)}</h2>
</div>