<script setup lang="ts">
import axios from 'axios';


const props = defineProps<{
    owner: number,
    edited_by: number,
    old_title: string,
    old_address: string,
    old_technical: number,
    old_description: string,
    old_date: string,
    old_start_time: string,
    old_end_time: string,

    new_title: string
    new_address: string
    new_technical: number
    new_description: string
    new_date: string
    new_start_time: string
    new_end_time: string
}>()

const owner_name = ref<string>('')
const edited_by_name = ref<string>('')
const old_technical_name = ref<string>('')
const new_technical_name = ref<string>('')

onMounted(async () => {
    await axios.get(getServerUrl() + '/users/' + props.owner + '/')
    .then((response) => {
        owner_name.value = response.data.username
    })
    .catch((error) => {
        console.log(error)
    })

    await axios.get(getServerUrl() + '/users/' + props.edited_by + '/')
    .then((response) => {
        edited_by_name.value = response.data.username
    })
    .catch((error) => {
        console.log(error)
    })

    old_technical_name.value = await getTechnicalData(props.old_technical)
    new_technical_name.value = await getTechnicalData(props.new_technical)
})

const getTechnicalData = async (technicalId: number): Promise<string> => {
    let technicalName: string = ''
    await axios.get(getServerUrl() + '/technicals/' + technicalId + '/')
    .then((response) => {
        technicalName = response.data.name
    })
    .catch((error) => {
        console.log(error)
    })

    return technicalName
}

</script>

<template>

<div  class="shadow-[0_3px_10px_rgb(0,0,0,0.2)]
        h-full w-full py-3 px-3 rounded-lg bg-slate-50">
        <p><strong>Autor:</strong> {{ owner_name }}</p>
        <p><strong>Editado por:</strong> {{ owner_name }}</p>
        <p class="font-bold text-xl my-3">Antes</p>
        <p><strong>Título:</strong> {{ old_title }}</p>
        <p><strong>Endereço:</strong> {{ old_address }}</p>
        <p><strong>Técnico:</strong> {{ old_technical_name }}</p>
        <p><strong>Descrição:</strong> {{ old_description }}</p>
        <p><strong>Data:</strong> {{ old_date.split('-').reverse().join('/') }}</p>
        <p><strong>Início:</strong> {{ old_start_time }}</p>
        <p><strong>Fim:</strong> {{ old_end_time }}</p>
        <p class="font-bold text-xl my-3">Depois</p>
        <p><strong>Título:</strong> {{ new_title }}</p>
        <p><strong>Endereço:</strong> {{ new_address }}</p>
        <p><strong>Técnico:</strong> {{ new_technical_name }}</p>
        <p><strong>Descrição:</strong> {{ new_description }}</p>
        <p><strong>Data:</strong> {{ new_date.split('-').reverse().join('/') }}</p>
        <p><strong>Início:</strong> {{ new_start_time }}</p>
        <p><strong>Fim:</strong> {{ new_end_time }}</p>
</div>


</template>

<style scoped>

p {
    @apply truncate;
}

</style>