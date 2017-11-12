# 人人影视网爬虫

本人喜欢看美剧和美国电影，人人影视网可以某一天就会因为一些因素关闭，再也找不到像这样整理好的影视下载资源，所以写这个项目，把全站的下载链接采集下来，保存到自己的服务器，以备万一。

本项目使用了Scrapy分布式架构,使用scrapy-redis组件实现,Redis作为消息队列,MongoDB储存数据,防止服务器宕机,使用了MongoDB群集功能

数据流向:

- 调度器向Redis消息队列请求第一个Request,然后传给下载器

- 下载器将获取到的Response传给爬虫,爬虫对其进行解析,将数据打包为Item传给RedisPipeline,将新的Request传给Redis消息队列

- RedisPipeline将Item传给pipelines,pipelines对数据进行清洗,储存

# Linux系统安装项目过程

开发环境:

Ubuntu:16.04 LST

Redis:4.0.2

MongoDB:3.2.17

### 安装Redis

```
$ wget http://download.redis.io/releases/redis-4.0.2.tar.gz
$ tar xzf redis-3.2.5.tar.gz
$ cd redis-3.2.5
$ make
$ sudo make install
```

### 启动Redis服务

```
$ redis-server
```

### 安装MongoDB

```
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
$ echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
```

### 启动MongoDB集群服务

```
# 用两个终端窗口启动两个MongoDB服务
$ mongod --dbpath ~/mongodb/master/data --replSet repset
$ mongod --dbpath ~/mongodb/slave/data --port 27018 --replSet repset

# 再打开一个窗口启动MongoDB群集服务
$ mongo
$ use admin
$ config = { _id:"repset", members:[
  {_id:0,host:" 127.0.0.1:27017"},
  {_id:1,host:" 127.0.0.1:27018"},]
  }
$ rs.initiate(config)
# 查看节点信息
$ rs.status()
```

#任务队列

- 完成对影视信息的采集功能 [√]

- 完成对影视下载链接的采集功能 []

- 完成对影视下载链接的更新采集功能 []
