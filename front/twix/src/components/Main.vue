<template>    
    <b-container>
      <b-row>
        <b-col md='5'>
          <b-card title="Определение дефекта">
            <b-card-text>
              <label for="file">Загрузить фото
              <input id="file" type="file" @change="onFileChange" style='width: 105px;'/>
              </label>
            </b-card-text>
            
            <div v-if="loader" class="lds-heart"><div></div></div>
            <b-card-img v-if="url" :src="url"></b-card-img>
            <b-card-text>
                 <b-table striped hover :items="response"></b-table>
            </b-card-text>
          </b-card>
        </b-col>
        <b-col md='3'>
            <b-card title="Дообучение">
              <b-card-text>
                <label for="file">Загрузить архив
                <input id="file" type="file" @change="onZipChange" style='width: 105px;'/>
                </label>
              </b-card-text>
          </b-card>        
        </b-col>
        <b-col md='3'>
            <b-card title="АОЕ определение дефекта" >
              <b-card-text>
                <label for="file">Загрузить архив
                  <input id="file" type="file" @change="onZipChange" style='width: 105px;'/>
                </label>
              </b-card-text>
              <!-- <b-card-text style="height: 380px;overflow-x: auto;" >
                <div v-for="item in responseAOE"  v-bind:key="item">
                    <P>{{ item.photo_name }}</P>
                    <b-table striped hover :items="item.data"></b-table>
                </div>
              </b-card-text> -->
          </b-card> 
        </b-col>
      </b-row>
    </b-container>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Main',
  data() {
    return {
      url: null,
      loader: false,
      response: [
          // {'name': 'Волосеные трещены', 'accuracy': 0.95},
          // {'name': 'Волосеные трещены', 'accuracy': 0.93},
          // {'name': 'Волосеные трещены', 'accuracy': 0.92}
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
      var api = 'http://127.0.0.1:8000/api/'
      // predict/predict/
      let data = new FormData()

      data.append('name', 'image')
      data.append('file', event.target.files[0])

      let config = {
        header : {
          'Content-Type' : 'multipart/form-data'
        }
      };  
      var app = this;
      app.loader = true;
      axios.post(api+'predict/predict/', data, config).then(response => {
        // eslint-disable-next-line no-console
        console.log('response', response)
        app.response = response.data
        app.loader = false;
      }).catch(error => {
        // eslint-disable-next-line no-console
        console.log('error', error)
        alert("Что-то пошло не так :с")
        app.loader = false;
      })


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




.lds-heart {
  display: inline-block;
  position: relative;
  width: 80px;
  height: 80px;
  transform: rotate(45deg);
  transform-origin: 40px 40px;
}
.lds-heart div {
  top: 32px;
  left: 32px;
  position: absolute;
  width: 32px;
  height: 32px;
  background: #ff5050;
  animation: lds-heart 1.2s infinite cubic-bezier(0.215, 0.61, 0.355, 1);
}
.lds-heart div:after,
.lds-heart div:before {
  content: " ";
  position: absolute;
  display: block;
  width: 32px;
  height: 32px;
  background: #ff5050;
}
.lds-heart div:before {
  left: -24px;
  border-radius: 50% 0 0 50%;
}
.lds-heart div:after {
  top: -24px;
  border-radius: 50% 50% 0 0;
}
@keyframes lds-heart {
  0% {
    transform: scale(0.95);
  }
  5% {
    transform: scale(1.1);
  }
  39% {
    transform: scale(0.85);
  }
  45% {
    transform: scale(1);
  }
  60% {
    transform: scale(0.95);
  }
  100% {
    transform: scale(0.9);
  }
}

</style>
