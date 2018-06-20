<template>
  <section>

    <div class="form-horizontal">
      <h4>서버 이미지 선택</h4>
      <p class="mt-10 color-gray">CentOS, Ubuntu, Windows 및 DBMS 서버 이미지를 제공합니다. 이미지 및 부팅 디스크 크기를 선택하세요.<br>
      <span class="color-primary">(현재 Windows 에 대해서만 부팅 디스크로 100GB 선택이 가능하며, VDS를 사용하려면 100GB를 선택하세요.)</span></p>
      <hr class="mv-30" style="border-color: #000;">

      <div class="form-group">
        <label for="username" class="col-sm-3 control-label">부팅 디스크 크기</label>
        <div class="col-sm-9">
          <ul class="list-unstyle list-inline">
            <li>
              <label class="md-check"><input type="radio" name="bootingDiskSizeRadio" value="53687091200" v-model="selected.bootingDiskSize"><i class="blue"></i>
                50GB
              </label>
            </li>
            <li>
              <label class="md-check"><input type="radio" name="bootingDiskSizeRadio" value="107374182400" v-model="selected.bootingDiskSize" ><i class="blue"></i>
                100GB
              </label>
            </li>
          </ul>
        </div>
      </div>

      <div class="form-group">
        <label for="username" class="col-sm-3 control-label">이미지타입</label>
        <div class="col-sm-9">
          <ul class="list-unstyle list-inline">
            <li>
              <label class="md-check"><input type="radio" name="osTypeRadio" class="has-value" value="os" v-model="selected.osType"> <i class="blue"></i>
                OS
              </label>
            </li>
            <li>
              <label class="md-check"><input type="radio" name="osTypeRadio" class="has-value" value="db" v-model="selected.osType"> <i class="blue"></i>
                Application
              </label>
            </li>
          </ul>
        </div>
      </div>

      <div class="form-group" v-if="selected.osType === 'os'">
        <label for="username" class="col-sm-3 control-label">OS 이미지타입</label>
        <div class="col-sm-9">
          <ul class="list-unstyle list-inline">
            <li>
              <label class="md-check"><input type="radio" name="osDetailTypeRadio" class="has-value" value="ALL" v-model="selected.osDetailType"> <i class="blue"></i>
                All
              </label>
            </li>
            <li>
              <label class="md-check"><input type="radio" name="osDetailTypeRadio" class="has-value" value="LNX" v-model="selected.osDetailType"> <i class="blue"></i>
                CentOS
              </label>
            </li>
            <li>
              <label class="md-check"><input type="radio" name="osDetailTypeRadio" class="has-value" value="UBT" v-model="selected.osDetailType"> <i class="blue"></i>
                Ubuntu
              </label>
            </li>
            <li>
              <label class="md-check"><input type="radio" name="osDetailTypeRadio" class="has-value" value="WND" v-model="selected.osDetailType"> <i class="blue"></i>
                Windows
              </label>
            </li>
          </ul>
        </div>
      </div>

      <div class="form-group" v-if="selected.osType === 'db'">
        <label for="username" class="col-sm-3 control-label">Application 이미지타입</label>
        <div class="col-sm-9">
          <ul class="list-unstyle list-inline">
            <li>
              <label class="md-check"><input type="radio" name="dbmsOsDetailTypeRadio" class="has-value" value="ALL" v-model="selected.dbmsOsDetailType"> <i class="blue"></i>
                All
              </label>
            </li>
            <li>
              <label class="md-check"><input type="radio" name="dbmsOsDetailTypeRadio" class="has-value" value="MYSQL" v-model="selected.dbmsOsDetailType"> <i class="blue"></i>
                MySQL
              </label>
            </li>
            <li>
              <label class="md-check"><input type="radio" name="dbmsOsDetailTypeRadio" class="has-value" value="MSSQL" v-model="selected.dbmsOsDetailType"> <i class="blue"></i>
                MSSQL
              </label>
            </li>
            <li>
              <label class="md-check"><input type="radio" name="dbmsOsDetailTypeRadio" class="has-value" value="CBRID" v-model="selected.dbmsOsDetailType"> <i class="blue"></i>
                Cubrid
              </label>
            </li>
            <li>
              <label class="md-check"><input type="radio" name="dbmsOsDetailTypeRadio" class="has-value" value="REDIS" v-model="selected.dbmsOsDetailType"> <i class="blue"></i>
                Redis
              </label>
            </li>
            <li>
              <label class="md-check"><input type="radio" name="dbmsOsDetailTypeRadio" class="has-value" value="PSTGR" v-model="selected.dbmsOsDetailType"> <i class="blue"></i>
                PostgreSQL
              </label>
            </li>
            <li>
              <label class="md-check"><input type="radio" name="dbmsOsDetailTypeRadio" class="has-value" value="MariaDB" v-model="selected.dbmsOsDetailType"> <i class="blue"></i>
                MariaDB
              </label>
            </li>
          </ul>
        </div>
      </div>

      <hr class="mv-30">

      <table class="table no-ouline mt-30">
        <colgroup>
          <col width="40%">
          <col width="auto">
          <col width="100px">
        </colgroup>
        <thead>
          <tr>
            <th>서버 이미지 이름</th>
            <th colspan="2">설명</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in severImages" :key="index" v-if="checkSelected(item)">
            <td><i class="icon-os-cent m-r-sm"></i>{{item.title}}</td>
            <td>{{item.description}}</td>
            <td class="text-center"><button type="button" @click="setServerImage(item)" class="btn btn-sm btn-block btn-primary">다음</button></td>
          </tr>
        </tbody>
      </table>
    </div>

  </section>
