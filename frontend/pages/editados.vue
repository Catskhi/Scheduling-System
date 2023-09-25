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
}

const isLogged = ref<boolean>(false)
const userData = ref<userData>()
const editedEvents = ref<editedEventData[]>([])

onBeforeMount(async () => {
    isLogged.value = await getIsLogged()
    if (!isLogged.value) {
        useRouter().push('login/')
    }
    userData.value = await getUserData()
    if (userData.value?.user_type !== 1) {
        useRouter().push('/')
    }
    await axios.get(getServerUrl() + '/changes/')
    .then((response) => {
        editedEvents.value = response.data
    })
    
})

const getTechnicalName = async (id: number) => {
    let name:string = ''
    await axios.get(getServerUrl() + '/technicals/' + id + '/')
    .then(response => {
        console.log(response.data)
        name = response.data.name
    })
    .catch(error => {
        console.log(error)
    })
    return name
}

</script>

<template>
<div class="bg-gradient-cyan  w-full h-full fixed pointer-events-none">

</div>
<main class="absolute h-full w-full">
    <h1 class="text-center text-3xl font-bold mt-10 text-white">
        Eventos Editados
    </h1>
    <div class="mt-10 grid grid-cols-3 items-center justify-center px-5 gap-x-5 gap-y-5 mb-10">
        <div v-for="event in editedEvents" class="shadow-[0_3px_10px_rgb(0,0,0,0.2)]
        h-full w-full py-3 px-3 rounded-lg bg-slate-50">
            <div>
                <p class="font-bold">Antes</p>
                <p><strong>Título: </strong>{{ event.old_title }}</p>
                <p><strong>Endereço: </strong>{{ event.old_address }}</p>
                <p><strong>Descrição: </strong>{{ event.old_description }}</p>
                <p><strong>Técnico: </strong>{{ getTechnicalName(event.old_technical) }}</p>
            </div>
        </div>
    </div>
</main>
</template>

<style scoped>

p {
    @apply truncate;
}

</style>