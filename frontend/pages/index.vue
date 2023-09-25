<script setup lang="ts">
import { getIsLogged, userData } from '~/utils/AuthUtils';
import { eventData, getAllEvents } from '~/utils/EventsUtils';

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
<div class="bg-gradient-cyan  w-full h-full fixed pointer-events-none">

</div>
<main class="absolute w-full h-full">
    <h1 class="text-center text-3xl font-bold mt-10 text-white">
        Eventos Criados
    </h1>
    <div class="flex items-center justify-center space-x-3">
        <button class="shadow-[0_3px_10px_rgb(0,0,0,0.2)] bg-white px-10 py-1 rounded 
            flex items-center justify-center text-lg mt-7
            hover:scale-95 active:scale-90 transition-all duration-150
        "
        @click="async () => await useRouter().push('/events/create/')"
        >
            Criar Evento <Icon name="ic:baseline-plus" class="ml-3" />
        </button> 
        <button 
            v-if="userData?.user_type === 1"
            class="shadow-[0_3px_10px_rgb(0,0,0,0.2)] bg-white px-10 py-1 rounded
            flex items-center justify-center text-lg mt-7
            hover:scale-95 active:scale-90 transition-all duration-150
        "
        @click="useRouter().push('/editados/')"
        >
            Ver Eventos Editados <Icon name="mdi:eye" class="ml-3" />
        </button>   
    </div>
    <div v-if="allEvents"
    class="mt-10 grid grid-cols-3 items-center justify-center px-5 gap-x-5 gap-y-5 mb-10">
        <EventsCard v-for="event in allEvents" 
        :key="event.id"
        :id="event.id"
        :title="event.title"
        :address="event.address"
        :technical="event.technical"
        :date="event.date"
        :start_time="event.start_time"
        :end_time="event.end_time"
        />
    </div>
</main>
</template>