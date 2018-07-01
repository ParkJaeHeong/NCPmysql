<template>
  <section id="result" class="container">

    <header class="text-center pv-md">
      <h2>서버 생성 결과</h2>
      <p class="mt-10 color-gray-light">생성된 VM 서버 결과입니다</p>
    </header>
    
    <table class="table-server" v-if="servers !== []">
      <tbody>
        <tr v-for="(server, index) in servers" :key="index">
          <td class="text-center">
            <img src="/img/server.gif" alt="server icon" style="width:50px">
            <p class="mt-5">{{server.name}}</p>
          </td>
          <td>
            <b>Ping</b>
            <p v-for="(master, index2) in server.masters" :key="index2" class="mt-5">
              Server_id: {{master.Server_id}},
              Host: {{master.Host}},
              Slave_UUID: {{master.Slave_UUID}},
              Port: {{master.Port}},
              Master_id: {{master.Master_id}}
            </p>
            <p v-for="(slave, index2) in server.slaves" :key="index2" class="mt-5">
              Slave_IO_Running: {{slave.Slave_IO_Running}},
              Seconds_Behind_Master: {{slave.Seconds_Behind_Master}},
              Slave_SQL_Running: {{slave.Slave_SQL_Running}},
              Slave_id: {{slave.Slave_id}}
            </p>
          </td>
          <td>
            <div class="server-status" :class="{ 'off': !server.status }"></div>
          </td>
        </tr>
      </tbody>
    </table>
    <div class="pv-lg" v-else>
      <clip-loader color="#14adea"/>
    </div>

    <div class="mt-30 text-center">
      <nuxt-link :to="{ name: 'server' }" class="btn btn-primary">서버 세팅 추가하기</nuxt-link>
    </div>

  </section>
</template>

<script>
import ClipLoader from 'vue-spinner/src/ClipLoader.vue'
export default {
  components: {
    ClipLoader
  },
  data () {
    return {
      servers: [],
      masterInfo: null,
      slaveInfo: null
    }
  },
  created: function () {
    let result = this.$store.state.result
    if (result.masterInfo) {
      this.masterInfo = result.masterInfo
      this.slaveInfo = result.slaveInfo
      this.setServerArr()
      this.$store.commit('set_result', null)
    } else {
      this.$router.push('/server')
    }
  },
  methods: {
    setServerArr () {
      let tempArr = []
      let tempName = ''
      this.masterInfo.forEach((mInfo, index) => {
        if (tempArr.indexOf(Number(mInfo.Master_id)) === -1) {
          tempArr.push(Number(mInfo.Master_id))
          if (index === 0) tempName = mInfo.Host.substring(0, mInfo.Host.length - 1)
        }
      })
      this.slaveInfo.forEach(sInfo => {
        if (tempArr.indexOf(Number(sInfo.Slave_id)) === -1) {
          tempArr.push(Number(sInfo.Slave_id))
        }
      })
      tempArr.sort()
      tempArr.forEach(index => {
        this.servers.push({
          id: `${index}`,
          name: `${tempName}${index}`,
          masters: [],
          slaves: [],
          status: false
        })
      })
      this.setMaserInfo()
      this.setSlaveInfo()
    },
    setMaserInfo () {
      this.masterInfo.forEach(mInfo => {
        if (mInfo) this.servers[mInfo.Master_id - 1].status = true
        this.servers[mInfo.Master_id - 1].masters.push(mInfo)
      })
    },
    setSlaveInfo () {
      this.slaveInfo.forEach(sInfo => {
        this.servers[sInfo.Slave_id - 1].slaves.push(sInfo)
        if (sInfo.Slave_IO_Running === 'Yes' && sInfo.Seconds_Behind_Master === '0' && sInfo.Slave_SQL_Running === 'Yes') {
          this.servers[sInfo.Slave_id - 1].status = true
        }
      })
    }
  }
}
</script>

<style lang="less" scoped>
  @import "~assets/less/bootstrap/variables.less";

  .table-server {
    width: 100%;
    border-top: 1px solid @brand-primary;
    th, td {
      padding: 20px;
      border-bottom: 1px solid #ddd;
    }
  }

  .server-status {
    position: relative;
    width: 50px;
    height: 25px;
    border-radius: 25px;
    background-color: @brand-success;
    &:before {
      position: absolute;
      top: 2px;
      left: 26px;
      display: block;
      content: '';
      width: 21px;
      height: 21px;
      border-radius: 10px;
      background-color: #fff;
    }

    &.off {
      background-color: @brand-danger;
      &:before {
        left: 3px;
      }
    }
  }
</style>
