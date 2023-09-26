// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  pages: true,
  modules: [
    '@nuxtjs/tailwindcss',
    'nuxt-icon',
    // '@invictus.codes/nuxt-vuetify',
  ],
  // vuetify: {
  //   vuetifyOptions: {
  //     theme: {
  //       defaultTheme: 'light'
  //     }
  //   },
  //   moduleOptions: {
  //     autoImport: true
  //   }
  // }
})
