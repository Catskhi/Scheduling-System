<script setup lang="ts">

const route = useRoute()

</script>

<template>

<EventsForm
method="Edit"
:event_id="parseInt(route.params.id as string)"
/>

</template>