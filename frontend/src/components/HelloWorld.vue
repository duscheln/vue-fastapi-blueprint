<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-img
          :src="require('../assets/logo.svg')"
          class="my-3"
          contain
          height="200"
        />
      </v-col>

      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3">
          Welcome to Vuetify
        </h1>
      </v-col>


      <v-col
        class="mb-5"
        cols="12"
      >
        <h2 class="headline font-weight-bold mb-3">
          {{testText}}
        </h2>

        <v-row justify="center">
          <v-btn
          color="deep-purple lighten-2"
          text
          @click="testFunction"
          >
          Lade Text
          </v-btn>

                    <v-btn
          color="lighten-2"
          text
          @click="startContainer"
          >
          Starte Container
          </v-btn>
        </v-row>
      </v-col>

    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';

  export default {
    name: 'HelloWorld',

    methods:{

        startContainer: function(){

          axios
            .post(process.env.VUE_APP_ROOT_API + 'startContainer')
            .then(res => {
              console.log(res.data)
            })
            .catch(error => {
              // handle error
              console.error(error);
            })

        },

        testFunction: function(){
        //let urlParams = new URLSearchParams(window.location.search);
            // console.log(urlParams.has('instance')); // true
            // console.log(urlParams.get('instance')); // "MyParam" 
        console.log("Hello")
        console.log(process.env.VUE_APP_ROOT_API + 'helloWorld')
          axios
            .get(process.env.VUE_APP_ROOT_API + 'helloWorld')
            .then(res => {
              this.testText = res.data.text
              console.log(res)
            })
            .catch(error => {
              // handle error
              console.error(error);
            })
      }

    },

    data: () => ({
      testText: "Das ist ein test",

      ecosystem: [
        {
          text: 'vuetify-loader',
          href: 'https://github.com/vuetifyjs/vuetify-loader',
        },
        {
          text: 'github',
          href: 'https://github.com/vuetifyjs/vuetify',
        },
        {
          text: 'awesome-vuetify',
          href: 'https://github.com/vuetifyjs/awesome-vuetify',
        },
      ],
      importantLinks: [
        {
          text: 'Documentation',
          href: 'https://vuetifyjs.com',
        },
        {
          text: 'Chat',
          href: 'https://community.vuetifyjs.com',
        },
        {
          text: 'Made with Vuetify',
          href: 'https://madewithvuejs.com/vuetify',
        },
        {
          text: 'Twitter',
          href: 'https://twitter.com/vuetifyjs',
        },
        {
          text: 'Articles',
          href: 'https://medium.com/vuetify',
        },
      ],
      whatsNext: [
        {
          text: 'Explore components',
          href: 'https://vuetifyjs.com/components/api-explorer',
        },
        {
          text: 'Select a layout',
          href: 'https://vuetifyjs.com/getting-started/pre-made-layouts',
        },
        {
          text: 'Frequently Asked Questions',
          href: 'https://vuetifyjs.com/getting-started/frequently-asked-questions',
        },
      ],
    }),
  }
</script>
