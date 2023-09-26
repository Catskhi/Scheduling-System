<script setup lang="ts">
import axios from 'axios';


const props = defineProps<{
    id: number
    title: string,
    address: string,
    date: string,
    technical: number,
    description: string
    start_time: string,
    end_time: string
}>()

const technical_name = ref<string>('')
const formatted_date = computed((): string => {
    return props.date.split('-').reverse().join('/')
})

onMounted(async () => {
    console.log(getServerUrl() + '/technicals/' + props.technical + '/')
    await axios.get(getServerUrl() + '/technicals/' + props.technical + '/')
    .then((response) => {
        technical_name.value = response.data.name as string
    })
    .catch((error) => {
        console.log(error.response.data)
    })
})

const destroyEvent = async (eventId: number) => {
    await axios.delete(getServerUrl() + '/events/' + eventId + '/', {
        headers: {
                Authorization: `Bearer ${localStorage.getItem('token')}`
        }  
    })
    .then((response) => {
        console.log(response)
    })
    .catch((error) => {
        console.log(error.response.data)
    })
    location.reload()
}

</script>

<template>
    <div class="shadow-[0_3px_10px_rgb(0,0,0,0.2)]
        h-full w-full py-3 px-3 rounded-lg bg-slate-50 pb-5
        border-2
    ">
        <p>
            <Icon name="mdi:calendar" class="text-lg" /> 
            <span class="ml-1 opacity-75 font-semibold">
                {{ formatted_date }}
            </span>
            <Icon name="mdi:clock" class="ml-3 text-lg" />
            <span class="ml-1 opacity-75 font-semibold">
                {{ start_time }} - {{ end_time }}
            </span>
        </p>
        <p class="font-bold text-xl truncate mt-3">{{ title }}</p>
        <p class="font-light mt-1 ml-1">{{ description }}</p>
        <hr class="mt-5 mb-3" />
        <div class="grid grid-cols-2 justify-items-stretch">
            <div>
                <p class="space-x-3">
                    <span><Icon name="mdi:location" /> {{ address }}</span>
                </p>
                <p>
                    <span><Icon name="mdi:worker" /> {{ technical_name }}</span>
                </p>
            </div>
            <div class="flex space-x-3 justify-self-end mr-3 mt-3">
                <button class="flex items-center justify-center bg-blue-600 rounded
                    hover:bg-blue-700 hover:scale-95 active:scale-90
                    transition-all duration-150 w-full h-8 px-3 text-white
                "
                    @click="() => useRouter().push('/events/' + id + '/')"
                >
                    <Icon name="mdi:pencil" class="mr-1" /> Editar
                </button>
                <button class="flex items-center justify-center bg-red-500 rounded
                    hover:bg-red-600 hover:scale-95 active:scale-90 text-white
                    transition-all duration-150 w-full h-8 px-2
                "
                @click="destroyEvent(props.id)"
                >
                    <Icon name="mdi:trash" class="mr-1" /> Deletar
                </button>
            </div>
        </div>
    </div>
</template>

<style scoped>

p {
    @apply truncate;
}

</style>