<script lang="ts">
    import '$lib/styles/achievementCategoryOption.scss';
    import { getCleanCategoryName } from '$lib/scripts/commonScripts';

    let {category_name, is_checked = $bindable(false)} : {category_name: string, is_checked: boolean} = $props();
</script>

<div class="flex-category-wrapper">
    <div class="category-wrapper">
        <input class="category-checkbox" type="checkbox" bind:checked={is_checked} />
        <div class="category-name"><strong>{getCleanCategoryName(category_name)}</strong></div>
    </div>
</div>
