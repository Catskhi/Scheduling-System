<script setup lang="ts">

const logout = async () => {
    localStorage.removeItem('token')
    await useRouter().push('/login/')
}

</script>

<template>
<header>
    <nav class="shadow-[0_3px_10px_rgb(0,0,0,0.2)]
    w-full h-20 backdrop-blur flex items-center px-10 z-0 bg-slate-50
    space-x-5
    ">
    <NuxtLink to="/" class="text-2xl font-semibold">Eventos</NuxtLink>
    <div class="absolute right-10 space-x-5">
        <button class="bg-blue-600 text-white font-bold px-10 py-1
        rounded hover:scale-95 active:scale-90 transition-all duration-150
        shadow-[0_3px_10px_rgb(0,0,0,0.2)]
        "
        @click="async () => await useRouter().push('/editados/')"
        >
            Eventos Editados <Icon name="mdi:eye" class="ml-3" />
        </button>
        <button class="bg-blue-600 text-white font-bold px-10 py-1
        rounded hover:scale-95 active:scale-90 transition-all duration-150
        shadow-[0_3px_10px_rgb(0,0,0,0.2)]
        "
        @click="async () => await useRouter().push('/events/create/')"
        >
            Criar <Icon name="ic:baseline-plus" class="mr-1 text-lg"/>
        </button>
        <button class="bg-red-600 text-white font-bold px-10 py-1
        rounded hover:scale-95 active:scale-90 transition-all duration-150
        shadow-[0_3px_10px_rgb(0,0,0,0.2)]
        "
        @click="logout"
        >
            Sair 
        </button>
    </div>
    </nav>
</header>
</template>