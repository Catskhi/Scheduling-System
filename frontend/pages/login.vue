<script setup lang="ts">
import axios from 'axios'
import { getIsLogged } from '~/utils/AuthUtils';

definePageMeta({
    layout: false
})

const loading = ref<boolean>(false)
const hasErrors = ref<boolean>(false)
const isLogged = ref<boolean>(false)

const email = ref<string>('')
const password = ref<string>('')

const makeLogin = async () => {
    loading.value = true
    hasErrors.value = false
    await axios.post(getServerUrl() + '/token/', {
        email: email.value,
        password: password.value
    })
    .then((response) => {
        if (response.data.access) {
            localStorage.setItem('token', response.data.access)
        }
    })
    .catch((error) => {
        console.log(error.response.data)
        hasErrors.value = true
    })
    if (await getIsLogged()) {
        useRouter().push('/')
    }
    loading.value = false
}

onBeforeMount(async () => {
    isLogged.value = await getIsLogged()
    if (isLogged.value) {
        useRouter().push('/')
    }
})

</script>

<template>
    <AuthLoading />
    <main class="absolute w-full h-full bg-gradient-cyan
        flex items-center justify-center
    ">
        <div class="w-3/4 h-2/3 lg:w-1/3 bg-white rounded relative
        shadow-[0_2.8px_2.2px_rgba(0,_0,_0,_0.034),_0_6.7px_5.3px_rgba(0,_0,_0,_0.048),_0_12.5px_10px_rgba(0,_0,_0,_0.06),_0_22.3px_17.9px_rgba(0,_0,_0,_0.072),_0_41.8px_33.4px_rgba(0,_0,_0,_0.086),_0_100px_80px_rgba(0,_0,_0,_0.12)]
             transition-all duration-150
        "
            :class="{'ring-4 ring-red-500': hasErrors}"
        >
            <h1 class="text-center mt-12 text-3xl">
                Login
            </h1>
            <form class="flex flex-col px-20">
                <label for="email" class="mt-5 mb-1">
                    Email
                </label>
                <input v-model="email" id="email" type="email" placeholder="Email"
                    class="border-2 focus:outline-none focus:ring-2 ring-cyan-400
                        transition-all duration-300 rounded px-3 py-1
                    "
                />  
                <label for="password" class="mt-5 mb-1">
                    Senha
                </label>
                <input v-model="password" id="password" type="password" placeholder="Senha"
                    class="border-2 focus:outline-none focus:ring-2 ring-cyan-400
                        transition-all duration-300 rounded px-3 py-1
                    "
                />
            </form>
            <div class="w-full flex items-center justify-center">
                <div class="mt-5">
                    <p class="text-red-500 font-bold transition-all duration-150"
                        :class="[hasErrors ? 'opacity-100' : 'opacity-0']"
                    >Email ou senha inválidos.</p>
                </div>
                <button type="button" class="text-white bg-gradient-to-r from-blue-500 via-blue-600 to-blue-700 font-bold 
                    hover:scale-95 active:scale-90 transition-all duration-150
                    px-20 py-2 rounded absolute bottom-10 text-xl
                "
                    @click="makeLogin"
                >
                    Login 
                    <Icon v-if="loading" name="line-md:loading-loop" class="text-[25px]" />
                </button>
            </div>
        </div>

        <div>

        </div>
    </main>
</template>