<script setup lang="ts">
import axios from 'axios';


interface editedEventData extends eventData {
    edited_by: number
    owner: number
    old_title: string
    old_address: string
    old_technical: number
    old_description: string
    old_date: string
    old_start_time: string
    old_end_time: string

    new_title: string
    new_address: string
    new_technical: number
    new_description: string
    new_date: string
    new_start_time: string
    new_end_time: string
}

const isLogged = ref<boolean>(false)
const userData = ref<userData>()
const editedEvents = ref<editedEventData[]>([])

const pageLoading = ref<boolean>(true)

onBeforeMount(async () => {
    isLogged.value = await getIsLogged()
    if (!isLogged.value) {
        useRouter().push('/login/')
    }
    userData.value = await getUserData()
    if (userData.value?.user_type != 1) {
        useRouter().push('/')
    }
    await axios.get(getServerUrl() + '/changes/')
    .then((response) => {
        editedEvents.value = response.data
    })
    pageLoading.value = false
})

</script>

<template>
<CustomLoading :is-loading="pageLoading" />
<main class="h-full w-full">
    <h1 class="text-center text-3xl font-bold mt-10 text-black">
        Eventos Editados
    </h1>
    <div class="mt-10 grid grid-cols-3 items-center justify-center px-5 gap-x-5 gap-y-5 mb-10">
        <div v-for="event in editedEvents">
            <EventsEditedCard 
            :owner="event.owner"
            :edited_by="event.edited_by"

            :old_title="event.old_title"
            :old_address="event.old_address"
            :old_technical="event.old_technical"
            :old_description="event.old_description"
            :old_date="event.old_date"
            :old_start_time="event.old_start_time"
            :old_end_time="event.old_end_time"

            :new_title="event.new_title"
            :new_address="event.new_address"
            :new_technical="event.new_technical"
            :new_description="event.new_description"
            :new_date="event.new_date"
            :new_start_time="event.new_start_time"
            :new_end_time="event.new_end_time"
            />
        </div>
    </div>
</main>
</template>

<style scoped>

p {
    @apply truncate;
}

</style>