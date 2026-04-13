<script lang="ts">
    import '$lib/styles/advancedOptions.scss';
    import optionIcon from "$lib/assets/optionIcon.png";

    let {show_options = $bindable(false)} : {show_options: boolean} = $props();

    function toggleOptionState(){
        show_options = !show_options;
        if(show_options){
            toggleOpen();
        }
        else {
            toggleClosed();
        }
    }

    function toggleOpen() {
        let icon = document.getElementById("advanced-options-icon");
        if(icon){
            icon.style.transform = "rotate(90deg)";
        }
    }

    function toggleClosed() {
        let icon = document.getElementById("advanced-options-icon");
        if(icon){
            icon.style.transform = "rotate(0deg)";
        }
    }

</script>

<div id="advanced-options-header">
    <button id="option-toggle-button" onclick={toggleOptionState}>
        <!-- svelte-ignore hydration_attribute_changed -->
        <img src="{optionIcon}" alt="advanced options icon" id="advanced-options-icon"/>
    </button>
    <div id="advanced-options-text">
        ADVANCED OPTIONS
    </div>
</div>