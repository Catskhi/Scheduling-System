<script setup lang="ts">
import { getIsLogged, userData } from '~/utils/AuthUtils';
import { eventData, getAllEvents } from '~/utils/EventsUtils';

definePageMeta({
    layout: 'events'
})

const isLogged = ref<boolean>(false)
const pageLoading = ref<boolean>(true)
const allEvents = ref<eventData[] | null>(null)

const userData = ref<userData>()

onBeforeMount(async () => {
    isLogged.value = await getIsLogged()
    if (!isLogged.value) {
        useRouter().push('login/')
    }
    allEvents.value = await getAllEvents()
    userData.value = await getUserData()
    pageLoading.value = false
})

</script>

<template>
<CustomLoading :is-loading="pageLoading" />
<main class="absolute w-full h-full">
    <div v-if="allEvents"
    class="mt-10 grid grid-cols-1 items-center justify-center px-5 gap-x-5 gap-y-5 mb-10">
        <EventsCard v-for="event in allEvents" 
        :key="event.id"
        :id="event.id"
        :title="event.title"
        :address="event.address"
        :technical="event.technical"
        :description="event.description"
        :date="event.date"
        :start_time="event.start_time"
        :end_time="event.end_time"
        />
    </div>
</main>
</template>