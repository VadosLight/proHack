<template>    
    <b-container>
      <b-row>
        <b-col md='4'>
          <b-card title="Определение дефекта">
            <b-card-text>
              <label for="file">Загрузить фото
              <input id="file" type="file" @change="onFileChange" style='width: 105px;'/>
              </label>
            </b-card-text>
            <b-card-img v-if="url" :src="url"></b-card-img>
            <b-card-text>
                 <b-table striped hover :items="response"></b-table>
            </b-card-text>
          </b-card>
        </b-col>
        <b-col md='4'>
            <b-card title="Дообучение">
              <b-card-text>
                <label for="file">Загрузить архив
                <input id="file" type="file" @change="onZipChange" style='width: 105px;'/>
                </label>
              </b-card-text>
          </b-card>        
        </b-col>
        <b-col md='4'>
            <b-card title="АОЕ определение дефекта" >
              <b-card-text>
                <label for="file">Загрузить архив
                  <input id="file" type="file" @change="onZipChange" style='width: 105px;'/>
                </label>
              </b-card-text>
              <b-card-text style="height: 380px;overflow-x: auto;">
                <div v-for="item in responseAOE"  v-bind:key="item">
                    <P>{{ item.photo_name }}</P>
                    <b-table striped hover :items="item.data"></b-table>
                </div>
              </b-card-text>
          </b-card> 
        </b-col>
      </b-row>
    </b-container>
</template>

<script>
export default {
  name: 'Main',
  data() {
    return {
      url: null,
      response: [
          {'name': 'Волосеные трещены', 'accuracy': 0.95},
          {'name': 'Волосеные трещены', 'accuracy': 0.93},
          {'name': 'Волосеные трещены', 'accuracy': 0.92}
        ],
      responseAOE:[
        {
          photo_name: '1.jpg',
          data: [
              {'name': 'Волосеные трещены', 'accuracy': 0.95},
              {'name': 'Волосеные трещены', 'accuracy': 0.93},
              {'name': 'Волосеные трещены', 'accuracy': 0.92}
            ],
        },
        {
          photo_name: '2.jpg',
          data: [
              {'name': 'Волосеные трещены', 'accuracy': 0.95},
              {'name': 'Волосеные трещены', 'accuracy': 0.93},
              {'name': 'Волосеные трещены', 'accuracy': 0.92}
            ],
        },
        {
          photo_name: '2.jpg',
          data: [
              {'name': 'Волосеные трещены', 'accuracy': 0.95},
              {'name': 'Волосеные трещены', 'accuracy': 0.93},
              {'name': 'Волосеные трещены', 'accuracy': 0.92}
            ],
        },
        {
          photo_name: '3.jpg',
          data: [
              {'name': 'Волосеные трещены', 'accuracy': 0.95},
              {'name': 'Волосеные трещены', 'accuracy': 0.93},
              {'name': 'Волосеные трещены', 'accuracy': 0.92}
            ],
        },
      ]
    }
  },
  methods: {
    onFileChange(e) {
      const file = e.target.files[0];
      this.url = URL.createObjectURL(file);
    },
    onZipChange(e){
      const file = e.target.files[0];
      this.url = URL.createObjectURL(file); 
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
body {
  background-color: #e2e2e2;
}

#app {
  padding: 20px;
}

#preview {
  display: flex;
  justify-content: center;
  align-items: center;
}

#preview img {
  max-width: 100%;
  max-height: 500px;
}
</style>
