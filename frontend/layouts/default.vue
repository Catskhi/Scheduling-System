<script setup lang="ts">

const logout = async () => {
    localStorage.removeItem('token')
    await useRouter().push('/login/')
}

</script>

<template>
<header>
    <nav class="w-full h-14 backdrop-blur flex items-center px-10 z-0">
        <button class="bg-red-600 text-white font-bold px-10 py-1
            rounded hover:scale-95 active:scale-90 transition-all duration-150
        "
            @click="logout"
        >
            Sair
        </button>
    </nav>
</header>
</template>