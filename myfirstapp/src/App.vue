<template>
  <div id="app">
    <h1>Hola mundo</h1>
       <tes/>
  </div>
 
</template>

<script>

 import tes from './components/tes.vue';

export default {

 


  name: 'App',
  components: {

    tes
   
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