</template>

<script>
export default {
  props: {
    inputData: {
      type: Object
    },
    nextFunc: {
      type: Function
    }
  },
  data () {
    return {
      selected: {
        bootingDiskSize: "53687091200",
        osType: 'os',
        osDetailType: 'ALL',
        dbmsOsDetailType: 'ALL'
      },
      severImages: [
        { bootingDiskSize: '53687091200', osDetailType: 'LNX', dbmsOsDetailType: '', title: 'centos-7.3-64', description: 'CentOS 7.3 (64-bit)' },
        { bootingDiskSize: '53687091200', osDetailType: 'LNX', dbmsOsDetailType: '', title: 'centos-7.2-64', description: 'CentOS 7.2 (64-bit)' },
        { bootingDiskSize: '53687091200', osDetailType: 'LNX', dbmsOsDetailType: '', title: 'centos-6.6-64', description: 'CentOS 6.6 (64-bit)' },
        { bootingDiskSize: '53687091200', osDetailType: 'LNX', dbmsOsDetailType: '', title: 'centos-6.3-64', description: 'CentOS 6.3 (64-bit)' },
        { bootingDiskSize: '53687091200', osDetailType: 'LNX', dbmsOsDetailType: '', title: 'centos-6.3-32', description: 'CentOS 6.3 (32-bit)' },
        { bootingDiskSize: '53687091200', osDetailType: 'LNX', dbmsOsDetailType: '', title: 'centos-5.11-64', description: 'CentOS 5.11 (64-bit)' },
        { bootingDiskSize: '53687091200', osDetailType: 'LNX', dbmsOsDetailType: 'MYSQL', title: 'mysql(5.7)-centos-7.2-64', description: 'CentOS 7.2 with MySQL 5.7 (64-bit)' },
        { bootingDiskSize: '53687091200', osDetailType: 'LNX', dbmsOsDetailType: 'MYSQL', title: 'mysql(5.7)-centos-6.6-64', description: 'CentOS 6.6 with MySQL 5.7 (64-bit)' },
        { bootingDiskSize: '53687091200', osDetailType: 'LNX', dbmsOsDetailType: 'MYSQL', title: 'mysql(5.6)-centos-7.2-64', description: 'CentOS 7.2 with MySQL 5.6 (64-bit)' },
        { bootingDiskSize: '53687091200', osDetailType: 'LNX', dbmsOsDetailType: 'MYSQL', title: 'mysql(5.6)-centos-6.6-64', description: 'CentOS 6.6 with MySQL 5.6 (64-bit)' },
        { bootingDiskSize: '53687091200', osDetailType: 'LNX', dbmsOsDetailType: 'CBRID', title: 'cubrid(9.2)-centos-7.3-64', description: 'CentOS 7.3 with Cubrid 9.2 (64-bit)' },
        { bootingDiskSize: '53687091200', osDetailType: 'LNX', dbmsOsDetailType: 'CBRID', title: 'cubrid(9.2)-centos-6.6-64', description: 'CentOS 6.6 with Cubrid 9.2 (64-bit)' },
        { bootingDiskSize: '53687091200', osDetailType: 'LNX', dbmsOsDetailType: 'REDIS', title: 'redis(3.2.8)-centos-7.3-64', description: 'CentOS 7.3 with Redis 3.2.8 (64-bit)' },
        { bootingDiskSize: '53687091200', osDetailType: 'LNX', dbmsOsDetailType: 'REDIS', title: 'redis(3.2.8)-centos-6.6-64', description: 'CentOS 6.6 with Redis 3.2.8 (64-bit)' },
        { bootingDiskSize: '53687091200', osDetailType: 'LNX', dbmsOsDetailType: 'MariaDB', title: 'mariadb(10.2)-centos-7.3-64', description: 'CentOS 7.3 with MariaDB 10.2 (64-bit)' },
        { bootingDiskSize: '53687091200', osDetailType: 'LNX', dbmsOsDetailType: 'PSTGR', title: 'PostgreSQL 9.4-centos-7.3-64', description: 'CentOS 7.3 with PostgreSQL 9.4 (64-bit)' },
        { bootingDiskSize: '53687091200', osDetailType: 'LNX', dbmsOsDetailType: 'PSTGR', title: 'PostgreSQL 9.4-centos-6.6-64', description: 'CentOS 6.6 with PostgreSQL 9.4 (64-bit)' },
        { bootingDiskSize: '53687091200', osDetailType: 'LNX', dbmsOsDetailType: '', title: 'rabbitmq(3.7.0)-centos-7.3-64', description: 'CentOS 7.3 with RabbitMQ 3.7.0 (64-bit)' },
        { bootingDiskSize: '53687091200', osDetailType: 'LNX', dbmsOsDetailType: '', title: 'rabbitmq(3.7.0)-centos-6.6-64', description: 'CentOS 6.6 with RabbitMQ 3.7.0 (64-bit)' },
        { bootingDiskSize: '53687091200', osDetailType: 'LNX', dbmsOsDetailType: '', title: 'tensorflow-centos-7.3-64', description: 'CentOS 7.3 with Tensorflow (64-bit)' },
        { bootingDiskSize: '53687091200', osDetailType: 'LNX', dbmsOsDetailType: '', title: 'Jenkins 2.73-centos-7.3-64', description: 'CentOS 7.3 with Jenkins 2.73 (64-bit)' },
        { bootingDiskSize: '53687091200', osDetailType: 'LNX', dbmsOsDetailType: '', title: 'Jenkins 2.73-centos-6.6-64', description: 'CentOS 6.6 with Jenkins 2.73 (64-bit)' },
        { bootingDiskSize: '53687091200', osDetailType: 'UBT', dbmsOsDetailType: '', title: 'ubuntu-16.04-64-server', description: 'Ubuntu Server 16.04 (64-bit)(※ Ubuntu 커널 업데이트는 지원하지 않으며, 업데이트 진행시 VM 사용이 불가능하며, 복구를 지원하지 않습니다.)' },
        { bootingDiskSize: '53687091200', osDetailType: 'UBT', dbmsOsDetailType: '', title: 'ubuntu-14.04-64-server', description: 'Ubuntu Server 14.04 (64-bit)(※ Ubuntu 커널 업데이트는 지원하지 않으며, 업데이트 진행시 VM 사용이 불가능하며, 복구를 지원하지 않습니다.)' },
        { bootingDiskSize: '53687091200', osDetailType: 'UBT', dbmsOsDetailType: '', title: 'ubuntu-12.04-64-server', description: 'Ubuntu 12.04 Server (64-bit)(※ Ubuntu 커널 업데이트는 지원하지 않으며, 업데이트 진행시 VM 사용이 불가능하며, 복구를 지원하지 않습니다.)' },
        { bootingDiskSize: '53687091200', osDetailType: 'UBT', dbmsOsDetailType: '', title: 'ubuntu-12.04-64-desktop', description: 'Ubuntu 12.04 Desktop (64-bit)(※ Ubuntu 커널 업데이트는 지원하지 않으며, 업데이트 진행시 VM 사용이 불가능하며, 복구를 지원하지 않습니다.)' },
        { bootingDiskSize: '53687091200', osDetailType: 'UBT', dbmsOsDetailType: 'MYSQL', title: 'mysql(5.7)-ubuntu-16.04-64-server', description: 'Ubuntu Server 16.04 with MySQL 5.7 (64-bit)(※ Ubuntu 커널 업데이트는 지원하지 않으며, 업데이트 진행시 VM 사용이 불가능하며, 복구를 지원하지 않습니다.)' },
        { bootingDiskSize: '53687091200', osDetailType: 'UBT', dbmsOsDetailType: 'MYSQL', title: 'mysql(5.7)-ubuntu-14.04-64-server', description: 'Ubuntu Server 14.04 with MySQL 5.7 (64-bit)(※ Ubuntu 커널 업데이트는 지원하지 않으며, 업데이트 진행시 VM 사용이 불가능하며, 복구를 지원하지 않습니다.)' },
        { bootingDiskSize: '53687091200', osDetailType: 'UBT', dbmsOsDetailType: 'MYSQL', title: 'mysql(5.6)-ubuntu-14.04-64-server', description: 'Ubuntu Server 14.04 with MySQL 5.6 (64-bit)(※ Ubuntu 커널 업데이트는 지원하지 않으며, 업데이트 진행시 VM 사용이 불가능하며, 복구를 지원하지 않습니다.)' },
        { bootingDiskSize: '53687091200', osDetailType: 'UBT', dbmsOsDetailType: 'CBRID', title: 'cubrid(9.2)-ubuntu-16.04-64-server', description: 'Ubuntu Server 16.04 with Cubrid 9.2 (64-bit)(※ Ubuntu 커널 업데이트는 지원하지 않으며, 업데이트 진행시 VM 사용이 불가능하며, 복구를 지원하지 않습니다.)' },
        { bootingDiskSize: '53687091200', osDetailType: 'UBT', dbmsOsDetailType: 'CBRID', title: 'cubrid(9.2)-ubuntu-14.04-64-server', description: 'Ubuntu Server 14.04 with Cubrid 9.2 (64-bit)(※ Ubuntu 커널 업데이트는 지원하지 않으며, 업데이트 진행시 VM 사용이 불가능하며, 복구를 지원하지 않습니다.)' },
        { bootingDiskSize: '53687091200', osDetailType: 'UBT', dbmsOsDetailType: 'REDIS', title: 'redis(3.2.8)-ubuntu-16.04-64-server', description: 'Ubuntu Server 16.04 with Redis 3.2.8 (64-bit)(※ Ubuntu 커널 업데이트는 지원하지 않으며, 업데이트 진행시 VM 사용이 불가능하며, 복구를 지원하지 않습니다.)' },
        { bootingDiskSize: '53687091200', osDetailType: 'UBT', dbmsOsDetailType: 'REDIS', title: 'redis(3.2.8)-ubuntu-14.04-64-server', description: 'Ubuntu Server 14.04 with Redis 3.2.8 (64-bit)(※ Ubuntu 커널 업데이트는 지원하지 않으며, 업데이트 진행시 VM 사용이 불가능하며, 복구를 지원하지 않습니다.)' },
        { bootingDiskSize: '53687091200', osDetailType: 'UBT', dbmsOsDetailType: 'MariaDB', title: 'mariadb(10.2)-ubuntu-16.04-64-server', description: 'Ubuntu Server 16.04 with MariaDB 10.2 (64-bit)(※ Ubuntu 커널 업데이트는 지원하지 않으며, 업데이트 진행시 VM 사용이 불가능하며, 복구를 지원하지 않습니다.)' },
        { bootingDiskSize: '53687091200', osDetailType: 'UBT', dbmsOsDetailType: '', title: 'rabbitmq(3.7.0)-ubuntu-16.04-64-server', description: 'Ubuntu Server 16.04 with RabbitMQ 3.7.0 (64-bit)(※ Ubuntu 커널 업데이트는 지원하지 않으며, 업데이트 진행시 VM 사용이 불가능하며, 복구를 지원하지 않습니다.)' },
        { bootingDiskSize: '53687091200', osDetailType: 'UBT', dbmsOsDetailType: '', title: 'rabbitmq(3.7.0)-ubuntu-14.04-64-server', description: 'Ubuntu Server 14.04 with RabbitMQ 3.7.0 (64-bit)(※ Ubuntu 커널 업데이트는 지원하지 않으며, 업데이트 진행시 VM 사용이 불가능하며, 복구를 지원하지 않습니다.)' },
        { bootingDiskSize: '53687091200', osDetailType: 'UBT', dbmsOsDetailType: '', title: 'tensorflow-ubuntu-16.04-64-server', description: 'Ubuntu Server 16.04 with Tensorflow (64-bit)(※ Ubuntu 커널 업데이트는 지원하지 않으며, 업데이트 진행시 VM 사용이 불가능하며, 복구를 지원하지 않습니다.)' },
        { bootingDiskSize: '53687091200', osDetailType: 'UBT', dbmsOsDetailType: '', title: 'tensorflow-cluster-ubuntu-16.04-64-master', description: 'Ubuntu Server 16.04 with Tensorflow-Cluster-Master (64-bit)(※ Ubuntu 커널 업데이트는 지원하지 않으며, 업데이트 진행시 VM 사용이 불가능하며, 복구를 지원하지 않습니다.)' },
        { bootingDiskSize: '53687091200', osDetailType: 'UBT', dbmsOsDetailType: '', title: 'Jenkins 2.73-ubuntu-16.04-64-server', description: 'Ubuntu Server 16.04 with Jenkins 2.73 (64-bit)(※ Ubuntu 커널 업데이트는 지원하지 않으며, 업데이트 진행시 VM 사용이 불가능하며, 복구를 지원하지 않습니다.)' },
        { bootingDiskSize: '53687091200', osDetailType: 'UBT', dbmsOsDetailType: '', title: 'Jenkins 2.73-ubuntu-14.04-64-server', description: 'Ubuntu Server 14.04 with Jenkins 2.73 (64-bit)(※ Ubuntu 커널 업데이트는 지원하지 않으며, 업데이트 진행시 VM 사용이 불가능하며, 복구를 지원하지 않습니다.)' },
        { bootingDiskSize: '53687091200', osDetailType: 'WND', dbmsOsDetailType: '', title: 'win-2008-64-R2-en', description: 'Windows Server 2008 R2 with SP1 (64-bit) English Edition(※ Micro 타입의 서버는 지원하지 않습니다.)' },
        { bootingDiskSize: '53687091200', osDetailType: 'WND', dbmsOsDetailType: '', title: 'win-2012-64-R2-en', description: 'Windows Server 2012(64bit) R2 English Edition(※ Micro 타입의 서버는 지원하지 않습니다.)' },
        { bootingDiskSize: '53687091200', osDetailType: 'WND', dbmsOsDetailType: '', title: 'win-2016-64-en', description: 'Windows Server 2016 (64-bit) English Edition(※ Micro 타입의 서버는 지원하지 않습니다.)' },
        { bootingDiskSize: '53687091200', osDetailType: 'WND', dbmsOsDetailType: 'MSSQL', title: 'mssql(2016exp)-win-2012-64-R2', description: 'Windows Server 2012 R2 with MSSQL 2016 Express (64-bit)(※ Micro 타입의 서버는 지원하지 않습니다.)' },
        { bootingDiskSize: '53687091200', osDetailType: 'WND', dbmsOsDetailType: 'MSSQL', title: 'mssql(2016std)-win-2012-64-R2', description: 'Windows Server 2012 R2 with MSSQL 2016 Standard (64-bit)(※ Micro 타입의 서버는 지원하지 않습니다.)' },
        { bootingDiskSize: '53687091200', osDetailType: 'WND', dbmsOsDetailType: 'MSSQL', title: 'mssql(2014std)-win-2012-64-R2', description: 'Windows Server 2012 R2 with MSSQL 2014 Standard (64-bit)(※ Micro 타입의 서버는 지원하지 않습니다.)' },
        { bootingDiskSize: '53687091200', osDetailType: 'WND', dbmsOsDetailType: 'MSSQL', title: 'mssql(2012std)-win-2012-64-R2', description: 'Windows Server 2012 R2 with MSSQL 2012 Standard (64-bit)(※ Micro 타입의 서버는 지원하지 않습니다.)' },
        { bootingDiskSize: '53687091200', osDetailType: 'WND', dbmsOsDetailType: 'MSSQL', title: 'mssql(2008std)-win-2008-64-R2', description: 'Windows Server 2008 R2 with MSSQL 2008 Standard (64-bit)(※ Micro, High-Memory 타입의 서버는 지원하지 않습니다.)' },
        { bootingDiskSize: '107374182400', osDetailType: 'WND', dbmsosDetailType: 'MSSQL', title: 'win-2008-64-R2-en', description: 'Windows Server 2008 R2 with SP1 (64-bit) English Edition(※ Micro 타입의 서버는 지원하지 않습니다.)' },
        { bootingDiskSize: '107374182400', osDetailType: 'WND', dbmsosDetailType: 'MSSQL', title: 'win-2012-64-R2-en', description: 'Windows Server 2012(64bit) R2 English Edition(※ Micro 타입의 서버는 지원하지 않습니다.)' },
        { bootingDiskSize: '107374182400', osDetailType: 'WND', dbmsosDetailType: 'MSSQL', title: 'win-2016-64-en', description: 'Windows Server 2016 (64-bit) English Edition(※ Micro 타입의 서버는 지원하지 않습니다.)' },
        { bootingDiskSize: '107374182400', osDetailType: 'WND', dbmsosDetailType: 'MSSQL', title: 'mssql(2016exp)-win-2012-64-R2', description: 'Windows Server 2012 R2 with MSSQL 2016 Express (64-bit)(※ Micro 타입의 서버는 지원하지 않습니다.)' },
        { bootingDiskSize: '107374182400', osDetailType: 'WND', dbmsosDetailType: 'MSSQL', title: 'mssql(2016std)-win-2012-64-R2', description: 'Windows Server 2012 R2 with MSSQL 2016 Standard (64-bit)(※ Micro 타입의 서버는 지원하지 않습니다.)' },
        { bootingDiskSize: '107374182400', osDetailType: 'WND', dbmsosDetailType: 'MSSQL', title: 'mssql(2014std)-win-2012-64-R2', description: 'Windows Server 2012 R2 with MSSQL 2014 Standard (64-bit)(※ Micro 타입의 서버는 지원하지 않습니다.)' },
        { bootingDiskSize: '107374182400', osDetailType: 'WND', dbmsosDetailType: 'MSSQL', title: 'mssql(2012std)-win-2012-64-R2', description: 'Windows Server 2012 R2 with MSSQL 2012 Standard (64-bit)(※ Micro 타입의 서버는 지원하지 않습니다.)' },
        { bootingDiskSize: '107374182400', osDetailType: 'WND', dbmsosDetailType: 'MSSQL', title: 'mssql(2008std)-win-2008-64-R2', description: 'Windows Server 2008 R2 with MSSQL 2008 Standard (64-bit)(※ Micro 타입의 서버는 지원하지 않습니다.)' }
      ]
    }
  },
  methods: {
    setServerImage (item) {
      this.inputData.name = item.title
      this.inputData.description = item.description
      this.nextFunc()
    },
    checkSelected (item) {
      if (this.selected.bootingDiskSize !== item.bootingDiskSize) return false

      if (this.selected.osType === 'os') {
        if (this.selected.osDetailType !== "ALL") {
          if (item.osDetailType !== this.selected.osDetailType) return false
        }
      } else {
        if (this.selected.dbmsOsDetailType !== "ALL") {
          if (item.dbmsOsDetailType !== this.selected.dbmsOsDetailType) return false
        }
      }
      return true
    }
  }
}
</script>

