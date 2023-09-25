<script setup lang="ts">
import axios from 'axios';


const props = defineProps<{
    id: number
    title: string,
    address: string,
    date: string,
    technical: number,
    start_time: string,
    end_time: string
}>()

const technicalName = ref<string>('')

onMounted(async () => {
    console.log(getServerUrl() + '/technicals/' + props.technical + '/')
    await axios.get(getServerUrl() + '/technicals/' + props.technical + '/')
    .then((response) => {
        technicalName.value = response.data.name as string
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
        h-full w-full py-3 px-3 rounded-lg bg-slate-50
    ">
        <p class="font-bold text-lg truncate">{{ title }}</p>
        <div class="my-1">
            <p class="truncate">
                <Icon name="bi:geo-alt-fill" class="text-lg" />
                {{ address }}
            </p>
        </div>
        <div class="my-1 space-y-1">
            <p class="truncate">
                <Icon name="mdi:calendar" /> Data:
                {{ date }}
            </p>
            <p class="truncate">
                <Icon name="mdi:clock" /> Início:
                {{ start_time }}
            </p>
            <p class="truncate">
                <Icon name="mdi:clock" /> Fim:
                {{ end_time }}
            </p>
            <p class="truncate">
                <Icon name="mdi:worker" /> Técnico:
                {{ technicalName }}
            </p>
        </div>
        <div class="h-10 w-full flex justify-end space-x-2">
            <button class="flex items-center justify-center bg-emerald-400 rounded
                hover:bg-emerald-500 active:scale-95
                transition-all duration-150 w-10
            "
                @click="() => useRouter().push('/events/' + id + '/')"
            >
                <Icon name="mdi:pencil" />
            </button>
            <button class="flex items-center justify-center bg-red-400 rounded
                hover:bg-red-500 active:scale-95
                transition-all duration-150 w-10
            "
            @click="destroyEvent(props.id)"
            >
                <Icon name="mdi:trash" />
            </button>
        </div>
    </div>
</template>