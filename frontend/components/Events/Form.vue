<script setup lang="ts">
import axios from 'axios';
import { userData } from '~/utils/AuthUtils';
import { getAllTechnicals } from '~/utils/EventsUtils';

interface old_props {
    title: string
    address: string
    technical: number
    description: string
    date: string
    start_time: string
    end_time: string
}

const props = defineProps<{
    event_id?: number
    old_props?: old_props
    method: 'Create' | 'Edit'
}>()

const title = ref<string>('')
const address = ref<string>('')
const technical = ref<number>()
const description = ref<string>('')
const date = ref<string>('')
const start_time = ref<string>('')
const end_time = ref<string>('')

const allTechnicals = ref<technicalData[]>([])

const loadingFormAction = ref<boolean>(false)
const isLogged = ref<boolean>(false)
const userData = ref<userData | undefined>()
const old_event_data = ref<eventData>()

const edit_mode = ref<boolean>(false)

onBeforeMount(async () => {
    isLogged.value = await getIsLogged()
    if (!isLogged.value) {
        useRouter().push('/login/')
    }
})

onMounted(async () => {
    allTechnicals.value = await getAllTechnicals()
    userData.value = await getUserData()
    if (props.method === 'Edit') {
        edit_mode.value = true
        old_event_data.value = await getEventData(props.event_id as number)
        if(!old_event_data.value) {
            await useRouter().push('/')
        } else {
            title.value = old_event_data.value.title,
            address.value = old_event_data.value.address,
            technical.value = old_event_data.value.technical,
            description.value = old_event_data.value.description,
            date.value = old_event_data.value.date,
            start_time.value = old_event_data.value.start_time,
            end_time.value = old_event_data.value.end_time
        }
    }
})

const performFormAction = async () => {
    loadingFormAction.value = true
    if (props.method === 'Create') {
        await axios.post(getServerUrl() + '/events/', {
            title: title.value,
            address: address.value,
            owner: userData.value?.id,
            technical: technical.value,
            description: description.value,
            date: date.value,
            start_time: start_time.value,
            end_time: end_time.value
        }, 
        {
            headers: {
                Authorization: `Bearer ${localStorage.getItem('token')}`
            }
        })
        .then((response) => {
            console.log(response.data)
        })
        .catch((error) => {
            console.log(error.response.data)
        }) 
    } else if (props.method === 'Edit') {
        await axios.put(getServerUrl() + '/events/' + props.event_id + '/', {
            title: title.value,
            address: address.value,
            owner: userData.value?.id,
            technical: technical.value,
            description: description.value,
            date: date.value,
            start_time: start_time.value,
            end_time: end_time.value
        },
        {
            headers: {
                Authorization: `Bearer ${localStorage.getItem('token')}`
            }  
        })
        .then((response) => {
            console.log(response.data)
        })
        .catch((error) => {
            console.log(error.response.data)
        }) 
    }
    loadingFormAction.value = false
    useRouter().push('/')
}

</script>

<template>
<main class="absolute w-full h-full bg-gradient-cyan flex items-center justify-center">
    <div class="shadow-[0_3px_10px_rgb(0,0,0,0.2)] w-3/4 h-[95%] lg:w-1/3 bg-white rounded">
        <form class="px-10 flex flex-col">
            <h1 class="text-center mt-7 text-2xl font-bold">
                {{ method == 'Create' ? 'Criar' : 'Editar' }} Evento
            </h1>
            <label for="title">
                Título
            </label>
            <input v-model="title" id="title" type="text" placeholder="Título do evento" required
            class="border-2 focus:outline-none focus:ring-2 ring-cyan-400
                        transition-all duration-300 rounded px-3 py-1"
            />
            <label for="address">
                Endereço
            </label>
            <input v-model="address" id="address" type="text" placeholder="Endereço do Evento" required
            class="border-2 focus:outline-none focus:ring-2 ring-cyan-400
                        transition-all duration-300 rounded px-3 py-1"
            />
            <label for="technical">
                Técnico
            </label>
            <select v-model="technical" id="technical"
                class="bg-white border-2 px-3 py-2 rounded cursor-pointer"
            >
                <option v-for="technical in allTechnicals"
                    :value="technical.id"
                >
                    {{ technical.name }}
                </option>
            </select>
            <label for="description">
                Descrição
            </label>
            <textarea id="description" v-model="description" placeholder="Descrição do evento" required
                class="border-2 focus:outline-none focus:ring-2 ring-cyan-400
                        transition-all duration-300 rounded px-3 py-1 resize-none h-36">

            </textarea>
            <label for="date">
                Data
            </label>
            <input type="date" id="date" v-model="date" required
                class="border-2 focus:outline-none focus:ring-2 ring-cyan-400
                        transition-all duration-300 rounded px-3 py-1"
            />
            <label for="start_time">
                Início
            </label>
            <input type="time" id="start_time" v-model="start_time" required
                class="border-2 focus:outline-none focus:ring-2 ring-cyan-400
                        transition-all duration-300 rounded px-3 py-1s"
            />  
            <label for="end_time">
                Fim
            </label>
            <input type="time" id="end_time" v-model="end_time" required
                class="border-2 focus:outline-none focus:ring-2 ring-cyan-400
                        transition-all duration-300 rounded px-3 py-1s"
            />  
            <button type="button" class="bg-cyan-500 text-white font-bold mt-5 py-2 rounded
                hover:bg-cyan-600 transition-all duration-150
                hover:scale-95 active:scale-90
            "
                @click="performFormAction"
            >
                Salvar
                <Icon v-if="loadingFormAction" name="line-md:loading-loop" class="text-[25px]" />
            </button>
        </form>
    </div>
</main>
</template>

<style scoped>

label {
    @apply text-lg font-bold mt-3 mb-1;
}

</style>